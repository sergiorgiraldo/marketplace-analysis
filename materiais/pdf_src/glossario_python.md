---
title: "Glossário de Python e Pandas"
subtitle: "Workshop de Análise de Dados com Python"
author: ""
date: ""
geometry: margin=2cm
fontsize: 11pt
mainfont: "Helvetica Neue"
monofont: "Menlo"
linestretch: 1.25
colorlinks: true
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\small Workshop de Análise de Dados}
  - \fancyhead[R]{\small Glossário}
  - \fancyfoot[C]{}
---

\begin{center}
\textit{Referência rápida dos termos técnicos que aparecem nos notebooks.\\Cada termo está explicado sem assumir conhecimento prévio de programação.}
\end{center}

\vspace{0.5em}

## Estruturas de Dados

**DataFrame** --- Tabela de dados no pandas. Funciona como uma planilha do Excel: linhas são registros, colunas são variáveis. Quando você carrega um CSV com `pd.read_csv()`, o resultado é um DataFrame.

**Series** --- Uma única coluna de um DataFrame. Se `df` é uma tabela, `df['price']` é uma Series contendo todos os valores de preço.

**NaN** --- "Not a Number". Representa um valor ausente (missing). Aparece quando o dado não foi preenchido, não existe, ou foi corrompido. Não é zero, não é vazio: é a ausência de informação.

## Inspecionar os Dados

**`.shape`** --- Mostra quantas linhas e colunas um DataFrame tem. `df.shape` retorna algo como `(99441, 8)`: 99.441 linhas e 8 colunas.

**`.dtypes`** --- Mostra o tipo de cada coluna (número inteiro, número decimal, texto, data). Uma coluna de data aparecendo como texto indica que precisa de conversão.

**`.head()` e `.tail()`** --- Mostram as primeiras ou últimas linhas do DataFrame. `.head(5)` exibe as 5 primeiras linhas. Serve para inspecionar o formato real dos dados.

**`.describe()`** --- Gera estatísticas resumidas (média, mediana, mínimo, máximo, desvio padrão) de todas as colunas numéricas. Primeiro lugar para detectar valores absurdos.

**`.isnull()`** --- Verifica se cada valor é ausente (NaN). `.isnull().sum()` conta quantos valores ausentes existem em cada coluna.

**`.value_counts()`** --- Conta quantas vezes cada valor aparece numa coluna. `df['category'].value_counts()` mostra quantos itens existem em cada categoria, do maior para o menor.

## Transformar e Limpar

**`.drop_duplicates()`** --- Remove linhas duplicadas. `df.drop_duplicates(subset='order_id', keep='last')` mantém apenas o último registro de cada pedido duplicado.

**`.sort_values()`** --- Ordena o DataFrame por uma coluna. `.sort_values('price', ascending=False)` coloca os mais caros primeiro.

**`pd.to_datetime()`** --- Converte texto para formato de data. O parâmetro `format='mixed'` aceita formatos misturados no mesmo campo.

**`pd.cut()`** --- Divide valores numéricos em faixas. `pd.cut(df['delay_days'], bins=[-999, 0, 7, 14, 999])` cria faixas de atraso (sem atraso, até 7 dias, até 14 dias, acima de 14).

**`.to_csv()`** --- Salva um DataFrame como arquivo CSV. `df.to_csv('dados_limpos.csv', index=False)` grava a tabela em disco. O `index=False` evita uma coluna extra com números de linha.

## Agrupar e Cruzar

**`.groupby()`** --- Agrupa os dados por uma variável e permite calcular estatísticas por grupo. `df.groupby('category')['price'].mean()` calcula o preço médio de cada categoria. Equivalente a uma tabela dinâmica do Excel.

**`.agg()`** --- Aplica múltiplas funções de uma vez a um grupo. Permite calcular média, mediana e contagem ao mesmo tempo dentro de um `.groupby()`.

**`.merge()`** --- Junta duas tabelas usando uma coluna em comum. `orders.merge(reviews, on='order_id')` combina pedidos com avaliações. Equivalente ao PROCV ou a um JOIN de SQL.

**`pivot_table`** --- Reorganiza dados em formato de tabela cruzada. Cada célula mostra uma estatística (ex: nota média) para uma combinação de duas variáveis. Similar a uma tabela dinâmica do Excel.

## Visualização

**`.mean()` e `.median()`** --- Calculam a média e a mediana. A média é sensível a valores extremos; a mediana é o valor do meio quando os dados estão ordenados.

**`plt.subplots()`** --- Cria uma figura (área de desenho) com um ou mais gráficos. `fig, ax = plt.subplots()` cria uma figura com um gráfico. `fig, axes = plt.subplots(1, 2)` cria dois lado a lado.

**`sns.heatmap()`** --- Cria um mapa de calor a partir de uma tabela de números. Cada célula recebe uma cor proporcional ao valor. Útil para visualizar cruzamentos entre duas variáveis categóricas.
