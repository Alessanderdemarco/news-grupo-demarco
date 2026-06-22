"""
Coleta modelos e versões disponíveis no mercado brasileiro
para a aba de análise de concorrência.
Fonte: Webmotors (API pública de estoque 0km).
Atualização recomendada: semanal.
"""

import requests
import warnings
import json
import os
import re
from datetime import datetime

warnings.filterwarnings("ignore")

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Marcas concorrentes a monitorar (além das nossas)
MARCAS_CONCORRENTES = [
    "Volkswagen", "Jeep", "Fiat", "Toyota", "Honda",
    "Hyundai", "Kia", "Nissan", "BYD", "Caoa Chery",
    "Chevrolet", "Ford", "Mitsubishi", "Volvo", "BMW",
]

# Nossas marcas (também atualizadas para ter versões reais)
MARCAS_PROPRIAS = ["Renault", "GWM", "Peugeot", "Citroen", "Geely"]

TODAS_MARCAS = MARCAS_PROPRIAS + MARCAS_CONCORRENTES

ARQUIVO_SAIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "concorrentes_data.json")


def buscar_modelos_webmotors(marca, tipo="carros"):
    """
    Usa a API pública da Webmotors para listar modelos 0km de uma marca.
    Retorna lista de dicts com modelo, versões, preço, motor, etc.
    """
    url = f"https://www.webmotors.com.br/api/search/car?tipoveiculo=1&marca={marca}&novo=true&order=1&top=100"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10, verify=False)
        if r.status_code == 200:
            data = r.json()
            return data
    except Exception:
        pass

    # Fallback: endpoint alternativo
    url2 = f"https://www.webmotors.com.br/carros/novos/{marca.lower().replace(' ','-')}/"
    try:
        r2 = requests.get(url2, headers=HEADERS, timeout=10, verify=False)
        # Extrai JSON embutido
        m = re.search(r'window\.__STATE__\s*=\s*({.*?});', r2.text, re.S)
        if m:
            return json.loads(m.group(1))
    except Exception:
        pass

    return None


def buscar_tabela_fipe_modelos(marca):
    """
    Usa a API da FIPE para listar modelos de uma marca (mais estável).
    """
    # Primeiro busca o código da marca
    try:
        r = requests.get(
            "https://parallelum.com.br/fipe/api/v1/carros/marcas",
            headers=HEADERS, timeout=8
        )
        marcas = r.json()
        codigo_marca = None
        for m in marcas:
            if marca.lower() in m["nome"].lower():
                codigo_marca = m["codigo"]
                break
        if not codigo_marca:
            return []

        # Busca modelos da marca
        r2 = requests.get(
            f"https://parallelum.com.br/fipe/api/v1/carros/marcas/{codigo_marca}/modelos",
            headers=HEADERS, timeout=8
        )
        data = r2.json()
        return [m["nome"] for m in data.get("modelos", [])]
    except Exception:
        return []


def buscar_icarros(marca):
    """
    Alternativa: iCarros lista modelos 0km.
    """
    url = f"https://www.icarros.com.br/ache/listaanuncios.jsp?marca={marca}&novo=true"
    try:
        r = requests.get(url, headers=HEADERS, timeout=10, verify=False)
        modelos = re.findall(r'"modeloNome"\s*:\s*"([^"]+)"', r.text)
        return sorted(set(modelos))
    except Exception:
        return []


def coletar_todos():
    """
    Coleta modelos disponíveis de todas as marcas.
    Retorna dict {marca: {modelo: {versoes, preco_min, preco_max, motor, ...}}}
    """
    resultado = {}
    total_marcas = len(TODAS_MARCAS)

    for i, marca in enumerate(TODAS_MARCAS):
        print(f"  [{i+1}/{total_marcas}] {marca}...")

        # Tenta FIPE (mais estável, sem bloqueio)
        modelos_fipe = buscar_tabela_fipe_modelos(marca)

        if modelos_fipe:
            # Filtra apenas modelos de passeio recentes (remove anos antigos)
            modelos_filtrados = []
            for nome in modelos_fipe:
                # Exclui modelos com ano muito antigo no nome
                ano_match = re.search(r'\b(19|200[0-9]|201[0-5])\b', nome)
                if not ano_match:
                    modelos_filtrados.append(nome)

            resultado[marca] = {
                "modelos": modelos_filtrados[:30],
                "fonte": "FIPE",
                "atualizado": datetime.now().strftime("%Y-%m-%d"),
            }
            print(f"    {len(modelos_filtrados)} modelos via FIPE")
        else:
            resultado[marca] = {
                "modelos": [],
                "fonte": "indisponivel",
                "atualizado": datetime.now().strftime("%Y-%m-%d"),
            }
            print(f"    sem dados")

    return resultado


def salvar(dados):
    with open(ARQUIVO_SAIDA, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    print(f"\nSalvo em: {ARQUIVO_SAIDA}")


def carregar():
    if os.path.exists(ARQUIVO_SAIDA):
        with open(ARQUIVO_SAIDA, encoding="utf-8") as f:
            return json.load(f)
    return {}


if __name__ == "__main__":
    print("=" * 50)
    print("  Coleta de Concorrentes — Mercado BR")
    print("=" * 50)
    dados = coletar_todos()
    salvar(dados)
