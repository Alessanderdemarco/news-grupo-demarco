"""
Painel Mercado — Emplacamentos reais Jan–Jun 2026
Filtros: Marca → Área de Influência (micro-região) → Cidade → Tipo Veículo
"""

import os, json

_DIR  = os.path.dirname(os.path.abspath(__file__))
_JSON = os.path.join(_DIR, "emplacamentos_2026.json")

# Labels amigáveis para micro-regiões
MICRO_LABEL = {
    "BLUMENAU":          "Blumenau",
    "CAMPOS DE LAGES":   "Campos de Lages",
    "CANOINHAS":         "Canoinhas",
    "CHAPECO":           "Chapecó",
    "CONCORDIA":         "Concórdia",
    "CRICIUMA":          "Criciúma (+ Araranguá e Tubarão)",
    "JOACABA":           "Joaçaba",
    "PORTO UNIAO":       "Porto União",
    "RIO DO SUL":        "Rio do Sul",
    "SAO MIGUEL DO OESTE":"São Miguel do Oeste",
    "XANXERE":           "Xanxerê",
}

def gerar_secao():
    if not os.path.exists(_JSON):
        return """<div style="background:#0f1623;color:#fb923c;padding:40px;border-radius:14px;
border:1px solid #fb923c40;text-align:center;margin:20px">
  <b>⚠ emplacamentos_2026.json não encontrado.</b><br>
  Execute <code>processar_emplacamentos.py</code> primeiro.
</div>"""

    with open(_JSON, encoding="utf-8") as f:
        data = json.load(f)

    meses_pt        = data["meses_pt"]
    marcas_grupo    = data["marcas_grupo"]     # {RAW: label}
    areas_inf       = data["areas_influencia"] # {RAW_MARCA: [MICRO...]}
    micro_data      = data["micro"]            # {MICRO: {marcas, modelos, cidades}}
    periodo         = f"Jan–{meses_pt[-1]} 2026"

    # ── Opções do seletor de marcas (apenas as que têm área de influência) ──
    marcas_opts = "\n".join(
        f'<option value="{raw}">{label}</option>'
        for raw, label in marcas_grupo.items()
        if raw in areas_inf
    )

    # ── Meses ──
    meses_opts = "\n".join(
        f'<option value="{i}">{m}</option>'
        for i, m in enumerate(meses_pt)
    ) + f'\n<option value="all" selected>Acumulado {periodo}</option>'

    # ── Embed do JSON no HTML (apenas campos necessários) ──
    js_data = json.dumps({
        "meses_pt":        meses_pt,
        "brasil":          data["brasil"],
        "brasil_vp":       data.get("brasil_vp", {}),
        "brasil_vu":       data.get("brasil_vu", {}),
        "sc":              data["sc"],
        "sc_vp":           data.get("sc_vp", {}),
        "sc_vu":           data.get("sc_vu", {}),
        "r1":              data["r1"],
        "r1_vp":           data.get("r1_vp", {}),
        "r1_vu":           data.get("r1_vu", {}),
        "brasil_prop":     data.get("brasil_prop", {}),
        "sc_prop":         data.get("sc_prop", {}),
        "r1_prop":         data.get("r1_prop", {}),
        "micro":           micro_data,
        "areas_influencia":areas_inf,
        "grupo":           marcas_grupo,
        "micro_label":     MICRO_LABEL,
    }, ensure_ascii=False, separators=(",", ":"))

    return f"""
<div id="mkt-root" class="mercado-root">

<!-- ═══ FILTROS ═══ -->
<div class="mercado-filtros">
  <div class="filtro-grupo">
    <label>Período</label>
    <select id="mf-mes" onchange="mercadoAtualizar()">
      {meses_opts}
    </select>
  </div>
  <div class="filtro-grupo">
    <label>Marca do Grupo</label>
    <select id="mf-marca" onchange="mercadoTrocarMarca()">
      {marcas_opts}
    </select>
  </div>
  <div class="filtro-grupo">
    <label>Área de Influência</label>
    <select id="mf-micro" onchange="mercadoTrocarMicro()">
    </select>
  </div>
  <div class="filtro-grupo">
    <label>Cidade</label>
    <select id="mf-cidade" onchange="mercadoAtualizar()">
    </select>
  </div>
  <div class="filtro-grupo">
    <label>Tipo de Veículo</label>
    <select id="mf-tipo" onchange="mercadoAtualizar()">
      <option value="all" selected>VP + VU</option>
      <option value="VP">VP — Passeio</option>
      <option value="VU">VU — Utilitário</option>
    </select>
  </div>
  <div class="filtro-grupo">
    <label>Propulsão</label>
    <select id="mf-prop" onchange="mercadoAtualizar()">
      <option value="all" selected>Todas as propulsões</option>
      <option value="COMBUSTAO">🔥 Combustão</option>
      <option value="__HIBRIDO__">⚡ Híbrido (HEV+MHEV+PHEV)</option>
      <option value="HEV">  ↳ HEV — Híbrido convencional</option>
      <option value="MHEV"> ↳ MHEV — Micro-híbrido</option>
      <option value="PHEV"> ↳ PHEV — Plug-in híbrido</option>
      <option value="__ELETRICO__">🔋 Elétrico (BEV+EV)</option>
      <option value="BEV">  ↳ BEV — Elétrico puro</option>
      <option value="EV">   ↳ EV — Elétrico</option>
    </select>
  </div>
  <div class="filtro-grupo" style="align-self:flex-end">
    <div style="font-size:10px;color:#475569;line-height:1.6">
      Fonte: FENABRAVE/DENATRAN<br>
      <span style="color:#34d399;font-weight:700">● Dados reais {periodo}</span>
    </div>
  </div>
</div>

<!-- ═══ KPIs ═══ -->
<div class="mkt-kpis">
  <div class="kpi-card" style="--accent:#f5c518">
    <div class="kpi-icon" style="color:#f5c518">&#9651;</div>
    <div class="kpi-valor" id="kv-area">—</div>
    <div class="kpi-label" id="kl-area">Empl. Área</div>
    <div class="kpi-sub" id="ks-area">Área selecionada</div>
  </div>
  <div class="kpi-card" style="--accent:#fb923c">
    <div class="kpi-icon" style="color:#fb923c">%</div>
    <div class="kpi-valor" id="kv-share-area">—</div>
    <div class="kpi-label" id="kl-share-area">Share Área</div>
    <div class="kpi-sub" id="ks-share-area">vs total da área</div>
  </div>
  <div class="kpi-card" style="--accent:#4ade80">
    <div class="kpi-icon" style="color:#4ade80">&#9651;</div>
    <div class="kpi-valor" id="kv-sc">—</div>
    <div class="kpi-label">Empl. SC</div>
    <div class="kpi-sub">Santa Catarina</div>
  </div>
  <div class="kpi-card" style="--accent:#38bdf8">
    <div class="kpi-icon" style="color:#38bdf8">%</div>
    <div class="kpi-valor" id="kv-share-sc">—</div>
    <div class="kpi-label">Share SC</div>
    <div class="kpi-sub">Santa Catarina</div>
  </div>
  <div class="kpi-card" style="--accent:#818cf8">
    <div class="kpi-icon" style="color:#818cf8">&#9651;</div>
    <div class="kpi-valor" id="kv-br">—</div>
    <div class="kpi-label">Empl. Brasil</div>
    <div class="kpi-sub">{periodo}</div>
  </div>
  <div class="kpi-card kpi-destaque" style="--accent:#22d3ee">
    <div class="kpi-icon" style="color:#22d3ee">%</div>
    <div class="kpi-valor" id="kv-share-br">—</div>
    <div class="kpi-label">Share Brasil</div>
    <div class="kpi-sub">Participação nacional</div>
  </div>
</div>

<!-- ═══ Linha 1: Top 10 marcas na área + Modelos da marca ═══ -->
<div class="mkt-row">
  <div class="mkt-chart-card" style="flex:1.2">
    <div class="chart-title" id="ct-top10">Top 10 Marcas — Área Selecionada</div>
    <canvas id="chartTop10" height="250"></canvas>
  </div>
  <div class="mkt-chart-card" style="flex:1">
    <div class="chart-title" id="ct-modelos">Modelos da Marca — Área Selecionada</div>
    <canvas id="chartModelos" height="250"></canvas>
  </div>
</div>

<!-- ═══ Linha 2: Share comparativo mês a mês ═══ -->
<div class="mkt-row">
  <div class="mkt-chart-card full">
    <div class="chart-title" id="ct-share">
      Market Share — Evolução Mês a Mês: Área vs SC vs Sul R1 vs Brasil (%)
    </div>
    <canvas id="chartShare" height="75"></canvas>
  </div>
</div>

<!-- ═══ Linha 3: Evolução mensal top marcas + pizza ═══ -->
<div class="mkt-row">
  <div class="mkt-chart-card" style="flex:2">
    <div class="chart-title" id="ct-evo">
      Evolução Mensal de Emplacamentos — Top Marcas na Área
    </div>
    <canvas id="chartEvo" height="95"></canvas>
  </div>
  <div class="mkt-chart-card" style="flex:1">
    <div class="chart-title" id="ct-pizza">Share na Área (acumulado)</div>
    <canvas id="chartPizza" height="250"></canvas>
  </div>
</div>

<!-- ═══ Linha 4: Tabela ranking ═══ -->
<div class="mkt-row">
  <div class="mkt-chart-card full">
    <div class="chart-title" id="ct-tabela">Ranking de Emplacamentos — Área Selecionada</div>
    <div style="overflow-x:auto">
      <table class="mkt-table">
        <thead>
          <tr>
            <th style="text-align:left">#</th>
            <th style="text-align:left">Marca</th>
            <th>Área</th>
            <th>Share Área</th>
            <th>Share SC</th>
            <th>Share Brasil</th>
          </tr>
        </thead>
        <tbody id="tbody-ranking"></tbody>
      </table>
    </div>
  </div>
</div>

<div style="text-align:center;font-size:11px;color:#475569;padding:12px 0 4px">
  Fonte: FENABRAVE/DENATRAN — {periodo} — Micro-regiões de influência Grupo De Marco
</div>
</div>

<style>
.mercado-root {{ background:#080c14; color:#e2e8f0; padding:28px 32px; max-width:1400px; margin:0 auto; }}
.mercado-filtros {{
  display:flex; gap:16px; flex-wrap:wrap; align-items:flex-end;
  background:#0f1623; border:1px solid #1e293b; border-radius:14px;
  padding:18px 22px; margin-bottom:20px;
}}
.filtro-grupo {{ display:flex; flex-direction:column; gap:5px; min-width:160px; }}
.filtro-grupo label {{ font-size:10px; font-weight:700; color:#475569; text-transform:uppercase; letter-spacing:.5px; }}
.filtro-grupo select {{
  background:#161f2e; border:1px solid #1e293b; color:#e2e8f0;
  border-radius:8px; padding:8px 32px 8px 12px; font-size:13px;
  cursor:pointer; outline:none; -webkit-appearance:none; appearance:none;
  background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='12' height='12' viewBox='0 0 12 12'%3E%3Cpath fill='%2394a3b8' d='M6 8L1 3h10z'/%3E%3C/svg%3E");
  background-repeat:no-repeat; background-position:right 10px center;
  transition:border-color .15s;
}}
.filtro-grupo select:focus {{ border-color:#f5c518; box-shadow:0 0 0 2px #f5c51820; }}
@media(max-width:900px){{ .mercado-root{{ padding:20px 14px; }} .mercado-filtros{{ gap:10px; }} .filtro-grupo{{ min-width:140px; }} }}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
// ════════════════════════════════════════════
//  DADOS EMBUTIDOS
// ════════════════════════════════════════════
const _D = {js_data};

Chart.defaults.font.family = "'Segoe UI',sans-serif";
Chart.defaults.color = '#475569';
Chart.defaults.borderColor = '#1e293b';
const GRID = {{ color:'#1e293b' }};

const PAL20 = [
  '#f5c518','#38bdf8','#22d3ee','#818cf8','#34d399','#fb923c',
  '#4ade80','#a78bfa','#2dd4bf','#fbbf24','#60a5fa','#c084fc',
  '#86efac','#67e8f9','#fcd34d','#93c5fd','#d8b4fe','#6ee7b7',
  '#f0f9ff','#fefce8'
];
const COR_GRUPO = {{
  RENAULT:'#f5c518', GWM:'#22d3ee', YAMAHA:'#38bdf8',
  TRIUMPH:'#818cf8', 'CF MOTO':'#fb923c', PEUGEOT:'#4ade80',
  CITROEN:'#f97316', GEELY:'#34d399'
}};

let charts = {{}};
function destroyChart(id) {{ if(charts[id]){{ charts[id].destroy(); delete charts[id]; }} }}

// ── Helpers ──
function sumM(arr, idx) {{
  if(!arr) return 0;
  if(idx==='all') return arr.reduce((a,b)=>a+b,0);
  return arr[parseInt(idx)] || 0;
}}
function pct(v,t) {{ return t>0 ? (v/t*100).toFixed(1)+'%' : '—'; }}
function fmt(n) {{
  if(n>=1000000) return (n/1000000).toFixed(1)+'M';
  if(n>=10000)   return (n/1000).toFixed(1)+'k';
  return n.toLocaleString('pt-BR');
}}
function top10obj(obj, mesIdx, n=10) {{
  return Object.entries(obj)
    .map(([k,v])=>[k, sumM(v,mesIdx)])
    .filter(([,v])=>v>0)
    .sort((a,b)=>b[1]-a[1]).slice(0,n);
}}
function palCor(marca, idx) {{ return COR_GRUPO[marca] || PAL20[idx % PAL20.length]; }}

// ════════════════════════════════════════════
//  HELPERS DE SOMA ENTRE MICRO-REGIÕES
// ════════════════════════════════════════════
function mergeMarcas(micros, sfx) {{
  const result = {{}};
  for (const m of micros) {{
    const md = _D.micro[m]; if(!md) continue;
    const src = md['marcas'+sfx] || md.marcas || {{}};
    for (const [mar, vals] of Object.entries(src)) {{
      if(!result[mar]) result[mar] = vals.map(()=>0);
      vals.forEach((v,i)=> result[mar][i] += v);
    }}
  }}
  return result;
}}
function mergeModelos(micros, marcaKey, sfx) {{
  const result = {{}};
  for (const m of micros) {{
    const md = _D.micro[m]; if(!md) continue;
    const mods = (md['modelos'+sfx] || md.modelos || {{}})[marcaKey] || {{}};
    for (const [mod, vals] of Object.entries(mods)) {{
      if(!result[mod]) result[mod] = vals.map(()=>0);
      vals.forEach((v,i)=> result[mod][i] += v);
    }}
  }}
  return result;
}}

// ════════════════════════════════════════════
//  INICIALIZA DROPDOWNS
// ════════════════════════════════════════════
function mercadoTrocarMarca() {{
  const marca = document.getElementById('mf-marca').value;
  const areas  = (_D.areas_influencia[marca] || []).filter(m => _D.micro[m]);
  const sel    = document.getElementById('mf-micro');
  // Primeira opção: soma de todas as áreas da marca
  sel.innerHTML =
    `<option value="__all__">Toda a Área de Influência (${{areas.length}} micro-regiões)</option>` +
    areas.map(m => `<option value="${{m}}">${{_D.micro_label[m] || m}}</option>`).join('');
  mercadoTrocarMicro();
}}

function mercadoTrocarMicro() {{
  const marca  = document.getElementById('mf-marca').value;
  const micro  = document.getElementById('mf-micro').value;
  let cidades = [];
  if (micro === '__all__') {{
    // Todas as cidades de todas as micro-regiões da marca
    const areas = (_D.areas_influencia[marca] || []).filter(m => _D.micro[m]);
    const cidSet = new Set();
    for (const m of areas) Object.keys(_D.micro[m].cidades || {{}}).forEach(c => cidSet.add(c));
    cidades = [...cidSet].sort();
  }} else if (micro && _D.micro[micro]) {{
    cidades = Object.keys(_D.micro[micro].cidades || {{}}).sort();
  }}
  const sel = document.getElementById('mf-cidade');
  sel.innerHTML = '<option value="all">Toda a micro-região</option>' +
    cidades.map(c => `<option value="${{c}}">${{c.replace(/\\b\\w/g,l=>l.toUpperCase())}}</option>`).join('');
  mercadoAtualizar();
}}

// ════════════════════════════════════════════
//  ATUALIZA PAINEL PRINCIPAL
// ════════════════════════════════════════════
function mercadoAtualizar() {{
  const mesIdx  = document.getElementById('mf-mes').value;
  const marca   = document.getElementById('mf-marca').value;
  const microNm = document.getElementById('mf-micro').value;
  const cidNm   = document.getElementById('mf-cidade').value;
  const tipo    = document.getElementById('mf-tipo').value;  // 'all','VP','VU'
  const prop    = document.getElementById('mf-prop').value;  // 'all','COMBUSTAO','HIBRIDO','ELETRICO'

  if(!microNm) return;
  if(microNm !== '__all__' && !_D.micro[microNm]) return;

  // Sufixo de chave: '' para VP+VU, '_vp' para VP, '_vu' para VU
  const sfx = tipo === 'VP' ? '_vp' : tipo === 'VU' ? '_vu' : '';

  // Grupos de propulsão
  const PROP_GRUPOS = {{
    '__HIBRIDO__': ['HEV','MHEV','PHEV'],
    '__ELETRICO__': ['BEV','EV'],
  }};
  const propTipos = prop === 'all' ? [] : (PROP_GRUPOS[prop] || [prop]);

  // Helper: filtra mapa {{marca:[vals]}} por propulsão usando _prop dicts
  function filtrarPorProp(propDict, tipos) {{
    const merged = {{}};
    for (const t of tipos) {{
      const src = propDict[t] || {{}};
      for (const [mar,vals] of Object.entries(src)) {{
        if(!merged[mar]) merged[mar] = vals.map(()=>0);
        vals.forEach((v,i) => merged[mar][i] += v);
      }}
    }}
    return merged;
  }}

  // Seleciona as chaves de brasil/sc/r1 conforme tipo e propulsão
  let brMap = _D['brasil' + sfx] || _D.brasil;
  let scMap = _D['sc'     + sfx] || _D.sc;
  let r1Map = _D['r1'     + sfx] || _D.r1;
  if (propTipos.length > 0) {{
    const brF = filtrarPorProp(_D.brasil_prop || {{}}, propTipos);
    const scF = filtrarPorProp(_D.sc_prop     || {{}}, propTipos);
    const r1F = filtrarPorProp(_D.r1_prop     || {{}}, propTipos);
    if (Object.keys(brF).length) brMap = brF;
    if (Object.keys(scF).length) scMap = scF;
    if (Object.keys(r1F).length) r1Map = r1F;
  }}

  // Resolve areaMarcas / areaModelos / areaLabel
  let areaMarcas, areaModelos, areaLabel;
  if (microNm === '__all__') {{
    // Soma todas as micro-regiões da marca
    const micros = (_D.areas_influencia[marca] || []).filter(m => _D.micro[m]);
    if (cidNm && cidNm !== 'all') {{
      // Cidade específica que pode estar em qualquer micro
      const mMap = {{}}, modMap = {{}};
      for (const m of micros) {{
        const cObj = (_D.micro[m].cidades || {{}})[cidNm];
        if (!cObj) continue;
        const src  = cObj['marcas'+sfx]  || cObj.marcas  || {{}};
        const msrc = (cObj['modelos'+sfx] || cObj.modelos || {{}})[marca] || {{}};
        for (const [mar,vals] of Object.entries(src))  {{ if(!mMap[mar]) mMap[mar]=vals.map(()=>0); vals.forEach((v,i)=>mMap[mar][i]+=v); }}
        for (const [mod,vals] of Object.entries(msrc)) {{ if(!modMap[mod]) modMap[mod]=vals.map(()=>0); vals.forEach((v,i)=>modMap[mod][i]+=v); }}
      }}
      areaMarcas = mMap; areaModelos = modMap;
      areaLabel  = cidNm.replace(/\\b\\w/g, l=>l.toUpperCase()) + ' (todas as áreas)';
    }} else {{
      areaMarcas = mergeMarcas(micros, sfx);
      areaModelos= mergeModelos(micros, marca, sfx);
      areaLabel  = 'Toda a Área de Influência';
    }}
  }} else {{
    const microData = _D.micro[microNm];
    if (cidNm && cidNm !== 'all' && microData.cidades[cidNm]) {{
      const cObj = microData.cidades[cidNm];
      areaMarcas  = cObj['marcas'+sfx]  || cObj.marcas  || {{}};
      areaModelos = (cObj['modelos'+sfx] || cObj.modelos || {{}})[marca] || {{}};
      areaLabel   = cidNm.replace(/\\b\\w/g, l=>l.toUpperCase());
    }} else {{
      areaMarcas  = microData['marcas'+sfx]  || microData.marcas  || {{}};
      areaModelos = (microData['modelos'+sfx] || microData.modelos || {{}})[marca] || {{}};
      areaLabel   = _D.micro_label[microNm] || microNm;
    }}
  }}

  // ── Aplica filtro de propulsão na área (substitui areaMarcas se necessário) ──
  if (propTipos.length > 0) {{
    let propSrc;
    if (microNm === '__all__') {{
      const micros = (_D.areas_influencia[marca] || []).filter(m => _D.micro[m]);
      const merged = {{}};
      for (const m of micros) {{
        const baseObj = (cidNm && cidNm !== 'all' && (_D.micro[m].cidades||{{}})[cidNm])
          ? _D.micro[m].cidades[cidNm] : _D.micro[m];
        const src = filtrarPorProp(baseObj.prop || {{}}, propTipos);
        for (const [mar,vals] of Object.entries(src)) {{
          if(!merged[mar]) merged[mar] = vals.map(()=>0);
          vals.forEach((v,i) => merged[mar][i] += v);
        }}
      }}
      propSrc = merged;
    }} else {{
      const microData = _D.micro[microNm];
      const baseObj = (cidNm && cidNm !== 'all' && microData.cidades[cidNm])
        ? microData.cidades[cidNm] : microData;
      propSrc = filtrarPorProp(baseObj.prop || {{}}, propTipos);
    }}
    if (Object.keys(propSrc).length > 0) areaMarcas = propSrc;
  }}

  // ── KPIs ──
  const totArea = Object.values(areaMarcas).reduce((s,v)=>s+sumM(v,mesIdx),0);
  const totSC   = Object.values(scMap).reduce((s,v)=>s+sumM(v,mesIdx),0);
  const totBR   = Object.values(brMap).reduce((s,v)=>s+sumM(v,mesIdx),0);
  const vArea   = sumM(areaMarcas[marca], mesIdx);
  const vSC     = sumM(scMap[marca],      mesIdx);
  const vBR     = sumM(brMap[marca],      mesIdx);
  const marcaLabel = _D.grupo[marca] || marca;

  document.getElementById('kv-area').textContent       = fmt(vArea);
  document.getElementById('kl-area').textContent       = `Empl. ${{marcaLabel}}`;
  document.getElementById('ks-area').textContent       = areaLabel;
  document.getElementById('kv-share-area').textContent = pct(vArea, totArea);
  document.getElementById('kl-share-area').textContent = `Share ${{areaLabel}}`;
  document.getElementById('kv-sc').textContent         = fmt(vSC);
  document.getElementById('kv-share-sc').textContent   = pct(vSC, totSC);
  document.getElementById('kv-br').textContent         = fmt(vBR);
  document.getElementById('kv-share-br').textContent   = pct(vBR, totBR);

  const corMarca = COR_GRUPO[marca] || '#f5c518';
  const meses    = _D.meses_pt;

  // ── GRÁFICO 1: Top 10 marcas na área ──
  const top10 = top10obj(areaMarcas, mesIdx, 10);
  const t10l = top10.map(([m])=>m);
  const t10v = top10.map(([,v])=>v);
  destroyChart('g1');
  charts['g1'] = new Chart(document.getElementById('chartTop10'),{{
    type:'bar',
    data:{{ labels:t10l, datasets:[{{
      data: t10v,
      backgroundColor: t10l.map((m,i) => m===marca ? palCor(m,i) : palCor(m,i)+'66'),
      borderColor:     t10l.map((m,i) => m===marca ? '#ffffff' : 'transparent'),
      borderWidth:     t10l.map(m => m===marca ? 2 : 0),
      borderRadius:6
    }}]}},
    options:{{ indexAxis:'y', responsive:true,
      plugins:{{ legend:{{display:false}},
        tooltip:{{callbacks:{{label:ctx=>` ${{ctx.raw.toLocaleString('pt-BR')}} empl.`}}}}
      }},
      scales:{{
        x:{{beginAtZero:true,grid:GRID,ticks:{{color:'#475569',callback:v=>v>=1000?(v/1000).toFixed(0)+'k':v}}}},
        y:{{grid:{{display:false}},ticks:{{
          color: (ctx) => t10l[ctx.index]===marca ? '#f5c518' : '#94a3b8',
          font:  (ctx) => ({{ weight: t10l[ctx.index]===marca ? '800':'normal' }})
        }}}}
      }}
    }}
  }});
  document.getElementById('ct-top10').textContent = `Top 10 Marcas — ${{areaLabel}}`;

  // ── GRÁFICO 2: Modelos da marca na área ──
  const modTop = Object.entries(areaModelos)
    .map(([m,v])=>[m, sumM(v,mesIdx)]).filter(([,v])=>v>0)
    .sort((a,b)=>b[1]-a[1]).slice(0,10);
  destroyChart('g2');
  if(modTop.length) {{
    charts['g2'] = new Chart(document.getElementById('chartModelos'),{{
      type:'bar',
      data:{{ labels:modTop.map(([m])=>m), datasets:[{{
        data: modTop.map(([,v])=>v),
        backgroundColor: modTop.map((_,i)=> i===0 ? corMarca : corMarca+'55'),
        borderColor:corMarca, borderWidth:1, borderRadius:6
      }}]}},
      options:{{ indexAxis:'y', responsive:true,
        plugins:{{ legend:{{display:false}} }},
        scales:{{
          x:{{beginAtZero:true,grid:GRID,ticks:{{color:'#475569'}}}},
          y:{{grid:{{display:false}},ticks:{{color:'#94a3b8'}}}}
        }}
      }}
    }});
  }} else {{
    const ctx = document.getElementById('chartModelos').getContext('2d');
    ctx.clearRect(0,0,ctx.canvas.width,ctx.canvas.height);
    ctx.fillStyle='#334155'; ctx.font='13px Segoe UI'; ctx.textAlign='center';
    ctx.fillText('Sem dados de modelo para esta seleção', ctx.canvas.width/2, 80);
  }}
  document.getElementById('ct-modelos').textContent = `Modelos ${{marcaLabel}} — ${{areaLabel}}`;

  // ── GRÁFICO 3: Share comparativo mês a mês (linha) ──
  function sharePorMes(mapaObj, marcaKey) {{
    return meses.map((_,i) => {{
      const tot = Object.values(mapaObj).reduce((s,v)=>s+(v[i]||0),0);
      const vm  = (mapaObj[marcaKey]?.[i] || 0);
      return tot>0 ? parseFloat((vm/tot*100).toFixed(2)) : 0;
    }});
  }}
  const shareArea = sharePorMes(areaMarcas, marca);
  const shareSC   = sharePorMes(scMap,      marca);
  const shareR1   = sharePorMes(r1Map,      marca);
  const shareBR   = sharePorMes(brMap,      marca);

  destroyChart('g3');
  charts['g3'] = new Chart(document.getElementById('chartShare'),{{
    type:'line',
    data:{{ labels:meses, datasets:[
      {{label:areaLabel, data:shareArea, borderColor:corMarca, backgroundColor:corMarca+'25',
        tension:.4, fill:true, pointRadius:5, borderWidth:3,
        pointBackgroundColor:corMarca, pointBorderColor:'#0f1623', pointBorderWidth:2}},
      {{label:'Santa Catarina', data:shareSC, borderColor:'#38bdf8', backgroundColor:'transparent',
        tension:.4, fill:false, pointRadius:4, borderWidth:2,
        pointBackgroundColor:'#38bdf8', pointBorderColor:'#0f1623', pointBorderWidth:1}},
      {{label:'Sul R1', data:shareR1, borderColor:'#818cf8', backgroundColor:'transparent',
        tension:.4, fill:false, pointRadius:4, borderWidth:2, borderDash:[5,3],
        pointBackgroundColor:'#818cf8', pointBorderColor:'#0f1623', pointBorderWidth:1}},
      {{label:'Brasil', data:shareBR, borderColor:'#475569', backgroundColor:'transparent',
        tension:.4, fill:false, pointRadius:4, borderWidth:1.5, borderDash:[7,4],
        pointBackgroundColor:'#475569', pointBorderColor:'#0f1623', pointBorderWidth:1}},
    ]}},
    options:{{ responsive:true, interaction:{{mode:'index',intersect:false}},
      plugins:{{ legend:{{position:'top',labels:{{color:'#94a3b8',font:{{size:11}},boxWidth:10}}}},
        tooltip:{{callbacks:{{label:ctx=>` ${{ctx.dataset.label}}: ${{ctx.raw}}%`}}}}
      }},
      scales:{{
        y:{{beginAtZero:true,grid:GRID,ticks:{{color:'#475569',callback:v=>v+'%'}}}},
        x:{{grid:GRID,ticks:{{color:'#475569'}}}}
      }}
    }}
  }});
  document.getElementById('ct-share').textContent =
    `Market Share ${{marcaLabel}} — Mês a Mês: ${{areaLabel}} vs SC vs Sul R1 vs Brasil (%)`;

  // ── GRÁFICO 4: Evolução mensal top 6 marcas na área ──
  const top6evo = top10obj(areaMarcas,'all',6).map(([m])=>m);
  if(marca && !top6evo.includes(marca) && areaMarcas[marca]) top6evo.push(marca);

  destroyChart('g4');
  charts['g4'] = new Chart(document.getElementById('chartEvo'),{{
    type:'line',
    data:{{ labels:meses, datasets: top6evo.map((m,i) => {{
      const cor    = palCor(m,i);
      const isSel  = m===marca;
      return {{
        label:m, data:meses.map((_,mi)=>(areaMarcas[m]?.[mi]||0)),
        borderColor:cor, backgroundColor: isSel ? cor+'22':'transparent',
        tension:.4, fill:isSel, pointRadius:isSel?5:3,
        borderWidth:isSel?3:1.5,
        pointBackgroundColor:cor, pointBorderColor:'#0f1623', pointBorderWidth:isSel?2:1
      }};
    }})}},
    options:{{ responsive:true, interaction:{{mode:'index',intersect:false}},
      plugins:{{ legend:{{position:'top',labels:{{color:'#94a3b8',font:{{size:11}},boxWidth:10}}}}}},
      scales:{{
        y:{{beginAtZero:true,grid:GRID,ticks:{{color:'#475569'}}}},
        x:{{grid:GRID,ticks:{{color:'#475569'}}}}
      }}
    }}
  }});
  document.getElementById('ct-evo').textContent =
    `Evolução Mensal — Top Marcas em ${{areaLabel}} (jan–jun 2026)`;

  // ── GRÁFICO 5: Pizza ──
  const pie8 = top10obj(areaMarcas, mesIdx, 8);
  const outrosV = totArea - pie8.reduce((s,[,v])=>s+v,0);
  const pieL = pie8.map(([m])=>m); if(outrosV>0) pieL.push('Outros');
  const pieV = pie8.map(([,v])=>v); if(outrosV>0) pieV.push(outrosV);
  destroyChart('g5');
  charts['g5'] = new Chart(document.getElementById('chartPizza'),{{
    type:'doughnut',
    data:{{ labels:pieL, datasets:[{{
      data:pieV,
      backgroundColor:pieL.map((m,i)=> palCor(m,i)),
      borderWidth:3, borderColor:'#0f1623', hoverOffset:8
    }}]}},
    options:{{ responsive:true, cutout:'58%',
      plugins:{{
        legend:{{position:'right',labels:{{color:'#94a3b8',font:{{size:10}}}}}},
        tooltip:{{callbacks:{{label:ctx=>` ${{ctx.label}}: ${{pct(ctx.raw,totArea)}}`}}}}
      }}
    }}
  }});
  document.getElementById('ct-pizza').textContent = `Share em ${{areaLabel}}`;

  // ── Tabela ranking ──
  const tbody = document.getElementById('tbody-ranking');
  tbody.innerHTML = '';
  top10.forEach(([m, vol], idx) => {{
    const vsc2 = sumM(scMap[m], mesIdx);
    const vbr2 = sumM(brMap[m], mesIdx);
    const isSel = m === marca;
    const cor   = palCor(m, idx);
    tbody.innerHTML += `<tr style="${{isSel?'background:#111c11':''}}">
      <td style="color:#334155;font-size:11px">#${{idx+1}}</td>
      <td style="color:${{cor}};font-weight:${{isSel?800:400}}">${{m}}</td>
      <td class="num bold">${{vol.toLocaleString('pt-BR')}}</td>
      <td class="num">${{pct(vol, totArea)}}</td>
      <td class="num">${{pct(vsc2, totSC)}}</td>
      <td class="num">${{pct(vbr2, totBR)}}</td>
    </tr>`;
  }});
  document.getElementById('ct-tabela').textContent = `Ranking — ${{areaLabel}}`;
}}

// ════════════════════════════════════════════
//  INICIALIZAÇÃO
// ════════════════════════════════════════════
function mercadoInit() {{
  mercadoTrocarMarca();  // preenche áreas → cidades → atualiza painel
}}

// Dispara ao abrir a aba
(function(){{
  const origAbrirAba = window.abrirAba;
  window.abrirAba = function(nome, btn) {{
    origAbrirAba(nome, btn);
    if(nome==='mercado') setTimeout(mercadoInit, 60);
  }};
}})();

// Também inicializa se a aba já estiver ativa ao carregar
if(document.getElementById('aba-mercado')?.classList.contains('active')) mercadoInit();
</script>
"""
