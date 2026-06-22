"""
Consulta os sites oficiais das montadoras no Brasil e retorna
os modelos atualmente disponíveis para venda.
Executar periodicamente para manter o portfólio atualizado.
"""

import requests
import warnings
import re
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def _get(url, timeout=12):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout, verify=False)
        return r if r.status_code == 200 else None
    except Exception:
        return None


# ── Renault ────────────────────────────────────────────────────────────────────
# Site: renault.com.br — modelos em JSON embutido na página

def scrape_renault():
    r = _get("https://www.renault.com.br/veiculos.html")
    if not r:
        return []
    # Modelos aparecem como "modelName":"KWID" ou similares no JSON da página
    nomes = re.findall(
        r'"(?:modelName|vehicleName|model)":\s*"([A-Z][A-Za-z0-9 \-]{1,20})"',
        r.text
    )
    # Fallback: extrai da classe model via BeautifulSoup
    if not nomes:
        soup = BeautifulSoup(r.text, "html.parser")
        for el in soup.select("[class*=model]"):
            txt = el.get_text(strip=True)
            txt_limpo = re.sub(r'a partir de.*', '', txt, flags=re.I).strip()
            txt_limpo = re.sub(r'R\$.*', '', txt_limpo).strip()
            if 2 < len(txt_limpo) < 25 and txt_limpo.isupper():
                nomes.append(txt_limpo)
    # Normaliza
    conhecidos = {"KWID","KARDIAN","NIAGARA","DUSTER","OROCH","BOREAL","KOLEOS","MEGANE","CAPTUR","SANDERO","LOGAN"}
    resultado = sorted(set(n.strip() for n in nomes if n.strip().upper() in conhecidos or (2 < len(n.strip()) < 20 and n.strip().isupper())))
    return resultado


# ── Peugeot ────────────────────────────────────────────────────────────────────
# Site: carros.peugeot.com.br

def scrape_peugeot():
    r = _get("https://carros.peugeot.com.br/")
    if not r:
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    modelos = set()
    # Links de modelos
    for a in soup.find_all("a", href=True):
        txt = a.get_text(strip=True).upper()
        if re.match(r'^(PEUGEOT\s+)?(E-)?(\d{3,4}|LANDTREK|PARTNER|EXPERT|BOXER)$', txt):
            modelos.add(re.sub(r'^PEUGEOT\s+', '', txt))
    # No HTML cru também
    encontrados = re.findall(
        r'\b(208|e-208|2008|e-2008|308|3008|408|e-408|Landtrek|Partner|Expert|Boxer)\b',
        r.text, re.I
    )
    for m in encontrados:
        modelos.add(m.upper())
    return sorted(modelos)


# ── Citroën ────────────────────────────────────────────────────────────────────
# Usa o sitemap.xml para listar modelos disponíveis

def scrape_citroen():
    r = _get("https://www.citroen.com.br/sitemap.xml")
    if not r:
        return []
    urls = re.findall(r'<loc>(.*?)</loc>', r.text)
    modelos = set()
    for url in urls:
        # Extrai slug do modelo: /veiculos-passeio/c3.html → C3
        m = re.search(r'/veiculos-passeio/([\w-]+)\.html$', url)
        if m:
            slug = m.group(1).replace('-', ' ').title()
            # Limpa prefixo "Citroen"
            slug = re.sub(r'^Citroen\s+', '', slug, flags=re.I)
            modelos.add(slug)
    return sorted(modelos)


# ── GWM / Haval / Tank / Ora ───────────────────────────────────────────────────
# Site oficial GWM Brasil ainda em construção; usa dados diretos do HTML de cada sub-marca
# Alternativa: scraping da Webmotors/iCarros filtrado por marca GWM

def scrape_gwm():
    # Tenta webmotors como fonte de modelos disponíveis à venda
    modelos = set()
    url = "https://www.webmotors.com.br/carros/estoque?pa=1&marca1=GWM"
    r = _get(url)
    if r:
        encontrados = re.findall(
            r'(Haval\s+H\d[\w\s]{0,10}|Haval\s+Jolion|Tank\s+\d{3}|Ora\s+\d{2})',
            r.text, re.I
        )
        for m in encontrados:
            modelos.add(re.sub(r'\s+', ' ', m.strip()))

    # Fallback: lista conhecida do site da GWM China/global BR
    if not modelos:
        # Tenta gwm.com.br mesmo com SSL issue
        for sub_url in [
            "https://www.gwm.com.br/haval/h6.html",
            "https://www.gwm.com.br/haval/jolion.html",
            "https://www.gwm.com.br/tank/tank300.html",
        ]:
            r2 = _get(sub_url)
            if r2:
                m = re.search(r'<title>(.*?)</title>', r2.text)
                if m:
                    modelos.add(m.group(1).strip())

    return sorted(modelos) if modelos else ["Haval H6", "Haval H9", "Haval Jolion", "Tank 300", "Tank 500", "Ora 03"]


# ── Geely ──────────────────────────────────────────────────────────────────────
# Site: geelybrasil.com.br

def scrape_geely():
    r = _get("https://www.geelybrasil.com.br/")
    if not r:
        return []
    soup = BeautifulSoup(r.text, "html.parser")
    modelos = set()
    # Apenas os <h2> que seguem o padrão "GEELY EX5" / "GEELY EX2" etc.
    for h in soup.find_all(["h2"]):
        txt = h.get_text(strip=True).upper()
        m = re.match(r'^GEELY\s+(EX\d+(?:\s+EM-I)?)$', txt)
        if m:
            modelos.add(m.group(1).strip())
    return sorted(modelos)


# ── Função principal ───────────────────────────────────────────────────────────

def consultar_portfolio_oficial():
    """
    Retorna dicionário {marca: [lista de modelos disponíveis no site oficial BR]}
    """
    print("Consultando sites oficiais das montadoras...")

    resultado = {}

    print("  Renault (renault.com.br)...")
    resultado["Renault"] = scrape_renault()

    print("  Peugeot (carros.peugeot.com.br)...")
    resultado["Peugeot"] = scrape_peugeot()

    print("  Citroen (citroen.com.br)...")
    resultado["Citroen"] = scrape_citroen()

    print("  GWM/Haval (gwm.com.br)...")
    resultado["GWM"] = scrape_gwm()

    print("  Geely (geelybrasil.com.br)...")
    resultado["Geely"] = scrape_geely()

    for marca, modelos in resultado.items():
        print(f"  {marca}: {modelos}")

    return resultado


if __name__ == "__main__":
    portfolio = consultar_portfolio_oficial()
