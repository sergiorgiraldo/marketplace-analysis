## MODIFIED Requirements

### Requirement: Estrutura do Dia 1 - Fundamentos e Data Cleaning
O Dia 1 SHALL cobrir 4 blocos sequenciais em ~4 horas: (1) Diagnóstico do dataset (30min), (2) Limpeza estruturada (60min), (3) Análise exploratória inicial (60min), (4) Definição de perguntas analíticas e encerramento (60min). Os blocos MUST incluir intervalos de 10min entre eles.

#### Scenario: Bloco 1 - Diagnóstico do dataset
- **WHEN** o workshop inicia no Dia 1
- **THEN** o participante recebe o dataset bruto e executa células de diagnóstico (shape, dtypes, head, describe, missings, duplicatas) no notebook guiado; a demonstração do instrutor usa diretamente a tabela `orders` do Olist, e o exercício cobre as tabelas `items` e `reviews`; o participante identifica pelo menos 3 problemas reais no dataset antes de qualquer limpeza

#### Scenario: Bloco 2 - Limpeza estruturada
- **WHEN** os problemas do dataset foram identificados no diagnóstico
- **THEN** o participante aplica limpeza seguindo checklist estruturado: tratamento de missings (decisão documentada de dropar vs. imputar), remoção de duplicatas, correção de tipos, tratamento de outliers com justificativa por escrito no notebook

#### Scenario: Bloco 3 - Análise exploratória inicial
- **WHEN** o dataset está limpo
- **THEN** o participante gera distribuições das variáveis principais, identifica padrões visuais (histogramas, boxplots, countplots) e documenta pelo menos 3 observações no notebook

#### Scenario: Bloco 4 - Perguntas analíticas e encerramento
- **WHEN** a exploração inicial está completa
- **THEN** o participante formula pelo menos 3 perguntas de negócio respondíveis com o dataset, realiza revisão entre pares usando os 3 critérios (respondível, acionável, específica), executa o salvamento dos dados limpos em paralelo durante a revisão entre pares, e participa do encerramento cliffhanger nos últimos 10-15 minutos do dia

### Requirement: Demonstrações ao vivo pelo instrutor
Cada bloco MUST começar com demonstração ao vivo do Caio (10-15min) antes dos participantes executarem. A demonstração SHALL mostrar o raciocínio por trás das decisões, não apenas o código. No Bloco 1, a demonstração MUST usar diretamente o dataset Olist (tabela `orders`), sem dataset separado para a fase de demonstração.

#### Scenario: Demonstração antes de exercício
- **WHEN** um novo bloco de conteúdo inicia
- **THEN** o Caio demonstra ao vivo o processo usando o dataset Olist (tabela `orders` no Bloco 1), verbalizando decisões e trade-offs, antes de os participantes replicarem no notebook com as tabelas designadas para o exercício

## ADDED Requirements

### Requirement: Encerramento do Dia 1 como cliffhanger
Os últimos 10-15 minutos do Dia 1 SHALL ser conduzidos como cliffhanger pedagógico: o instrutor seleciona a melhor pergunta analítica formulada pelos participantes durante a revisão entre pares do Bloco 4, conduz EDA parcial ao vivo que revela uma correlação clara, e para deliberadamente antes de responder a questão causal — criando tensão intencional para o Dia 2.

#### Scenario: Seleção da pergunta para o cliffhanger
- **WHEN** a revisão entre pares do Bloco 4 está em andamento
- **THEN** o instrutor identifica a pergunta mais adequada para o cliffhanger: uma que envolva pelo menos dois campos com correlação clara e que abra ambiguidade causal evidente (ex.: nota × atraso de entrega)

#### Scenario: EDA ao vivo e revelação da ambiguidade
- **WHEN** o cliffhanger tem início com a pergunta selecionada
- **THEN** o instrutor conduz EDA ao vivo por 5-7 minutos até exibir correlação clara nos dados, então formula a pergunta "isso prova que X causa Y?" sem respondê-la, e encerra o dia com "isso tem um nome — amanhã a gente enfrenta"

#### Scenario: Encerramento sem resolução
- **WHEN** a análise ao vivo revela a ambiguidade causal
- **THEN** o instrutor encerra o Dia 1 sem resolver a questão, não cede à pressão da sala por resposta imediata, e o dia termina com a pergunta aberta
