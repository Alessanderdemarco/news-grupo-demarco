"""
Extrai atributos de mercado de um artigo de lançamento:
  carroceria, preco_num, potencia_num, motorizacao (para o motor de concorrência)
  + specs textuais para exibição na tabela
"""

import re
import requests
from bs4 import BeautifulSoup

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# ── Detecção de carroceria ────────────────────────────────────────────────────

MAPA_CARROCERIA = [
    (["suv elétrico", "suv elétric", "crossover elétric"],         "suv"),
    (["suv", "crossover", "utilitário esportivo"],                  "suv"),
    (["picape", "pick-up", "pickup", "caminhonete"],                "picape"),
    (["hatch", "hatchback"],                                         "hatch"),
    (["sedã", "sedan", "fastback"],                                  "sedan"),
    (["minivan", "monovolume", "van de passeio"],                    "minivan"),
    (["perua", "station wagon", " sw "],                            "perua"),
    (["naked", "streetfighter"],                                     "naked"),
    (["adventure", "trail", "enduro"],                              "adventure"),
    (["scooter", "maxi-scooter"],                                    "scooter"),
    (["esportiva", "supersport"],                                    "esportiva"),
    (["custom", "cruiser", "chopper"],                              "custom"),
    (["touring", " gt "],                                            "touring"),
]

def detectar_carroceria(texto):
    t = texto.lower()
    for termos, carroceria in MAPA_CARROCERIA:
        if any(term in t for term in termos):
            return carroceria
    return ""

# ── Detecção de motorização ───────────────────────────────────────────────────

def detectar_motorizacao(texto):
    t = texto.lower()
    if any(p in t for p in ["plug-in", "phev", "híbrido plug", "hibrido plug", "recarregável"]):
        return "hibrido"
    if any(p in t for p in ["elétric", "electric", "bev", "bateria de íon", "kwh", "autonomia elétrica"]):
        return "eletrico"
    if any(p in t for p in ["mild hybrid", "híbrido leve", "hibrido leve", "mhev", "48v", "48 v"]):
        return "hibrido_leve"
    if any(p in t for p in ["híbrido", "hibrido", " hev "]):
        return "hibrido"
    return "combustao"

# ── Extração numérica ─────────────────────────────────────────────────────────

def extrair_preco_num(texto):
    """Retorna o menor preço encontrado em R$ como float, ou None."""
    t = texto.lower()
    matches = re.findall(r'r\$\s*([\d\.]+(?:\.\d{3})*(?:,\d{2})?)', t)
    valores = []
    for m in matches:
        raw = re.sub(r'[^\d]', '', m)
        if 4 <= len(raw) <= 7:
            try:
                valores.append(int(raw))
            except:
                pass
    return min(valores) if valores else None

def extrair_potencia_num(texto):
    """Retorna a potência em cv como float, ou None."""
    t = texto.lower()
    matches = re.findall(r'(\d{2,4}(?:[,\.]\d+)?)\s*(?:cv|hp|cavalos)', t)
    valores = []
    for m in matches:
        try:
            v = float(m.replace(',', '.'))
            if 15 <= v <= 1500:  # filtro de sanidade
                valores.append(v)
        except:
            pass
    # Retorna o valor mediano para evitar outliers
    if valores:
        valores.sort()
        return valores[len(valores) // 2]
    return None

# ── Extração de specs textuais ────────────────────────────────────────────────

def extrair_specs_texto(texto):
    specs = {}
    t = texto.lower()

    padroes = {
        "motor": [
            r"([\d,\.]+[\s-]*(?:litros?|l\b)[\s\w]{0,20}(?:turbo|híbrido|elétrico|aspirado)?)",
            r"(\d{3,4}\s*cc[\s\w]{0,15})",
            r"motor\s+([\w\s\d,\.]{4,30}(?:cilindros?|turbo|híbrido))",
        ],
        "potencia": [
            r"(\d{2,4}(?:[,\.]\d+)?\s*(?:cv|hp)\b)",
        ],
        "torque": [
            r"(\d{1,3}(?:[,\.]\d+)?\s*(?:kgf[\.\s]?m|n\.?m\b))",
        ],
        "cambio": [
            r"(autom[aá]tico\s+(?:de\s+)?\d+\s*(?:marchas?|velocidades?|v\b)[^\.,]{0,15})",
            r"(cvt|dct|amt|pdk)",
            r"(manual\s+de\s+\d+\s*(?:marchas?|velocidades?))",
        ],
        "tracao": [
            r"(tra[çc][aã]o\s+(?:4x4|4wd|awd|fwd|dianteira|traseira|integral|nas\s+quatro))",
            r"\b(4x4|awd|4wd)\b",
        ],
    }

    for campo, lista in padroes.items():
        for padrao in lista:
            m = re.search(padrao, t)
            if m:
                val = re.sub(r'\s+', ' ', m.group(1)).strip()
                if len(val) > 1:
                    specs[campo] = val
                    break

    # Preço formatado
    preco_num = extrair_preco_num(texto)
    if preco_num:
        specs["preco"] = f"R$ {preco_num:,.0f}".replace(",", ".")

    return specs

# ── Função principal ──────────────────────────────────────────────────────────

def buscar_texto_artigo(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "nav", "header", "footer", "aside"]):
            tag.decompose()
        for sel in [".mc-body", ".content-text", "article", "main"]:
            el = soup.select_one(sel)
            if el:
                return el.get_text(" ", strip=True)
        return soup.get_text(" ", strip=True)
    except:
        return ""

def analisar_lancamento(titulo, resumo, link):
    """
    Retorna dicionário com todos os atributos extraídos do lançamento:
      carroceria, motorizacao, preco_num, potencia_num, specs (dict textual)
    """
    texto_base = titulo + " " + resumo
    texto_completo = buscar_texto_artigo(link) if link else texto_base
    texto_tudo = texto_base + " " + texto_completo

    carroceria  = detectar_carroceria(texto_tudo)
    motorizacao = detectar_motorizacao(texto_tudo)
    preco_num   = extrair_preco_num(texto_tudo)
    potencia_num = extrair_potencia_num(texto_tudo)
    specs       = extrair_specs_texto(texto_tudo)

    return {
        "carroceria":   carroceria,
        "motorizacao":  motorizacao,
        "preco_num":    preco_num,
        "potencia_num": potencia_num,
        "specs":        specs,
    }
