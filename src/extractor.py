import json


def extrair_produtos(caminho_json: str) -> list[dict]:
    with open(caminho_json, "r", encoding="utf-8") as f:
        dados = json.load(f)
    return dados["sao"]["produtos"]
