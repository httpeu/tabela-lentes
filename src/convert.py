import json
from pathlib import Path

import pandas as pd


def flatten_dict(d, parent_key="", sep="_"):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def json_to_xlsx(json_path: str, xlsx_path: str):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    produtos = data.get("sao", {}).get("produtos", [])

    flattened = [flatten_dict(produto) for produto in produtos]
    df = pd.DataFrame(flattened)

    output_path = Path(xlsx_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_excel(xlsx_path, index=False, engine="openpyxl")
    print(f"Converted {json_path} to {xlsx_path}")


def extract_product_names_to_xlsx(json_path: str, xlsx_path: str):
    """Extract only the 'nome' field from each product and save to xlsx."""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    produtos = data.get("sao", {}).get("produtos", [])

    names = [produto.get("nome", "") for produto in produtos]
    df = pd.DataFrame({"nome": names})

    output_path = Path(xlsx_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    df.to_excel(xlsx_path, index=False, engine="openpyxl")
    print(f"Extracted {len(names)} product names to {xlsx_path}")


if __name__ == "__main__":
    json_path = Path(__file__).parent.parent / "exemple.json"
    xlsx_path = Path(__file__).parent.parent / "output.xlsx"
    json_to_xlsx(str(json_path), str(xlsx_path))

    names_xlsx = Path(__file__).parent.parent / "product_names.xlsx"
    extract_product_names_to_xlsx(str(json_path), str(names_xlsx))
