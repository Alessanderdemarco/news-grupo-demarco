"""
processar_emplacamentos.py
Lê a base bruta de emplacamentos (897k linhas) e gera emplacamentos_2026.json
Inclui micro-regiões (coluna L) com cidades em cascata (coluna J).
Coluna S (índice 18) = type_vehicle: VP / VU / outros
"""

import os, json, unicodedata, collections
import openpyxl

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PAI_DIR  = os.path.dirname(BASE_DIR)
SAIDA    = os.path.join(BASE_DIR, "emplacamentos_2026.json")

XLSX_POSSIVEIS = [
    os.path.join(PAI_DIR,  "Base de dados mtmjan a jun 2026.xlsx"),
    os.path.join(BASE_DIR, "Base de dados mtmjan a jun 2026.xlsx"),
]

MARCAS_GRUPO = {
    "RENAULT":  "Renault",
    "GWM":      "GWM",
    "YAMAHA":   "Yamaha",
    "TRIUMPH":  "Triumph",
    "CF MOTO":  "CF Motos",
    "PEUGEOT":  "Peugeot",
    "CITROEN":  "Citroën",
    "GEELY":    "Geely",
}

AREAS_INFLUENCIA = {
    "GWM":     ["CHAPECO", "CRICIUMA", "CAMPOS DE LAGES"],
    "RENAULT": ["BLUMENAU", "SAO MIGUEL DO OESTE", "CHAPECO", "CONCORDIA",
                "JOACABA", "PORTO UNIAO", "XANXERE", "CANOINHAS", "RIO DO SUL"],
    "GEELY":   ["BLUMENAU", "CHAPECO"],
    "TRIUMPH": ["BLUMENAU", "CHAPECO"],
    "YAMAHA":  ["JOACABA", "CHAPECO"],
    "PEUGEOT": ["CANOINHAS"],
    "CITROEN": ["CANOINHAS"],
    "CF MOTO": ["CHAPECO"],
}

MICRO_REGIOES_SC = sorted({
    m for areas in AREAS_INFLUENCIA.values() for m in areas
})

# Micro-regiões que devem ser agregadas dentro de outra micro-região
MICRO_AGRUPAMENTO = {
    "ARARANGUA": "CRICIUMA",
    "TUBARAO":   "CRICIUMA",
}

MESES_PT = {1:"Jan",2:"Fev",3:"Mar",4:"Abr",5:"Mai",6:"Jun",
            7:"Jul",8:"Ago",9:"Set",10:"Out",11:"Nov",12:"Dez"}

# Tipos de veículo que nos interessam
TIPOS_VEI = {"VP", "VU"}

def _norm(s):
    if s is None: return ""
    if isinstance(s, (int, float)): s = str(int(s))  # 208 → "208", 2008 → "2008"
    if not isinstance(s, str): return ""
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.upper().strip()

def encontrar_base():
    for p in XLSX_POSSIVEIS:
        if os.path.exists(p): return p
    return None

def _dd_int():
    return collections.defaultdict(int)

def _dd2():
    return collections.defaultdict(_dd_int)

def _dd3():
    return collections.defaultdict(_dd2)

def _dd4():
    return collections.defaultdict(_dd3)

def processar(verbose=True):
    path = encontrar_base()
    if not path:
        if verbose: print("  [Emplacamentos] Base não encontrada — pulando")
        return False
    if verbose: print(f"  Lendo {os.path.basename(path)}...")

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb.active

    # Índices 0-based: mes=2, estado=8, cidade=9, micro=12, marca=14, modelo=16,
    #                  tipo_vei=18, prop=29, total=40, regiao=6
    CI = dict(mes=2, estado=8, cidade=9, micro=12, marca=14,
              modelo=16, versao=17, tipo=18, prop=29, total=40, regiao=6)

    meses_set = set()

    # Estruturas: {tipo: {marca: {mes: total}}}
    # tipo in {"VP","VU","ALL"}
    br      = collections.defaultdict(_dd2)   # brasil
    sc_acc  = collections.defaultdict(_dd2)   # SC
    r1_acc  = collections.defaultdict(_dd2)   # R1
    # Propulsão nacional/estadual/regional (apenas ALL): {prop: {marca: {mes: total}}}
    br_prop  = collections.defaultdict(_dd2)
    sc_prop  = collections.defaultdict(_dd2)
    r1_prop  = collections.defaultdict(_dd2)
    # micro: {tipo: {micro: {marca: {mes: total}}}}
    mic     = collections.defaultdict(_dd3)
    # mic_mod: {tipo: {micro: {marca: {modelo: {mes: total}}}}}
    mic_mod = collections.defaultdict(_dd4)
    # mic_cid: {tipo: {micro: {cidade: {marca: {mes: total}}}}}
    mic_cid = collections.defaultdict(_dd4)
    # mic_cid_mod: {tipo: {micro: {cidade: {marca: {modelo: {mes: total}}}}}}
    def _dd5(): return collections.defaultdict(_dd4)
    mic_cid_mod = collections.defaultdict(_dd5)

    # Propulsão por micro/cidade: {micro: {prop: {marca: {mes: total}}}}
    mic_prop     = collections.defaultdict(_dd3)   # {micro: {prop: {marca: {mes}}}}
    mic_cid_prop = collections.defaultdict(_dd4)   # {micro: {cidade: {prop: {marca: {mes}}}}}

    for row in ws.iter_rows(min_row=2, values_only=True):
        mes    = row[CI["mes"]]
        estado = _norm(row[CI["estado"]])
        cidade = _norm(row[CI["cidade"]])
        micro  = _norm(row[CI["micro"]])
        marca  = _norm(row[CI["marca"]])
        modelo = _norm(row[CI["modelo"]])
        if not modelo:
            # fallback: extrai modelo de desc_veh_version (ex: "PEUGEOT/208 ACTIVE PACK" → "208")
            versao = _norm(row[CI["versao"]]) if row[CI["versao"]] else ""
            partes = versao.split("/", 1)
            if len(partes) > 1:
                modelo = partes[1].split()[0] if partes[1].split() else ""
            elif versao:
                modelo = versao.split()[0]
        tipo   = _norm(row[CI["tipo"]])    # VP / VU / etc.
        prop_raw = row[CI["prop"]]          # desc_electric_propulsion
        prop   = _norm(prop_raw) if prop_raw else "COMBUSTAO"
        if not prop:
            prop = "COMBUSTAO"
        total  = int(row[CI["total"]]) if isinstance(row[CI["total"]], (int,float)) else 0
        regiao = _norm(row[CI["regiao"]])

        if not isinstance(mes, int) or total == 0: continue
        meses_set.add(mes)

        # Agrupa micro-regiões subordinadas no pai (ex: Araranguá → Criciúma)
        micro = MICRO_AGRUPAMENTO.get(micro, micro)

        # Normaliza tipo para VP / VU / (ignora outros para split, mas conta em ALL)
        tipo_norm = tipo if tipo in TIPOS_VEI else None

        for t in (["ALL"] + ([tipo_norm] if tipo_norm else [])):
            br[t][marca][mes]     += total
            if estado == "SC":
                sc_acc[t][marca][mes] += total
            if regiao == "R1":
                r1_acc[t][marca][mes] += total
        # Propulsão nacional/estadual/regional (sem cruzamento tipo×prop)
        br_prop[prop][marca][mes] += total
        if estado == "SC":
            sc_prop[prop][marca][mes] += total
        if regiao == "R1":
            r1_prop[prop][marca][mes] += total

        if estado == "SC" and micro in MICRO_REGIOES_SC:
            for t in (["ALL"] + ([tipo_norm] if tipo_norm else [])):
                mic[t][micro][marca][mes]              += total
                mic_cid[t][micro][cidade][marca][mes]  += total
                if marca in MARCAS_GRUPO:
                    mic_mod[t][micro][marca][modelo][mes]             += total
                    mic_cid_mod[t][micro][cidade][marca][modelo][mes] += total
            # Propulsão (apenas para ALL — sem cruzamento tipo×propulsão)
            mic_prop[micro][prop][marca][mes]           += total
            mic_cid_prop[micro][cidade][prop][marca][mes] += total

    wb.close()

    meses    = sorted(meses_set)
    meses_pt = [MESES_PT.get(m, str(m)) for m in meses]
    if verbose: print(f"  Meses: {meses_pt}")

    def _flat(d_mes):
        return [d_mes.get(m, 0) for m in meses]

    # Top 30 marcas Brasil por volume total
    top30 = sorted(br["ALL"], key=lambda m: sum(br["ALL"][m].values()), reverse=True)[:30]

    def _marcas_bloco(tipo, src):
        """Retorna dict marca→[v1..vn] para todos que têm dados."""
        return {m: _flat(src[tipo][m]) for m in src[tipo]}

    def _marcas_bloco_top30(tipo):
        return {m: _flat(br[tipo][m]) for m in top30 if m in br[tipo]}

    out = {
        "meses":    meses,
        "meses_pt": meses_pt,
        "areas_influencia": AREAS_INFLUENCIA,
        "marcas_grupo":     MARCAS_GRUPO,
        # Brasil: ALL / VP / VU
        "brasil":    _marcas_bloco_top30("ALL"),
        "brasil_vp": _marcas_bloco_top30("VP"),
        "brasil_vu": _marcas_bloco_top30("VU"),
        # SC
        "sc":    _marcas_bloco("ALL", sc_acc),
        "sc_vp": _marcas_bloco("VP",  sc_acc),
        "sc_vu": _marcas_bloco("VU",  sc_acc),
        # R1
        "r1":    _marcas_bloco("ALL", r1_acc),
        "r1_vp": _marcas_bloco("VP",  r1_acc),
        "r1_vu": _marcas_bloco("VU",  r1_acc),
        # Propulsão por escopo nacional/estadual/regional
        "brasil_prop": {p: {m: _flat(v) for m, v in pm.items()} for p, pm in br_prop.items()},
        "sc_prop":     {p: {m: _flat(v) for m, v in pm.items()} for p, pm in sc_prop.items()},
        "r1_prop":     {p: {m: _flat(v) for m, v in pm.items()} for p, pm in r1_prop.items()},
        "micro": {},
    }

    if verbose: print("  Montando micro-regiões...")
    for micro_nm in MICRO_REGIOES_SC:
        if not mic["ALL"].get(micro_nm): continue

        def _mmap(tipo):
            return {m: _flat(v) for m, v in mic[tipo][micro_nm].items()}

        def _modmap(tipo):
            return {
                m: {mod: _flat(mic_mod[tipo][micro_nm][m][mod])
                    for mod in mic_mod[tipo][micro_nm][m]}
                for m in MARCAS_GRUPO if m in mic_mod[tipo][micro_nm]
            }

        # Propulsão por micro: {prop: {marca: [v1..vn]}}
        prop_micro = {
            p: {m: _flat(v) for m, v in mic_prop[micro_nm][p].items()}
            for p in mic_prop[micro_nm]
        }

        out_micro = {
            "marcas":    _mmap("ALL"),
            "marcas_vp": _mmap("VP"),
            "marcas_vu": _mmap("VU"),
            "modelos":    _modmap("ALL"),
            "modelos_vp": _modmap("VP"),
            "modelos_vu": _modmap("VU"),
            "prop":      prop_micro,
            "cidades": {},
        }

        for cid_nm in mic_cid["ALL"].get(micro_nm, {}):
            def _cmap(tipo):
                return {m: _flat(v) for m, v in mic_cid[tipo][micro_nm][cid_nm].items()}

            def _cmodmap(tipo):
                return {
                    m: {mod: _flat(mic_cid_mod[tipo][micro_nm][cid_nm][m][mod])
                        for mod in mic_cid_mod[tipo][micro_nm][cid_nm][m]}
                    for m in MARCAS_GRUPO if m in mic_cid_mod[tipo][micro_nm][cid_nm]
                }

            prop_cid = {
                p: {m: _flat(v) for m, v in mic_cid_prop[micro_nm][cid_nm][p].items()}
                for p in mic_cid_prop[micro_nm][cid_nm]
            }
            out_micro["cidades"][cid_nm] = {
                "marcas":    _cmap("ALL"),
                "marcas_vp": _cmap("VP"),
                "marcas_vu": _cmap("VU"),
                "modelos":    _cmodmap("ALL"),
                "modelos_vp": _cmodmap("VP"),
                "modelos_vu": _cmodmap("VU"),
                "prop":      prop_cid,
            }

        out["micro"][micro_nm] = out_micro

    with open(SAIDA, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))

    size_kb = os.path.getsize(SAIDA) // 1024
    if verbose:
        print(f"  Salvo: emplacamentos_2026.json ({size_kb} KB)")
        print(f"  Micro-regiões processadas: {sorted(out['micro'].keys())}")
    return True

if __name__ == "__main__":
    processar(verbose=True)
