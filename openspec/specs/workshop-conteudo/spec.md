## ADDED Requirements

### Requirement: Estrutura do Dia 1 - Fundamentos e Data Cleaning
O Dia 1 SHALL cobrir 4 blocos sequenciais em ~4 horas: (1) Diagnóstico do dataset (45min), (2) Limpeza estruturada (60min), (3) Análise exploratória inicial (60min), (4) Definição de perguntas analíticas (45min). Os blocos MUST incluir intervalos de 10min entre eles.

#### Scenario: Bloco 1 - Diagnóstico do dataset
- **WHEN** o workshop inicia no Dia 1
- **THEN** o participante recebe o dataset bruto e executa células de diagnóstico (shape, dtypes, head, describe, missings, duplicatas) no notebook guiado, identificando pelo menos 3 problemas reais no dataset antes de qualquer limpeza

#### Scenario: Bloco 2 - Limpeza estruturada
- **WHEN** os problemas do dataset foram identificados no diagnóstico
- **THEN** o participante aplica limpeza seguindo checklist estruturado: tratamento de missings (decisão documentada de dropar vs. imputar), remoção de duplicatas, correção de tipos, tratamento de outliers com justificativa por escrito no notebook

#### Scenario: Bloco 3 - Análise exploratória inicial
- **WHEN** o dataset está limpo
- **THEN** o participante gera distribuições das variáveis principais, identifica padrões visuais (histogramas, boxplots, countplots) e documenta pelo menos 3 observações no notebook

#### Scenario: Bloco 4 - Perguntas analíticas
- **WHEN** a exploração inicial está completa
- **THEN** o participante formula pelo menos 3 perguntas de negócio respondíveis com o dataset, priorizando por impacto e viabilidade, e documenta no notebook com justificativa

### Requirement: Estrutura do Dia 2 - Análise e Comunicação
O Dia 2 SHALL cobrir 4 blocos sequenciais em ~4 horas: (1) Análise estatística aplicada (60min), (2) Visualizações interpretativas (60min), (3) Storytelling com dados (45min), (4) Documento final de análise (45min). Os blocos MUST incluir intervalos de 10min entre eles.

#### Scenario: Bloco 1 - Análise estatística aplicada
- **WHEN** o Dia 2 inicia com as perguntas definidas no Dia 1
- **THEN** o participante responde cada pergunta usando agrupamentos, correlações e comparações entre segmentos, com output numérico e interpretação textual no notebook

#### Scenario: Bloco 2 - Visualizações interpretativas
- **WHEN** as respostas estatísticas estão documentadas
- **THEN** o participante cria pelo menos 4 visualizações finais (uma por pergunta ou tema), cada uma com título descritivo, eixos rotulados e anotação que destaque o insight principal

#### Scenario: Bloco 3 - Storytelling com dados
- **WHEN** as visualizações estão prontas
- **THEN** o participante organiza os insights em uma narrativa coerente com estrutura: contexto → problema → descoberta → recomendação, escrita em markdown no notebook

#### Scenario: Bloco 4 - Documento final
- **WHEN** a narrativa está completa
- **THEN** o participante exporta uma versão limpa do notebook (sem código visível) como documento de análise apresentável, contendo: resumo executivo, metodologia resumida, principais descobertas com visualizações e recomendações

### Requirement: Demonstrações ao vivo pelo instrutor
Cada bloco MUST começar com demonstração ao vivo do Caio (10-15min) antes dos participantes executarem. A demonstração SHALL mostrar o raciocínio por trás das decisões, não apenas o código.

#### Scenario: Demonstração antes de exercício
- **WHEN** um novo bloco de conteúdo inicia
- **THEN** o Caio demonstra ao vivo o processo completo usando uma amostra diferente ou ângulo diferente do dataset, verbalizando decisões e trade-offs, antes de os participantes replicarem no seu notebook

### Requirement: Checkpoints de progresso
O workshop MUST ter checkpoints verificáveis ao final de cada bloco para que participantes saibam se estão no ritmo.

#### Scenario: Checkpoint ao final do bloco
- **WHEN** o tempo de um bloco termina
- **THEN** o participante consegue verificar se atingiu o output mínimo esperado (ex: "seu dataset deve ter X linhas após limpeza", "você deve ter pelo menos 3 perguntas documentadas") através de célula de verificação no notebook
