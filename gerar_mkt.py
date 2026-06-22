"""
Gera a seção HTML do Painel de Marketing.
Dados de exemplo — substitua pelos reais exportados do NBS/CRM.
"""

def gerar_secao():
    return """
<div id="mkt-root">

<!-- KPIs -->
<div class="mkt-kpis">
  <div class="kpi-card" style="--accent:#f59e0b">
    <div class="kpi-icon">&#9654;</div>
    <div class="kpi-valor" id="kpi-leads">1.284</div>
    <div class="kpi-label">Leads no Mês</div>
    <div class="kpi-delta pos">&#9650; 12% vs mês anterior</div>
  </div>
  <div class="kpi-card" style="--accent:#10b981">
    <div class="kpi-icon">&#10003;</div>
    <div class="kpi-valor" id="kpi-vendas">187</div>
    <div class="kpi-label">Vendas Fechadas</div>
    <div class="kpi-delta pos">&#9650; 8% vs mês anterior</div>
  </div>
  <div class="kpi-card" style="--accent:#6366f1">
    <div class="kpi-icon">&#37;</div>
    <div class="kpi-valor" id="kpi-conv">14,6%</div>
    <div class="kpi-label">Taxa de Conversão</div>
    <div class="kpi-delta neg">&#9660; 0,4pp vs mês anterior</div>
  </div>
  <div class="kpi-card" style="--accent:#ec4899">
    <div class="kpi-icon">R$</div>
    <div class="kpi-valor" id="kpi-ticket">R$ 148k</div>
    <div class="kpi-label">Ticket Médio</div>
    <div class="kpi-delta pos">&#9650; 5% vs mês anterior</div>
  </div>
  <div class="kpi-card" style="--accent:#0ea5e9">
    <div class="kpi-icon">&#9733;</div>
    <div class="kpi-valor" id="kpi-nps">72</div>
    <div class="kpi-label">NPS</div>
    <div class="kpi-delta pos">&#9650; 3pts vs mês anterior</div>
  </div>
  <div class="kpi-card" style="--accent:#f97316">
    <div class="kpi-icon">&#9993;</div>
    <div class="kpi-valor" id="kpi-followup">64%</div>
    <div class="kpi-label">Follow-up em dia</div>
    <div class="kpi-delta neg">&#9660; 2% vs mês anterior</div>
  </div>
</div>

<!-- Linha 1: Evolução de vendas + Vendas por marca -->
<div class="mkt-row">
  <div class="mkt-chart-card wide">
    <div class="chart-title">Evolução de Vendas — Últimos 12 Meses</div>
    <canvas id="chartEvolucao" height="90"></canvas>
  </div>
  <div class="mkt-chart-card">
    <div class="chart-title">Vendas por Marca</div>
    <canvas id="chartMarcas" height="180"></canvas>
  </div>
</div>

<!-- Linha 2: Funil + Origem de leads -->
<div class="mkt-row">
  <div class="mkt-chart-card">
    <div class="chart-title">Funil de Vendas — Mês Atual</div>
    <canvas id="chartFunil" height="200"></canvas>
  </div>
  <div class="mkt-chart-card">
    <div class="chart-title">Origem dos Leads</div>
    <canvas id="chartOrigens" height="200"></canvas>
  </div>
  <div class="mkt-chart-card">
    <div class="chart-title">Mix por Segmento</div>
    <canvas id="chartSegmento" height="200"></canvas>
  </div>
</div>

<!-- Linha 3: Performance por loja -->
<div class="mkt-row">
  <div class="mkt-chart-card full">
    <div class="chart-title">Performance por Loja — Vendas vs Meta</div>
    <canvas id="chartLojas" height="80"></canvas>
  </div>
</div>

<!-- Linha 4: Motorização + Conversão por canal -->
<div class="mkt-row">
  <div class="mkt-chart-card">
    <div class="chart-title">Vendas por Motorização</div>
    <canvas id="chartMotorizacao" height="200"></canvas>
  </div>
  <div class="mkt-chart-card wide">
    <div class="chart-title">Conversão por Canal de Atendimento</div>
    <canvas id="chartCanal" height="200"></canvas>
  </div>
</div>

<div style="text-align:center;font-size:11px;color:#94a3b8;padding:16px 0 4px">
  Dados de exemplo — conecte ao NBS/CRM para dados reais
</div>

</div>

<style>
#mkt-root { padding: 28px 32px; max-width: 1400px; margin: 0 auto; }

.mkt-kpis {
  display: grid;
  grid-template-columns: repeat(6, 1fr);
  gap: 16px;
  margin-bottom: 24px;
}
@media(max-width:1100px){ .mkt-kpis{ grid-template-columns: repeat(3,1fr); } }
@media(max-width:700px){ .mkt-kpis{ grid-template-columns: repeat(2,1fr); } }

.kpi-card {
  background: #fff;
  border-radius: 14px;
  padding: 20px 18px;
  box-shadow: 0 2px 12px rgba(0,0,0,.07);
  border-top: 4px solid var(--accent);
  position: relative;
  overflow: hidden;
}
.kpi-card::before {
  content:'';
  position:absolute;
  top:-20px; right:-20px;
  width:80px; height:80px;
  background: var(--accent);
  opacity:.07;
  border-radius:50%;
}
.kpi-icon {
  font-size: 18px;
  color: var(--accent);
  margin-bottom: 8px;
  font-weight: 700;
}
.kpi-valor {
  font-size: 26px;
  font-weight: 800;
  color: #1e293b;
  line-height: 1;
  margin-bottom: 4px;
}
.kpi-label {
  font-size: 12px;
  color: #6b7280;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: .5px;
  margin-bottom: 6px;
}
.kpi-delta { font-size: 11px; font-weight: 600; }
.kpi-delta.pos { color: #10b981; }
.kpi-delta.neg { color: #ef4444; }

.mkt-row {
  display: flex;
  gap: 20px;
  margin-bottom: 20px;
  flex-wrap: wrap;
}
.mkt-chart-card {
  background: #fff;
  border-radius: 14px;
  padding: 20px 22px;
  box-shadow: 0 2px 12px rgba(0,0,0,.07);
  flex: 1;
  min-width: 240px;
}
.mkt-chart-card.wide { flex: 2; }
.mkt-chart-card.full { flex: 1 1 100%; }

.chart-title {
  font-size: 13px;
  font-weight: 700;
  color: #374151;
  text-transform: uppercase;
  letter-spacing: .5px;
  margin-bottom: 16px;
  padding-bottom: 10px;
  border-bottom: 2px solid #f1f5f9;
}
</style>

<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script>
Chart.defaults.font.family = "'Segoe UI', sans-serif";
Chart.defaults.color = '#6b7280';

const MESES = ['Jul/24','Ago/24','Set/24','Out/24','Nov/24','Dez/24','Jan/25','Fev/25','Mar/25','Abr/25','Mai/25','Jun/25'];
const CORES = {
  renault:'#f2c200', gwm:'#c00020', peugeot:'#1a3a6b',
  citroen:'#e05a00', geely:'#0050b0', motos:'#7c3aed'
};

// 1. Evolução de vendas
new Chart(document.getElementById('chartEvolucao'), {
  type: 'line',
  data: {
    labels: MESES,
    datasets: [
      { label:'Renault',  data:[28,31,29,35,30,22,18,24,30,33,36,38], borderColor:CORES.renault,  backgroundColor:CORES.renault+'22',  tension:.4, fill:true, pointRadius:4 },
      { label:'GWM',      data:[18,20,22,24,19,15,12,16,22,25,26,28], borderColor:CORES.gwm,      backgroundColor:CORES.gwm+'22',      tension:.4, fill:true, pointRadius:4 },
      { label:'Peugeot',  data:[14,15,13,16,12,10,9,11,14,15,17,18],  borderColor:CORES.peugeot,  backgroundColor:CORES.peugeot+'22',  tension:.4, fill:true, pointRadius:4 },
      { label:'Citroen',  data:[12,13,14,15,11,9,8,10,13,14,15,16],   borderColor:CORES.citroen,  backgroundColor:CORES.citroen+'22',  tension:.4, fill:true, pointRadius:4 },
      { label:'Geely',    data:[5,6,7,8,7,5,4,6,8,9,10,11],           borderColor:CORES.geely,    backgroundColor:CORES.geely+'22',    tension:.4, fill:true, pointRadius:4 },
      { label:'Motos',    data:[10,11,12,13,9,8,7,9,11,12,13,14],     borderColor:CORES.motos,    backgroundColor:CORES.motos+'22',    tension:.4, fill:true, pointRadius:4 },
    ]
  },
  options: { responsive:true, interaction:{mode:'index',intersect:false}, plugins:{legend:{position:'top'}}, scales:{y:{beginAtZero:true,grid:{color:'#f1f5f9'}},x:{grid:{color:'#f1f5f9'}}} }
});

// 2. Vendas por marca (doughnut)
new Chart(document.getElementById('chartMarcas'), {
  type: 'doughnut',
  data: {
    labels:['Renault','GWM','Peugeot','Citroen','Geely','Motos'],
    datasets:[{ data:[38,28,18,16,11,14], backgroundColor:Object.values(CORES), borderWidth:3, borderColor:'#fff', hoverOffset:8 }]
  },
  options: { responsive:true, cutout:'65%', plugins:{legend:{position:'right'},tooltip:{callbacks:{label:ctx=>' '+ctx.label+': '+ctx.raw+' un.'}}} }
});

// 3. Funil
new Chart(document.getElementById('chartFunil'), {
  type: 'bar',
  data: {
    labels:['Leads','Contato','Agendamento','Test Drive','Proposta','Venda'],
    datasets:[{ data:[1284,820,490,310,230,187], backgroundColor:['#dbeafe','#bfdbfe','#93c5fd','#60a5fa','#3b82f6','#1d4ed8'], borderRadius:6, borderSkipped:false }]
  },
  options: { indexAxis:'y', responsive:true, plugins:{legend:{display:false}}, scales:{x:{beginAtZero:true,grid:{color:'#f1f5f9'}},y:{grid:{display:false}}} }
});

// 4. Origem dos leads (pie)
new Chart(document.getElementById('chartOrigens'), {
  type: 'pie',
  data: {
    labels:['Instagram','Google Ads','Site','Indicação','Walk-in','WhatsApp','OLX/Webmotors'],
    datasets:[{ data:[28,22,15,12,8,10,5], backgroundColor:['#ec4899','#f97316','#10b981','#6366f1','#0ea5e9','#84cc16','#f59e0b'], borderWidth:3, borderColor:'#fff' }]
  },
  options:{ responsive:true, plugins:{legend:{position:'right'}} }
});

// 5. Mix por segmento
new Chart(document.getElementById('chartSegmento'), {
  type: 'doughnut',
  data: {
    labels:['SUV Compacto','Hatch','SUV Médio','Picape','Elétrico/PHEV','Motos'],
    datasets:[{ data:[38,20,18,12,7,5], backgroundColor:['#0ea5e9','#10b981','#6366f1','#f59e0b','#22d3ee','#a78bfa'], borderWidth:3, borderColor:'#fff', hoverOffset:8 }]
  },
  options:{ responsive:true, cutout:'60%', plugins:{legend:{position:'right'}} }
});

// 6. Performance por loja
new Chart(document.getElementById('chartLojas'), {
  type: 'bar',
  data: {
    labels:['Renault Chapecó','GWM Chapecó','Peugeot Chapecó','Citroen Chapecó','Renault Xanxerê','GWM Concórdia','Peugeot Joaçaba','Geely Chapecó','Triumph/Yamaha','CF Moto'],
    datasets:[
      { label:'Vendas', data:[38,28,18,16,22,15,12,11,14,10], backgroundColor:'#3b82f6', borderRadius:5 },
      { label:'Meta',   data:[35,30,20,18,20,18,15,12,15,12], backgroundColor:'#e2e8f0', borderRadius:5 }
    ]
  },
  options:{ responsive:true, plugins:{legend:{position:'top'}}, scales:{x:{grid:{display:false}},y:{beginAtZero:true,grid:{color:'#f1f5f9'}}} }
});

// 7. Motorização
new Chart(document.getElementById('chartMotorizacao'), {
  type: 'doughnut',
  data: {
    labels:['Combustão','Híbrido/PHEV','Elétrico','Híbrido Leve'],
    datasets:[{ data:[68,15,12,5], backgroundColor:['#6b7280','#16a34a','#2563eb','#ca8a04'], borderWidth:3, borderColor:'#fff', hoverOffset:8 }]
  },
  options:{ responsive:true, cutout:'60%', plugins:{legend:{position:'right'}} }
});

// 8. Conversão por canal
new Chart(document.getElementById('chartCanal'), {
  type: 'bar',
  data: {
    labels:['WhatsApp','Visita presencial','Telefone','Site','Instagram','Google Ads','Indicação'],
    datasets:[{
      label:'Taxa de conversão (%)',
      data:[22,31,18,12,9,14,28],
      backgroundColor:['#10b981','#3b82f6','#f59e0b','#6366f1','#ec4899','#f97316','#0ea5e9'],
      borderRadius:6
    }]
  },
  options:{ responsive:true, plugins:{legend:{display:false}}, scales:{x:{grid:{display:false}},y:{beginAtZero:true,max:40,ticks:{callback:v=>v+'%'},grid:{color:'#f1f5f9'}}} }
});
</script>
"""
