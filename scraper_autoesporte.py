"""
Scraper da seção de lançamentos da Autoesporte (globo.com).
Não depende de RSS — faz scraping direto da listagem e dos artigos.
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
BASE_URL = "https://autoesporte.globo.com"
URL_LANCAMENTOS = "https://autoesporte.globo.com/carros/lancamentos-de-carros/"


def buscar_lista_lancamentos(max_artigos=20):
    """Retorna lista de {titulo, link} da página de lançamentos."""
    try:
        r = requests.get(URL_LANCAMENTOS, headers=HEADERS, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        artigos = []
        vistos = set()
        for tag in ["h2", "h3", "h4"]:
            for el in soup.find_all(tag):
                a = el.find("a", href=True)
                if not a:
                    continue
                href = a.get("href", "")
                if "autoesporte.globo.com" not in href or href in vistos:
                    continue
                if "/noticia/" not in href and ".ghtml" not in href:
                    continue
                vistos.add(href)
                artigos.append({"titulo": el.get_text(strip=True), "link": href})
                if len(artigos) >= max_artigos:
                    return artigos
        return artigos
    except Exception as e:
        print(f"  Erro ao listar lançamentos: {e}")
        return []


def extrair_artigo_autoesporte(url):
    """
    Acessa o artigo e extrai:
    - resumo/lead
    - specs técnicas (motor, potência, torque, câmbio, tração, preço)
    - data de publicação
    """
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        soup = BeautifulSoup(r.text, "html.parser")

        # ── Data ──────────────────────────────────────────────────────────────
        data = ""
        for sel in ["time", ".content-publication-data", "[itemprop='datePublished']"]:
            el = soup.select_one(sel)
            if el:
                data = el.get("datetime", el.get_text(strip=True))[:16]
                break

        # ── Resumo / lead ─────────────────────────────────────────────────────
        resumo = ""
        for sel in [".content-head__subtitle", ".lead", "h2.content-head__subtitle", "p.content-head__subtitle"]:
            el = soup.select_one(sel)
            if el:
                resumo = el.get_text(strip=True)
                break
        if not resumo:
            # Pega o primeiro parágrafo do corpo
            for p in soup.select(".mc-body p, .content-text p, article p"):
                txt = p.get_text(strip=True)
                if len(txt) > 60:
                    resumo = txt[:350]
                    break

        # ── Texto completo para extração de specs ─────────────────────────────
        corpo = ""
        for sel in [".mc-body", ".content-text", "article", "main"]:
            el = soup.select_one(sel)
            if el:
                for tag in el(["script", "style", "nav", "aside"]):
                    tag.decompose()
                corpo = el.get_text(" ", strip=True).lower()
                break

        specs = extrair_specs_texto(corpo)
        return {"resumo": resumo, "data": data, "specs": specs}

    except Exception as e:
        return {"resumo": "", "data": "", "specs": {}}


def extrair_specs_texto(texto):
    """Extrai specs técnicas de um texto em português via regex."""
    specs = {}

    padroes = {
        "motor": [
            r"([\d,\.]+[\s-]*(?:litros?|l\b)[\s\w]{0,25}(?:turbo|híbrido|elétrico|aspirado)?)",
            r"(\d{3,4}\s*cc[\s\w]{0,20})",
            r"motor\s+([\w\s\d,\.]{4,35}(?:cilindros?|turbo|híbrido))",
        ],
        "potencia": [
            r"(\d{2,4}(?:\.\d+)?\s*(?:cv|hp|kw|cavalos))",
            r"potência[^\d]*(\d{2,4}\s*(?:cv|hp|kw))",
            r"gera[^\d]*(\d{2,4})\s*(?:cv|hp)",
        ],
        "torque": [
            r"(\d{1,3}(?:[,\.]\d+)?\s*(?:kgf[\.\s]?m|n\.?m\b))",
            r"torque[^\d]*(\d{1,3}(?:[,\.]\d+)?\s*(?:kgf[\.\s]?m|n\.?m))",
        ],
        "preco": [
            r"r\$\s*([\d\.]+(?:\.\d{3})*(?:,\d{2})?)",
            r"partir\s+de\s+r?\$?\s*([\d\.]+(?:\.\d{3})*)",
            r"custa\s+r?\$?\s*([\d\.]+(?:\.\d{3})*)",
            r"vendido\s+por\s+r?\$?\s*([\d\.]+(?:\.\d{3})*)",
            r"pre[çc]o[^\d]*r?\$?\s*([\d\.]+(?:\.\d{3})*)",
        ],
        "cambio": [
            r"(autom[aá]tico\s+(?:de\s+)?\d+\s*(?:marchas?|velocidades?|v\b)[^\.,]{0,15})",
            r"(câmbio\s+\w+[\s\w]{0,20})",
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
            m = re.search(padrao, texto)
            if m:
                val = re.sub(r'\s+', ' ', m.group(1)).strip()
                if len(val) > 2:
                    specs[campo] = val
                    break

    # Normaliza preço
    if "preco" in specs:
        raw = re.sub(r'[^\d]', '', specs["preco"])
        if raw and 4 <= len(raw) <= 7:
            try:
                specs["preco"] = f"R$ {int(raw):,.0f}".replace(",", ".")
            except:
                pass
        else:
            del specs["preco"]

    return specs


def buscar_lancamentos_autoesporte(max_artigos=20):
    """
    Função principal: retorna lista de lançamentos com todos os dados.
    Cada item: titulo, link, data, resumo, specs
    """
    print("  Buscando lista em Autoesporte...")
    lista = buscar_lista_lancamentos(max_artigos)
    print(f"  {len(lista)} artigos encontrados. Acessando cada um...")

    resultado = []
    for i, item in enumerate(lista):
        print(f"  [{i+1}/{len(lista)}] {item['titulo'][:55]}...")
        detalhe = extrair_artigo_autoesporte(item["link"])
        resultado.append({
            "portal": "Autoesporte",
            "titulo": item["titulo"],
            "link":   item["link"],
            "data":   detalhe["data"],
            "resumo": detalhe["resumo"],
            "specs":  detalhe["specs"],
        })

    return resultado
