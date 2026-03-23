# Dicionário de Dados - Workshop de Análise de Dados

Dataset de um marketplace brasileiro de e-commerce. Contém informações sobre pedidos, itens vendidos e avaliações de clientes.

---

## Tabela: orders

Cada linha representa um pedido feito por um cliente no marketplace.

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `order_id` | string | Identificador único do pedido | `e481f51cbdc54678b7cc49136f2d6af7` |
| `customer_id` | string | Identificador único do cliente | `9ef432eb6251297304e76186b10a928d` |
| `order_status` | string | Status do pedido (delivered, shipped, canceled, etc.) | `delivered` |
| `purchase_date` | string | Data e hora da compra | `2017-10-02 10:56:33` |
| `approved_date` | string | Data e hora da aprovação do pagamento | `2017-10-02 11:07:15` |
| `delivered_date` | string | Data e hora da entrega ao cliente | `2017-10-10 21:25:13` |
| `estimated_delivery_date` | string | Data estimada de entrega informada ao cliente | `2017-10-18 00:00:00` |

**Observações:** Um pedido pode ter múltiplos itens (ver tabela `items`). O campo `purchase_date` pode conter formatos de data diferentes.

---

## Tabela: items

Cada linha representa um item dentro de um pedido. Um pedido pode conter vários itens.

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `order_id` | string | Identificador do pedido (FK para `orders`) | `00010242fe8c5a6d1ba2dd792cb16214` |
| `order_item_id` | int | Número sequencial do item dentro do pedido (1, 2, 3...) | `1` |
| `product_id` | string | Identificador único do produto | `4244733e06e7ecb4970a6e2683c13e61` |
| `category` | string | Categoria do produto em inglês | `cool_stuff` |
| `price` | float | Preço do item em reais (R$) | `58.90` |
| `freight_value` | float | Custo do frete do item em reais (R$) | `13.29` |

**Observações:** O campo `category` pode conter variações de grafia para a mesma categoria. Alguns preços são atipicamente altos (possíveis compras em volume/B2B).

---

## Tabela: reviews

Cada linha representa uma avaliação feita por um cliente após receber o pedido.

| Coluna | Tipo | Descrição | Exemplo |
|--------|------|-----------|---------|
| `review_id` | string | Identificador único da avaliação | `7bc2406110b926393aa56f80a40eba40` |
| `order_id` | string | Identificador do pedido avaliado (FK para `orders`) | `73fc7af87114b39712e6da79b0a377eb` |
| `review_score` | float | Nota dada pelo cliente (1 a 5) | `5.0` |
| `review_comment_title` | string | Título do comentário (opcional, pode estar vazio) | `recomendo` |
| `review_comment_message` | string | Texto do comentário (opcional, pode estar vazio) | `Recebi bem antes do prazo estipulado.` |
| `review_creation_date` | string | Data em que a avaliação foi criada | `2018-01-18 00:00:00` |

**Observações:** Nem todos os pedidos possuem avaliação. O campo `review_score` pode estar ausente em alguns registros. Os campos de texto do comentário frequentemente estão vazios.

---

## Relações entre tabelas

```
orders (1) ──── (N) items       via order_id
orders (1) ──── (1) reviews     via order_id
```

Um pedido tem um ou mais itens e no máximo uma avaliação.
