# Roteiro do Instrutor - Workshop de Análise de Dados

## Dia 1: Fundamentos e Data Cleaning (4h)

### Abertura (15 min) | 09:00-09:15
- Apresentação pessoal (2 min): background rápido, por que isso importa
- Promessa do workshop: "Vocês saem daqui com uma análise real no portfólio"
- Mostrar o produto final (notebook executado do Dia 2) - isso é o que vocês vão construir
- Distribuir glossário (`glossario_python.md`) + checklist de EDA junto com o notebook
- **Setup técnico via Colab (instrução principal):** pedir que abram o link do notebook no Google Colab e executem a primeira célula de setup. O Colab instala dependências e baixa os dados automaticamente.
- **Fallback local:** para quem preferir ambiente local, verificar que ativaram o venv e que o Jupyter abre normalmente. Os notebooks funcionam nos dois modos.

### Bloco 1: Diagnóstico do Dataset (30 min) | 09:15-09:45

**Demonstração ao vivo (10 min):**
- Abrir diretamente o dataset Olist — tabela `orders`
- Mostrar o fluxo mental: "Primeiro eu olho o shape... depois os tipos... depois os missings..."
- Verbalizar as perguntas que surgem: "Hmm, por que essa coluna está como object?"

**Exercício dos participantes (15 min):**
- Participantes executam o notebook guiado nas tabelas `items` e `reviews`
- Circular, responder dúvidas, ajudar quem travou no setup

**Checkpoint (5 min):**
- Pedir que executem a célula de checkpoint
- Quick poll: "Quantos problemas vocês encontraram? 3? 4? 5?"

**[TANGENCIAMENTO 1]** Durante a investigação de missings MAR:
> "Notem que os missings aqui não são aleatórios: pedidos caros têm mais ausência de avaliação. Isso é o que em estatística chamamos de Missing At Random, e tratar isso errado pode distorcer completamente uma análise. No CDO a gente dedica uma aula inteira a isso, porque a decisão de dropar vs. imputar é uma das que mais impacto tem no resultado final."

### Intervalo (10 min) | 09:45-09:55

### Bloco 2A: Limpeza Estrutural (30 min) | 09:55-10:25

**Demonstração ao vivo (8 min):**
- Mostrar o processo de limpeza de duplicatas: "Eu sempre verifico se são duplicatas exatas ou parciais"
- Demonstrar a conversão de datas com formato misto
- Enfatizar: "Limpeza sem justificativa não é limpeza, é destruição de dados"

**Exercício dos participantes (18 min):**
- Participantes limpam duplicatas e convertem datas
- Circular ajudando quem não entendeu a diferença entre duplicata exata e parcial

**Mini-checkpoint (4 min):**
- Executar célula de mini-checkpoint
- "Duplicatas removidas? Datas convertidas? Se sim, vamos para a próxima etapa."

**Transição 2A → 2B:**
> "Vocês resolveram os problemas de estrutura: registros duplicados e datas inconsistentes. Agora vamos para os problemas de significado: dados que estão lá mas podem enganar."

### Bloco 2B: Limpeza Semântica (35 min) | 10:25-11:00

**Demonstração ao vivo (7 min):**
- Mostrar que os missings em review_score dependem do preço (MAR)
- Mostrar um exemplo de outlier e perguntar: "Isso é erro ou dado legítimo?"

**Exercício dos participantes (23 min):**
- Participantes tratam missings e outliers. Categorias agora são scaffold: o aluno executa o código de padronização e interpreta, sem investigar typos manualmente
- Circular focando nos que travam na decisão "dropar ou não dropar"

**Checkpoint final (5 min)**

**[TANGENCIAMENTO 2]** Na discussão sobre outliers:
> "Decidir o que é outlier vs. dado legítimo é uma decisão que depende do contexto de negócio. Esses preços extremos podem ser B2B misturado com B2C. No mundo real, isso é a diferença entre cortar 5% da receita ou descobrir um segmento novo. Modelagem preditiva sofre muito com outliers tratados errado, e a gente cobre isso em profundidade na formação."

### Intervalo (10 min) | 11:00-11:10

### Bloco 3: Análise Exploratória Inicial (30 min) | 11:10-11:40

**Demonstração ao vivo (5 min):**
- Interpretar a distribuição bimodal de review_score ao vivo: "Dois picos, 1 e 5. A média engana."
- Foco na leitura do gráfico, não na construção (os participantes já sabem plt.hist)

**Exercício dos participantes (20 min):**
- Participantes executam as visualizações (scaffold mais completo) e documentam observações
- Foco em interpretação: "O que esse gráfico te diz?" em vez de "Complete o código"

**Checkpoint (5 min)**

### Intervalo (10 min) | 11:40-11:50

### Bloco 4: Perguntas Analíticas e Encerramento (70 min) | 11:50-13:00

**Demonstração ao vivo (10 min):**
- Formular uma pergunta ao vivo usando as observações
- Mostrar a diferença entre pergunta vaga ("os dados são bons?") e pergunta analítica ("em quais categorias a nota média está abaixo da mediana geral?")

**Exercício de formulação (20 min):**
- Formular 3+ perguntas, preencher tabela de priorização
- Incluir o desafio "pergunta não-respondível por EDA" (antes era opcional, agora é parte do fluxo)

**Revisão entre pares + discussão em grupo (20 min):**
- Trocar perguntas com um colega, avaliar usando os 3 critérios (respondível, acionável, específica)
- **Ao iniciar a revisão:** pedir que os participantes executem a célula de salvamento em paralelo — "Enquanto vocês revisam as perguntas do colega, rodem esta célula — ela salva os dados limpos que vão precisar amanhã. No Colab ela vai baixar os arquivos automaticamente."
- **Durante a revisão:** identificar a melhor pergunta para o cliffhanger — buscar uma que envolva nota + outra variável com correlação evidente nos dados (ex: nota × atraso de entrega). Se nenhuma for adequada, usar a pergunta de reserva nas notas de aula.
- Discussão em grupo: 2-3 compartilham suas perguntas e o feedback recebido

**Cliffhanger — Encerramento do Dia 1 (10-15 min):**
1. Anunciar a pergunta selecionada para a sala: "Deixa eu pegar a melhor pergunta que vi aqui..."
2. Abrir o notebook e fazer o groupby ao vivo: mostrar a correlação clara
3. Pausar. Olhar para a sala. Perguntar: "Isso prova que X causa Y?"
4. Não responder.
5. Encerrar: "Isso tem um nome. Amanhã a gente enfrenta."

> **Nota:** Não ceder à pressão da sala por resposta. A abertura é deliberada. Se alguém insistir: "Deixar sem resposta é proposital. Boa análise levanta mais perguntas do que resolve. Amanhã vocês entendem por quê."

---

## Dia 2: Análise e Comunicação (~4h)

### Abertura Dia 2 + Demo Margem de Erro (20 min) | 09:00-09:20

**Recap (5 min):**
- Recap rápido do Dia 1
- Sobre o cliffhanger: "Ficou uma pergunta no ar ontem sobre correlação e causalidade. Vamos voltar nela quando analisarmos atraso vs nota."
- **Carregar dados limpos:** no Colab, o notebook pede upload dos CSVs que baixaram ontem. Se alguém perdeu, há fallback automático para versões pré-limpas.

**Demo de IC (10 min):**
- Abrir notebook de solução projetado na tela
- Fazer groupby rápido: ranking de satisfação por categoria (só médias)
- "Parece claro, certo? office_furniture é a pior, books_general_interest é a melhor."
- **Votação:** "Levantem a mão quem acha que audio é significativamente pior que a média geral."
- Executar célula de IC: barras de erro aparecem. Ranking colapsa.
- Silêncio 3-4 segundos.
- "Vocês votaram num ranking que não existe."
- Analogia: margem de erro como pesquisa eleitoral
- Frase-âncora: **"Média sem margem de erro é opinião, não é evidência."**

**Reframe (5 min):**
- "Pra agora, vamos com o filtro de 100. Suficiente pro briefing da Marina."
- "Mas guardem esse gráfico. Tudo que fizerem hoje: qual o n?"
- Objetivo do dia: "Hoje vocês respondem as perguntas e montam o relatório"

### Bloco 1: Análise Estatística Aplicada (60 min) | 09:20-10:20

**Demonstração ao vivo (15 min):**
- Mostrar como responder uma pergunta com groupby + agg
- Demonstrar análise de satisfação por categoria com volume mínimo
- "Nunca tire conclusão de categoria com 5 avaliações"

**Exercício dos participantes (40 min):**
- 3 análises: por categoria, atraso vs satisfação, sazonalidade

**Checkpoint (5 min)**

**[TANGENCIAMENTO 4]** Na análise de correlação atraso vs. nota:
> "A correlação aqui é -0.3, que é moderada. Mas cuidado: correlação não é causalidade. Pode ser que regiões distantes tenham mais atraso E mais insatisfação por outros motivos. Para separar o efeito do atraso dos confundidores geográficos, precisaríamos de regressão controlada ou matching. É o tipo de pergunta que a gente ataca no módulo de inferência causal."

### Intervalo (10 min) | 10:20-10:30

### Bloco 2: Visualizações Interpretativas (60 min) | 10:30-11:30

**Demonstração ao vivo (10 min):**
- Criar uma visualização final ao vivo com título, labels e anotação
- Mostrar a diferença entre "gráfico exploratório" (para mim) e "gráfico final" (para stakeholder)

**Exercício dos participantes (45 min):**
- 4 visualizações: categoria, atraso, temporal, heatmap guiado
- A Viz 4 (heatmap) tem scaffold de ~60%: o código está pronto, o aluno executa, interpreta e opcionalmente ajusta parâmetros visuais. Introduz pivot_table e sns.heatmap.

**Checkpoint (5 min)**

### Intervalo (10 min) | 11:30-11:40

### Bloco 3: Storytelling com Dados (45 min) | 11:40-12:25

**Demonstração ao vivo (10 min):**
- Mostrar a estrutura contexto > problema > descoberta > recomendação
- "O resumo executivo é a parte mais importante: é o que a diretoria lê"
- Escrever um parágrafo de resumo executivo ao vivo

**Exercício dos participantes (35 min):**
- Preencher o documento de análise no notebook

### Bloco 4: Documento Final (20 min) | 12:25-12:45

**Exercício (15 min):**
- Exportar notebook como HTML
- Revisar qualidade do documento final
- Checkpoint final

**Fechamento (5 min):**
- Mostrar os documentos de 2-3 participantes
- Destacar o que ficou bom

### CTA e Encerramento (15 min) | 12:45-13:00

Ver script de encerramento em `materiais/script_cta.md`

---

## Notas para o Instrutor

**Tempo:** Os tempos são orientativos. Se um bloco estiver rendendo, estenda 5-10 min e encurte o próximo. Os 5 min de folga entre 2A e 2B absorvem o mini-checkpoint.

**Tom:** Demonstrações ao vivo são o diferencial. Mostre seus erros, suas dúvidas, seu raciocínio. Não pareça preparado demais.

**Monitores:** Ideal ter 1 monitor a cada 20 participantes no chat para resolver travamentos técnicos sem interromper o fluxo.

**Participantes atrasados:** O notebook guiado com scaffold permite que alguém que perdeu 10 minutos se recupere executando as células anteriores. Os checkpoints servem para saber onde estão.

**Glossário:** Entregar junto com o checklist de EDA no início do workshop. Referir quando surgir termo que confunde participantes ("Quando eu falo DataFrame, é isso aqui: uma tabela. Está no glossário que vocês receberam.").

**Colab como ambiente primário:** A instrução principal é abrir no Colab. O ambiente local funciona, mas o Colab elimina problemas de instalação. Se alguém insistir no local, os notebooks detectam automaticamente e ajustam os caminhos.

**Tempos revisados do Dia 1:**

| Bloco | Tempo | Horário |
|-------|:-----:|:-------:|
| Abertura | 15 min | 09:00-09:15 |
| Bloco 1 (diagnóstico) | 30 min | 09:15-09:45 |
| Intervalo | 10 min | 09:45-09:55 |
| Bloco 2A (limpeza estrutural) | 30 min | 09:55-10:25 |
| Bloco 2B (limpeza semântica) | 35 min | 10:25-11:00 |
| Intervalo | 10 min | 11:00-11:10 |
| Bloco 3 (exploração) | 30 min | 11:10-11:40 |
| Intervalo | 10 min | 11:40-11:50 |
| Bloco 4 (perguntas + encerramento) | 70 min | 11:50-13:00 |
| **Total** | **4h00** | |
