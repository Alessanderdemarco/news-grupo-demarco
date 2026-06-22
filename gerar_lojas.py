"""
Gera a seção HTML da aba Nossas Lojas.
Edite a lista LOJAS abaixo com as cidades e marcas reais do grupo.
"""

# ─── EDITE AQUI ──────────────────────────────────────────────────────────────
# status: "aberta" | "abrindo"
# lat/lng: coordenadas GPS da cidade (use maps.google.com para obter)

LOJAS = [
    # ── Chapecó (SC) ──────────────────────────────────────────────────────────
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1004, "lng": -52.6156,
     "marca": "Renault",  "loja": "Demarco Renault Chapecó",   "status": "aberta"},
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1020, "lng": -52.6180,
     "marca": "GWM",      "loja": "Demarco GWM Chapecó",       "status": "aberta"},
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1035, "lng": -52.6140,
     "marca": "Peugeot",  "loja": "Demarco Peugeot Chapecó",   "status": "aberta"},
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1050, "lng": -52.6160,
     "marca": "Citroen",  "loja": "Demarco Citroen Chapecó",   "status": "aberta"},
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1060, "lng": -52.6200,
     "marca": "Geely",    "loja": "Demarco Geely Chapecó",     "status": "aberta"},
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1070, "lng": -52.6120,
     "marca": "Yamaha",   "loja": "Tozzo Yamaha Chapecó",      "status": "aberta"},
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1080, "lng": -52.6130,
     "marca": "Triumph",  "loja": "Tozzo Triumph Chapecó",     "status": "aberta"},
    # ── Xanxerê (SC) ──────────────────────────────────────────────────────────
    {"cidade": "Xanxerê", "estado": "SC", "lat": -26.8759, "lng": -52.4036,
     "marca": "Renault",  "loja": "Demarco Renault Xanxerê",   "status": "aberta"},
    {"cidade": "Xanxerê", "estado": "SC", "lat": -26.8780, "lng": -52.4060,
     "marca": "GWM",      "loja": "Demarco GWM Xanxerê",       "status": "abrindo"},
    # ── Concórdia (SC) ────────────────────────────────────────────────────────
    {"cidade": "Concórdia", "estado": "SC", "lat": -27.2336, "lng": -52.0273,
     "marca": "Renault",  "loja": "Demarco Renault Concórdia", "status": "aberta"},
    {"cidade": "Concórdia", "estado": "SC", "lat": -27.2350, "lng": -52.0290,
     "marca": "GWM",      "loja": "Demarco GWM Concórdia",     "status": "abrindo"},
    # ── Joaçaba (SC) ──────────────────────────────────────────────────────────
    {"cidade": "Joaçaba", "estado": "SC", "lat": -27.1750, "lng": -51.5070,
     "marca": "Peugeot",  "loja": "Demarco Peugeot Joaçaba",  "status": "aberta"},
    {"cidade": "Joaçaba", "estado": "SC", "lat": -27.1760, "lng": -51.5090,
     "marca": "Citroen",  "loja": "Demarco Citroen Joaçaba",  "status": "abrindo"},
    # ── CF Moto ───────────────────────────────────────────────────────────────
    {"cidade": "Chapecó", "estado": "SC", "lat": -27.1090, "lng": -52.6110,
     "marca": "CF Moto",  "loja": "Tozzo CF Moto Chapecó",     "status": "aberta"},
]
# ─────────────────────────────────────────────────────────────────────────────

COR_MARCA = {
    "Renault":  "#f2c200",
    "GWM":      "#c00020",
    "Peugeot":  "#1a3a6b",
    "Citroen":  "#e05a00",
    "Geely":    "#0050b0",
    "Yamaha":   "#003087",
    "Triumph":  "#8b0000",
    "CF Moto":  "#e04000",
}

def gerar_secao():
    # Constrói JSON das lojas para o JS
    import json
    lojas_json = json.dumps(LOJAS, ensure_ascii=False)

    # Resumo por marca
    resumo = {}
    for l in LOJAS:
        m = l["marca"]
        if m not in resumo:
            resumo[m] = {"aberta": 0, "abrindo": 0}
        resumo[m][l["status"]] += 1

    cards_resumo = ""
    for marca, cnt in resumo.items():
        cor = COR_MARCA.get(marca, "#374151")
        cards_resumo += f"""
<div style="background:#fff;border-radius:12px;border-top:4px solid {cor};padding:16px 20px;min-width:150px;box-shadow:0 2px 8px rgba(0,0,0,.07)">
  <div style="font-size:11px;font-weight:700;color:{cor};text-transform:uppercase;letter-spacing:1px;margin-bottom:6px">{marca}</div>
  <div style="display:flex;gap:12px;align-items:center">
    <div style="text-align:center">
      <div style="font-size:22px;font-weight:800;color:#1e293b">{cnt['aberta']}</div>
      <div style="font-size:10px;color:#6b7280">Abertas</div>
    </div>
    {'<div style="text-align:center"><div style="font-size:22px;font-weight:800;color:#f59e0b">'+str(cnt["abrindo"])+'</div><div style="font-size:10px;color:#6b7280">Em abertura</div></div>' if cnt['abrindo'] else ''}
  </div>
</div>"""

    total_abertas  = sum(1 for l in LOJAS if l["status"] == "aberta")
    total_abrindo  = sum(1 for l in LOJAS if l["status"] == "abrindo")
    cidades        = len(set(l["cidade"] for l in LOJAS))

    return f"""
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"/>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<div style="padding:28px 32px;max-width:1400px;margin:0 auto">

  <!-- Totalizadores -->
  <div style="display:flex;gap:16px;margin-bottom:24px;flex-wrap:wrap">
    <div class="loja-stat" style="--c:#10b981">
      <div class="loja-stat-num">{total_abertas}</div>
      <div class="loja-stat-label">Lojas Abertas</div>
    </div>
    <div class="loja-stat" style="--c:#f59e0b">
      <div class="loja-stat-num">{total_abrindo}</div>
      <div class="loja-stat-label">Em Abertura</div>
    </div>
    <div class="loja-stat" style="--c:#6366f1">
      <div class="loja-stat-num">{total_abertas + total_abrindo}</div>
      <div class="loja-stat-label">Total de Lojas</div>
    </div>
    <div class="loja-stat" style="--c:#0ea5e9">
      <div class="loja-stat-num">{cidades}</div>
      <div class="loja-stat-label">Cidades</div>
    </div>
  </div>

  <!-- Cards por marca -->
  <div style="display:flex;flex-wrap:wrap;gap:14px;margin-bottom:28px">
    {cards_resumo}
  </div>

  <!-- Mapa -->
  <div style="background:#fff;border-radius:14px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden;margin-bottom:24px">
    <div style="padding:16px 22px;border-bottom:1px solid #f1f5f9;display:flex;align-items:center;gap:12px;flex-wrap:wrap">
      <span style="font-size:13px;font-weight:700;color:#374151;text-transform:uppercase;letter-spacing:.5px">Mapa de Lojas</span>
      <span style="font-size:12px;padding:3px 10px;border-radius:20px;background:#dcfce7;color:#166534;font-weight:600">● Aberta</span>
      <span style="font-size:12px;padding:3px 10px;border-radius:20px;background:#fef3c7;color:#92400e;font-weight:600">◐ Em abertura</span>
    </div>
    <div id="mapa-lojas" style="height:480px;width:100%"></div>
  </div>

  <!-- Tabela de lojas -->
  <div style="background:#fff;border-radius:14px;box-shadow:0 2px 12px rgba(0,0,0,.08);overflow:hidden">
    <div style="padding:16px 22px;border-bottom:1px solid #f1f5f9">
      <span style="font-size:13px;font-weight:700;color:#374151;text-transform:uppercase;letter-spacing:.5px">Lista de Lojas</span>
    </div>
    <div style="overflow-x:auto">
      <table style="width:100%;border-collapse:collapse;font-size:13px">
        <thead>
          <tr style="background:#f8fafc">
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Loja</th>
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Marca</th>
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Cidade</th>
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Estado</th>
            <th style="padding:12px 16px;text-align:left;color:#6b7280;font-weight:600;border-bottom:1px solid #e5e7eb">Status</th>
          </tr>
        </thead>
        <tbody id="tabela-lojas-body"></tbody>
      </table>
    </div>
  </div>

</div>

<style>
.loja-stat {{
  background:#fff;border-radius:12px;padding:18px 22px;
  border-left:4px solid var(--c);
  box-shadow:0 2px 8px rgba(0,0,0,.07);
  min-width:120px;
}}
.loja-stat-num  {{ font-size:28px;font-weight:800;color:#1e293b;line-height:1; }}
.loja-stat-label{{ font-size:12px;color:#6b7280;font-weight:600;text-transform:uppercase;letter-spacing:.5px;margin-top:4px; }}
</style>

<script>
const COR_MARCA = {json.dumps(COR_MARCA, ensure_ascii=False)};
const LOJAS = {lojas_json};

// ── Mapa ──────────────────────────────────────────────────────────────────
const map = L.map('mapa-lojas').setView([-27.1, -52.0], 8);
L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
  attribution: '© OpenStreetMap contributors'
}}).addTo(map);

function svgPin(cor, aberta) {{
  const opacity = aberta ? '1' : '0.55';
  const dash    = aberta ? '' : 'stroke-dasharray="4 2"';
  return `<svg xmlns="http://www.w3.org/2000/svg" width="32" height="42" viewBox="0 0 32 42">
    <path d="M16 0C7.16 0 0 7.16 0 16c0 12 16 26 16 26s16-14 16-26C32 7.16 24.84 0 16 0z"
      fill="${{cor}}" opacity="${{opacity}}" stroke="#fff" stroke-width="2" ${{dash}}/>
    <circle cx="16" cy="16" r="7" fill="#fff" opacity="0.9"/>
  </svg>`;
}}

function makeIcon(cor, aberta) {{
  return L.divIcon({{
    html: svgPin(cor, aberta),
    iconSize:[32,42], iconAnchor:[16,42], popupAnchor:[0,-40],
    className:''
  }});
}}

LOJAS.forEach(l => {{
  const cor    = COR_MARCA[l.marca] || '#374151';
  const aberta = l.status === 'aberta';
  const icon   = makeIcon(cor, aberta);
  const tag    = aberta
    ? '<span style="background:#dcfce7;color:#166534;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:700">Aberta</span>'
    : '<span style="background:#fef3c7;color:#92400e;padding:2px 8px;border-radius:10px;font-size:11px;font-weight:700">Em abertura</span>';
  L.marker([l.lat, l.lng], {{icon}})
   .bindPopup(`<div style="font-family:Segoe UI,sans-serif;min-width:160px">
     <div style="font-weight:700;font-size:14px;color:#1e293b;margin-bottom:4px">${{l.loja}}</div>
     <div style="font-size:12px;color:#6b7280;margin-bottom:6px">${{l.cidade}} — ${{l.estado}}</div>
     ${{tag}}
   </div>`)
   .addTo(map);
}});

// ── Tabela ────────────────────────────────────────────────────────────────
const tbody = document.getElementById('tabela-lojas-body');
LOJAS.forEach((l,i) => {{
  const cor  = COR_MARCA[l.marca] || '#374151';
  const tag  = l.status === 'aberta'
    ? '<span style="background:#dcfce7;color:#166534;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700">Aberta</span>'
    : '<span style="background:#fef3c7;color:#92400e;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700">Em abertura</span>';
  const bg = i % 2 === 0 ? '#fff' : '#f9fafb';
  tbody.innerHTML += `<tr style="background:${{bg}}">
    <td style="padding:11px 16px;font-weight:600;color:#1e293b;border-bottom:1px solid #f1f5f9">${{l.loja}}</td>
    <td style="padding:11px 16px;border-bottom:1px solid #f1f5f9"><span style="background:${{cor}};color:#fff;padding:3px 10px;border-radius:10px;font-size:11px;font-weight:700">${{l.marca}}</span></td>
    <td style="padding:11px 16px;color:#374151;border-bottom:1px solid #f1f5f9">${{l.cidade}}</td>
    <td style="padding:11px 16px;color:#374151;border-bottom:1px solid #f1f5f9">${{l.estado}}</td>
    <td style="padding:11px 16px;border-bottom:1px solid #f1f5f9">${{tag}}</td>
  </tr>`;
}});
</script>
"""
