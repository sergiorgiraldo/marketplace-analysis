"""
Download do dataset público do Olist (Brazilian E-Commerce).
Fonte: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Uso:
    uv run python scripts/download_olist.py

Requer: kaggle CLI configurado com API key em ~/.kaggle/kaggle.json
Se não tiver, baixe manualmente de:
    https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
e coloque os CSVs em data/raw/
"""

import os
import subprocess
import sys
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
DATASET = "olistbr/brazilian-ecommerce"

REQUIRED_FILES = [
    "olist_orders_dataset.csv",
    "olist_order_items_dataset.csv",
    "olist_order_reviews_dataset.csv",
    "olist_products_dataset.csv",
]


def download_via_kaggle():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Baixando dataset {DATASET} para {RAW_DIR}...")
    result = subprocess.run(
        ["uv", "run", "kaggle", "datasets", "download", "-d", DATASET, "-p", str(RAW_DIR), "--unzip"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"Erro no download: {result.stderr}")
        print("\nBaixe manualmente de:")
        print(f"  https://www.kaggle.com/datasets/{DATASET}")
        print(f"  Coloque os CSVs em: {RAW_DIR}")
        sys.exit(1)
    print("Download concluído!")


def verify_files():
    missing = [f for f in REQUIRED_FILES if not (RAW_DIR / f).exists()]
    if missing:
        print(f"Arquivos faltando em {RAW_DIR}:")
        for f in missing:
            print(f"  - {f}")
        return False
    print("Todos os arquivos necessários presentes:")
    for f in REQUIRED_FILES:
        size_mb = (RAW_DIR / f).stat().st_size / (1024 * 1024)
        print(f"  {f} ({size_mb:.1f} MB)")
    return True


if __name__ == "__main__":
    if verify_files():
        print("\nDataset já baixado. Nada a fazer.")
    else:
        download_via_kaggle()
        if not verify_files():
            sys.exit(1)
