# Glossário de Python e Pandas para o Workshop

Referência rápida dos termos técnicos que aparecem nos notebooks. Cada termo está explicado sem assumir conhecimento prévio de programação.

---

**DataFrame** — Tabela de dados no pandas. Funciona como uma planilha do Excel: linhas são registros, colunas são variáveis. Quando você carrega um CSV com `pd.read_csv()`, o resultado é um DataFrame.

**Series** — Uma única coluna de um DataFrame. Se `df` é uma tabela, `df['price']` é uma Series contendo todos os valores de preço.

**NaN** — "Not a Number". Representa um valor ausente (missing). Aparece quando o dado não foi preenchido, não existe, ou foi corrompido. Não é zero, não é vazio: é a ausência de informação.

**.shape** — Mostra quantas linhas e colunas um DataFrame tem. `df.shape` retorna algo como `(99441, 8)`, que significa 99.441 linhas e 8 colunas.

**.dtypes** — Mostra o tipo de cada coluna (número inteiro, número decimal, texto, data). Serve para detectar problemas: uma coluna de data aparecendo como texto indica que precisa de conversão.

**.head()** e **.tail()** — Mostram as primeiras ou últimas linhas do DataFrame. `.head(5)` exibe as 5 primeiras linhas. Serve para inspecionar o formato real dos dados sem olhar a tabela inteira.

**.describe()** — Gera estatísticas resumidas (média, mediana, mínimo, máximo, desvio padrão) de todas as colunas numéricas. É o primeiro lugar para detectar valores absurdos: mínimo negativo num campo de preço, máximo de 50.000 onde se esperava 500.

**.isnull()** — Verifica se cada valor é ausente (NaN). `.isnull().sum()` conta quantos valores ausentes existem em cada coluna.

**.groupby()** — Agrupa os dados por uma variável e permite calcular estatísticas por grupo. `df.groupby('category')['price'].mean()` calcula o preço médio de cada categoria. Equivalente ao "agrupar por" de uma tabela dinâmica do Excel.

**.merge()** — Junta duas tabelas usando uma coluna em comum. `orders.merge(reviews, on='order_id')` combina pedidos com avaliações pela coluna `order_id`. Equivalente ao VLOOKUP/PROCV ou a um JOIN de SQL.

**.sort_values()** — Ordena o DataFrame por uma coluna. `.sort_values('price', ascending=False)` coloca os mais caros primeiro.

**.drop_duplicates()** — Remove linhas duplicadas. `df.drop_duplicates(subset='order_id', keep='last')` mantém apenas o último registro de cada pedido duplicado.

**.value_counts()** — Conta quantas vezes cada valor aparece numa coluna. `df['category'].value_counts()` mostra quantos itens existem em cada categoria, ordenados do maior para o menor.

**.mean()** e **.median()** — Calculam a média e a mediana de uma coluna numérica. A média é sensível a valores extremos; a mediana é o valor do meio quando os dados estão ordenados.

**.agg()** — Aplica múltiplas funções de uma vez a um grupo. Permite calcular média, mediana e contagem ao mesmo tempo dentro de um `.groupby()`.

**pd.to_datetime()** — Converte texto para formato de data. Necessário quando datas estão armazenadas como texto (string). O parâmetro `format='mixed'` aceita formatos misturados no mesmo campo.

**pd.cut()** — Divide valores numéricos em faixas. `pd.cut(df['delay_days'], bins=[-999, 0, 7, 14, 999])` cria faixas de atraso (sem atraso, até 7 dias, até 14 dias, acima de 14).

**plt.subplots()** — Cria uma figura (área de desenho) com um ou mais gráficos. `fig, ax = plt.subplots()` cria uma figura com um gráfico. `fig, axes = plt.subplots(1, 2)` cria dois gráficos lado a lado.

**sns.heatmap()** — Cria um mapa de calor a partir de uma tabela de números. Cada célula recebe uma cor proporcional ao valor. Útil para visualizar cruzamentos entre duas variáveis categóricas (exemplo: nota média por categoria e faixa de atraso).

**.to_csv()** — Salva um DataFrame como arquivo CSV. `df.to_csv('dados_limpos.csv', index=False)` grava a tabela em disco. O `index=False` evita gravar uma coluna extra com números de linha.

**pivot_table** — Reorganiza dados em formato de tabela cruzada. `df.pivot_table(values='review_score', index='category', columns='delay_band', aggfunc='mean')` cria uma grade onde cada célula mostra a nota média para uma combinação de categoria e faixa de atraso. Similar a uma tabela dinâmica do Excel.
