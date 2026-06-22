import webbrowser
import os
import feedparser
from bs4 import BeautifulSoup
from datetime import datetime

from scraper_autoesporte import buscar_lancamentos_autoesporte
from extrator_lancamento import analisar_lancamento
from specs_portfolio import (
    SPECS, PORTFOLIO, LABEL_MOTORIZACAO,
    get_spec, encontrar_concorrentes, fmt_preco,
)
from gerar_concorrencia import gerar_secao as gerar_secao_concorrencia
from gerar_mkt   import gerar_secao as gerar_secao_mkt
from gerar_lojas import gerar_secao as gerar_secao_lojas

# ─── Feeds de notícias gerais ─────────────────────────────────────────────────

FEEDS_GERAIS = [
    {"portal": "Quatro Rodas",         "url": "https://quatrorodas.abril.com.br/feed/"},
    {"portal": "Flatout",              "url": "https://flatout.com.br/feed/"},
    {"portal": "Noticias Automotivas", "url": "https://www.noticiasautomotivas.com.br/feed/"},
    {"portal": "MotorPress",           "url": "https://www.motorpress.com.br/feed/"},
    {"portal": "Autos Segredos",       "url": "https://autossegredos.com.br/feed/"},
    {"portal": "Auto Industria",       "url": "https://autoindustria.com.br/feed/"},
]

HEADERS_RSS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

def detectar_marca_grupo(texto):
    texto_lower = texto.lower()
    for marca, info in PORTFOLIO.items():
        termos = [marca] + info.get("aliases", [])
        if any(t.lower() in texto_lower for t in termos):
            return marca
    return None

def buscar_noticias_gerais():
    noticias = []
    vistos = set()
    for feed_info in FEEDS_GERAIS:
        print(f"  {feed_info['portal']}...")
        try:
            feed = feedparser.parse(feed_info["url"], request_headers=HEADERS_RSS)
            for entry in feed.entries[:40]:
                link = entry.get("link", "")
                if link in vistos:
                    continue
                titulo = entry.get("title", "")
                resumo = BeautifulSoup(entry.get("summary", ""), "html.parser").get_text()[:350]
                marca  = detectar_marca_grupo(titulo + " " + resumo)
                if marca:
                    vistos.add(link)
                    noticias.append({
                        "portal": feed_info["portal"],
                        "titulo": titulo,
                        "resumo": resumo,
                        "link":   link,
                        "data":   entry.get("published", "")[:16],
                        "marca":  marca,
                        "tipo":   PORTFOLIO[marca]["tipo"],
                    })
        except Exception as e:
            print(f"    Erro: {e}")
    return noticias

# ─── Badges de motorização ────────────────────────────────────────────────────

BADGE_MOT = {
    "combustao":    '<span class="mot-comb">Combustão</span>',
    "hibrido_leve": '<span class="mot-hleve">Híbrido Leve</span>',
    "hibrido":      '<span class="mot-hib">Híbrido / PHEV</span>',
    "eletrico":     '<span class="mot-elet">Elétrico</span>',
}

def badge_mot(tipo):
    return BADGE_MOT.get(tipo, BADGE_MOT["combustao"])

# ─── Tabela comparativa ───────────────────────────────────────────────────────

def tabela_comparacao(titulo, analise):
    concs = analise["concorrentes"]  # lista de (nome, score, motivos)
    specs_lanc = analise["specs"]
    motorizacao_lanc = analise["motorizacao"]

    if not concs and not specs_lanc:
        return ""

    COLUNAS = ["Motorização", "Motor", "Potência", "Torque", "Câmbio", "Tração", "Preço"]

    ths = "".join(f"<th>{c}</th>" for c in COLUNAS)

    def cells_lanc():
        return "".join([
            f"<td>{badge_mot(motorizacao_lanc)}</td>",
            f"<td>{specs_lanc.get('motor','—')}</td>",
            f"<td>{specs_lanc.get('potencia','—')}</td>",
            f"<td>{specs_lanc.get('torque','—')}</td>",
            f"<td>{specs_lanc.get('cambio','—')}</td>",
            f"<td>{specs_lanc.get('tracao','—')}</td>",
            f"<td>{specs_lanc.get('preco','—')}</td>",
        ])

    nome_curto = titulo[:44] + "…" if len(titulo) > 44 else titulo
    linha_novo = ""
    if specs_lanc:
        linha_novo = (
            f'<tr class="tr-novo"><td class="td-modelo">'
            f'<span class="tag-novo">LANÇAMENTO</span><br>{nome_curto}</td>'
            f'{cells_lanc()}</tr>'
        )

    linhas_port = ""
    for nome, score, motivos in concs:
        sp = get_spec(nome)
        if not sp:
            continue
        preco = fmt_preco(sp["preco_from"], sp["preco_to"])
        mot   = sp.get("motorizacao", "combustao")
        score_bar = f'<span class="score-bar" style="width:{score}%"></span>'
        score_txt = f'<span class="score-num">{score}</span>'
        dica = " | ".join(motivos)
        linhas_port += (
            f'<tr class="tr-portfolio" title="{dica}">'
            f'<td class="td-modelo">'
            f'<span class="td-marca-tag">{sp.get("marca","")}</span>{nome}'
            f'<div class="score-wrap">{score_bar}{score_txt}</div></td>'
            f'<td>{badge_mot(mot)}</td>'
            f'<td>{sp.get("motor","—")}</td>'
            f'<td>{sp.get("potencia","—")}</td>'
            f'<td>{sp.get("torque","—")}</td>'
            f'<td>{sp.get("cambio","—")}</td>'
            f'<td>{sp.get("tracao","—")}</td>'
            f'<td>{preco}</td>'
            f'</tr>'
        )

    if not linha_novo and not linhas_port:
        return ""

    carroceria_label = analise["carroceria"].title() if analise["carroceria"] else "—"
    return f"""
    <div class="tabela-comp-wrap">
        <div class="tabela-comp-titulo">
            Concorrentes no portfolio &mdash; Carroceria: <strong>{carroceria_label}</strong>
            &nbsp;|&nbsp; Motorização: <strong>{LABEL_MOTORIZACAO.get(analise['motorizacao'],'—')}</strong>
        </div>
        <div class="tabela-scroll">
        <table class="tabela-comp">
            <thead><tr><th>Modelo</th>{ths}</tr></thead>
            <tbody>{linha_novo}{linhas_port}</tbody>
        </table>
        </div>
    </div>"""

# ─── Cards ────────────────────────────────────────────────────────────────────

def card_lancamento(item):
    analise = item["analise"]
    tem_concs = len(analise["concorrentes"]) > 0
    tabela_html = tabela_comparacao(item["titulo"], analise)
    resumo = item["resumo"] or "Acesse a materia completa."

    badge_conc = '<span class="badge-concorre">Concorre conosco</span>' if tem_concs else ""
    badge_c = f'<span class="badge-seg">{analise["carroceria"].title()}</span>' if analise["carroceria"] else ""
    badge_m = badge_mot(analise["motorizacao"])

    return f"""
    <div class="card {'card-concorre' if tem_concs else 'card-outro'}">
        <div class="card-header">
            <span class="portal">Autoesporte</span>
            {badge_c}{badge_m}{badge_conc}
        </div>
        <h3><a href="{item['link']}" target="_blank">{item['titulo']}</a></h3>
        <p class="resumo">{resumo}</p>
        {tabela_html}
        <div class="card-footer">
            <span class="data">{item['data']}</span>
            <a href="{item['link']}" target="_blank" class="btn-ler">Ler na Autoesporte &rarr;</a>
        </div>
    </div>"""

def card_noticia_geral(item):
    tipo_badge = '<span class="badge-moto">Moto</span>' if item["tipo"] == "moto" else '<span class="badge-carro">Carro</span>'
    return f"""
    <div class="card card-geral">
        <div class="card-header">
            <span class="portal">{item['portal']}</span>
            <span class="marca">{item['marca']}</span>
            {tipo_badge}
        </div>
        <h3><a href="{item['link']}" target="_blank">{item['titulo']}</a></h3>
        <p class="resumo">{item['resumo']}</p>
        <div class="card-footer">
            <span class="data">{item['data']}</span>
            <a href="{item['link']}" target="_blank" class="btn-ler">Ler materia &rarr;</a>
        </div>
    </div>"""

# ─── HTML completo ────────────────────────────────────────────────────────────

def gerar_html(lancamentos, noticias_gerais):
    agora = datetime.now().strftime("%d/%m/%Y as %H:%M")
    n_conc = sum(1 for i in lancamentos if i["analise"]["concorrentes"])

    cards_lanc   = "\n".join(card_lancamento(i) for i in lancamentos) \
                   or "<p class='vazio'>Nenhum lancamento encontrado.</p>"
    cards_gerais = "\n".join(card_noticia_geral(i) for i in noticias_gerais) \
                   or "<p class='vazio'>Nenhuma noticia encontrada.</p>"

    secao_concorrencia = gerar_secao_concorrencia()
    secao_mkt          = gerar_secao_mkt()
    secao_lojas        = gerar_secao_lojas()

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Grupo Demarco / Tozzo</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: 'Segoe UI', sans-serif; background: #f0f2f5; color: #222; }}

  header {{
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    color: white; padding: 24px 40px;
    display: flex; justify-content: space-between; align-items: center;
  }}
  header h1 {{ font-size: 1.5rem; font-weight: 700; letter-spacing: 1px; }}
  .meta {{ font-size: 0.85rem; opacity: 0.7; text-align: right; }}

  /* ── Navegação por abas ── */
  .tabs-nav {{
    background: #1e293b;
    padding: 0 32px;
    display: flex;
    gap: 0;
    border-bottom: 1px solid #334155;
  }}
  .tab-btn {{
    padding: 13px 24px;
    color: #94a3b8;
    font-size: 14px;
    font-weight: 600;
    border: none;
    border-bottom: 3px solid transparent;
    background: none;
    cursor: pointer;
    transition: color .15s;
    white-space: nowrap;
  }}
  .tab-btn:hover {{ color: #e2e8f0; }}
  .tab-btn.active {{ color: #f59e0b; border-bottom-color: #f59e0b; }}

  .tab-content {{ display: none; }}
  .tab-content.active {{ display: block; }}

  /* ── Stats bar ── */
  .stats {{
    background: white; padding: 14px 40px;
    display: flex; gap: 28px; align-items: center;
    border-bottom: 1px solid #e0e0e0; flex-wrap: wrap;
  }}
  .stats .num {{ font-size: 0.88rem; color: #555; }}
  .stats strong {{ color: #1a1a2e; font-size: 1.05rem; }}

  /* ── Conteúdo de notícias ── */
  .container {{ max-width: 1400px; margin: 0 auto; padding: 32px 20px; }}
  h2 {{ font-size: 1.1rem; font-weight: 700; margin-bottom: 6px;
        padding-left: 12px; border-left: 4px solid #e63946; color: #1a1a2e; }}
  h2.noticias {{ border-color: #2d9e6b; }}
  .h2-sub {{ font-size: 0.78rem; color: #888; margin: 0 0 20px 16px; }}

  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(460px, 1fr)); gap: 24px; margin-bottom: 48px; }}

  .card {{
    background: white; border-radius: 10px; padding: 20px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07); border-top: 3px solid #ccc;
    display: flex; flex-direction: column; gap: 12px; transition: transform 0.15s;
  }}
  .card:hover {{ transform: translateY(-2px); box-shadow: 0 5px 16px rgba(0,0,0,0.1); }}
  .card.card-concorre {{ border-top-color: #e63946; }}
  .card.card-outro    {{ border-top-color: #aaa; }}
  .card.card-geral    {{ border-top-color: #2d9e6b; }}

  .card-header {{ display: flex; gap: 6px; align-items: center; flex-wrap: wrap; }}
  .portal {{ background: #f0f2f5; padding: 2px 10px; border-radius: 20px; font-size: 0.71rem; color: #666; }}
  .marca  {{ background: #1a1a2e; color: white; padding: 2px 10px; border-radius: 20px; font-size: 0.71rem; font-weight: 700; }}
  .badge-concorre {{ background: #e63946; color: white; padding: 2px 10px; border-radius: 20px; font-size: 0.71rem; font-weight: 700; }}
  .badge-seg   {{ background: #e8f0fe; color: #1a56db; padding: 2px 9px; border-radius: 20px; font-size: 0.71rem; }}
  .badge-carro {{ background: #e8f0fe; color: #1a56db; padding: 2px 8px; border-radius: 20px; font-size: 0.71rem; }}
  .badge-moto  {{ background: #fef3e2; color: #c0622a; padding: 2px 8px; border-radius: 20px; font-size: 0.71rem; }}

  .mot-comb  {{ background:#f3f4f6; color:#374151; padding:2px 8px; border-radius:4px; font-size:0.7rem; font-weight:600; white-space:nowrap; }}
  .mot-hleve {{ background:#fef3c7; color:#92400e; padding:2px 8px; border-radius:4px; font-size:0.7rem; font-weight:600; white-space:nowrap; }}
  .mot-hib   {{ background:#ede9fe; color:#5b21b6; padding:2px 8px; border-radius:4px; font-size:0.7rem; font-weight:600; white-space:nowrap; }}
  .mot-elet  {{ background:#d1fae5; color:#065f46; padding:2px 8px; border-radius:4px; font-size:0.7rem; font-weight:600; white-space:nowrap; }}

  .card h3 {{ font-size: 0.95rem; line-height: 1.4; }}
  .card h3 a {{ color: #1a1a2e; text-decoration: none; }}
  .card h3 a:hover {{ color: #e63946; }}
  .resumo {{ font-size: 0.82rem; color: #555; line-height: 1.6; }}

  .tabela-comp-wrap {{ background: #f4f6ff; border: 1px solid #dde3f0; border-radius: 8px; padding: 14px; }}
  .tabela-comp-titulo {{ font-size: 0.74rem; color: #444; margin-bottom: 10px; }}
  .tabela-comp-titulo strong {{ color: #1a1a2e; }}
  .tabela-scroll {{ overflow-x: auto; }}
  .tabela-comp {{ width: 100%; border-collapse: collapse; font-size: 0.73rem; }}
  .tabela-comp th {{ background: #1a1a2e; color: white; padding: 7px 10px; text-align: left; white-space: nowrap; }}
  .tabela-comp td {{ padding: 6px 10px; border-bottom: 1px solid #eee; vertical-align: middle; }}
  .td-modelo {{ font-weight: 600; min-width: 170px; }}
  .td-marca-tag {{ display: inline-block; background: #1a1a2e; color: white; font-size: 0.62rem; padding: 1px 6px; border-radius: 4px; margin-right: 5px; vertical-align: middle; }}
  .tr-novo td {{ background: #fff5f5; }}
  .tr-portfolio td {{ background: white; }}
  .tr-portfolio:hover td {{ background: #f0f7ff; cursor: help; }}
  .tag-novo {{ display: inline-block; background: #e63946; color: white; font-size: 0.62rem; font-weight: 700; padding: 1px 7px; border-radius: 4px; vertical-align: middle; }}

  .score-wrap {{ position: relative; height: 4px; background: #eee; border-radius: 2px; margin-top: 4px; width: 100%; }}
  .score-bar  {{ position: absolute; left: 0; top: 0; height: 4px; background: #e63946; border-radius: 2px; }}
  .score-num  {{ font-size: 0.6rem; color: #aaa; margin-left: 2px; position: absolute; right: 0; top: -1px; }}

  .card-footer {{ display: flex; justify-content: space-between; align-items: center; margin-top: auto; }}
  .data {{ font-size: 0.71rem; color: #bbb; }}
  .btn-ler {{ font-size: 0.79rem; color: #457b9d; text-decoration: none; font-weight: 600; }}
  .btn-ler:hover {{ color: #e63946; }}
  .vazio {{ color: #999; font-style: italic; padding: 20px 0; }}

  /* ── Aba concorrência ── */
  .conc-wrap {{ max-width: 1300px; margin: 28px auto; padding: 0 24px; }}
</style>
</head>
<body>

<header>
  <div>
    <div style="font-size:0.7rem;opacity:0.5;margin-bottom:4px;letter-spacing:2px">GRUPO DEMARCO / TOZZO</div>
    <h1>Central de Inteligencia Automotiva</h1>
  </div>
  <div class="meta">Atualizado em<br><strong style="font-size:1rem;opacity:1">{agora}</strong></div>
</header>

<nav class="tabs-nav">
  <button class="tab-btn active" onclick="abrirAba('lancamentos', this)">Lancamentos</button>
  <button class="tab-btn" onclick="abrirAba('noticias', this)">Noticias das Marcas</button>
  <button class="tab-btn" onclick="abrirAba('concorrencia', this)">Concorrencia</button>
  <button class="tab-btn" onclick="abrirAba('lojas', this)">Nossas Lojas</button>
  <button class="tab-btn" onclick="abrirAba('mkt', this)">Painel MKT</button>
</nav>

<!-- ABA: Lancamentos -->
<div id="aba-lancamentos" class="tab-content active">
  <div class="stats">
    <div class="num"><strong>{len(lancamentos)}</strong> lancamentos analisados</div>
    <div class="num"><strong>{n_conc}</strong> concorrem com nosso portfolio</div>
    <div class="num">Fonte: Autoesporte</div>
  </div>
  <div class="container">
    <h2>Lancamentos do Mercado</h2>
    <p class="h2-sub">Cards com borda vermelha concorrem com o portfolio. Tabela mostra todos os modelos concorrentes por carroceria + preco + potencia + motorizacao.</p>
    <div class="grid">{cards_lanc}</div>
  </div>
</div>

<!-- ABA: Noticias gerais -->
<div id="aba-noticias" class="tab-content">
  <div class="stats">
    <div class="num"><strong>{len(noticias_gerais)}</strong> noticias encontradas</div>
    <div class="num">Fontes: Quatro Rodas, Flatout, Noticias Automotivas, MotorPress e outros</div>
  </div>
  <div class="container">
    <h2 class="noticias">Noticias das Nossas Marcas</h2>
    <div class="grid">{cards_gerais}</div>
  </div>
</div>

<!-- ABA: Concorrência -->
<div id="aba-concorrencia" class="tab-content">
  <div class="conc-wrap">
    <div style="background:#fff;border-radius:10px;padding:14px 20px;margin-bottom:8px;border-left:4px solid #f59e0b;font-size:13px;color:#374151">
      <b>Guia Comercial</b> — portfolio do grupo x mercado brasileiro. Use como base de treinamento e consulta de vendedores.
    </div>
    {secao_concorrencia}
    <div style="text-align:center;padding:24px 0 8px;font-size:12px;color:#9ca3af">Grupo Demarco / Tozzo &mdash; {agora}</div>
  </div>
</div>

<!-- ABA: Nossas Lojas -->
<div id="aba-lojas" class="tab-content">
  {secao_lojas}
</div>

<!-- ABA: Painel MKT -->
<div id="aba-mkt" class="tab-content">
  {secao_mkt}
</div>

<script>
function abrirAba(nome, btn) {{
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById('aba-' + nome).classList.add('active');
  btn.classList.add('active');
}}
</script>
</body>
</html>"""

# ─── Main ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  News Grupo Demarco/Tozzo")
    print("=" * 55)

    print("\n[1/2] Lancamentos — Autoesporte")
    lancamentos_raw = buscar_lancamentos_autoesporte(max_artigos=20)

    lancamentos = []
    for i, item in enumerate(lancamentos_raw):
        print(f"  Analisando [{i+1}/{len(lancamentos_raw)}]: {item['titulo'][:50]}...")
        analise = analisar_lancamento(item["titulo"], item["resumo"], item["link"])
        analise["concorrentes"] = encontrar_concorrentes(
            analise["carroceria"],
            analise["preco_num"],
            analise["potencia_num"],
            analise["motorizacao"],
        )
        item["analise"] = analise
        n = len(analise["concorrentes"])
        if n:
            print(f"    -> {n} concorrentes | carroceria={analise['carroceria']} mot={analise['motorizacao']}")
        lancamentos.append(item)

    n_conc = sum(1 for i in lancamentos if i["analise"]["concorrentes"])
    print(f"\nTotal: {len(lancamentos)} lancamentos | {n_conc} concorrem com o portfolio")

    print("\n[2/2] Noticias gerais — multiplos portais")
    noticias_gerais = buscar_noticias_gerais()
    print(f"  {len(noticias_gerais)} noticias encontradas")

    html = gerar_html(lancamentos, noticias_gerais)

    saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
    with open(saida, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"\nHTML gerado: {saida}")
    webbrowser.open(f"file:///{saida}")

    # ── Publica no GitHub Pages automaticamente ───────────────────────────────
    print("\nPublicando no GitHub Pages...")
    import subprocess
    try:
        subprocess.run(["git", "add", "index.html"], cwd=os.path.dirname(saida), check=True)
        agora_pub = datetime.now().strftime("%d/%m/%Y %H:%M")
        subprocess.run(["git", "commit", "-m", f"Atualizacao automatica {agora_pub}"], cwd=os.path.dirname(saida))
        result = subprocess.run(["git", "push"], cwd=os.path.dirname(saida), capture_output=True, text=True)
        print("  Publicado em: https://alessanderdemarco.github.io/news-grupo-demarco/")
    except Exception as e:
        print(f"  Aviso: nao foi possivel publicar automaticamente — {e}")
