"""
Painel de Marketing Digital — Grupo De Marco / Tozzo
Dados reais extraídos de GrupoDeMarco_Dashboard_Mkt.xlsx (Jan–Jun 2026)
"""

def gerar_secao():
    return """
<div id="mkt-root">

<!-- ── KPIs ── -->
<div class="mkt-kpis">
  <div class="kpi-card" style="--accent:#f59e0b">
    <div class="kpi-icon">&#128081;</div>
    <div class="kpi-valor">14.293</div>
    <div class="kpi-label">Total de Leads 2026</div>
    <div class="kpi-sub">Jan – Jun acumulado</div>
  </div>
  <div class="kpi-card" style="--accent:#10b981">
    <div class="kpi-icon">R$</div>
    <div class="kpi-valor">213,7k</div>
    <div class="kpi-label">Investimento Total</div>
    <div class="kpi-sub">Meta Ads + Google Ads</div>
  </div>
  <div class="kpi-card" style="--accent:#6366f1">
    <div class="kpi-icon">&#128200;</div>
    <div class="kpi-valor">R$ 14,95</div>
    <div class="kpi-label">CPL Médio Geral</div>
    <div class="kpi-sub">Custo por lead</div>
  </div>
  <div class="kpi-card" style="--accent:#ec4899">
    <div class="kpi-icon">&#128247;</div>
    <div class="kpi-valor">484</div>
    <div class="kpi-label">Postagens Instagram</div>
    <div class="kpi-sub">Todas as marcas</div>
  </div>
  <div class="kpi-card" style="--accent:#0ea5e9">
    <div class="kpi-icon">&#128101;</div>
    <div class="kpi-valor">76.371</div>
    <div class="kpi-label">Seguidores Totais</div>
    <div class="kpi-sub">Soma de todos os perfis</div>
  </div>
  <div class="kpi-card" style="--accent:#f97316">
    <div class="kpi-icon">&#128269;</div>
    <div class="kpi-valor">R$ 11,49</div>
    <div class="kpi-label">Melhor CPL</div>
    <div class="kpi-sub">Yamaha — mais eficiente</div>
  </div>
</div>

<!-- ── Linha 1: Investimento mensal + Leads por marca ── -->
<div class="mkt-row">
  <div class="mkt-chart-card" style="flex:2">
    <div class="chart-title">Investimento Mensal por Marca — Meta Ads (R$)</div>
    <canvas id="chartInvest" height="100"></canvas>
  </div>
  <div class="mkt-chart-card" style="flex:1">
    <div class="chart-title">Total de Leads por Marca (Jan–Jun)</div>
    <canvas id="chartLeadsMarca" height="220"></canvas>
  </div>
</div>

<!-- ── Linha 2: Leads mensais + CPL por marca ── -->
<div class="mkt-row">
  <div class="mkt-chart-card" style="flex:2">
    <div class="chart-title">Leads Gerados por Mês — por Marca</div>
    <canvas id="chartLeadsMes" height="100"></canvas>
  </div>
  <div class="mkt-chart-card" style="flex:1">
    <div class="chart-title">CPL por Marca (R$) — Jan a Jun</div>
    <canvas id="chartCPL" height="220"></canvas>
  </div>
</div>

<!-- ── Linha 3: Seguidores + CPL Mensal geral ── -->
<div class="mkt-row">
  <div class="mkt-chart-card" style="flex:1">
    <div class="chart-title">Seguidores no Instagram por Perfil</div>
    <canvas id="chartSeguidores" height="220"></canvas>
  </div>
  <div class="mkt-chart-card" style="flex:1">
    <div class="chart-title">Evolução do CPL Geral do Grupo (R$)</div>
    <canvas id="chartCPLGeral" height="220"></canvas>
  </div>
  <div class="mkt-chart-card" style="flex:1">
    <div class="chart-title">Share de Investimento por Marca</div>
    <canvas id="chartShareInvest" height="220"></canvas>
  </div>
</div>

<!-- ── Linha 4: Tabela resumo ── -->
<div class="mkt-row">
  <div class="mkt-chart-card full">
    <div class="chart-title">Resumo por Marca — Jan a Jun 2026</div>
    <div style="overflow-x:auto">
    <table style="width:100%;border-collapse:collapse;font-size:13px">
      <thead>
        <tr style="background:#1e293b;color:#fff">
          <th style="padding:11px 16px;text-align:left;font-weight:600;border-radius:8px 0 0 0">Marca</th>
          <th style="padding:11px 16px;text-align:right;font-weight:600">Seguidores IG</th>
          <th style="padding:11px 16px;text-align:right;font-weight:600">Postagens</th>
          <th style="padding:11px 16px;text-align:right;font-weight:600">Invest. Meta</th>
          <th style="padding:11px 16px;text-align:right;font-weight:600">Invest. Google</th>
          <th style="padding:11px 16px;text-align:right;font-weight:600">Total Invest.</th>
          <th style="padding:11px 16px;text-align:right;font-weight:600">Total Leads</th>
          <th style="padding:11px 16px;text-align:right;font-weight:600;border-radius:0 8px 0 0">CPL Geral</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:#fff">
          <td style="padding:10px 16px;font-weight:700;border-bottom:1px solid #f1f5f9"><span style="background:#e04000;color:#fff;padding:2px 8px;border-radius:8px;font-size:11px">CF Off Road</span></td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">926</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">58</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">R$ 10.890</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">—</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">R$ 10.890</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">874</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9"><span style="background:#dcfce7;color:#166534;padding:2px 8px;border-radius:8px;font-size:12px;font-weight:700">R$ 13,10</span></td>
        </tr>
        <tr style="background:#f9fafb">
          <td style="padding:10px 16px;font-weight:700;border-bottom:1px solid #f1f5f9"><span style="background:#003087;color:#fff;padding:2px 8px;border-radius:8px;font-size:11px">Yamaha</span></td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">7.925</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">110</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">R$ 41.805</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">—</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">R$ 41.805</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">3.739</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9"><span style="background:#dcfce7;color:#166534;padding:2px 8px;border-radius:8px;font-size:12px;font-weight:700">R$ 11,49 ★</span></td>
        </tr>
        <tr style="background:#fff">
          <td style="padding:10px 16px;font-weight:700;border-bottom:1px solid #f1f5f9"><span style="background:#7c0000;color:#fff;padding:2px 8px;border-radius:8px;font-size:11px">Triumph</span></td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">8.251</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">90</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">R$ 19.578</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">—</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">R$ 19.578</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">1.545</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9"><span style="background:#fef3c7;color:#92400e;padding:2px 8px;border-radius:8px;font-size:12px;font-weight:700">R$ 13,41</span></td>
        </tr>
        <tr style="background:#f9fafb">
          <td style="padding:10px 16px;font-weight:700;border-bottom:1px solid #f1f5f9"><span style="background:#c00020;color:#fff;padding:2px 8px;border-radius:8px;font-size:11px">GWM</span></td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">7.541</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">128</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">R$ 76.756</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">R$ 11.314</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">R$ 88.070</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">4.760</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9"><span style="background:#fee2e2;color:#991b1b;padding:2px 8px;border-radius:8px;font-size:12px;font-weight:700">R$ 18,10</span></td>
        </tr>
        <tr style="background:#fff">
          <td style="padding:10px 16px;font-weight:700;border-bottom:1px solid #f1f5f9"><span style="background:#f2c200;color:#1e293b;padding:2px 8px;border-radius:8px;font-size:11px">Renault</span></td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">20.957</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">98</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">R$ 53.356</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9">—</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">R$ 53.356</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9;font-weight:600">3.375</td>
          <td style="padding:10px 16px;text-align:right;border-bottom:1px solid #f1f5f9"><span style="background:#fef3c7;color:#92400e;padding:2px 8px;border-radius:8px;font-size:12px;font-weight:700">R$ 16,16</span></td>
        </tr>
        <tr style="background:#1e293b;color:#fff">
          <td style="padding:11px 16px;font-weight:700">TOTAL GRUPO</td>
          <td style="padding:11px 16px;text-align:right;font-weight:700">76.371</td>
          <td style="padding:11px 16px;text-align:right;font-weight:700">484</td>
          <td style="padding:11px 16px;text-align:right;font-weight:700">R$ 202.387</td>
          <td style="padding:11px 16px;text-align:right;font-weight:700">R$ 11.314</td>
          <td style="padding:11px 16px;text-align:right;font-weight:700">R$ 213.701</td>
          <td style="padding:11px 16px;text-align:right;font-weight:700">14.293</td>
          <td style="padding:11px 16px;text-align:right;font-weight:700">R$ 14,95</td>
        </tr>
      </tbody>
    </table>
    </div>
  </div>
</div>

<div style="text-align:center;font-size:11px;color:#94a3b8;padding:12px 0 4px">
  Fonte: GrupoDeMarco_Dashboard_Mkt.xlsx &mdash; Jan a Jun 2026
</div>

</div><!-- fim mkt-root -->

<style>
#mkt-root { padding: 28px 32px; max-width: 1400px; margin: 0 auto; }
.mkt-kpis {
  display: grid;
  grid-template-columns: repeat(6,1fr);
  gap: 14px;
  margin-bottom: 22px;
}
@media(max-width:1100px){ .mkt-kpis{ grid-template-columns:repeat(3,1fr); } }
@media(max-width:640px) { .mkt-kpis{ grid-template-columns:repeat(2,1fr); } }
.kpi-card {
  background:#fff; border-radius:14px; padding:18px 16px;
  box-shadow:0 2px 12px rgba(0,0,0,.07);
  border-top:4px solid var(--accent);
  position:relative; overflow:hidden;
}
.kpi-card::before {
  content:''; position:absolute; top:-18px; right:-18px;
  width:72px; height:72px; background:var(--accent);
  opacity:.08; border-radius:50%;
}
.kpi-icon  { font-size:17px; color:var(--accent); margin-bottom:6px; }
.kpi-valor { font-size:22px; font-weight:800; color:#1e293b; line-height:1; margin-bottom:3px; }
.kpi-label { font-size:11px; color:#374151; font-weight:700; text-transform:uppercase; letter-spacing:.5px; margin-bottom:2px; }
.kpi-sub   { font-size:10px; color:#9ca3af; }
.mkt-row   { display:flex; gap:18px; margin-bottom:18px; flex-wrap:wrap; }
.mkt-chart-card {
  background:#fff; border-radius:14px; padding:20px 22px;
  box-shadow:0 2px 12px rgba(0,0,0,.07); flex:1; min-width:220px;
}
.mkt-chart-card.full { flex:1 1 100%; }
.chart-title {
  font-size:12px; font-weight:700; color:#374151;
  text-transform:uppercase; letter-spacing:.5px;
  margin-bottom:14px; padding-bottom:10px;
  border-bottom:2px solid #f1f5f9;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
Chart.defaults.font.family = "'Segoe UI',sans-serif";
Chart.defaults.color = '#6b7280';
Chart.defaults.plugins.legend.labels.boxWidth = 12;

const MESES  = ['Jan','Fev','Mar','Abr','Mai','Jun'];
const MARCAS = ['CF Off Road','Yamaha','Triumph','GWM','Renault'];
const CORES  = ['#e04000','#003087','#7c0000','#c00020','#f2c200'];

// Investimento mensal (Meta Ads)
const investData = [
  [950.54,2458.58,1770.59,2020.01,2196.11,1494.75],   // CF
  [3900.56,2942.97,10201.08,9777.12,11956.4,3027.48],  // Yamaha
  [2144.59,3226.05,4021.88,4399.68,3996.93,1789.10],   // Triumph
  [10009.03,10851.24,20969.66,27027.81,19212.38,0],     // GWM
  [6994.4,7578.17,10414.81,10768.41,9500.13,8100.53],  // Renault
];

// Leads mensais
const leadsData = [
  [86,167,182,178,186,75],
  [533,412,944,755,925,170],
  [170,170,309,289,456,151],
  [601,654,1180,1257,1068,0],
  [361,525,588,675,738,488],
];

// CPL por marca acumulado
const cplMarca = [13.10,11.49,13.41,18.10,16.16];

// Totais por marca
const totalLeads = [874,3739,1545,4760,3375];

// CPL geral mensal
const cplGeral = [13.71,14.03,14.79,17.12,13.89,16.30];

// Seguidores
const seguidores = {
  labels:['Renault','Triumph','Yamaha','GWM','Semi Novos','Grupo','Yamaha CF','Peugeot','Citroën'],
  data:  [20957,8251,7925,7541,18100,11500,926,552,619]
};

// 1. Investimento mensal
new Chart(document.getElementById('chartInvest'),{
  type:'bar',
  data:{ labels:MESES, datasets: MARCAS.map((m,i)=>({label:m,data:investData[i],backgroundColor:CORES[i],borderRadius:4,stack:'a'})) },
  options:{ responsive:true, plugins:{legend:{position:'top'}},
    scales:{ x:{stacked:true,grid:{display:false}}, y:{stacked:true,beginAtZero:true,ticks:{callback:v=>'R$'+v.toLocaleString('pt-BR')},grid:{color:'#f1f5f9'}} } }
});

// 2. Total de leads por marca (doughnut)
new Chart(document.getElementById('chartLeadsMarca'),{
  type:'doughnut',
  data:{ labels:MARCAS, datasets:[{data:totalLeads,backgroundColor:CORES,borderWidth:3,borderColor:'#fff',hoverOffset:8}] },
  options:{ responsive:true,cutout:'62%',
    plugins:{ legend:{position:'right'}, tooltip:{callbacks:{label:ctx=>' '+ctx.label+': '+ctx.raw.toLocaleString('pt-BR')+' leads'}} } }
});

// 3. Leads mensais por marca
new Chart(document.getElementById('chartLeadsMes'),{
  type:'line',
  data:{ labels:MESES, datasets: MARCAS.map((m,i)=>({label:m,data:leadsData[i],borderColor:CORES[i],backgroundColor:CORES[i]+'22',tension:.4,fill:true,pointRadius:4,borderWidth:2})) },
  options:{ responsive:true,interaction:{mode:'index',intersect:false},
    plugins:{legend:{position:'top'}}, scales:{y:{beginAtZero:true,grid:{color:'#f1f5f9'}},x:{grid:{color:'#f1f5f9'}}} }
});

// 4. CPL por marca (bar horizontal)
new Chart(document.getElementById('chartCPL'),{
  type:'bar',
  data:{ labels:MARCAS,
    datasets:[{data:cplMarca,backgroundColor:CORES,borderRadius:6,borderSkipped:false}] },
  options:{ indexAxis:'y',responsive:true,
    plugins:{ legend:{display:false}, tooltip:{callbacks:{label:ctx=>' R$ '+ctx.raw.toFixed(2)}} },
    scales:{ x:{beginAtZero:true,ticks:{callback:v=>'R$'+v},grid:{color:'#f1f5f9'}}, y:{grid:{display:false}} } }
});

// 5. Seguidores Instagram (bar)
new Chart(document.getElementById('chartSeguidores'),{
  type:'bar',
  data:{ labels:seguidores.labels,
    datasets:[{data:seguidores.data,
      backgroundColor:['#f2c200','#7c0000','#003087','#c00020','#059669','#6366f1','#e04000','#1a3a6b','#e05a00'],
      borderRadius:6}] },
  options:{ indexAxis:'y',responsive:true,
    plugins:{legend:{display:false}},
    scales:{x:{beginAtZero:true,ticks:{callback:v=>v>=1000?(v/1000).toFixed(0)+'k':v},grid:{color:'#f1f5f9'}},y:{grid:{display:false}}} }
});

// 6. CPL geral evolução
new Chart(document.getElementById('chartCPLGeral'),{
  type:'line',
  data:{ labels:MESES,
    datasets:[{label:'CPL Geral (R$)',data:cplGeral,borderColor:'#6366f1',backgroundColor:'#6366f122',tension:.4,fill:true,pointRadius:5,borderWidth:2.5,
      pointBackgroundColor:'#6366f1'}] },
  options:{ responsive:true,
    plugins:{legend:{display:false}},
    scales:{y:{beginAtZero:false,min:12,max:19,ticks:{callback:v=>'R$'+v.toFixed(0)},grid:{color:'#f1f5f9'}},x:{grid:{color:'#f1f5f9'}}} }
});

// 7. Share de investimento (pie)
new Chart(document.getElementById('chartShareInvest'),{
  type:'pie',
  data:{ labels:MARCAS,
    datasets:[{data:[10891,41806,19578,88070,53356],backgroundColor:CORES,borderWidth:3,borderColor:'#fff',hoverOffset:8}] },
  options:{ responsive:true,
    plugins:{legend:{position:'right'}, tooltip:{callbacks:{label:ctx=>' R$'+ctx.raw.toLocaleString('pt-BR')}}} }
});
</script>
"""
