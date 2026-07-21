from src.models import Produto


def transformar(produto_dict: dict) -> Produto:
    nome = produto_dict.get("nome", "")
    return Produto(nome=nome)


def transformar_lista(produtos_dict: list[dict]) -> list[Produto]:
    return [transformar(p) for p in produtos_dict]
