"""
Nossas Lojas — Grupo De Marco / Tozzo
Dados extraídos do PDF de Reestruturação (Jun/2026)
Estado: Santa Catarina
"""
import json

# status: "aberta" | "abrindo"
LOJAS = [
    # ── CHAPECÓ ──────────────────────────────────────────────────────────────
    {"cidade":"Chapecó","estado":"SC","lat":-27.1004,"lng":-52.6156,"marca":"Renault",  "loja":"Renault Chapecó",         "status":"aberta"},
    {"cidade":"Chapecó","estado":"SC","lat":-27.1020,"lng":-52.6180,"marca":"GWM",      "loja":"GWM Haval Chapecó",       "status":"aberta"},
    {"cidade":"Chapecó","estado":"SC","lat":-27.1035,"lng":-52.6140,"marca":"Peugeot",  "loja":"Peugeot Chapecó",         "status":"aberta"},
    {"cidade":"Chapecó","estado":"SC","lat":-27.1050,"lng":-52.6160,"marca":"Citroën",  "loja":"Citroën Chapecó",         "status":"aberta"},
    {"cidade":"Chapecó","estado":"SC","lat":-27.1060,"lng":-52.6200,"marca":"Geely",    "loja":"Geely Chapecó",           "status":"abrindo"},
    {"cidade":"Chapecó","estado":"SC","lat":-27.1070,"lng":-52.6120,"marca":"Yamaha",   "loja":"Yamaha Chapecó",          "status":"aberta"},
    {"cidade":"Chapecó","estado":"SC","lat":-27.1080,"lng":-52.6130,"marca":"CF Moto",  "loja":"CF Off Road Chapecó",     "status":"aberta"},
    {"cidade":"Chapecó","estado":"SC","lat":-27.1090,"lng":-52.6110,"marca":"Seminovos","loja":"Seminovos Chapecó",       "status":"abrindo"},
    # ── CAÇADOR ───────────────────────────────────────────────────────────────
    {"cidade":"Caçador","estado":"SC","lat":-26.7742,"lng":-51.0139,"marca":"Renault",  "loja":"Renault Caçador",         "status":"aberta"},
    {"cidade":"Caçador","estado":"SC","lat":-26.7760,"lng":-51.0160,"marca":"Yamaha",   "loja":"Yamaha Caçador",          "status":"aberta"},
    {"cidade":"Caçador","estado":"SC","lat":-26.7780,"lng":-51.0120,"marca":"CF Moto",  "loja":"CF Off Road Caçador",     "status":"aberta"},
    # ── RIO DO SUL ────────────────────────────────────────────────────────────
    {"cidade":"Rio do Sul","estado":"SC","lat":-27.2136,"lng":-49.6431,"marca":"Renault","loja":"Renault Rio do Sul",     "status":"abrindo"},
    {"cidade":"Rio do Sul","estado":"SC","lat":-27.2150,"lng":-49.6450,"marca":"Geely",  "loja":"Geely Rio do Sul",       "status":"abrindo"},
    {"cidade":"Rio do Sul","estado":"SC","lat":-27.2160,"lng":-49.6420,"marca":"GWM",    "loja":"GWM Rio do Sul",         "status":"abrindo"},
    # ── CONCÓRDIA ─────────────────────────────────────────────────────────────
    {"cidade":"Concórdia","estado":"SC","lat":-27.2336,"lng":-52.0273,"marca":"Renault", "loja":"Renault Concórdia",      "status":"aberta"},
    # ── JOAÇABA ───────────────────────────────────────────────────────────────
    {"cidade":"Joaçaba","estado":"SC","lat":-27.1750,"lng":-51.5070,"marca":"Renault",   "loja":"Renault Joaçaba",        "status":"aberta"},
    {"cidade":"Joaçaba","estado":"SC","lat":-27.1760,"lng":-51.5090,"marca":"Geely",     "loja":"Geely Joaçaba",          "status":"abrindo"},
    {"cidade":"Joaçaba","estado":"SC","lat":-27.1770,"lng":-51.5060,"marca":"GWM",       "loja":"GWM Joaçaba",            "status":"abrindo"},
    {"cidade":"Joaçaba","estado":"SC","lat":-27.1780,"lng":-51.5080,"marca":"Seminovos", "loja":"Seminovos Joaçaba",      "status":"abrindo"},
    # ── BLUMENAU ──────────────────────────────────────────────────────────────
    {"cidade":"Blumenau","estado":"SC","lat":-26.9194,"lng":-49.0661,"marca":"Renault",  "loja":"Renault Blumenau",       "status":"aberta"},
    {"cidade":"Blumenau","estado":"SC","lat":-26.9210,"lng":-49.0680,"marca":"Geely",    "loja":"Geely Blumenau",         "status":"abrindo"},
    {"cidade":"Blumenau","estado":"SC","lat":-26.9220,"lng":-49.0645,"marca":"Triumph",  "loja":"Triumph Blumenau",       "status":"abrindo"},
    # ── CANOINHAS ─────────────────────────────────────────────────────────────
    {"cidade":"Canoinhas","estado":"SC","lat":-26.1806,"lng":-50.3897,"marca":"Renault", "loja":"Renault Canoinhas",      "status":"abrindo"},
    # ── CRICIÚMA ──────────────────────────────────────────────────────────────
    {"cidade":"Criciúma","estado":"SC","lat":-28.6777,"lng":-49.3700,"marca":"Triumph",  "loja":"Triumph Criciúma",       "status":"abrindo"},
    # ── SÃO MIGUEL DO OESTE ───────────────────────────────────────────────────
    {"cidade":"São Miguel do Oeste","estado":"SC","lat":-26.7256,"lng":-53.5135,"marca":"Renault","loja":"Renault São Miguel do Oeste","status":"aberta"},
    # ── LAGES ─────────────────────────────────────────────────────────────────
    {"cidade":"Lages","estado":"SC","lat":-27.8158,"lng":-50.3264,"marca":"Renault",     "loja":"Renault Lages",          "status":"aberta"},
    # ── TUBARÃO ───────────────────────────────────────────────────────────────
    {"cidade":"Tubarão","estado":"SC","lat":-28.4673,"lng":-49.0089,"marca":"GWM",       "loja":"GWM Tubarão",            "status":"abrindo"},
    # ── VIDEIRA ───────────────────────────────────────────────────────────────
    {"cidade":"Videira","estado":"SC","lat":-27.0046,"lng":-51.1538,"marca":"Outlet",    "loja":"Outlet De Marco / Tozzo Videira","status":"abrindo"},
]

COR_MARCA = {
    "Renault":  "#f2c200",
    "GWM":      "#c00020",
    "Peugeot":  "#1a3a6b",
    "Citroën":  "#e05a00",
    "Geely":    "#0050b0",
    "Yamaha":   "#003087",
    "Triumph":  "#7c0000",
    "CF Moto":  "#e04000",
    "Seminovos":"#059669",
    "Outlet":   "#7c3aed",
}

def gerar_secao():
    lojas_json  = json.dumps(LOJAS, ensure_ascii=False)
    cores_json  = json.dumps(COR_MARCA, ensure_ascii=False)

    resumo = {}
    for l in LOJAS:
        m = l["marca"]
        if m not in resumo:
            resumo[m] = {"aberta":0,"abrindo":0}
        resumo[m][l["status"]] += 1

    cards_resumo = ""
    for marca, cnt in resumo.items():
        cor = COR_MARCA.get(marca,"#374151")
        tag_abrindo = f'<div style="text-align:center"><div style="font-size:20px;font-weight:800;color:#f59e0b">{cnt["abrindo"]}</div><div style="font-size:10px;color:#6b7280;text-transform:uppercase">Em abertura</div></div>' if cnt["abrindo"] else ""
        cards_resumo += f"""
<div style="background:#fff;border-radius:12px;border-top:4px solid {cor};padding:14px 18px;box-shadow:0 2px 8px rgba(0,0,0,.07);min-width:130px">
  <div style="font-size:10px;font-weight:700;color:{cor};text-transform:uppercase;letter-spacing:1px;margin-bottom:8px">{marca}</div>
  <div style="display:flex;gap:14px;align-items:center">
    <div style="text-align:center">
      <div style="font-size:22px;font-weight:800;color:#1e293b">{cnt['aberta']}</div>
      <div style="font-size:10px;color:#6b7280;text-transform:uppercase">Abertas</div>
    </div>
    {tag_abrindo}
  </div>
</div>"""

    total_abertas = sum(1 for l in LOJAS if l["status"]=="aberta")
    total_abrindo = sum(1 for l in LOJAS if l["status"]=="abrindo")
    cidades = len(set(l["cidade"] for l in LOJAS))

    return f"""
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div style="padding:28px 32px;max-width:1400px;margin:0 auto">

  <!-- Totalizadores -->
  <div style="display:flex;gap:14px;margin-bottom:22px;flex-wrap:wrap">
    <div style="background:#fff;border-radius:12px;padding:18px 24px;border-left:4px solid #10b981;box-shadow:0 2px 8px rgba(0,0,0,.07);min-width:120px">
      <div style="font-size:28px;font-weight:800;color:#1e293b">{total_abertas}</div>
      <div style="font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Lojas Abertas</div>
    </div>
    <div style="background:#fff;border-radius:12px;padding:18px 24px;border-left:4px solid #f59e0b;box-shadow:0 2px 8px rgba(0,0,0,.07);min-width:120px">
      <div style="font-size:28px;font-weight:800;color:#1e293b">{total_abrindo}</div>
      <div style="font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Em Abertura</div>
    </div>
    <div style="background:#fff;border-radius:12px;padding:18px 24px;border-left:4px solid #6366f1;box-shadow:0 2px 8px rgba(0,0,0,.07);min-width:120px">
      <div style="font-size:28px;font-weight:800;color:#1e293b">{total_abertas+total_abrindo}</div>
      <div style="font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Total de Lojas</div>
    </div>
    <div style="background:#fff;border-radius:12px;padding:18px 24px;border-left:4px solid #0ea5e9;box-shadow:0 2px 8px rgba(0,0,0,.07);min-width:120px">
      <div style="font-size:28px;font-weight:800;color:#1e293b">{cidades}</div>
      <div style="font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Cidades SC</div>
    </div>
    <div style="background:#fff;border-radius:12px;padding:18px 24px;border-left:4px solid #ec4899;box-shadow:0 2px 8px rgba(0,0,0,.07);min-width:120px">
      <div style="font-size:28px;font-weight:800;color:#1e293b">31</div>
      <div style="font-size:11px;color:#6b7280;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-top:3px">Meta Total</div>
    </div>
  </div>

  <!-- Cards por marca -->
  <div style="display:flex;flex-wrap:wrap;gap:12px;margin-bottom:26px">
    {cards_resumo}
  </div>

  <!-- Mapa -->
  <div style="background:#fff;border-radius:14px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;margin-bottom:24px">
    <div style="padding:14px 22px;border-bottom:1px solid #f1f5f9;display:flex;align-items:center;gap:16px;flex-wrap:wrap">
      <span style="font-size:13px;font-weight:700;color:#374151;text-transform:uppercase;letter-spacing:.5px">Mapa — Santa Catarina</span>
      <span style="font-size:12px;padding:3px 12px;border-radius:20px;background:#dcfce7;color:#166534;font-weight:600">● Aberta</span>
      <span style="font-size:12px;padding:3px 12px;border-radius:20px;background:#fef3c7;color:#92400e;font-weight:600">◐ Em abertura</span>
      <span style="font-size:11px;color:#9ca3af">Clique nos marcadores para detalhes</span>
    </div>
    <div id="mapa-lojas" style="height:500px;width:100%"></div>
  </div>

  <!-- Tabela -->
  <div style="background:#fff;border-radius:14px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden">
    <div style="padding:14px 22px;border-bottom:1px solid #f1f5f9;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px">
      <span style="font-size:13px;font-weight:700;color:#374151;text-transform:uppercase;letter-spacing:.5px">Lista de Lojas</span>
      <div style="display:flex;gap:8px">
        <button onclick="filtrarTabela('todas')" style="padding:5px 14px;border-radius:20px;border:1px solid #e5e7eb;background:#fff;cursor:pointer;font-size:12px;font-weight:600">Todas</button>
        <button onclick="filtrarTabela('aberta')" style="padding:5px 14px;border-radius:20px;border:none;background:#dcfce7;color:#166534;cursor:pointer;font-size:12px;font-weight:600">Abertas</button>
        <button onclick="filtrarTabela('abrindo')" style="padding:5px 14px;border-radius:20px;border:none;background:#fef3c7;color:#92400e;cursor:pointer;font-size:12px;font-weight:600">Em abertura</button>
      </div>
    </div>
    <div style="overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:13px">
        <thead>
          <tr style="background:#f8fafc">
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Loja</th>
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Marca</th>
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Cidade</th>
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Status</th>
          </tr>
        </thead>
        <tbody id="tabela-lojas-body"></tbody>
      </table>
    </div>
  </div>
</div>

<script>
const COR_MARCA_L = {cores_json};
const LOJAS_DATA  = {lojas_json};

// ── Mapa ──────────────────────────────────────────────────────────────────
const map = L.map('mapa-lojas').setView([-27.4,-50.8],7);
L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png',{{attribution:'© OpenStreetMap contributors'}}).addTo(map);

function svgPin(cor, aberta){{
  const op   = aberta ? '1' : '0.6';
  const dash = aberta ? '' : 'stroke-dasharray="5 3"';
  return `<svg xmlns="http://www.w3.org/2000/svg" width="34" height="44" viewBox="0 0 34 44">
    <path d="M17 0C7.6 0 0 7.6 0 17c0 13 17 27 17 27S34 30 34 17C34 7.6 26.4 0 17 0z"
      fill="${{cor}}" opacity="${{op}}" stroke="#fff" stroke-width="2.5" ${{dash}}/>
    <circle cx="17" cy="17" r="7" fill="#fff" opacity=".95"/>
  </svg>`;
}}

LOJAS_DATA.forEach(l => {{
  const cor   = COR_MARCA_L[l.marca] || '#374151';
  const aberta= l.status === 'aberta';
  const icon  = L.divIcon({{html:svgPin(cor,aberta),iconSize:[34,44],iconAnchor:[17,44],popupAnchor:[0,-44],className:''}});
  const badge = aberta
    ? '<span style="background:#dcfce7;color:#166534;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700">● Aberta</span>'
    : '<span style="background:#fef3c7;color:#92400e;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700">◐ Em abertura</span>';
  L.marker([l.lat,l.lng],{{icon}})
   .bindPopup(`<div style="font-family:Segoe UI,sans-serif;min-width:180px;padding:4px">
     <div style="font-weight:700;font-size:14px;color:#1e293b;margin-bottom:2px">${{l.loja}}</div>
     <div style="font-size:12px;color:#6b7280;margin-bottom:8px">${{l.cidade}} — SC</div>
     ${{badge}}
   </div>`)
   .addTo(map);
}});

// ── Tabela ────────────────────────────────────────────────────────────────
function renderTabela(filtro){{
  const tbody = document.getElementById('tabela-lojas-body');
  tbody.innerHTML = '';
  const lista = filtro === 'todas' ? LOJAS_DATA : LOJAS_DATA.filter(l => l.status === filtro);
  lista.forEach((l,i) => {{
    const cor  = COR_MARCA_L[l.marca] || '#374151';
    const tag  = l.status === 'aberta'
      ? '<span style="background:#dcfce7;color:#166534;padding:3px 12px;border-radius:10px;font-size:11px;font-weight:700">● Aberta</span>'
      : '<span style="background:#fef3c7;color:#92400e;padding:3px 12px;border-radius:10px;font-size:11px;font-weight:700">◐ Em abertura</span>';
    tbody.innerHTML += `<tr style="background:${{i%2===0?'#fff':'#f9fafb'}}">
      <td style="padding:11px 16px;font-weight:600;color:#1e293b;border-bottom:1px solid #f1f5f9">${{l.loja}}</td>
      <td style="padding:11px 16px;border-bottom:1px solid #f1f5f9"><span style="background:${{cor}};color:#fff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700">${{l.marca}}</span></td>
      <td style="padding:11px 16px;color:#374151;border-bottom:1px solid #f1f5f9">${{l.cidade}}</td>
      <td style="padding:11px 16px;border-bottom:1px solid #f1f5f9">${{tag}}</td>
    </tr>`;
  }});
}}
function filtrarTabela(f){{ renderTabela(f); }}
renderTabela('todas');
</script>
"""
