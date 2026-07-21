# Tabela Produtos

Script Python CLI que lê um JSON de produtos, extrai o nome de cada item e gera uma planilha `.xlsx` padronizada para importação em sistema de gestão.

## Estrutura

```
tabela-lentes/
├── data/input/          # Coloque os arquivos .json aqui
├── data/output/         # Planilhas geradas
├── src/                 # Código-fonte
│   ├── main.py          # Entry point
│   ├── extractor.py     # Leitura do JSON
│   ├── transformer.py   # Flatten dos dados
│   ├── generator.py     # Geração do .xlsx
│   └── models.py        # Dataclasses
```

## Requisitos

- Python 3.10+
- `openpyxl` (instalado automaticamente via `pip`)

## Instalação

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt   # Linux/macOS
.venv\Scripts\pip install -r requirements.txt  # Windows
```

## Uso

```bash
python -m src.main data/input/produtos.json -o data/output/tabela-produtos.xlsx
```

- `caminho_json` (obrigatório): arquivo JSON com a estrutura `sao.produtos[]`
- `-o` / `--output` (opcional): caminho de saída do `.xlsx` (default: `tabela-produtos.xlsx`)


## Formato do JSON de entrada

```json
{
    "sao": {
        "produtos": [
            { "nome": "VS ZEISS Mineral Lantal", "...": "..." }
        ]
    }
}
```

Apenas o campo `nome` é extraído e mapeado para a coluna **Descrição** na planilha. As demais colunas (~70) ficam vazias, conforme layout do sistema de destino.
