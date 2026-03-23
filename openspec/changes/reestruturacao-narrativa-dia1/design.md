## Context

O Dia 1 atual tem dois problemas estruturais identificados na proposal: carga cognitiva dupla no Bloco 1 (dois datasets) e encerramento fraco no Bloco 4 (logística de salvamento). A mudança toca três artefatos: roteiro de tempos, notas de aula e o notebook do aluno.

O princípio do workshop — início e fim fortes por efeito primacy/recency — é a restrição que guia todas as decisões. O encerramento atual (salvar arquivos, checkpoint, preview do Dia 2) é o pior tipo de final: utilitário e sem energia.

## Goals / Non-Goals

**Goals:**
- Bloco 1 começa direto no Olist, sem segundo dataset
- Bloco 1 cabe em ~30 min sem cortar conteúdo essencial
- Os 10 min finais do Dia 1 são pedagógicos e emocionalmente fortes (cliffhanger)
- Salvar arquivos acontece sem tomar tempo próprio (paralelo à revisão entre pares)
- Mudanças são cirúrgicas: apenas o que a proposal especifica

**Non-Goals:**
- Não reescrever o Bloco 2 ou qualquer outro bloco
- Não mudar o dataset ou os 5 problemas injetados
- Não alterar a estrutura do Dia 2
- Não criar material novo além do script do cliffhanger

## Decisions

**Qual tabela usar na demo do Bloco 1**

Usar `orders` — a tabela mais intuitiva (pedidos com status, datas, preços). A demo faz o mesmo raciocínio verbal que hoje usa iris/tips: shape, dtypes, head/tail, describe, isnull. A diferença é que o contexto é imediatamente reconhecível ("isso é um pedido de marketplace") e elimina a transição mental entre datasets.

Alternativa descartada: usar a tabela completa já no começo. O risco é mostrar problemas que só serão tratados nos Blocos 2A/2B antes de o aluno saber o que fazer com eles, criando ansiedade e perguntas fora de hora.

**Como redistribuir os 15 min liberados no Bloco 1**

Demo: de 15 min para ~10 min (o raciocínio verbal é o mesmo, mas sem a overhead de "vou mostrar com um dataset diferente primeiro"). Exercício: de 25 min para 15 min — os alunos trabalham em `items` e `reviews` em vez de repetir o que o instrutor acabou de fazer em `orders`. Checkpoint: mantido em 5 min. Total: 30 min.

Os 15 min liberados vão para: +5 min na revisão entre pares (Bloco 4), +10 min para o cliffhanger.

**Estrutura do cliffhanger**

A sequência é: seleção da melhor pergunta → EDA parcial ao vivo → revelação da ambiguidade → parada deliberada.

O que não pode acontecer: o instrutor resolver a pergunta. A parada deve parecer natural, não forçada. O mecanismo é a correlação vs. causalidade: qualquer análise de satisfação/nota vai chegar num ponto onde "X está correlacionado com nota baixa" não responde "X causa nota baixa?". Esse é o cliff.

A pergunta ideal para o cliffhanger é sobre atraso de entrega e nota (a mais óbvia dos dados). O instrutor faz o groupby, mostra a correlação clara, e então: "Isso prova que atraso causa insatisfação?" — e não responde. "Isso tem um nome. Amanhã a gente enfrenta."

Alternativa descartada: usar uma pergunta formulada pelos alunos no momento. Risco muito alto de a pergunta não ser analítica o suficiente, ou ninguém sugerir algo bom. O instrutor seleciona a melhor pergunta do exercício do Bloco 4 durante a revisão entre pares, o que dá controle sobre o que vai aparecer.

**Onde encaixar o salvamento dos arquivos**

Durante a revisão entre pares (Bloco 4), enquanto os alunos trocam perguntas analíticas com o colega, o instrutor pede que deixem rodando a célula de save em paralelo. "Enquanto vocês fazem a revisão, rodem essa célula — ela vai salvar e disponibilizar os CSVs limpos. No Colab vai aparecer um link de download; no local vai salvar na pasta `data/prepared/`."

A célula de save (Cell 61 no notebook) não precisa mudar — só precisa de instrução no roteiro para ser executada nesse momento, e não no encerramento.

## Risks / Trade-offs

**Cliffhanger depende de o instrutor ter escolhido a pergunta certa durante a revisão entre pares** → Mitigação: o script das notas de aula especifica qual tipo de pergunta procurar (algo sobre nota + outra variável). Se ninguém formular algo adequado, o instrutor tem uma pergunta-padrão de reserva.

**Alguns alunos podem ficar irritados por "não ter sido resolvido"** → Esse é exatamente o efeito desejado. O risco real é o instrutor ceder à pressão e resolver. Mitigação: o script das notas deve incluir a frase de encerramento que normaliza a abertura ("deixar sem resposta é proposital — análise de dados bem feita levanta mais perguntas do que resolve").

**Reduzir o exercício do Bloco 1 de 25 para 15 min pode deixar alunos mais lentos para trás** → Com `items` e `reviews` como foco do exercício (em vez de repetir o diagnóstico completo em todas as tabelas), o escopo é menor, o que compensa. O instrutor ainda circula. Alunos que não terminam passam para o Bloco 2 com o diagnóstico parcial — não quebra o fluxo.

**Salvar arquivos em paralelo pode ser esquecido** → Mitigação: a célula de save fica visível no notebook com instrução textual clara ("Execute esta célula durante a revisão entre pares"). O roteiro deve ter uma nota explícita para o instrutor lembrar de mencionar isso antes de começar a revisão.

## Migration Plan

1. **roteiro_instrutor.md**: Atualizar tabela de tempos do Bloco 1 (45 → 30 min, com redistribuição interna) e do Bloco 4 (encerramento de logística → revisão entre pares expandida + cliffhanger). Ajustar horários cascata: se Bloco 1 termina às 09:45 em vez de 10:00, o intervalo e os blocos seguintes adiantam 15 min.
2. **notas_aula.md**: Substituir texto do Bloco 1 (remover menção a iris/tips, descrever nova demo diretamente em `orders`). Adicionar script do cliffhanger ao final do Bloco 4: como selecionar a pergunta, a sequência de EDA ao vivo, as frases exatas de parada.
3. **dia1_fundamentos_cleaning.ipynb**: Remover células de demo com iris/tips (identificar por conteúdo, não por índice — os índices mudam). Mover instrução de save para dentro do bloco de revisão entre pares, com texto de instrução atualizado.

Rollback: o notebook e os materiais são texto/JSON. Qualquer mudança é reversível via git. Não há dados, pipelines ou scripts afetados.

## Open Questions

- Deve existir uma pergunta-padrão de reserva para o cliffhanger escrita nas notas? (Recomendado: sim, com o exemplo de atraso × nota já pré-computado para o instrutor mostrar se necessário.)
- O roteiro deve indicar explicitamente ao instrutor que deve "caçar" a pergunta ideal durante a revisão entre pares, ou isso fica implícito na sequência? (Recomendado: explícito, com critério — "uma pergunta que envolva dois campos numéricos ou uma variável de grupo + nota".)
