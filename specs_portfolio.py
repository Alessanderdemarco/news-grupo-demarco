# ─── specs_portfolio.py ───────────────────────────────────────────────────────
# Portfólio baseado nos modelos DISPONÍVEIS NOS SITES OFICIAIS das montadoras no Brasil
# Última verificação automática: renault.com.br | carros.peugeot.com.br |
#   citroen.com.br | gwm.com.br (fallback) | geelybrasil.com.br
#
# Critérios de concorrência (score 0-100):
#   carroceria     → +40 pts  (obrigatório — sem match não entra)
#   faixa_preco    → +30 pts  (±30% de sobreposição)
#   faixa_potencia → +20 pts  (±35% de sobreposição)
#   motorizacao    → +10 pts  (compatibilidade entre grupos)
# Limiar para "concorre": score >= 60

# ── Grupos de carroceria ─────────────────────────────────────────────────────

GRUPOS_CARROCERIA = {
    "hatch":     ["hatch", "hatchback"],
    "sedan":     ["sedan", "sedã", "fastback"],
    "suv":       ["suv", "crossover", "suv coupe", "suv off-road"],
    "picape":    ["picape", "pickup", "pick-up"],
    "minivan":   ["minivan", "van", "monovolume"],
    "perua":     ["perua", "sw", "station wagon"],
    "naked":     ["naked", "roadster", "streetfighter"],
    "adventure": ["adventure", "trail", "enduro"],
    "scooter":   ["scooter", "maxi-scooter"],
    "esportiva": ["esportiva", "supersport"],
    "custom":    ["custom", "cruiser", "chopper"],
    "touring":   ["touring", "gt moto"],
}

# ── Compatibilidade de motorização ───────────────────────────────────────────

COMPATIBILIDADE_MOTORIZACAO = {
    "combustao":    ["combustao", "hibrido_leve"],
    "hibrido_leve": ["combustao", "hibrido_leve", "hibrido"],
    "hibrido":      ["hibrido_leve", "hibrido", "combustao"],
    "eletrico":     ["eletrico", "hibrido"],
}

LABEL_MOTORIZACAO = {
    "combustao":    "Combustão",
    "hibrido_leve": "Híbrido Leve",
    "hibrido":      "Híbrido / PHEV",
    "eletrico":     "Elétrico",
}

# ── Portfólio de marcas ───────────────────────────────────────────────────────

PORTFOLIO = {
    "Renault": {
        "tipo": "carro",
        "modelos": ["Kwid", "Kardian", "Duster", "Oroch", "Boreal", "Niagara", "Kangoo", "Master"],
        # Koleos e Megane saíram de linha no Brasil
    },
    "GWM": {
        "tipo": "carro",
        "modelos": ["Haval H6", "Haval H9", "Haval Jolion", "Tank 300", "Tank 500", "Ora 03"],
        "aliases": ["Haval", "Tank", "Ora"],
    },
    "Peugeot": {
        "tipo": "carro",
        "modelos": ["208", "2008", "Partner", "Expert", "Boxer"],
    },
    "Citroen": {
        "tipo": "carro",
        "aliases": ["Citroën", "Citroen"],
        "modelos": ["C3", "Aircross", "Basalt"],
    },
    "Geely": {
        "tipo": "carro",
        "modelos": ["EX2", "EX5", "EX5 EM-I"],
    },
    "CF Moto": {
        "tipo": "moto",
        "aliases": ["CFMoto", "CF-Moto"],
        "modelos": ["300NK", "400NK", "650NK", "650MT", "700CL-X", "800MT", "1000NK"],
    },
    "Yamaha": {
        "tipo": "moto",
        "modelos": ["MT-03", "MT-07", "MT-09", "R3", "XMAX", "Fazer", "Lander", "Crosser", "Nmax"],
    },
    "Triumph": {
        "tipo": "moto",
        "modelos": ["Street Triple", "Tiger", "Bonneville", "Scrambler", "Rocket", "Speed Twin", "Trident"],
    },
}

# ── Especificações dos modelos (carros de passeio/SUV) ────────────────────────
# potencia_min/max em cv | preco_from/to em R$

SPECS = {
    # ── RENAULT ───────────────────────────────────────────────────────────────
    "Renault Kwid": {
        "marca": "Renault", "carroceria": "hatch",
        "preco_from": 82790,  "preco_to": 100990,
        "potencia_min": 68,   "potencia_max": 71,
        "motor": "1.0 SCe", "potencia": "68–71 cv", "torque": "9,5 kgfm",
        "cambio": "Manual 5v / CVT", "tracao": "FWD",
        "segmento_label": "Hatch Entry", "motorizacao": "combustao",
    },
    "Renault Kardian": {
        "marca": "Renault", "carroceria": "suv",
        "preco_from": 113690, "preco_to": 149990,
        "potencia_min": 125,  "potencia_max": 125,
        "motor": "1.0 TCe Turbo", "potencia": "125 cv", "torque": "20 kgfm",
        "cambio": "Manual 6v / CVT", "tracao": "FWD",
        "segmento_label": "SUV Compacto", "motorizacao": "combustao",
    },
    "Renault Duster": {
        "marca": "Renault", "carroceria": "suv",
        "preco_from": 131990, "preco_to": 189990,
        "potencia_min": 130,  "potencia_max": 163,
        "motor": "1.3 TCe / 1.6 16V", "potencia": "130–163 cv", "torque": "24–26 kgfm",
        "cambio": "Manual / CVT / Auto 6v", "tracao": "FWD / 4x4",
        "segmento_label": "SUV Compacto / Médio", "motorizacao": "combustao",
    },
    "Renault Oroch": {
        "marca": "Renault", "carroceria": "picape",
        "preco_from": 139990, "preco_to": 189990,
        "potencia_min": 112,  "potencia_max": 163,
        "motor": "1.3 TCe / 2.0 16V", "potencia": "112–163 cv", "torque": "20–26 kgfm",
        "cambio": "Manual / Auto 6v", "tracao": "FWD / 4x4",
        "segmento_label": "Picape Compacta", "motorizacao": "combustao",
    },
    "Renault Boreal": {
        "marca": "Renault", "carroceria": "suv",
        "preco_from": 179990, "preco_to": 219990,
        "potencia_min": 163,  "potencia_max": 163,
        "motor": "1.3 TCe", "potencia": "163 cv", "torque": "27 kgfm",
        "cambio": "Auto 7v EDC", "tracao": "FWD",
        "segmento_label": "SUV Médio", "motorizacao": "combustao",
    },
    "Renault Niagara": {
        "marca": "Renault", "carroceria": "picape",
        "preco_from": 219990, "preco_to": 249990,
        "potencia_min": 163,  "potencia_max": 163,
        "motor": "1.3 TCe", "potencia": "163 cv", "torque": "27 kgfm",
        "cambio": "Auto 7v EDC", "tracao": "4x4",
        "segmento_label": "Picape Média", "motorizacao": "combustao",
    },
    # ── GWM / HAVAL / TANK / ORA ──────────────────────────────────────────────
    "Haval H6": {
        "marca": "GWM", "carroceria": "suv",
        "preco_from": 199990, "preco_to": 249990,
        "potencia_min": 169,  "potencia_max": 238,
        "motor": "1.5T / 2.0T", "potencia": "169–238 cv", "torque": "28–39 kgfm",
        "cambio": "Auto 7v DCT", "tracao": "FWD / AWD",
        "segmento_label": "SUV Médio", "motorizacao": "combustao",
    },
    "Haval H9": {
        "marca": "GWM", "carroceria": "suv",
        "preco_from": 319990, "preco_to": 369990,
        "potencia_min": 218,  "potencia_max": 218,
        "motor": "2.0T", "potencia": "218 cv", "torque": "35 kgfm",
        "cambio": "Auto 8v", "tracao": "4x4",
        "segmento_label": "SUV Grande Off-road", "motorizacao": "combustao",
    },
    "Haval Jolion": {
        "marca": "GWM", "carroceria": "suv",
        "preco_from": 164990, "preco_to": 194990,
        "potencia_min": 147,  "potencia_max": 147,
        "motor": "1.5T", "potencia": "147 cv", "torque": "22 kgfm",
        "cambio": "Auto 7v DCT", "tracao": "FWD",
        "segmento_label": "SUV Compacto", "motorizacao": "combustao",
    },
    "Tank 300": {
        "marca": "GWM", "carroceria": "suv",
        "preco_from": 349990, "preco_to": 389990,
        "potencia_min": 227,  "potencia_max": 227,
        "motor": "2.0T", "potencia": "227 cv", "torque": "38 kgfm",
        "cambio": "Auto 8v", "tracao": "4x4",
        "segmento_label": "SUV Off-road", "motorizacao": "combustao",
    },
    "Tank 500": {
        "marca": "GWM", "carroceria": "suv",
        "preco_from": 469990, "preco_to": 499990,
        "potencia_min": 449,  "potencia_max": 449,
        "motor": "3.0T V6 PHEV", "potencia": "449 cv", "torque": "76 kgfm",
        "cambio": "Auto 9v", "tracao": "4x4",
        "segmento_label": "SUV Grande PHEV", "motorizacao": "hibrido",
    },
    "Ora 03": {
        "marca": "GWM", "carroceria": "hatch",
        "preco_from": 179990, "preco_to": 209990,
        "potencia_min": 143,  "potencia_max": 204,
        "motor": "Elétrico", "potencia": "143–204 cv", "torque": "21–34 kgfm",
        "cambio": "Direto", "tracao": "FWD",
        "segmento_label": "Hatch Elétrico", "motorizacao": "eletrico",
    },
    # ── PEUGEOT ───────────────────────────────────────────────────────────────
    "Peugeot 208": {
        "marca": "Peugeot", "carroceria": "hatch",
        "preco_from": 104990, "preco_to": 134990,
        "potencia_min": 100,  "potencia_max": 122,
        "motor": "1.0 Turbo / 1.6 16V", "potencia": "100–122 cv", "torque": "17–16 kgfm",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "segmento_label": "Hatch Compacto", "motorizacao": "combustao",
    },
    "Peugeot 2008": {
        "marca": "Peugeot", "carroceria": "suv",
        "preco_from": 134990, "preco_to": 174990,
        "potencia_min": 130,  "potencia_max": 130,
        "motor": "1.0 Turbo", "potencia": "130 cv", "torque": "20 kgfm",
        "cambio": "Auto 6v", "tracao": "FWD",
        "segmento_label": "SUV Compacto", "motorizacao": "combustao",
    },
    # ── CITROËN ───────────────────────────────────────────────────────────────
    "Citroen C3": {
        "marca": "Citroen", "carroceria": "hatch",
        "preco_from": 94990,  "preco_to": 119990,
        "potencia_min": 75,   "potencia_max": 100,
        "motor": "1.0 / 1.0 Turbo", "potencia": "75–100 cv", "torque": "10–17 kgfm",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "segmento_label": "Hatch Compacto", "motorizacao": "combustao",
    },
    "Citroen Aircross": {
        "marca": "Citroen", "carroceria": "suv",
        "preco_from": 119990, "preco_to": 154990,
        "potencia_min": 130,  "potencia_max": 130,
        "motor": "1.0 Turbo", "potencia": "130 cv", "torque": "20 kgfm",
        "cambio": "Auto 6v", "tracao": "FWD",
        "segmento_label": "SUV Compacto", "motorizacao": "combustao",
    },
    "Citroen Basalt": {
        "marca": "Citroen", "carroceria": "suv",
        "preco_from": 109990, "preco_to": 139990,
        "potencia_min": 75,   "potencia_max": 130,
        "motor": "1.0 / 1.0 Turbo", "potencia": "75–130 cv", "torque": "10–20 kgfm",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "segmento_label": "SUV Compacto Entry", "motorizacao": "combustao",
    },
    # ── GEELY ─────────────────────────────────────────────────────────────────
    "Geely EX2": {
        "marca": "Geely", "carroceria": "hatch",
        "preco_from": 149990, "preco_to": 179990,
        "potencia_min": 95,   "potencia_max": 95,
        "motor": "Elétrico", "potencia": "95 cv", "torque": "15 kgfm",
        "cambio": "Direto", "tracao": "FWD",
        "segmento_label": "Hatch Elétrico Compacto", "motorizacao": "eletrico",
    },
    "Geely EX5": {
        "marca": "Geely", "carroceria": "suv",
        "preco_from": 199990, "preco_to": 239990,
        "potencia_min": 218,  "potencia_max": 218,
        "motor": "Elétrico", "potencia": "218 cv", "torque": "32 kgfm",
        "cambio": "Direto", "tracao": "FWD",
        "segmento_label": "SUV Elétrico Compacto", "motorizacao": "eletrico",
    },
    "Geely EX5 EM-I": {
        "marca": "Geely", "carroceria": "suv",
        "preco_from": 219990, "preco_to": 259990,
        "potencia_min": 326,  "potencia_max": 326,
        "motor": "1.5T + Elétrico PHEV", "potencia": "326 cv", "torque": "50 kgfm",
        "cambio": "Direto (PHEV)", "tracao": "AWD",
        "segmento_label": "SUV Compacto PHEV", "motorizacao": "hibrido",
    },
    # ── CF MOTO ───────────────────────────────────────────────────────────────
    "CF Moto 300NK": {
        "marca": "CF Moto", "carroceria": "naked",
        "preco_from": 18990,  "preco_to": 18990,
        "potencia_min": 25,   "potencia_max": 25,
        "motor": "300cc mono", "potencia": "25 cv", "torque": "2,5 kgfm",
        "cambio": "Manual 6v", "tracao": "Corrente",
        "segmento_label": "Naked Entry", "motorizacao": "combustao",
    },
    "CF Moto 650NK": {
        "marca": "CF Moto", "carroceria": "naked",
        "preco_from": 34990,  "preco_to": 34990,
        "potencia_min": 61,   "potencia_max": 61,
        "motor": "649cc bi", "potencia": "61 cv", "torque": "6,3 kgfm",
        "cambio": "Manual 6v", "tracao": "Corrente",
        "segmento_label": "Naked Médio", "motorizacao": "combustao",
    },
    "CF Moto 650MT": {
        "marca": "CF Moto", "carroceria": "adventure",
        "preco_from": 39990,  "preco_to": 39990,
        "potencia_min": 61,   "potencia_max": 61,
        "motor": "649cc bi", "potencia": "61 cv", "torque": "6,3 kgfm",
        "cambio": "Manual 6v", "tracao": "Corrente",
        "segmento_label": "Adventure Médio", "motorizacao": "combustao",
    },
    "CF Moto 800MT": {
        "marca": "CF Moto", "carroceria": "adventure",
        "preco_from": 59990,  "preco_to": 64990,
        "potencia_min": 95,   "potencia_max": 95,
        "motor": "799cc bi", "potencia": "95 cv", "torque": "8,5 kgfm",
        "cambio": "Manual 6v", "tracao": "Corrente",
        "segmento_label": "Adventure Grande", "motorizacao": "combustao",
    },
    # ── YAMAHA ────────────────────────────────────────────────────────────────
    "Yamaha MT-03": {
        "marca": "Yamaha", "carroceria": "naked",
        "preco_from": 34990,  "preco_to": 34990,
        "potencia_min": 42,   "potencia_max": 42,
        "motor": "321cc bi", "potencia": "42 cv", "torque": "3,0 kgfm",
        "cambio": "Manual 6v", "tracao": "Corrente",
        "segmento_label": "Naked Médio", "motorizacao": "combustao",
    },
    "Yamaha Lander": {
        "marca": "Yamaha", "carroceria": "adventure",
        "preco_from": 32990,  "preco_to": 35990,
        "potencia_min": 24,   "potencia_max": 24,
        "motor": "249cc mono", "potencia": "24,6 cv", "torque": "2,1 kgfm",
        "cambio": "Manual 5v", "tracao": "Corrente",
        "segmento_label": "Trail Médio", "motorizacao": "combustao",
    },
    "Yamaha XMAX": {
        "marca": "Yamaha", "carroceria": "scooter",
        "preco_from": 39990,  "preco_to": 39990,
        "potencia_min": 28,   "potencia_max": 28,
        "motor": "292cc mono", "potencia": "28 cv", "torque": "2,8 kgfm",
        "cambio": "Auto CVT", "tracao": "Corrente",
        "segmento_label": "Scooter GT", "motorizacao": "combustao",
    },
    # ── TRIUMPH ───────────────────────────────────────────────────────────────
    "Triumph Street Triple": {
        "marca": "Triumph", "carroceria": "naked",
        "preco_from": 79990,  "preco_to": 109990,
        "potencia_min": 120,  "potencia_max": 130,
        "motor": "765cc tri", "potencia": "120–130 cv", "torque": "7,9 kgfm",
        "cambio": "Manual 6v", "tracao": "Corrente",
        "segmento_label": "Naked Esportivo", "motorizacao": "combustao",
    },
    "Triumph Tiger 900": {
        "marca": "Triumph", "carroceria": "adventure",
        "preco_from": 99990,  "preco_to": 129990,
        "potencia_min": 95,   "potencia_max": 95,
        "motor": "888cc tri", "potencia": "95 cv", "torque": "8,7 kgfm",
        "cambio": "Manual 6v", "tracao": "Corrente",
        "segmento_label": "Adventure Grande", "motorizacao": "combustao",
    },
    "Triumph Bonneville": {
        "marca": "Triumph", "carroceria": "custom",
        "preco_from": 74990,  "preco_to": 99990,
        "potencia_min": 65,   "potencia_max": 105,
        "motor": "900–1200cc bi", "potencia": "65–105 cv", "torque": "8–11 kgfm",
        "cambio": "Manual 5–6v", "tracao": "Corrente",
        "segmento_label": "Roadster Clássico", "motorizacao": "combustao",
    },
}

# ── Motor de concorrência ─────────────────────────────────────────────────────

def _grupo_carroceria(carroceria):
    c = carroceria.lower().strip()
    for grupo, variantes in GRUPOS_CARROCERIA.items():
        if c == grupo or c in variantes:
            return grupo
    for grupo, variantes in GRUPOS_CARROCERIA.items():
        if any(v in c for v in variantes) or any(c in v for v in variantes):
            return grupo
    return c

def _sobreposicao(min1, max1, v2, tolerancia):
    if v2 is None:
        return True
    return (min1 * (1 - tolerancia)) <= v2 <= (max1 * (1 + tolerancia))

def pontuar_concorrencia(spec, carroceria_lanc, preco_lanc, potencia_lanc, motorizacao_lanc):
    score = 0
    motivos = []

    # Carroceria — obrigatório
    if _grupo_carroceria(spec["carroceria"]) != _grupo_carroceria(carroceria_lanc):
        return 0, []
    score += 40
    motivos.append(f"mesma carroceria ({_grupo_carroceria(carroceria_lanc)})")

    # Preço ±30%
    if preco_lanc:
        if _sobreposicao(spec["preco_from"], spec["preco_to"], preco_lanc, 0.30):
            score += 30
            motivos.append("faixa de preço compatível")
        # sem sobreposição — não penaliza mas não soma
    else:
        score += 15
        motivos.append("preço não identificado")

    # Potência ±35%
    if potencia_lanc:
        if _sobreposicao(spec["potencia_min"], spec["potencia_max"], potencia_lanc, 0.35):
            score += 20
            motivos.append("potência compatível")
    else:
        score += 10

    # Motorização
    mot_compat = COMPATIBILIDADE_MOTORIZACAO.get(motorizacao_lanc, [motorizacao_lanc])
    if spec["motorizacao"] in mot_compat:
        score += 10
        motivos.append(f"motorização compatível ({LABEL_MOTORIZACAO.get(motorizacao_lanc,'')})")

    return score, motivos

def encontrar_concorrentes(carroceria_lanc, preco_lanc, potencia_lanc, motorizacao_lanc, limiar=60):
    if not carroceria_lanc:
        return []
    resultados = []
    for nome, spec in SPECS.items():
        score, motivos = pontuar_concorrencia(spec, carroceria_lanc, preco_lanc, potencia_lanc, motorizacao_lanc)
        if score >= limiar:
            resultados.append((nome, score, motivos))
    resultados.sort(key=lambda x: x[1], reverse=True)
    return resultados

def get_spec(modelo):
    return SPECS.get(modelo)

def fmt_preco(p_from, p_to):
    if p_from == p_to:
        return f"R$ {p_from:,.0f}".replace(",", ".")
    return f"R$ {p_from:,.0f} – {p_to:,.0f}".replace(",", ".")
