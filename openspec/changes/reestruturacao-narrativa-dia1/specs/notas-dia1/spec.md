## MODIFIED Requirements

### Requirement: Notas do Bloco 1 - Diagnóstico
As notas MUST conter: roteiro da demonstração ao vivo diretamente na tabela `orders` do Olist (shape, dtypes, head/tail, describe, isnull — com raciocínio verbal explícito sobre o que cada métrica revela), explicação do conceito de "diagnóstico antes de ação", os 5 problemas que os participantes vão encontrar no dataset e como guiá-los sem entregar as respostas, e o tangenciamento sobre Missing At Random. A demonstração NÃO usa dataset separado (iris, tips ou similar).

#### Scenario: Demonstração ao vivo do diagnóstico
- **WHEN** o instrutor conduz a demonstração do Bloco 1
- **THEN** as notas descrevem passo a passo o que mostrar diretamente em `orders`, incluindo o raciocínio verbal ("Primeiro olho shape... depois dtypes... por que essa coluna está como object?") e o que cada resultado do describe revela sobre o dataset

#### Scenario: Erros comuns dos participantes no Bloco 1
- **WHEN** participantes executam o exercício de diagnóstico em `items` e `reviews`
- **THEN** as notas listam os 2-3 erros mais comuns e como abordar cada um sem dar a resposta diretamente

### Requirement: Notas do Bloco 4 - Perguntas Analíticas
As notas MUST conter: demonstração de como transformar observação em pergunta analítica, os 3 critérios de uma boa pergunta (respondível, acionável, específica), exemplos de perguntas boas e ruins usando o dataset, instrução para o instrutor mencionar o salvamento de dados durante a revisão entre pares, e o script completo do encerramento cliffhanger.

#### Scenario: Demonstração ao vivo de formulação de perguntas
- **WHEN** o instrutor conduz a demonstração do Bloco 4
- **THEN** as notas contêm exemplo de pergunta vaga transformada em pergunta analítica, com raciocínio passo a passo

#### Scenario: Salvamento em paralelo durante revisão entre pares
- **WHEN** a revisão entre pares começa no Bloco 4
- **THEN** as notas instruem o instrutor a pedir que os participantes executem a célula de save em paralelo enquanto fazem a revisão, com mensagem específica: "Enquanto vocês revisam as perguntas do colega, rodem esta célula — ela salva os dados limpos que vão precisar amanhã"

#### Scenario: Script do cliffhanger — seleção da pergunta
- **WHEN** a revisão entre pares está em andamento
- **THEN** as notas orientam o instrutor a identificar a pergunta ideal para o cliffhanger (uma pergunta sobre nota × outra variável com correlação clara), e incluem pergunta-padrão de reserva caso nenhuma seja suficientemente analítica: "Em quais categorias a nota média está abaixo da mediana geral, e isso tem relação com o tempo de entrega?"

#### Scenario: Script do cliffhanger — condução ao vivo
- **WHEN** os últimos 10-15 minutos do Dia 1 começam
- **THEN** as notas contêm a sequência exata: (1) anunciar a pergunta selecionada, (2) fazer o groupby ao vivo mostrando a correlação clara, (3) pausar e perguntar "isso prova que X causa Y?", (4) não responder, (5) encerrar com "isso tem um nome — amanhã a gente enfrenta"; as notas incluem orientação explícita de não ceder à pressão da sala por resposta
