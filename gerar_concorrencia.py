"""
Gera concorrencia.html — aba de análise de concorrência
Portfólio do Grupo Demarco/Tozzo x Mercado Brasileiro
Atualização recomendada: semanal
"""

import os
from datetime import datetime
from specs_portfolio import SPECS, PORTFOLIO, LABEL_MOTORIZACAO, GRUPOS_CARROCERIA

SAIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "concorrencia.html")

# ── Concorrentes do mercado por segmento ──────────────────────────────────────
# Dados de referência (atualizar mensalmente ou via scraper)

CONCORRENTES_MERCADO = {
    # Hatch Entry / Compacto
    "Hatch Entry": [
        {"modelo": "Chevrolet Onix", "marca": "Chevrolet", "preco": "R$ 82.990 – 107.990", "motor": "1.0 Turbo 116cv", "motorizacao": "combustao"},
        {"modelo": "Volkswagen Polo", "marca": "Volkswagen", "preco": "R$ 99.990 – 129.990", "motor": "1.0 TSI 116cv", "motorizacao": "combustao"},
        {"modelo": "Fiat Argo", "marca": "Fiat", "preco": "R$ 84.990 – 109.990", "motor": "1.0 / 1.3 Turbo 109cv", "motorizacao": "combustao"},
        {"modelo": "Hyundai HB20", "marca": "Hyundai", "preco": "R$ 89.990 – 119.990", "motor": "1.0 Turbo 120cv", "motorizacao": "combustao"},
        {"modelo": "Toyota Yaris", "marca": "Toyota", "preco": "R$ 112.990 – 134.990", "motor": "1.3 / 1.5 107–110cv", "motorizacao": "combustao"},
        {"modelo": "Caoa Chery iCAR S53", "marca": "Caoa Chery", "preco": "R$ 89.990 – 109.990", "motor": "1.5 Turbo 130cv", "motorizacao": "combustao"},
    ],
    # SUV Compacto Entry
    "SUV Compacto Entry": [
        {"modelo": "Fiat Pulse", "marca": "Fiat", "preco": "R$ 109.990 – 154.990", "motor": "1.0 Turbo 130cv", "motorizacao": "combustao"},
        {"modelo": "Volkswagen T-Cross", "marca": "Volkswagen", "preco": "R$ 129.990 – 164.990", "motor": "1.0 TSI 128cv", "motorizacao": "combustao"},
        {"modelo": "Hyundai Creta", "marca": "Hyundai", "preco": "R$ 134.990 – 184.990", "motor": "1.0 Turbo 120cv", "motorizacao": "combustao"},
        {"modelo": "Jeep Renegade", "marca": "Jeep", "preco": "R$ 129.990 – 169.990", "motor": "1.3 Turbo 185cv (4xe PHEV)", "motorizacao": "combustao"},
        {"modelo": "Honda HR-V", "marca": "Honda", "preco": "R$ 164.990 – 204.990", "motor": "1.5 Turbo 177cv", "motorizacao": "combustao"},
        {"modelo": "Toyota Corolla Cross", "marca": "Toyota", "preco": "R$ 174.990 – 229.990", "motor": "2.0 Hybrid 197cv", "motorizacao": "hibrido"},
        {"modelo": "Caoa Chery Tiggo 5x", "marca": "Caoa Chery", "preco": "R$ 119.990 – 154.990", "motor": "1.5 Turbo 150cv", "motorizacao": "combustao"},
        {"modelo": "BYD Dolphin Mini", "marca": "BYD", "preco": "R$ 99.800 – 119.800", "motor": "Elétrico 95cv", "motorizacao": "eletrico"},
    ],
    # SUV Médio
    "SUV Médio": [
        {"modelo": "Toyota RAV4", "marca": "Toyota", "preco": "R$ 259.990 – 319.990", "motor": "2.5 Hybrid 222cv", "motorizacao": "hibrido"},
        {"modelo": "Volkswagen Tiguan", "marca": "Volkswagen", "preco": "R$ 229.990 – 289.990", "motor": "1.4 TSI 150cv / 2.0 TSI 320cv", "motorizacao": "combustao"},
        {"modelo": "Jeep Compass", "marca": "Jeep", "preco": "R$ 179.990 – 259.990", "motor": "1.3 Turbo 185–270cv (4xe PHEV)", "motorizacao": "hibrido"},
        {"modelo": "Hyundai Tucson", "marca": "Hyundai", "preco": "R$ 219.990 – 279.990", "motor": "1.6 Turbo 180cv", "motorizacao": "combustao"},
        {"modelo": "Honda CR-V", "marca": "Honda", "preco": "R$ 259.990 – 299.990", "motor": "2.0 Hybrid 204cv", "motorizacao": "hibrido"},
        {"modelo": "Caoa Chery Tiggo 8", "marca": "Caoa Chery", "preco": "R$ 189.990 – 249.990", "motor": "1.6 Turbo 186cv", "motorizacao": "combustao"},
        {"modelo": "BYD Song Plus", "marca": "BYD", "preco": "R$ 219.990 – 269.990", "motor": "1.5 Turbo PHEV 243cv", "motorizacao": "hibrido"},
    ],
    # SUV Grande / Off-road
    "SUV Grande Off-road": [
        {"modelo": "Toyota Land Cruiser Prado", "marca": "Toyota", "preco": "R$ 469.990 – 569.990", "motor": "2.4 Turbo + Elétrico 326cv", "motorizacao": "hibrido"},
        {"modelo": "Jeep Grand Cherokee", "marca": "Jeep", "preco": "R$ 399.990 – 569.990", "motor": "2.0 Turbo 272cv / 4xe PHEV 375cv", "motorizacao": "hibrido"},
        {"modelo": "Volkswagen Amarok", "marca": "Volkswagen", "preco": "R$ 329.990 – 469.990", "motor": "2.0 / 3.0 TDI 204–258cv", "motorizacao": "combustao"},
        {"modelo": "Ford Bronco", "marca": "Ford", "preco": "R$ 399.990 – 469.990", "motor": "2.0 EcoBoost 330cv", "motorizacao": "combustao"},
        {"modelo": "Mitsubishi Pajero Sport", "marca": "Mitsubishi", "preco": "R$ 289.990 – 339.990", "motor": "2.4 Turbo Diesel 181cv", "motorizacao": "combustao"},
    ],
    # Picape Compacta
    "Picape Compacta": [
        {"modelo": "Fiat Strada", "marca": "Fiat", "preco": "R$ 109.990 – 154.990", "motor": "1.3 Turbo 109cv", "motorizacao": "combustao"},
        {"modelo": "Volkswagen Saveiro", "marca": "Volkswagen", "preco": "R$ 92.990 – 119.990", "motor": "1.6 8V 104cv", "motorizacao": "combustao"},
        {"modelo": "Chevrolet Montana", "marca": "Chevrolet", "preco": "R$ 139.990 – 184.990", "motor": "1.2 Turbo 133cv", "motorizacao": "combustao"},
    ],
    # Picape Média
    "Picape Média": [
        {"modelo": "Fiat Toro", "marca": "Fiat", "preco": "R$ 169.990 – 259.990", "motor": "1.3 Turbo / 2.0 Diesel 152–170cv", "motorizacao": "combustao"},
        {"modelo": "Toyota Hilux", "marca": "Toyota", "preco": "R$ 249.990 – 339.990", "motor": "2.8 Diesel 204cv", "motorizacao": "combustao"},
        {"modelo": "Volkswagen Amarok", "marca": "Volkswagen", "preco": "R$ 329.990 – 469.990", "motor": "2.0 / 3.0 V6 TDI 204–258cv", "motorizacao": "combustao"},
        {"modelo": "Chevrolet S10", "marca": "Chevrolet", "preco": "R$ 249.990 – 349.990", "motor": "2.5 / 2.8 Diesel 200cv", "motorizacao": "combustao"},
        {"modelo": "Mitsubishi L200", "marca": "Mitsubishi", "preco": "R$ 259.990 – 319.990", "motor": "2.4 Diesel 181cv", "motorizacao": "combustao"},
        {"modelo": "Ford Ranger", "marca": "Ford", "preco": "R$ 279.990 – 399.990", "motor": "2.0 / 3.0 Diesel 205–250cv", "motorizacao": "combustao"},
        {"modelo": "Jeep Gladiator", "marca": "Jeep", "preco": "R$ 399.990 – 449.990", "motor": "2.0 Turbo 272cv", "motorizacao": "combustao"},
    ],
    # Elétrico Compacto
    "Elétrico Compacto": [
        {"modelo": "BYD Dolphin", "marca": "BYD", "preco": "R$ 159.800 – 194.800", "motor": "Elétrico 204cv", "motorizacao": "eletrico"},
        {"modelo": "BYD Seagull", "marca": "BYD", "preco": "R$ 114.800 – 134.800", "motor": "Elétrico 74cv", "motorizacao": "eletrico"},
        {"modelo": "Caoa Chery iCAR Q6", "marca": "Caoa Chery", "preco": "R$ 179.990 – 209.990", "motor": "Elétrico 204cv", "motorizacao": "eletrico"},
        {"modelo": "Volkswagen ID.3", "marca": "Volkswagen", "preco": "R$ 209.990 – 229.990", "motor": "Elétrico 204cv", "motorizacao": "eletrico"},
    ],
    # SUV Elétrico
    "SUV Elétrico": [
        {"modelo": "BYD Atto 3", "marca": "BYD", "preco": "R$ 219.800 – 244.800", "motor": "Elétrico 204cv", "motorizacao": "eletrico"},
        {"modelo": "BYD Seal U DM-i", "marca": "BYD", "preco": "R$ 249.800 – 289.800", "motor": "PHEV 218cv", "motorizacao": "hibrido"},
        {"modelo": "Volkswagen ID.4", "marca": "Volkswagen", "preco": "R$ 289.990 – 329.990", "motor": "Elétrico 204–299cv", "motorizacao": "eletrico"},
        {"modelo": "Toyota bZ4X", "marca": "Toyota", "preco": "R$ 299.990 – 349.990", "motor": "Elétrico 204cv", "motorizacao": "eletrico"},
    ],
}

# ── Agrupamento do portfólio por segmento ─────────────────────────────────────

SEGMENTOS_PORTFOLIO = {
    "Hatch Entry": ["Renault Kwid"],
    "Hatch Compacto": ["Peugeot 208", "Citroen C3"],
    "Hatch Elétrico Compacto": ["Geely EX2"],
    "Hatch Elétrico": ["Ora 03"],
    "SUV Compacto Entry": ["Renault Kardian", "Citroen Basalt", "Citroen Aircross", "Peugeot 2008"],
    "SUV Compacto": ["Renault Duster", "Haval Jolion"],
    "SUV Médio": ["Renault Boreal", "Haval H6"],
    "SUV Elétrico Compacto": ["Geely EX5"],
    "SUV Compacto PHEV": ["Geely EX5 EM-I"],
    "SUV Grande PHEV": ["Tank 500"],
    "SUV Off-road": ["Tank 300"],
    "SUV Grande Off-road": ["Haval H9"],
    "Picape Compacta": ["Renault Oroch"],
    "Picape Média": ["Renault Niagara"],
}

# Mapeamento de segmento portfólio → chave em CONCORRENTES_MERCADO
MAPA_CONCORRENTES = {
    "Hatch Entry": "Hatch Entry",
    "Hatch Compacto": "Hatch Entry",
    "Hatch Elétrico Compacto": "Elétrico Compacto",
    "Hatch Elétrico": "Elétrico Compacto",
    "SUV Compacto Entry": "SUV Compacto Entry",
    "SUV Compacto": "SUV Compacto Entry",
    "SUV Médio": "SUV Médio",
    "SUV Elétrico Compacto": "SUV Elétrico",
    "SUV Compacto PHEV": "SUV Elétrico",
    "SUV Grande PHEV": "SUV Grande Off-road",
    "SUV Off-road": "SUV Grande Off-road",
    "SUV Grande Off-road": "SUV Grande Off-road",
    "Picape Compacta": "Picape Compacta",
    "Picape Média": "Picape Média",
}

COR_MARCA = {
    "Renault": "#f2c200",
    "GWM": "#c00020",
    "Peugeot": "#1a3a6b",
    "Citroen": "#e05a00",
    "Geely": "#0050b0",
    "CF Moto": "#e04000",
    "Yamaha": "#003087",
    "Triumph": "#c00020",
}


def badge_motorizacao(mot):
    cores = {
        "combustao": ("#6b7280", "Combustão"),
        "hibrido_leve": ("#ca8a04", "Híbrido Leve"),
        "hibrido": ("#16a34a", "Híbrido/PHEV"),
        "eletrico": ("#2563eb", "Elétrico"),
    }
    cor, label = cores.get(mot, ("#6b7280", mot))
    return f'<span style="background:{cor};color:#fff;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:600">{label}</span>'


def card_portfolio(modelo, spec):
    cor = COR_MARCA.get(spec["marca"], "#374151")
    mot_badge = badge_motorizacao(spec.get("motorizacao", "combustao"))
    preco = f"R$ {spec['preco_from']:,.0f}".replace(",", ".") + " – " + f"R$ {spec['preco_to']:,.0f}".replace(",", ".")
    potencia = spec.get("potencia", f"{spec['potencia_min']}–{spec['potencia_max']} cv")
    return f"""
<div style="background:#fff;border:2px solid {cor};border-radius:10px;padding:14px 16px;min-width:220px;max-width:280px">
  <div style="font-size:11px;color:{cor};font-weight:700;text-transform:uppercase;letter-spacing:1px">{spec['marca']}</div>
  <div style="font-size:17px;font-weight:700;color:#111;margin:2px 0 6px">{modelo}</div>
  <div style="font-size:12px;color:#4b5563;line-height:1.7">
    <b>Motor:</b> {spec.get('motor','—')}<br>
    <b>Potência:</b> {potencia}<br>
    <b>Preço:</b> {preco}<br>
    <b>Câmbio:</b> {spec.get('cambio','—')}<br>
    <b>Tração:</b> {spec.get('tracao','—')}
  </div>
  <div style="margin-top:8px">{mot_badge}</div>
</div>"""


def card_concorrente(c):
    cor_marca = {
        "Volkswagen": "#1b5f9e", "Jeep": "#2a6117", "Fiat": "#9b1c1c",
        "Toyota": "#c8102e", "Honda": "#cc0000", "Hyundai": "#002c5f",
        "Kia": "#c40b28", "Nissan": "#c3002f", "BYD": "#1d4ed8",
        "Caoa Chery": "#7c2d12", "Chevrolet": "#c79020", "Ford": "#003087",
        "Mitsubishi": "#c0392b", "Volvo": "#003057", "BMW": "#1c69d4",
    }
    cor = cor_marca.get(c.get("marca", ""), "#374151")
    mot_badge = badge_motorizacao(c.get("motorizacao", "combustao"))
    return f"""
<div style="background:#f9fafb;border:1.5px solid #d1d5db;border-left:4px solid {cor};border-radius:8px;padding:12px 14px;min-width:200px;max-width:260px">
  <div style="font-size:10px;color:{cor};font-weight:700;text-transform:uppercase;letter-spacing:1px">{c.get('marca','')}</div>
  <div style="font-size:15px;font-weight:700;color:#111;margin:2px 0 4px">{c.get('modelo','')}</div>
  <div style="font-size:12px;color:#6b7280;line-height:1.7">
    <b>Motor:</b> {c.get('motor','—')}<br>
    <b>Preço:</b> {c.get('preco','—')}
  </div>
  <div style="margin-top:6px">{mot_badge}</div>
</div>"""


def gerar_html():
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M")
    secoes_html = []

    for segmento, modelos_nossos in SEGMENTOS_PORTFOLIO.items():
        specs_nossos = [(m, SPECS[m]) for m in modelos_nossos if m in SPECS]
        if not specs_nossos:
            continue

        chave_conc = MAPA_CONCORRENTES.get(segmento)
        concorrentes = CONCORRENTES_MERCADO.get(chave_conc, []) if chave_conc else []

        cards_nossos = "\n".join(card_portfolio(m, s) for m, s in specs_nossos)
        cards_conc = "\n".join(card_concorrente(c) for c in concorrentes)

        conc_section = ""
        if concorrentes:
            conc_section = f"""
<div style="margin-top:12px">
  <div style="font-size:12px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">
    Concorrentes no Segmento
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:10px">
    {cards_conc}
  </div>
</div>"""

        secoes_html.append(f"""
<div style="background:#fff;border-radius:12px;box-shadow:0 1px 6px rgba(0,0,0,.08);padding:20px 24px;margin-bottom:24px">
  <div style="font-size:18px;font-weight:700;color:#111;border-bottom:2px solid #e5e7eb;padding-bottom:10px;margin-bottom:14px">
    {segmento}
  </div>
  <div style="font-size:12px;font-weight:700;color:#374151;text-transform:uppercase;letter-spacing:1px;margin-bottom:10px">
    Nosso Portfolio
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:12px">
    {cards_nossos}
  </div>
  {conc_section}
</div>""")

    corpo = "\n".join(secoes_html)

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Análise de Concorrência — Grupo Demarco/Tozzo</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #f1f5f9; color: #1f2937; }}
  .header {{ background: linear-gradient(135deg,#1a1a2e,#16213e); color: #fff; padding: 28px 32px; }}
  .header h1 {{ font-size: 24px; font-weight: 700; }}
  .header p {{ font-size: 13px; color: #94a3b8; margin-top: 4px; }}
  .tabs {{ display: flex; gap: 0; background: #1e293b; padding: 0 32px; }}
  .tab {{ padding: 12px 22px; color: #94a3b8; font-size: 14px; font-weight: 600; cursor: pointer; border-bottom: 3px solid transparent; text-decoration: none; }}
  .tab.active {{ color: #f59e0b; border-bottom-color: #f59e0b; }}
  .tab:hover {{ color: #fff; }}
  .content {{ max-width: 1200px; margin: 28px auto; padding: 0 24px; }}
  .info-bar {{ background: #fff; border-radius: 8px; padding: 12px 18px; margin-bottom: 24px; border-left: 4px solid #f59e0b; font-size: 13px; color: #374151; }}
  .legenda {{ display: flex; gap: 16px; flex-wrap: wrap; margin-bottom: 20px; align-items: center; }}
  .legenda-item {{ display: flex; align-items: center; gap: 6px; font-size: 12px; color: #6b7280; }}
  .dot {{ width: 14px; height: 14px; border-radius: 50%; }}
</style>
</head>
<body>

<div class="header">
  <h1>Grupo Demarco / Tozzo</h1>
  <p>Análise de Concorrência — Portfolio x Mercado Brasileiro</p>
</div>

<div class="tabs">
  <a href="news_grupo.html" class="tab">Noticias</a>
  <a href="concorrencia.html" class="tab active">Concorrência</a>
</div>

<div class="content">

  <div class="info-bar">
    Atualizado em {agora} &nbsp;|&nbsp;
    Fonte: sites oficiais das montadoras e tabela FIPE &nbsp;|&nbsp;
    <b>Base para treinamento e avaliação de vendedores</b>
  </div>

  <div class="legenda">
    <b style="font-size:13px">Legenda:</b>
    <div class="legenda-item"><div class="dot" style="background:#2563eb"></div> Card azul escuro = nosso portfólio</div>
    <div class="legenda-item"><div class="dot" style="background:#d1d5db"></div> Card cinza = concorrente de mercado</div>
    <div class="legenda-item" style="gap:4px">
      <span style="background:#6b7280;color:#fff;padding:1px 8px;border-radius:10px;font-size:11px">Combustão</span>
      <span style="background:#16a34a;color:#fff;padding:1px 8px;border-radius:10px;font-size:11px">Híbrido</span>
      <span style="background:#2563eb;color:#fff;padding:1px 8px;border-radius:10px;font-size:11px">Elétrico</span>
      <span style="background:#ca8a04;color:#fff;padding:1px 8px;border-radius:10px;font-size:11px">Híbrido Leve</span>
    </div>
  </div>

  {corpo}

  <div style="text-align:center;padding:32px 0 16px;font-size:12px;color:#9ca3af">
    Grupo Demarco / Tozzo &mdash; Análise Competitiva &mdash; {agora}
  </div>

</div>
</body>
</html>"""

    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Gerado: {SAIDA}")
    return SAIDA


if __name__ == "__main__":
    gerar_html()
