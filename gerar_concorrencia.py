"""
Gera concorrencia.html — Guia Comercial de Concorrência
Portfólio Grupo Demarco/Tozzo x Mercado Brasileiro
"""

import os
from datetime import datetime
from specs_portfolio import SPECS, PORTFOLIO, LABEL_MOTORIZACAO

SAIDA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "concorrencia.html")

# ─────────────────────────────────────────────────────────────────────────────
# DADOS COMERCIAIS COMPLETOS
# Estrutura: preco, motor, potencia, cambio, tracao, consumo_cidade,
#            consumo_estrada, comprimento, entre_eixos, porta_malas,
#            autonomia (eletricos/hibridos), pontos_fortes, pontos_fracos
# ─────────────────────────────────────────────────────────────────────────────

GUIA = {

    # ══════════════════════════════════════════════════════════════════════════
    # PORTFÓLIO PRÓPRIO — enriquecido
    # ══════════════════════════════════════════════════════════════════════════

    "Renault Kwid": {
        "marca": "Renault", "proprio": True, "segmento": "Hatch Entry",
        "preco": "R$ 82.790 – 100.990", "motor": "1.0 SCe 68–71 cv",
        "cambio": "Manual 5v / CVT", "tracao": "FWD",
        "consumo_cidade": "12,8 km/l", "consumo_estrada": "14,3 km/l",
        "comprimento": "3,73 m", "entre_eixos": "2,42 m", "porta_malas": "290 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Menor preço do segmento", "Baixo custo de manutenção", "Agilidade urbana", "Câmbio CVT disponível"],
        "pontos_fracos": ["Potência limitada", "Sem airbag lateral de série", "Porta-malas pequeno"],
    },
    "Renault Kardian": {
        "marca": "Renault", "proprio": True, "segmento": "SUV Compacto Entry",
        "preco": "R$ 113.690 – 149.990", "motor": "1.0 TCe Turbo 125 cv",
        "cambio": "Manual 6v / CVT", "tracao": "FWD",
        "consumo_cidade": "11,2 km/l", "consumo_estrada": "13,5 km/l",
        "comprimento": "4,12 m", "entre_eixos": "2,60 m", "porta_malas": "390 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Design moderno e jovem", "Tela central 10\"", "Melhor custo-benefício do segmento", "Conectividade completa"],
        "pontos_fracos": ["Somente tração dianteira", "Motor 1.0 pode ser insuficiente em carga"],
    },
    "Renault Duster": {
        "marca": "Renault", "proprio": True, "segmento": "SUV Compacto",
        "preco": "R$ 131.990 – 189.990", "motor": "1.3 TCe / 1.6 16V 130–163 cv",
        "cambio": "Manual / CVT / Auto 6v", "tracao": "FWD / 4x4",
        "consumo_cidade": "10,5 km/l", "consumo_estrada": "12,8 km/l",
        "comprimento": "4,34 m", "entre_eixos": "2,67 m", "porta_malas": "472 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Único com 4x4 no segmento abaixo de R$200k", "Maior porta-malas", "Robustez e off-road real", "Ampla rede de serviço"],
        "pontos_fracos": ["Interior menos premium que concorrentes", "Consumo maior na versão 4x4"],
    },
    "Renault Oroch": {
        "marca": "Renault", "proprio": True, "segmento": "Picape Compacta",
        "preco": "R$ 139.990 – 189.990", "motor": "1.3 TCe / 2.0 16V 112–163 cv",
        "cambio": "Manual / Auto 6v", "tracao": "FWD / 4x4",
        "consumo_cidade": "9,8 km/l", "consumo_estrada": "12,2 km/l",
        "comprimento": "4,75 m", "entre_eixos": "2,67 m", "porta_malas": "—",
        "carga_util": "650 kg", "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Caçamba mais versátil da categoria", "Disponível com 4x4", "Cabine dupla completa", "Custo-benefício forte"],
        "pontos_fracos": ["Motor 1.3 com menos torque que diesel", "Preço alto nas versões topo"],
    },
    "Renault Boreal": {
        "marca": "Renault", "proprio": True, "segmento": "SUV Médio",
        "preco": "R$ 179.990 – 219.990", "motor": "1.3 TCe 163 cv",
        "cambio": "Auto 7v EDC", "tracao": "FWD",
        "consumo_cidade": "10,1 km/l", "consumo_estrada": "12,9 km/l",
        "comprimento": "4,54 m", "entre_eixos": "2,74 m", "porta_malas": "540 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Design arrojado", "Interior espaçoso", "Excelente custo para o segmento", "Câmbio dupla embreagem"],
        "pontos_fracos": ["Sem versão 4x4", "Marca ainda pouco reconhecida no segmento médio"],
    },
    "Renault Niagara": {
        "marca": "Renault", "proprio": True, "segmento": "Picape Média",
        "preco": "R$ 219.990 – 249.990", "motor": "1.3 TCe 163 cv",
        "cambio": "Auto 7v EDC", "tracao": "4x4",
        "consumo_cidade": "9,4 km/l", "consumo_estrada": "11,8 km/l",
        "comprimento": "5,27 m", "entre_eixos": "3,10 m", "porta_malas": "—",
        "carga_util": "750 kg", "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["4x4 de série", "Maior picape média com motor a gasolina", "Acabamento premium", "Câmbio 7v EDC"],
        "pontos_fracos": ["Sem opção diesel", "Preço competitivo mas rede menor que Toyota/Ford"],
    },
    "Haval H6": {
        "marca": "GWM", "proprio": True, "segmento": "SUV Médio",
        "preco": "R$ 199.990 – 249.990", "motor": "1.5T / 2.0T 169–238 cv",
        "cambio": "Auto 7v DCT", "tracao": "FWD / AWD",
        "consumo_cidade": "9,6 km/l", "consumo_estrada": "12,1 km/l",
        "comprimento": "4,65 m", "entre_eixos": "2,74 m", "porta_malas": "507 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Muito equipado pelo preço", "Teto panorâmico de série", "AWD disponível", "HUD e assistentes avançados"],
        "pontos_fracos": ["Marca chinesa ainda gera desconfiança", "Rede de assistência em expansão"],
    },
    "Haval H9": {
        "marca": "GWM", "proprio": True, "segmento": "SUV Grande Off-road",
        "preco": "R$ 319.990 – 369.990", "motor": "2.0T 218 cv",
        "cambio": "Auto 8v", "tracao": "4x4",
        "consumo_cidade": "8,2 km/l", "consumo_estrada": "10,5 km/l",
        "comprimento": "4,88 m", "entre_eixos": "2,80 m", "porta_malas": "302 L (7 lug)",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["7 lugares de série", "4x4 com reduzida", "Interior luxuoso", "Melhor preço no segmento off-road 7 lugares"],
        "pontos_fracos": ["Consumo elevado", "Sem motor diesel", "Rede menor que Toyota/Jeep"],
    },
    "Haval Jolion": {
        "marca": "GWM", "proprio": True, "segmento": "SUV Compacto",
        "preco": "R$ 164.990 – 194.990", "motor": "1.5T 147 cv",
        "cambio": "Auto 7v DCT", "tracao": "FWD",
        "consumo_cidade": "10,3 km/l", "consumo_estrada": "12,8 km/l",
        "comprimento": "4,47 m", "entre_eixos": "2,68 m", "porta_malas": "410 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Excelente equipamento de série", "Tela 12,3\" central", "Design sofisticado", "Preço agressivo"],
        "pontos_fracos": ["Somente FWD", "Valor de revenda ainda consolidando"],
    },
    "Tank 300": {
        "marca": "GWM", "proprio": True, "segmento": "SUV Off-road",
        "preco": "R$ 349.990 – 389.990", "motor": "2.0T 227 cv",
        "cambio": "Auto 8v", "tracao": "4x4",
        "consumo_cidade": "8,0 km/l", "consumo_estrada": "10,2 km/l",
        "comprimento": "4,64 m", "entre_eixos": "2,75 m", "porta_malas": "420 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Visual icônico retrô", "4x4 com diff traseiro blocante", "Excelente off-road", "Interior moderno e luxuoso"],
        "pontos_fracos": ["Consumo urbano alto", "Preço elevado", "Sem 7 lugares"],
    },
    "Tank 500": {
        "marca": "GWM", "proprio": True, "segmento": "SUV Grande PHEV",
        "preco": "R$ 469.990 – 499.990", "motor": "3.0T V6 PHEV 449 cv",
        "cambio": "Auto 9v", "tracao": "4x4",
        "consumo_cidade": "6,5 km/l (modo híbrido)", "consumo_estrada": "9,8 km/l",
        "comprimento": "5,10 m", "entre_eixos": "2,95 m", "porta_malas": "350 L (7 lug)",
        "autonomia": "80 km (modo elétrico)", "motorizacao": "hibrido",
        "pontos_fortes": ["449 cv — mais potente do segmento", "Autonomia elétrica no urbano", "7 lugares com conforto premium", "4x4 com reduzida e diffs blocantes"],
        "pontos_fracos": ["Preço próximo de marcas premium europeias", "Rede de serviço em expansão"],
    },
    "Ora 03": {
        "marca": "GWM", "proprio": True, "segmento": "Hatch Elétrico",
        "preco": "R$ 179.990 – 209.990", "motor": "Elétrico 143–204 cv",
        "cambio": "Direto", "tracao": "FWD",
        "consumo_cidade": "—", "consumo_estrada": "—",
        "comprimento": "4,24 m", "entre_eixos": "2,65 m", "porta_malas": "228 L",
        "autonomia": "420–500 km (WLTP)", "motorizacao": "eletrico",
        "pontos_fortes": ["Design diferenciado e retrô", "Recarga rápida 80kW", "Autonomia acima de 400km", "Custo por km muito baixo"],
        "pontos_fracos": ["Porta-malas pequeno", "Poucas opções de cor", "Infraestrutura de recarga ainda limitada no Brasil"],
    },
    "Peugeot 208": {
        "marca": "Peugeot", "proprio": True, "segmento": "Hatch Compacto",
        "preco": "R$ 104.990 – 134.990", "motor": "1.0 Turbo / 1.6 16V 100–122 cv",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "11,5 km/l", "consumo_estrada": "13,8 km/l",
        "comprimento": "4,05 m", "entre_eixos": "2,54 m", "porta_malas": "311 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Design premium europeu", "Cockpit i-Cockpit diferenciado", "Acabamento sofisticado", "Marca com forte apelo"],
        "pontos_fracos": ["Preço acima de concorrentes nacionais", "Manutenção mais cara"],
    },
    "Peugeot 2008": {
        "marca": "Peugeot", "proprio": True, "segmento": "SUV Compacto Entry",
        "preco": "R$ 134.990 – 174.990", "motor": "1.0 Turbo 130 cv",
        "cambio": "Auto 6v", "tracao": "FWD",
        "consumo_cidade": "10,8 km/l", "consumo_estrada": "13,2 km/l",
        "comprimento": "4,30 m", "entre_eixos": "2,60 m", "porta_malas": "434 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Design europeu premium", "I-Cockpit 3D", "Boa relação espaço/preço", "Marca de prestígio"],
        "pontos_fracos": ["Somente FWD", "Custo de manutenção mais elevado"],
    },
    "Citroen C3": {
        "marca": "Citroen", "proprio": True, "segmento": "Hatch Compacto",
        "preco": "R$ 94.990 – 119.990", "motor": "1.0 / 1.0 Turbo 75–100 cv",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "12,1 km/l", "consumo_estrada": "14,0 km/l",
        "comprimento": "3,98 m", "entre_eixos": "2,54 m", "porta_malas": "316 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Preço competitivo", "Conforto de suspensão excepcional", "Produzido no Brasil (Porto Real)", "Custo de manutenção acessível"],
        "pontos_fracos": ["Versão sem turbo com potência limitada", "Interior simples nas versões de entrada"],
    },
    "Citroen Aircross": {
        "marca": "Citroen", "proprio": True, "segmento": "SUV Compacto Entry",
        "preco": "R$ 119.990 – 154.990", "motor": "1.0 Turbo 130 cv",
        "cambio": "Auto 6v", "tracao": "FWD",
        "consumo_cidade": "10,9 km/l", "consumo_estrada": "13,0 km/l",
        "comprimento": "4,35 m", "entre_eixos": "2,67 m", "porta_malas": "439 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["7 lugares disponível", "Melhor conforto de bancos do segmento", "Bom porta-malas", "Produzido no Brasil"],
        "pontos_fracos": ["Sem versão 4x4", "Menos tecnologia que rivais coreanos"],
    },
    "Citroen Basalt": {
        "marca": "Citroen", "proprio": True, "segmento": "SUV Compacto Entry",
        "preco": "R$ 109.990 – 139.990", "motor": "1.0 / 1.0 Turbo 75–130 cv",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "11,2 km/l", "consumo_estrada": "13,5 km/l",
        "comprimento": "4,35 m", "entre_eixos": "2,67 m", "porta_malas": "410 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Estilo fastback diferenciado", "Produzido no Brasil", "Excelente relação preço/tamanho", "Boa capacidade de porta-malas"],
        "pontos_fracos": ["Versão sem turbo com potência limitada", "Sem 7 lugares"],
    },
    "Geely EX2": {
        "marca": "Geely", "proprio": True, "segmento": "Hatch Elétrico Compacto",
        "preco": "R$ 149.990 – 179.990", "motor": "Elétrico 95 cv",
        "cambio": "Direto", "tracao": "FWD",
        "consumo_cidade": "—", "consumo_estrada": "—",
        "comprimento": "3,99 m", "entre_eixos": "2,55 m", "porta_malas": "255 L",
        "autonomia": "300 km (CLTC)", "motorizacao": "eletrico",
        "pontos_fortes": ["Elétrico compacto mais acessível", "Custo por km baixíssimo", "Carga AC e DC", "Garantia de bateria 8 anos"],
        "pontos_fracos": ["Autonomia real abaixo de 250km", "Infraestrutura de recarga limitada", "Marca pouco conhecida no Brasil"],
    },
    "Geely EX5": {
        "marca": "Geely", "proprio": True, "segmento": "SUV Elétrico Compacto",
        "preco": "R$ 199.990 – 239.990", "motor": "Elétrico 218 cv",
        "cambio": "Direto", "tracao": "FWD",
        "consumo_cidade": "—", "consumo_estrada": "—",
        "comprimento": "4,60 m", "entre_eixos": "2,75 m", "porta_malas": "440 L",
        "autonomia": "440 km (CLTC)", "motorizacao": "eletrico",
        "pontos_fortes": ["SUV elétrico com maior autonomia do segmento", "Recarga rápida 100kW", "Interior tecnológico", "218 cv com tração imediata"],
        "pontos_fracos": ["Autonomia real ~360km", "Rede de assistência em formação", "Valor de revenda incerto"],
    },
    "Geely EX5 EM-I": {
        "marca": "Geely", "proprio": True, "segmento": "SUV Compacto PHEV",
        "preco": "R$ 219.990 – 259.990", "motor": "1.5T + Elétrico PHEV 326 cv",
        "cambio": "Direto (PHEV)", "tracao": "AWD",
        "consumo_cidade": "4,5 km/l (modo híbrido)", "consumo_estrada": "7,2 km/l",
        "comprimento": "4,60 m", "entre_eixos": "2,75 m", "porta_malas": "420 L",
        "autonomia": "80 km (modo elétrico)", "motorizacao": "hibrido",
        "pontos_fortes": ["326 cv com AWD — melhor desempenho do segmento", "Autonomia elétrica para uso urbano", "Consumo baixíssimo no híbrido", "Tecnologia PHEV acessível"],
        "pontos_fracos": ["Preço mais alto", "Rede de serviço PHEV limitada", "Bateria menor que BEV puro"],
    },

    # ══════════════════════════════════════════════════════════════════════════
    # CONCORRENTES DE MERCADO
    # ══════════════════════════════════════════════════════════════════════════

    # Hatch Entry
    "Chevrolet Onix": {
        "marca": "Chevrolet", "proprio": False, "segmento": "Hatch Entry",
        "preco": "R$ 82.990 – 107.990", "motor": "1.0 Turbo 116 cv",
        "cambio": "Manual 6v / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "12,1 km/l", "consumo_estrada": "14,5 km/l",
        "comprimento": "4,06 m", "entre_eixos": "2,52 m", "porta_malas": "303 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Líder de vendas no Brasil", "Maior rede de concessionárias", "Custo de revisão acessível", "Motor mais potente da categoria"],
        "pontos_fracos": ["Design conservador", "Interior menos moderno que Polo e HB20"],
    },
    "Volkswagen Polo": {
        "marca": "Volkswagen", "proprio": False, "segmento": "Hatch Entry",
        "preco": "R$ 99.990 – 129.990", "motor": "1.0 TSI 116 cv",
        "cambio": "Manual 6v / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "11,8 km/l", "consumo_estrada": "14,2 km/l",
        "comprimento": "4,07 m", "entre_eixos": "2,56 m", "porta_malas": "300 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Melhor acabamento interno do segmento", "Valor de revenda alto", "Motor TSI eficiente", "Solidez VW"],
        "pontos_fracos": ["Preço mais alto", "Versão de entrada simples demais"],
    },
    "Fiat Argo": {
        "marca": "Fiat", "proprio": False, "segmento": "Hatch Entry",
        "preco": "R$ 84.990 – 109.990", "motor": "1.0 / 1.3 Turbo 101–109 cv",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "12,4 km/l", "consumo_estrada": "14,6 km/l",
        "comprimento": "3,99 m", "entre_eixos": "2,52 m", "porta_malas": "270 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Produção nacional (Betim)", "Boa rede de serviço", "Visual dinâmico", "Versão Trekking diferenciada"],
        "pontos_fracos": ["Porta-malas pequeno", "Motor aspirado fraco", "Custo de revisão intermediário"],
    },
    "Hyundai HB20": {
        "marca": "Hyundai", "proprio": False, "segmento": "Hatch Entry",
        "preco": "R$ 89.990 – 119.990", "motor": "1.0 Turbo 120 cv",
        "cambio": "Manual 6v / Auto IVT", "tracao": "FWD",
        "consumo_cidade": "12,3 km/l", "consumo_estrada": "14,8 km/l",
        "comprimento": "4,07 m", "entre_eixos": "2,53 m", "porta_malas": "300 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Motor mais potente na versão turbo", "Central multimídia completa", "Produzido no Brasil (Piracicaba)", "Garantia 5 anos"],
        "pontos_fracos": ["CVT com respostas lentas", "Acabamento interno básico"],
    },
    "Toyota Yaris": {
        "marca": "Toyota", "proprio": False, "segmento": "Hatch Entry",
        "preco": "R$ 112.990 – 134.990", "motor": "1.3 / 1.5 107–110 cv",
        "cambio": "Manual 6v / Auto CVT", "tracao": "FWD",
        "consumo_cidade": "12,6 km/l", "consumo_estrada": "15,1 km/l",
        "comprimento": "4,10 m", "entre_eixos": "2,55 m", "porta_malas": "286 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Confiabilidade Toyota lendária", "Melhor consumo do segmento", "Valor de revenda excelente", "Custo de manutenção baixo"],
        "pontos_fracos": ["Preço mais alto para o que oferece", "Interior datado", "Porta-malas pequeno"],
    },

    # SUV Compacto Entry
    "Fiat Pulse": {
        "marca": "Fiat", "proprio": False, "segmento": "SUV Compacto Entry",
        "preco": "R$ 109.990 – 154.990", "motor": "1.0 Turbo 130 cv",
        "cambio": "Auto 6v", "tracao": "FWD",
        "consumo_cidade": "10,6 km/l", "consumo_estrada": "13,1 km/l",
        "comprimento": "4,08 m", "entre_eixos": "2,52 m", "porta_malas": "370 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Melhor preço do segmento SUV", "Design arrojado", "Produção nacional", "Boa lista de equipamentos"],
        "pontos_fracos": ["Porta-malas menor da categoria", "Sem opção de câmbio manual top", "Motor sem muito torque baixo"],
    },
    "Volkswagen T-Cross": {
        "marca": "Volkswagen", "proprio": False, "segmento": "SUV Compacto Entry",
        "preco": "R$ 129.990 – 164.990", "motor": "1.0 TSI 128 cv",
        "cambio": "Auto 6v", "tracao": "FWD",
        "consumo_cidade": "10,9 km/l", "consumo_estrada": "13,5 km/l",
        "comprimento": "4,20 m", "entre_eixos": "2,65 m", "porta_malas": "373 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Solidez VW", "Bom valor de revenda", "Interior bem acabado", "Assistente de partida em rampa"],
        "pontos_fracos": ["Preço mais alto", "Motor básico na entrada", "Sem versão mais potente no Brasil"],
    },
    "Hyundai Creta": {
        "marca": "Hyundai", "proprio": False, "segmento": "SUV Compacto Entry",
        "preco": "R$ 134.990 – 184.990", "motor": "1.0 Turbo 120 cv / 2.0 167 cv",
        "cambio": "Auto IVT / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "10,4 km/l", "consumo_estrada": "12,8 km/l",
        "comprimento": "4,30 m", "entre_eixos": "2,61 m", "porta_malas": "402 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["SUV compacto mais vendido do Brasil", "Versão 2.0 com bom desempenho", "Lista completa de equipamentos", "Garantia 5 anos"],
        "pontos_fracos": ["Preço salgado nas versões equipadas", "Interior menos tecnológico que novos rivais"],
    },
    "Honda HR-V": {
        "marca": "Honda", "proprio": False, "segmento": "SUV Compacto Entry",
        "preco": "R$ 164.990 – 204.990", "motor": "1.5 Turbo 177 cv",
        "cambio": "Auto CVT", "tracao": "FWD",
        "consumo_cidade": "10,2 km/l", "consumo_estrada": "12,5 km/l",
        "comprimento": "4,37 m", "entre_eixos": "2,61 m", "porta_malas": "373 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Motor mais potente do segmento (177cv)", "Design elegante", "Bancos traseiros flat-floor", "Confiabilidade Honda"],
        "pontos_fracos": ["Preço alto para o segmento", "CVT pode ser lento", "Sem versão híbrida no Brasil"],
    },
    "Toyota Corolla Cross": {
        "marca": "Toyota", "proprio": False, "segmento": "SUV Compacto Entry",
        "preco": "R$ 174.990 – 229.990", "motor": "2.0 Hybrid 197 cv",
        "cambio": "Auto CVT (e-CVT)", "tracao": "FWD / AWD (híbrido)",
        "consumo_cidade": "15,4 km/l", "consumo_estrada": "14,1 km/l",
        "comprimento": "4,46 m", "entre_eixos": "2,64 m", "porta_malas": "487 L",
        "autonomia": "—", "motorizacao": "hibrido",
        "pontos_fortes": ["Único híbrido full do segmento < R$230k", "Consumo urbano muito baixo", "AWD no híbrido", "Confiabilidade Toyota"],
        "pontos_fracos": ["Preço elevado", "Sem recarga externa (não é PHEV)", "Interior conservador"],
    },

    # SUV Médio
    "Toyota RAV4": {
        "marca": "Toyota", "proprio": False, "segmento": "SUV Médio",
        "preco": "R$ 259.990 – 319.990", "motor": "2.5 Hybrid 222 cv",
        "cambio": "Auto CVT", "tracao": "AWD",
        "consumo_cidade": "14,8 km/l", "consumo_estrada": "13,5 km/l",
        "comprimento": "4,60 m", "entre_eixos": "2,69 m", "porta_malas": "580 L",
        "autonomia": "—", "motorizacao": "hibrido",
        "pontos_fortes": ["Referência do segmento", "Híbrido full com AWD", "Menor custo operacional da categoria", "Maior porta-malas", "Excelente revenda"],
        "pontos_fracos": ["Preço alto", "Interior sem grande apelo visual", "Sem PHEV no Brasil"],
    },
    "Volkswagen Tiguan": {
        "marca": "Volkswagen", "proprio": False, "segmento": "SUV Médio",
        "preco": "R$ 229.990 – 289.990", "motor": "1.4 TSI / 2.0 TSI 150–320 cv",
        "cambio": "Auto 6v DSG", "tracao": "FWD / 4Motion AWD",
        "consumo_cidade": "9,8 km/l", "consumo_estrada": "12,4 km/l",
        "comprimento": "4,51 m", "entre_eixos": "2,68 m", "porta_malas": "520 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Solidez e acabamento VW premium", "Versão R com 320cv", "AWD disponível", "7 lugares disponível"],
        "pontos_fracos": ["Preço elevado", "Manutenção cara", "Motor 1.4 fraco na entrada"],
    },
    "Jeep Compass": {
        "marca": "Jeep", "proprio": False, "segmento": "SUV Médio",
        "preco": "R$ 179.990 – 259.990", "motor": "1.3 Turbo 185–270 cv",
        "cambio": "Auto 6v / Auto 7v", "tracao": "FWD / 4xe AWD PHEV",
        "consumo_cidade": "10,1 km/l", "consumo_estrada": "12,2 km/l",
        "comprimento": "4,40 m", "entre_eixos": "2,64 m", "porta_malas": "438 L",
        "autonomia": "40 km (4xe PHEV)", "motorizacao": "hibrido",
        "pontos_fortes": ["Produzido no Brasil (Goiana-PE)", "Versão 4xe PHEV disponível", "Forte apelo de marca Jeep", "Melhor preço do segmento"],
        "pontos_fracos": ["Interior desvaloriza rápido", "Consumo na versão a combustão", "Custo de manutenção alto"],
    },
    "Hyundai Tucson": {
        "marca": "Hyundai", "proprio": False, "segmento": "SUV Médio",
        "preco": "R$ 219.990 – 279.990", "motor": "1.6 Turbo 180 cv",
        "cambio": "Auto 7v DCT", "tracao": "FWD",
        "consumo_cidade": "9,9 km/l", "consumo_estrada": "12,3 km/l",
        "comprimento": "4,50 m", "entre_eixos": "2,68 m", "porta_malas": "539 L",
        "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Design arrojado", "Motor turbo 180cv vibrante", "Maior porta-malas do segmento", "Garantia 5 anos"],
        "pontos_fracos": ["Sem versão híbrida no Brasil", "FWD apenas", "DCT seco pode ser travado no tráfego"],
    },

    # Picape Compacta
    "Fiat Strada": {
        "marca": "Fiat", "proprio": False, "segmento": "Picape Compacta",
        "preco": "R$ 109.990 – 154.990", "motor": "1.3 Turbo 109 cv",
        "cambio": "Manual 5v / Auto 6v", "tracao": "FWD",
        "consumo_cidade": "11,8 km/l", "consumo_estrada": "13,9 km/l",
        "comprimento": "4,67 m", "entre_eixos": "2,72 m", "porta_malas": "—",
        "carga_util": "720 kg", "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Picape compacta mais vendida do Brasil", "Versão Cabine Dupla disponível", "Boa carga útil", "Menor custo de revisão"],
        "pontos_fracos": ["Somente FWD", "Motor sem muita força em carga", "Acabamento simples"],
    },
    "Chevrolet Montana": {
        "marca": "Chevrolet", "proprio": False, "segmento": "Picape Compacta",
        "preco": "R$ 139.990 – 184.990", "motor": "1.2 Turbo 133 cv",
        "cambio": "Auto 6v", "tracao": "FWD",
        "consumo_cidade": "11,2 km/l", "consumo_estrada": "13,5 km/l",
        "comprimento": "5,10 m", "entre_eixos": "3,09 m", "porta_malas": "—",
        "carga_util": "690 kg", "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Design moderno e imponente", "Motor mais potente da categoria compacta", "Cabine dupla bem equipada", "Maior entre-eixos"],
        "pontos_fracos": ["Somente FWD", "Preço mais alto na categoria", "Menos testada em carga que rivais"],
    },

    # Picape Média
    "Toyota Hilux": {
        "marca": "Toyota", "proprio": False, "segmento": "Picape Média",
        "preco": "R$ 249.990 – 339.990", "motor": "2.8 Diesel 204 cv",
        "cambio": "Manual 6v / Auto 6v", "tracao": "4x4",
        "consumo_cidade": "9,0 km/l", "consumo_estrada": "11,2 km/l",
        "comprimento": "5,33 m", "entre_eixos": "3,08 m", "porta_malas": "—",
        "carga_util": "1.085 kg", "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Referência absoluta do segmento", "Diesel mais resistente do Brasil", "Valor de revenda superior", "Capacidade off-road real", "Maior carga útil"],
        "pontos_fracos": ["Preço premium", "Interior menos moderno que novos rivais", "Manutenção do diesel"],
    },
    "Ford Ranger": {
        "marca": "Ford", "proprio": False, "segmento": "Picape Média",
        "preco": "R$ 279.990 – 399.990", "motor": "2.0 / 3.0 Diesel 205–250 cv",
        "cambio": "Auto 10v", "tracao": "4x4",
        "consumo_cidade": "8,8 km/l", "consumo_estrada": "11,0 km/l",
        "comprimento": "5,37 m", "entre_eixos": "3,27 m", "porta_malas": "—",
        "carga_util": "1.080 kg", "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["V6 diesel mais potente da categoria (250cv)", "Câmbio 10v suave", "Matrix LED", "Interior estilo SUV premium", "Capacidade de reboque maior"],
        "pontos_fracos": ["Preço mais alto", "Custo de manutenção elevado"],
    },
    "Mitsubishi L200": {
        "marca": "Mitsubishi", "proprio": False, "segmento": "Picape Média",
        "preco": "R$ 259.990 – 319.990", "motor": "2.4 Diesel 181 cv",
        "cambio": "Auto 8v", "tracao": "4x4",
        "consumo_cidade": "8,5 km/l", "consumo_estrada": "10,8 km/l",
        "comprimento": "5,32 m", "entre_eixos": "3,00 m", "porta_malas": "—",
        "carga_util": "1.000 kg", "autonomia": "—", "motorizacao": "combustao",
        "pontos_fortes": ["Super Select 4WD exclusivo (4x4 em alta velocidade)", "Custo mais acessível", "Design renovado", "Suspensão traseira multilink"],
        "pontos_fracos": ["Motor menos potente que Ranger e Amarok", "Rede de concessionárias menor"],
    },

    # Elétrico
    "BYD Dolphin": {
        "marca": "BYD", "proprio": False, "segmento": "Hatch Elétrico",
        "preco": "R$ 159.800 – 194.800", "motor": "Elétrico 204 cv",
        "cambio": "Direto", "tracao": "FWD",
        "consumo_cidade": "—", "consumo_estrada": "—",
        "comprimento": "4,29 m", "entre_eixos": "2,70 m", "porta_malas": "345 L",
        "autonomia": "468 km (CLTC) / ~380km real", "motorizacao": "eletrico",
        "pontos_fortes": ["Maior autonomia do segmento elétrico compacto", "Recarga rápida 60kW", "Design moderno", "Interior com tela giratória"],
        "pontos_fracos": ["Preço mais alto que concorrentes EV", "Assistência técnica ainda em expansão no Brasil"],
    },
    "BYD Seagull": {
        "marca": "BYD", "proprio": False, "segmento": "Hatch Elétrico",
        "preco": "R$ 114.800 – 134.800", "motor": "Elétrico 74 cv",
        "cambio": "Direto", "tracao": "FWD",
        "consumo_cidade": "—", "consumo_estrada": "—",
        "comprimento": "3,78 m", "entre_eixos": "2,50 m", "porta_malas": "235 L",
        "autonomia": "300 km (CLTC) / ~240km real", "motorizacao": "eletrico",
        "pontos_fortes": ["Elétrico mais acessível do mercado", "Custo por km muito baixo", "Design simpático", "Ideal para uso urbano"],
        "pontos_fracos": ["Potência muito baixa (74cv)", "Autonomia limitada", "Porta-malas pequeno"],
    },
    "BYD Atto 3": {
        "marca": "BYD", "proprio": False, "segmento": "SUV Elétrico",
        "preco": "R$ 219.800 – 244.800", "motor": "Elétrico 204 cv",
        "cambio": "Direto", "tracao": "FWD",
        "consumo_cidade": "—", "consumo_estrada": "—",
        "comprimento": "4,46 m", "entre_eixos": "2,72 m", "porta_malas": "440 L",
        "autonomia": "480 km (CLTC) / ~390km real", "motorizacao": "eletrico",
        "pontos_fortes": ["SUV elétrico com melhor custo-benefício", "Interior criativo e espaçoso", "Recarga rápida 88kW", "ADAS completo"],
        "pontos_fracos": ["Marca ainda consolidando no Brasil", "Qualidade de acabamento variável"],
    },
    "Volkswagen ID.4": {
        "marca": "Volkswagen", "proprio": False, "segmento": "SUV Elétrico",
        "preco": "R$ 289.990 – 329.990", "motor": "Elétrico 204–299 cv",
        "cambio": "Direto", "tracao": "FWD / AWD",
        "consumo_cidade": "—", "consumo_estrada": "—",
        "comprimento": "4,58 m", "entre_eixos": "2,77 m", "porta_malas": "543 L",
        "autonomia": "520 km (WLTP) / ~420km real", "motorizacao": "eletrico",
        "pontos_fortes": ["Maior autonomia real do segmento", "AWD disponível", "Interior premium VW", "Solid brand trust"],
        "pontos_fracos": ["Preço mais alto", "Recarga máxima 135kW apenas"],
    },
}

# ─── Agrupamento por segmento ─────────────────────────────────────────────────

SEGMENTOS = [
    ("Hatch Entry",           ["Renault Kwid"],
     ["Chevrolet Onix", "Volkswagen Polo", "Fiat Argo", "Hyundai HB20", "Toyota Yaris"]),

    ("Hatch Compacto",        ["Peugeot 208", "Citroen C3"],
     ["Chevrolet Onix", "Volkswagen Polo", "Hyundai HB20"]),

    ("SUV Compacto Entry",    ["Renault Kardian", "Citroen Basalt", "Citroen Aircross", "Peugeot 2008"],
     ["Fiat Pulse", "Volkswagen T-Cross", "Hyundai Creta", "Honda HR-V", "Toyota Corolla Cross"]),

    ("SUV Compacto",          ["Renault Duster", "Haval Jolion"],
     ["Hyundai Creta", "Honda HR-V", "Fiat Pulse", "Volkswagen T-Cross"]),

    ("SUV Médio",             ["Renault Boreal", "Haval H6"],
     ["Toyota RAV4", "Volkswagen Tiguan", "Jeep Compass", "Hyundai Tucson"]),

    ("SUV Off-road",          ["Tank 300", "Haval H9"],
     []),

    ("SUV Grande PHEV",       ["Tank 500"],
     ["Toyota RAV4"]),

    ("Hatch Elétrico",        ["Ora 03"],
     ["BYD Dolphin", "BYD Seagull"]),

    ("Hatch Elétrico Compacto", ["Geely EX2"],
     ["BYD Seagull", "BYD Dolphin"]),

    ("SUV Elétrico Compacto", ["Geely EX5"],
     ["BYD Atto 3", "Volkswagen ID.4"]),

    ("SUV Compacto PHEV",     ["Geely EX5 EM-I"],
     ["Jeep Compass", "Toyota Corolla Cross"]),

    ("Picape Compacta",       ["Renault Oroch"],
     ["Fiat Strada", "Chevrolet Montana"]),

    ("Picape Média",          ["Renault Niagara"],
     ["Toyota Hilux", "Ford Ranger", "Mitsubishi L200"]),
]

# ─── Helpers ─────────────────────────────────────────────────────────────────

COR_MARCA_PROPRIA = {
    "Renault": "#f2c200", "GWM": "#c00020", "Peugeot": "#1a3a6b",
    "Citroen": "#e05a00", "Geely": "#0050b0",
}
COR_MARCA_CONC = {
    "Volkswagen": "#1b5f9e", "Jeep": "#2a6117", "Fiat": "#9b1c1c",
    "Toyota": "#c8102e", "Honda": "#cc0000", "Hyundai": "#002c5f",
    "Chevrolet": "#c79020", "Ford": "#003087", "Mitsubishi": "#c40b28",
    "BYD": "#1d4ed8", "Caoa Chery": "#7c2d12",
}

def cor(marca, proprio):
    if proprio:
        return COR_MARCA_PROPRIA.get(marca, "#374151")
    return COR_MARCA_CONC.get(marca, "#374151")

def badge_mot(mot):
    mapa = {
        "combustao":    ("#6b7280","Combustão"),
        "hibrido_leve": ("#ca8a04","Híbrido Leve"),
        "hibrido":      ("#16a34a","Híbrido/PHEV"),
        "eletrico":     ("#2563eb","Elétrico"),
    }
    c, l = mapa.get(mot, ("#6b7280","—"))
    return f'<span style="background:{c};color:#fff;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:600">{l}</span>'

def lista_itens(items, cor_bullet):
    return "".join(
        f'<li style="margin-bottom:3px;padding-left:4px"><span style="color:{cor_bullet};font-weight:700">+</span> {i}</li>'
        for i in items
    )

def lista_fracos(items):
    return "".join(
        f'<li style="margin-bottom:3px;padding-left:4px"><span style="color:#dc2626;font-weight:700">-</span> {i}</li>'
        for i in items
    )

def card_veiculo(nome, d):
    proprio = d.get("proprio", False)
    c = cor(d["marca"], proprio)
    borda_esq = f"4px solid {c}" if not proprio else f"3px solid {c}"
    bg = "#fff" if proprio else "#f9fafb"
    borda = f"2px solid {c}" if proprio else f"1px solid #e5e7eb"
    titulo_badge = f'<span style="background:{c};color:#fff;font-size:10px;padding:2px 7px;border-radius:10px;font-weight:700;text-transform:uppercase;letter-spacing:.5px">{d["marca"]}</span>'
    tag_proprio = '<span style="background:#dcfce7;color:#166534;font-size:10px;padding:2px 7px;border-radius:10px;font-weight:700">Nosso</span>' if proprio else ''

    autonomia_row = ""
    if d.get("autonomia") and d["autonomia"] != "—":
        autonomia_row = f'<tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Autonomia</td><td style="padding:3px 0;font-weight:600;color:#2563eb">{d["autonomia"]}</td></tr>'

    carga_row = ""
    if d.get("carga_util"):
        carga_row = f'<tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Carga útil</td><td style="padding:3px 0">{d["carga_util"]}</td></tr>'

    return f"""
<div style="background:{bg};border:{borda};border-left:{borda_esq};border-radius:10px;padding:16px 18px;width:310px;flex-shrink:0">
  <div style="display:flex;align-items:center;gap:6px;margin-bottom:8px;flex-wrap:wrap">
    {titulo_badge}{tag_proprio}{badge_mot(d.get("motorizacao","combustao"))}
  </div>
  <div style="font-size:17px;font-weight:700;color:#111;margin-bottom:12px">{nome}</div>

  <table style="font-size:12px;border-collapse:collapse;width:100%;margin-bottom:12px">
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Preco</td><td style="padding:3px 0;font-weight:600;color:#111">{d.get("preco","—")}</td></tr>
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Motor</td><td style="padding:3px 0">{d.get("motor","—")}</td></tr>
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Câmbio</td><td style="padding:3px 0">{d.get("cambio","—")}</td></tr>
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Tração</td><td style="padding:3px 0">{d.get("tracao","—")}</td></tr>
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Consumo</td><td style="padding:3px 0">{d.get("consumo_cidade","—")} (cid.) / {d.get("consumo_estrada","—")} (rod.)</td></tr>
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Comprimento</td><td style="padding:3px 0">{d.get("comprimento","—")}</td></tr>
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Entre-eixos</td><td style="padding:3px 0">{d.get("entre_eixos","—")}</td></tr>
    <tr><td style="color:#6b7280;padding:3px 8px 3px 0;white-space:nowrap">Porta-malas</td><td style="padding:3px 0">{d.get("porta_malas","—")}</td></tr>
    {carga_row}{autonomia_row}
  </table>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:11.5px">
    <div>
      <div style="font-weight:700;color:#166534;margin-bottom:4px;font-size:11px;text-transform:uppercase;letter-spacing:.5px">Pontos Fortes</div>
      <ul style="list-style:none;padding:0;margin:0;color:#1f2937;line-height:1.5">{lista_itens(d.get("pontos_fortes",[]), "#16a34a")}</ul>
    </div>
    <div>
      <div style="font-weight:700;color:#dc2626;margin-bottom:4px;font-size:11px;text-transform:uppercase;letter-spacing:.5px">Pontos Fracos</div>
      <ul style="list-style:none;padding:0;margin:0;color:#1f2937;line-height:1.5">{lista_fracos(d.get("pontos_fracos",[]))}</ul>
    </div>
  </div>
</div>"""

MENU = """
<nav style="background:#1e293b;padding:0 32px;display:flex;gap:0;border-bottom:1px solid #334155">
  <a href="news_grupo.html" style="padding:13px 22px;color:#94a3b8;font-size:14px;font-weight:600;border-bottom:3px solid transparent;text-decoration:none;transition:.2s">Noticias</a>
  <a href="concorrencia.html" style="padding:13px 22px;color:#f59e0b;font-size:14px;font-weight:600;border-bottom:3px solid #f59e0b;text-decoration:none">Concorrencia</a>
</nav>
"""

def gerar_html():
    agora = datetime.now().strftime("%d/%m/%Y as %H:%M")

    secoes = []
    for segmento, proprios, concorrentes_lista in SEGMENTOS:
        cards_p = []
        for nome in proprios:
            if nome in GUIA:
                cards_p.append(card_veiculo(nome, GUIA[nome]))

        cards_c = []
        for nome in concorrentes_lista:
            if nome in GUIA:
                cards_c.append(card_veiculo(nome, GUIA[nome]))

        sec_conc = ""
        if cards_c:
            sec_conc = f"""
<div style="margin-top:20px">
  <div style="font-size:11px;font-weight:700;color:#6b7280;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;border-top:1px dashed #e5e7eb;padding-top:16px">
    Concorrentes de Mercado
  </div>
  <div style="display:flex;flex-wrap:wrap;gap:14px">{"".join(cards_c)}</div>
</div>"""

        secoes.append(f"""
<section style="background:#fff;border-radius:14px;box-shadow:0 2px 8px rgba(0,0,0,.07);padding:24px 28px;margin-bottom:28px">
  <h2 style="font-size:18px;font-weight:700;color:#1e293b;margin-bottom:16px;padding-bottom:10px;border-bottom:2px solid #f1f5f9">
    {segmento}
  </h2>
  <div style="font-size:11px;font-weight:700;color:#374151;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">Nosso Portfolio</div>
  <div style="display:flex;flex-wrap:wrap;gap:14px">{"".join(cards_p)}</div>
  {sec_conc}
</section>""")

    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Analise de Concorrencia — Grupo Demarco/Tozzo</title>
<style>
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;background:#f1f5f9;color:#1f2937}}
  a{{color:inherit}}
  @media(max-width:700px){{nav{{padding:0 12px}}section{{padding:16px 12px!important}}}}
</style>
</head>
<body>

<header style="background:linear-gradient(135deg,#1a1a2e,#16213e);color:#fff;padding:24px 32px;display:flex;justify-content:space-between;align-items:center">
  <div>
    <div style="font-size:10px;opacity:.5;letter-spacing:2px;text-transform:uppercase;margin-bottom:4px">Grupo Demarco / Tozzo</div>
    <h1 style="font-size:22px;font-weight:700">Guia Comercial de Concorrencia</h1>
  </div>
  <div style="font-size:12px;opacity:.7;text-align:right">Atualizado em<br><strong style="font-size:14px;opacity:1">{agora}</strong></div>
</header>

{MENU}

<main style="max-width:1300px;margin:28px auto;padding:0 24px">

  <div style="background:#fff;border-radius:10px;padding:14px 20px;margin-bottom:24px;border-left:4px solid #f59e0b;font-size:13px;color:#374151;display:flex;gap:24px;flex-wrap:wrap">
    <span>Cards com <b>borda colorida dupla</b> = nosso portfolio</span>
    <span>Cards com <b>borda simples cinza</b> = concorrente de mercado</span>
    <span>Tag <b style="color:#166534">Nosso</b> = modelo do grupo</span>
    <span>Dados: precos, consumo, dimensoes, pontos fortes e fracos</span>
  </div>

  {"".join(secoes)}

  <footer style="text-align:center;padding:32px 0 16px;font-size:12px;color:#9ca3af">
    Grupo Demarco / Tozzo &mdash; Guia Comercial &mdash; {agora}
  </footer>

</main>
</body>
</html>"""

    with open(SAIDA, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Gerado: {SAIDA}")
    return SAIDA


if __name__ == "__main__":
    gerar_html()
