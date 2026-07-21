import argparse
import sys

from src.extractor import extrair_produtos
from src.generator import gerar_planilha
from src.transformer import transformar_lista


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera planilha de produtos a partir de JSON.")
    parser.add_argument("caminho_json", help="Caminho para o arquivo JSON de entrada")
    parser.add_argument(
        "-o", "--output",
        default="tabela-produtos.xlsx",
        help="Caminho para o arquivo .xlsx de saída (default: tabela-produtos.xlsx)",
    )
    args = parser.parse_args()

    try:
        produtos_dict = extrair_produtos(args.caminho_json)
    except Exception as e:
        print(f"Erro ao ler JSON: {e}", file=sys.stderr)
        sys.exit(1)

    produtos = transformar_lista(produtos_dict)
    caminho = gerar_planilha(produtos, args.output)

    print(f"Planilha gerada: {caminho.resolve()}")


if __name__ == "__main__":
    main()
