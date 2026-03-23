## 1. Notebook — remover demo iris/tips

- [x] 1.1 Identificar no `notebooks/dia1_fundamentos_cleaning.ipynb` todas as células de demonstração que referenciam iris, tips ou seaborn como dataset de exemplo (buscar por "iris", "tips", "sns.load_dataset" no source das células)
- [x] 1.2 Remover essas células do notebook; verificar que o fluxo de células restantes continua coerente (sem referências a variáveis criadas nas células removidas)
- [x] 1.3 Verificar que a célula de save (to_csv para orders_clean, items_clean, reviews_clean) está presente e funcional; atualizar o markdown da célula ou da célula imediatamente anterior para indicar que deve ser executada durante a revisão entre pares do Bloco 4

## 2. Roteiro — ajustar tempos do Bloco 1

- [x] 2.1 Em `materiais/roteiro_instrutor.md`, atualizar o cabeçalho do Bloco 1: de "Diagnóstico do Dataset (45 min) | 09:15-10:00" para "Diagnóstico do Dataset (30 min) | 09:15-09:45"
- [x] 2.2 Ajustar os horários em cascata: Intervalo passa de 10:00-10:10 para 09:45-09:55; Bloco 2A de 10:10-10:40 para 09:55-10:25; Bloco 2B de 10:40-11:15 para 10:25-11:00; Intervalo de 11:15-11:25 para 11:00-11:10; Bloco 3 de 11:25-11:55 para 11:10-11:40; Intervalo de 11:55-12:05 para 11:40-11:50; Bloco 4 de 12:05-13:00 para 11:50-13:00
- [x] 2.3 Atualizar a subdivisão interna do Bloco 1 no roteiro: Demonstração ao vivo de 15 min para 10 min; Exercício dos participantes de 25 min para 15 min (escopo: `items` e `reviews`); Checkpoint mantido em 5 min
- [x] 2.4 Atualizar o texto da demonstração ao vivo do Bloco 1 para remover a instrução de abrir dataset separado e substituir por "Abrir diretamente o dataset Olist — tabela `orders`"

## 3. Roteiro — redesenhar encerramento do Bloco 4

- [x] 3.1 Na seção "Revisão entre pares + discussão em grupo" do Bloco 4, adicionar instrução: ao iniciar a revisão entre pares, pedir que os participantes executem a célula de save em paralelo; incluir a mensagem exata a dizer
- [x] 3.2 Substituir a seção "Fechamento do Dia 1 (10 min)" atual (salvar dados, checkpoint, preview do Dia 2) pela sequência de cliffhanger: (1) selecionar melhor pergunta durante a revisão entre pares, (2) anunciar a pergunta para a sala, (3) EDA ao vivo por 5-7 min até revelar correlação clara, (4) parar com "isso prova que X causa Y?", (5) encerrar com "isso tem um nome — amanhã a gente enfrenta"
- [x] 3.3 Adicionar nota ao instrutor sobre critério de seleção da pergunta: "buscar uma pergunta que envolva nota + outra variável com correlação evidente nos dados; se nenhuma for adequada, usar a pergunta de reserva nas notas de aula"

## 4. Notas de aula — atualizar Bloco 1

- [x] 4.1 Em `materiais/notas_aula.md`, na seção "Bloco 1 — Demonstração ao vivo", remover o parágrafo que instrui abrir iris ou tips como dataset separado e o parágrafo que explica a justificativa pedagógica desse uso
- [x] 4.2 Substituir pela instrução de abrir `orders` diretamente, adaptando a sequência verbal (shape → dtypes → head/tail → describe → isnull) para usar os campos reais da tabela Olist; manter o mesmo raciocínio verbal mas aplicado a purchase_price, order_status, purchase_timestamp etc.
- [x] 4.3 Escrever o script de abertura do Bloco 1 para as notas: os primeiros minutos da demonstração devem estabelecer o gancho — nomear o volume real ("99 mil pedidos"), o contexto reconhecível (marketplace brasileiro), e o problema concreto da Marina — sem explicação prévia; o objetivo é criar expectativa que sustente a barriga técnica dos blocos do meio, não apenas contextualizar
- [x] 4.4 Ajustar a seção de erros comuns do Bloco 1 para refletir que o exercício cobre `items` e `reviews` (não todas as tabelas novamente)

## 5. Notas de aula — adicionar script do cliffhanger

- [x] 5.1 Em `materiais/notas_aula.md`, na seção "Bloco 4 — Perguntas Analíticas", adicionar subseção "Salvamento em paralelo durante revisão entre pares" com a instrução exata e o texto a falar: "Enquanto vocês revisam as perguntas do colega, rodem esta célula — ela salva os dados limpos que vão precisar amanhã"
- [x] 5.2 Adicionar subseção "Cliffhanger — seleção da pergunta" com: critério de seleção (pergunta sobre nota × variável com correlação clara), pergunta-padrão de reserva ("Em quais categorias a nota média está abaixo da mediana geral, e isso tem relação com o tempo de entrega?"), e instrução para identificar a pergunta durante a revisão entre pares
- [x] 5.3 Adicionar subseção "Cliffhanger — condução ao vivo" com a sequência de 5 passos: (1) anunciar a pergunta selecionada, (2) fazer groupby ao vivo e mostrar correlação, (3) pausar e perguntar "isso prova que X causa Y?", (4) não responder, (5) encerrar com "isso tem um nome — amanhã a gente enfrenta"
- [x] 5.4 Adicionar nota explícita: "Não ceder à pressão da sala — a abertura é intencional. Se alguém insistir, dizer: 'Deixar sem resposta é proposital. Boa análise de dados levanta mais perguntas do que resolve. Amanhã vocês vão entender por quê.'"
