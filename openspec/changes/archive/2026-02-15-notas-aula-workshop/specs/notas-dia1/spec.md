## ADDED Requirements

### Requirement: Notas da Abertura
As notas da abertura SHALL conter: fala de apresentação pessoal (quem é Caio, por que dados importa), a promessa do workshop com demonstração do produto final, e instruções de setup técnico com troubleshooting dos 3 problemas mais comuns.

#### Scenario: Instrutor consulta abertura
- **WHEN** o workshop inicia
- **THEN** as notas contêm texto de abertura com gancho que prende atenção, promessa clara, e checklist de setup

### Requirement: Notas do Bloco 1 - Diagnóstico
As notas MUST conter: roteiro da demonstração ao vivo (qual dataset usar, o que mostrar, que perguntas verbalizar), explicação do conceito de "diagnóstico antes de ação", os 5 problemas que os participantes vão encontrar no dataset e como guiá-los sem entregar as respostas, e o tangenciamento sobre Missing At Random.

#### Scenario: Demonstração ao vivo do diagnóstico
- **WHEN** o instrutor conduz a demonstração do Bloco 1
- **THEN** as notas descrevem passo a passo o que mostrar, incluindo o raciocínio verbal ("Primeiro olho shape... depois dtypes... por que essa coluna está como object?")

#### Scenario: Erros comuns dos participantes no Bloco 1
- **WHEN** participantes executam o exercício de diagnóstico
- **THEN** as notas listam os 2-3 erros mais comuns e como abordar cada um

### Requirement: Notas do Bloco 2 - Limpeza
As notas MUST conter: demonstração ao vivo de limpeza de duplicatas e datas, conceito de "limpeza documentada" (justificativa obrigatória), guia para ajudar participantes que travam na decisão "dropar ou manter", e tangenciamento sobre outliers e modelagem.

#### Scenario: Demonstração ao vivo da limpeza
- **WHEN** o instrutor conduz a demonstração do Bloco 2
- **THEN** as notas contêm a sequência de limpeza com raciocínio verbal e a frase-chave "Limpeza sem justificativa não é limpeza, é destruição de dados"

### Requirement: Notas do Bloco 3 - Exploração
As notas MUST conter: sequência de demonstração (univariada antes de bivariada), como interpretar distribuições comuns (bimodal, assimétrica, uniforme), e ênfase em documentar observações em vez de apenas gerar gráficos.

#### Scenario: Demonstração ao vivo da exploração
- **WHEN** o instrutor conduz a demonstração do Bloco 3
- **THEN** as notas explicam como interpretar cada tipo de distribuição com exemplo concreto do dataset

### Requirement: Notas do Bloco 4 - Perguntas Analíticas
As notas MUST conter: demonstração de como transformar observação em pergunta analítica, os 3 critérios de uma boa pergunta (respondível, acionável, específica), exemplos de perguntas boas e ruins usando o dataset, e tangenciamento sobre causalidade.

#### Scenario: Demonstração ao vivo de formulação de perguntas
- **WHEN** o instrutor conduz a demonstração do Bloco 4
- **THEN** as notas contêm exemplo de pergunta vaga transformada em pergunta analítica, com raciocínio passo a passo

### Requirement: Transições entre blocos
Cada transição entre blocos MUST ter frase de conexão que mostre como o bloco anterior alimenta o próximo, mantendo o arco narrativo do dia.

#### Scenario: Transição do diagnóstico para limpeza
- **WHEN** o Bloco 1 termina
- **THEN** as notas contêm frase de transição que conecta "identificamos os problemas" a "agora vamos tratar cada um"
