from pathlib import Path

from openpyxl import Workbook

from src.models import Produto

COLUNAS = [
    "Código",
    "Descrição",
    "Referência",
    "Cód. Auxiliar",
    "Fornecedor",
    "Fornecedor Exclusivo",
    "Comprador",
    "Empresa",
    "Contabiliza saldo em estoque",
    "Indisponivél para venda",
    "Setor",
    "Linha",
    "Marca",
    "Coleção",
    "Espessura",
    "Classificação",
    "Tamanho",
    "Cores",
    "Unidade de compra",
    "Fator de conversão",
    "Múltiplo de venda",
    "Moeda",
    "Custo com ICMS (R$)",
    "Desconto (%)",
    "Acréscimo (%)",
    "IPI (%)",
    "Frete (R$)",
    "Despesas acessórias (R$)",
    "Substituição tributária (R$)",
    "Diferencial ICMS (R$)",
    "Mark-up (%)",
    "Preço venda R$",
    "Permite desconto",
    "Comissão (%)",
    "Configuração tributária",
    "NCM",
    "CEST",
    "Produto supérfulo",
    "Tipo de item",
    "Origem da Mercadoria",
    "Regime de Incidência PIS e COFINS",
    "Produto é brinde",
    "Produto de catálago",
    "Descrição de catálogo",
    "Disponivel na loja virtual",
    "Exige controle",
    "Tipo de controle",
    "Tamanho controle",
    "Produto óptico",
    "Lente/Armação/Tratamento",
    "Entrega futura",
    "Pronta entrega",
    "Prazo de entrega (dias)",
    "Peso bruto (kg)",
    "Peso líquido (kg)",
    "Descrição complementar?",
    "Altura (frete)",
    "Largura (frete)",
    "Comprimento (frete)",
    "Altura",
    "Largura",
    "Comprimento",
    "Importado por balança",
    "Produto vendido por (balança)",
    "Quantidade mínima",
    "Quantidade máxima",
    "Quantidade compra",
    "Localização",
    "Observação",
    "Código de barras",
    "Características",
    "Status",
    "Código Integracao OMS",
    "Produto Desativado",
    "Bloqueia atualização de preço franqueadora",
]

INDICE_DESCRICAO = COLUNAS.index("Descrição")


def gerar_planilha(produtos: list[Produto], caminho_saida: str | Path) -> Path:
    wb = Workbook()
    ws = wb.active
    ws.title = "Produtos"

    ws.append(COLUNAS)

    for produto in produtos:
        linha = [""] * len(COLUNAS)
        linha[INDICE_DESCRICAO] = produto.nome
        ws.append(linha)

    caminho = Path(caminho_saida)
    wb.save(str(caminho))
    return caminho
