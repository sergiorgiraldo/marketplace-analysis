"""
Prepara o dataset do workshop a partir dos dados brutos do Olist.

Seleciona 3 tabelas (orders, items, reviews), enriquece com categorias de produto,
e introduz problemas realistas para o exercício de data cleaning.

Uso:
    uv run python scripts/prepare_dataset.py
"""

import numpy as np
import pandas as pd
from pathlib import Path

RAW_DIR = Path(__file__).parent.parent / "data" / "raw"
OUT_DIR = Path(__file__).parent.parent / "data" / "prepared"

np.random.seed(42)


def load_raw():
    orders = pd.read_csv(RAW_DIR / "olist_orders_dataset.csv")
    items = pd.read_csv(RAW_DIR / "olist_order_items_dataset.csv")
    reviews = pd.read_csv(RAW_DIR / "olist_order_reviews_dataset.csv")
    products = pd.read_csv(RAW_DIR / "olist_products_dataset.csv")
    categories = pd.read_csv(RAW_DIR / "product_category_name_translation.csv")
    return orders, items, reviews, products, categories


def enrich_items(items, products, categories):
    """Adiciona categoria do produto aos itens."""
    products = products.merge(categories, on="product_category_name", how="left")
    items = items.merge(
        products[["product_id", "product_category_name_english"]],
        on="product_id",
        how="left",
    )
    items.rename(columns={"product_category_name_english": "category"}, inplace=True)
    return items


def inject_missing_nonrandom(reviews, items):
    """
    Problema 1: Missings não-aleatórios.
    Remove review_score de pedidos com valor alto (>300) em ~40% dos casos
    e de certas categorias (electronics, computers) em ~30%.
    Isso cria padrão MAR detectável.
    """
    high_value_orders = items.groupby("order_id")["price"].sum()
    high_value_ids = high_value_orders[high_value_orders > 300].index

    mask_high_value = reviews["order_id"].isin(high_value_ids)
    drop_mask = mask_high_value & (np.random.random(len(reviews)) < 0.4)
    reviews.loc[drop_mask, "review_score"] = np.nan

    tech_orders = items[items["category"].isin(["electronics", "computers_accessories", "computers"])]["order_id"].unique()
    mask_tech = reviews["order_id"].isin(tech_orders) & ~drop_mask
    drop_tech = mask_tech & (np.random.random(len(reviews)) < 0.3)
    reviews.loc[drop_tech, "review_score"] = np.nan

    n_missing = reviews["review_score"].isna().sum()
    print(f"  Missings não-aleatórios em review_score: {n_missing} ({n_missing/len(reviews)*100:.1f}%)")
    return reviews


def inject_partial_duplicates(orders):
    """
    Problema 2: Duplicatas parciais.
    Copia ~500 pedidos mudando levemente o timestamp de compra (segundos diferentes)
    e em alguns casos o status.
    """
    sample = orders.sample(n=500, random_state=42).copy()

    timestamps = pd.to_datetime(sample["order_purchase_timestamp"])
    offsets = np.random.randint(1, 60, size=len(sample))
    sample["order_purchase_timestamp"] = (timestamps + pd.to_timedelta(offsets, unit="s")).astype(str)

    change_status = np.random.random(len(sample)) < 0.15
    sample.loc[change_status, "order_status"] = "processing"

    orders = pd.concat([orders, sample], ignore_index=True)
    print(f"  Duplicatas parciais inseridas: {len(sample)}")
    return orders


def inject_date_format_mix(orders):
    """
    Problema 3: Mix de formatos de data.
    Converte ~20% das datas de purchase_timestamp para formato BR (dd/mm/yyyy HH:MM:SS).
    """
    mask = np.random.random(len(orders)) < 0.20
    dates = pd.to_datetime(orders.loc[mask, "order_purchase_timestamp"], errors="coerce")
    orders.loc[mask, "order_purchase_timestamp"] = dates.dt.strftime("%d/%m/%Y %H:%M:%S")
    n_changed = mask.sum()
    print(f"  Datas com formato BR misturado: {n_changed} ({n_changed/len(orders)*100:.1f}%)")
    return orders


def inject_b2b_outliers(items):
    """
    Problema 4: Outliers B2B/B2C.
    Multiplica o preço de ~200 itens por 10-50x (simulando compras B2B em volume).
    Não são erros, são compras legítimas de perfil diferente.
    """
    mask = np.random.choice(len(items), size=200, replace=False)
    multipliers = np.random.uniform(10, 50, size=200)
    items.loc[mask, "price"] = items.loc[mask, "price"] * multipliers
    items.loc[mask, "price"] = items.loc[mask, "price"].round(2)
    print(f"  Outliers B2B inseridos: 200 itens com preços multiplicados")
    return items


def inject_category_typos(items):
    """
    Problema 5: Categorias com grafia inconsistente.
    Introduz variações em ~15% das categorias.
    """
    typo_map = {
        "health_beauty": ["Health_Beauty", "health beauty", "heath_beauty", "health_beuty"],
        "sports_leisure": ["Sports_Leisure", "sports leisure", "sport_leisure"],
        "housewares": ["Housewares", "house_wares", "housware"],
        "computers_accessories": ["Computers_Accessories", "computers accessories", "computer_accessories"],
        "furniture_decor": ["Furniture_Decor", "furniture decor", "furnitur_decor"],
        "watches_gifts": ["Watches_Gifts", "watches gifts", "watches_gift"],
        "telephony": ["Telephony", "telefony", "telephoni"],
        "bed_bath_table": ["Bed_Bath_Table", "bed bath table", "bed_bath"],
    }

    for original, typos in typo_map.items():
        cat_mask = items["category"] == original
        indices = items.index[cat_mask]
        n_to_change = int(len(indices) * 0.15)
        if n_to_change == 0:
            continue
        change_idx = np.random.choice(indices, size=n_to_change, replace=False)
        items.loc[change_idx, "category"] = np.random.choice(typos, size=n_to_change)

    print(f"  Categorias com grafia inconsistente inseridas em ~15% de 8 categorias")
    return items


def select_columns(orders, items, reviews):
    """Seleciona e renomeia colunas relevantes para o workshop."""
    orders = orders[[
        "order_id", "customer_id", "order_status",
        "order_purchase_timestamp", "order_approved_at",
        "order_delivered_customer_date", "order_estimated_delivery_date",
    ]].rename(columns={
        "order_purchase_timestamp": "purchase_date",
        "order_approved_at": "approved_date",
        "order_delivered_customer_date": "delivered_date",
        "order_estimated_delivery_date": "estimated_delivery_date",
    })

    items = items[[
        "order_id", "order_item_id", "product_id",
        "category", "price", "freight_value",
    ]]

    reviews = reviews[[
        "review_id", "order_id", "review_score",
        "review_comment_title", "review_comment_message",
        "review_creation_date",
    ]]

    return orders, items, reviews


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Carregando dados brutos...")
    orders, items, reviews, products, categories = load_raw()

    print("Enriquecendo itens com categorias...")
    items = enrich_items(items, products, categories)

    print("\nInjetando problemas realistas:")
    reviews = inject_missing_nonrandom(reviews, items)
    orders = inject_partial_duplicates(orders)
    orders = inject_date_format_mix(orders)
    items = inject_b2b_outliers(items)
    items = inject_category_typos(items)

    print("\nSelecionando colunas...")
    orders, items, reviews = select_columns(orders, items, reviews)

    print("\nSalvando datasets preparados:")
    for name, df in [("orders", orders), ("items", items), ("reviews", reviews)]:
        path = OUT_DIR / f"{name}.csv"
        df.to_csv(path, index=False)
        print(f"  {name}.csv: {df.shape[0]} linhas, {df.shape[1]} colunas")

    print("\nResumo:")
    print(f"  Orders: {orders.shape[0]} registros (tabela principal)")
    print(f"  Items: {items.shape[0]} registros")
    print(f"  Reviews: {reviews.shape[0]} registros")
    print(f"  Reviews sem score: {reviews['review_score'].isna().sum()}")
    print(f"  Categorias únicas em items: {items['category'].nunique()}")


if __name__ == "__main__":
    main()
