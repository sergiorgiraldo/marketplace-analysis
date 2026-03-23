## ADDED Requirements

### Requirement: Dataset baseado em e-commerce real
O dataset SHALL ser derivado do dataset público do Olist (Brazilian E-Commerce), usando um subconjunto de 3 tabelas: pedidos (orders), itens de pedido (order_items) e avaliações (reviews). O dataset MUST conter entre 50k e 120k registros na tabela principal.

#### Scenario: Carga inicial do dataset
- **WHEN** o participante executa a célula de carga do dataset
- **THEN** três DataFrames são carregados (orders, items, reviews) com schema documentado e dicionário de dados acessível no notebook

### Requirement: Problemas realistas pré-inseridos
O dataset MUST conter problemas reais que exijam decisões de limpeza, não apenas erros triviais. Os problemas SHALL incluir pelo menos: (1) missings não-aleatórios em campo de avaliação (pedidos não avaliados), (2) duplicatas parciais (mesmo pedido com timestamps levemente diferentes), (3) inconsistências de formato em datas (mix de formatos ISO e brasileiro), (4) outliers reais em valores de pedido (não erros, mas compras B2B misturadas com B2C), (5) categorias com grafia inconsistente.

#### Scenario: Missings não-aleatórios
- **WHEN** o participante analisa missings na coluna de avaliação
- **THEN** o padrão de ausência está correlacionado com outra variável (ex: pedidos acima de certo valor ou de certas categorias têm mais missings), forçando discussão sobre MCAR vs. MAR

#### Scenario: Duplicatas parciais
- **WHEN** o participante verifica duplicatas
- **THEN** existem registros que parecem duplicados mas diferem em campos de timestamp ou status, exigindo decisão sobre qual manter baseada em critério de negócio

#### Scenario: Outliers reais
- **WHEN** o participante analisa distribuição de valores
- **THEN** existem valores extremos que não são erros de digitação mas compras legítimas de volume diferente, forçando decisão de segmentar vs. remover com justificativa

### Requirement: Dicionário de dados
O dataset MUST ser acompanhado de dicionário de dados em markdown com: nome da coluna, tipo esperado, descrição de negócio e exemplo de valor para cada campo de cada tabela.

#### Scenario: Consulta ao dicionário
- **WHEN** o participante tem dúvida sobre o significado de uma coluna
- **THEN** o dicionário de dados está disponível como célula markdown no topo do notebook e como arquivo separado, com todas as colunas documentadas

### Requirement: História de negócio compreensível
O dataset MUST vir com contexto de negócio que permita ao participante formular perguntas relevantes: o marketplace quer entender padrões de satisfação, performance por categoria e sazonalidade de vendas.

#### Scenario: Briefing de negócio
- **WHEN** o workshop inicia
- **THEN** o participante recebe um "briefing do gestor" fictício com 2-3 perguntas de negócio abertas que direcionam a análise sem entregar as respostas
