---
title: "Roteiro de Aula"
subtitle: "Workshop de Análise de Dados com Python"
author: ""
date: ""
geometry: margin=1.8cm
fontsize: 10pt
mainfont: "Helvetica Neue"
monofont: "Menlo"
linestretch: 1.15
colorlinks: true
---

\thispagestyle{empty}
\begin{center}
{\small\textcolor{demo}{\textbf{[DEMO]}} = demonstração ao vivo \quad \textcolor{exercicio}{\textbf{[EX]}} = alunos trabalham \quad \textcolor{atencao}{\textbf{[!]}} = ponto crítico \quad \textcolor{transicao}{$\rightarrow$} = transição \quad \textcolor{conceito}{\textbf{[CONCEITO]}} = conceito avançado (decidir na hora se entra)}
\end{center}
\vspace{0.5em}

# DIA 1 — Fundamentos e Data Cleaning (4h)

## Abertura | 09:00–09:15

- Apresentação pessoal (2 frases: background + "faço no dia a dia o que vocês vão fazer agora")
- Promessa: "saem com análise real no portfólio, não é simulação"
- \demo{Abrir notebook executado do Dia 2, scrollar vizs e documento final}
- Distribuir glossário + checklist de EDA
- Setup Colab: "executem a primeira célula, levantem a mão quando Setup completo"
- \exercicio{Setup (3–4 min). Monitor resolve travamentos.}
- "Leiam o briefing da Marina. Nunca se começa sem entender o que o stakeholder quer."
- \exercicio{Leitura do briefing (2 min)}
- "Perguntas abertas de propósito. Parte do trabalho é transformar perguntas vagas em respondíveis."

\trans{"Os dados permitem responder o que ela quer? Pra saber, precisamos entender o que tem. Vamos diagnosticar."}

## Bloco 1 — Diagnóstico | 09:15–09:45

- "99 mil pedidos, marketplace brasileiro, NPS caindo, Marina precisa de diagnóstico"
- Pausa. Deixar pousar.
- "Nunca confie num dataset sem olhar pra dentro dele primeiro."
- \demo{Tabela orders — verbalizar raciocínio (10 min):}
    - shape $\rightarrow$ dtypes $\rightarrow$ head/tail $\rightarrow$ describe (min/max) $\rightarrow$ isnull
- "Diagnóstico antes de ação. Médico não receita sem examinar."
- \exercicio{Alunos fazem em items e reviews (15 min). Circular.}
- Checkpoint: "Quantos problemas acharam? 3? 4? 5?"
- Se não investigaram missings: "Pouco em relação a quê? E se os 6% forem os clientes mais valiosos?"
- \tangencia{MAR — quando perceberem que preço alto = mais missing em review\_score:}
    - "Missings não são aleatórios: pedidos caros têm mais ausência de avaliação"
    - "Dropar = subestimar preço médio. Imputar mediana = diluir efeito."
    - \conceito{Viés de seleção — dropar esses registros cria uma amostra enviesada. Você analisa só quem avaliou, não o marketplace inteiro. Conclusões mudam.}
    - \conceito{MCAR / MAR / MNAR — a taxonomia completa. Aqui é MAR (depende do preço, que a gente observa). Se quem teve experiência ruim simplesmente não avalia, seria MNAR, e aí é pior.}
    - Mencionar CDO (tom informativo, não vendedor)

\trans{"Encontraram os problemas. Vamos começar pelos de estrutura: duplicatas e formatos."}

## Intervalo | 09:45–09:55

## Bloco 2A — Limpeza Estrutural | 09:55–10:25

- \demo{Limpeza de duplicatas no notebook do exercício (8 min):}
    - Identificar $\rightarrow$ Investigar ("timestamps diferentes") $\rightarrow$ Decidir ("manter mais recente") $\rightarrow$ Documentar
    - \conceito{Idempotência — sistemas bem feitos não geram duplicatas. Se gerou, ou o sistema não é idempotente ou tem event sourcing (cada mudança de status vira registro novo). Muda como você decide qual manter.}
- \atencao{"Limpeza sem justificativa não é limpeza, é destruição de dados." (REPETIR)}
- \demo{Datas mistas: "'2017-10-02' e '02/10/2017' no mesmo campo. Sem cuidado, outubro vira fevereiro."}
- \exercicio{Limpam duplicatas e convertem datas (18 min). Circular.}
- Mini-checkpoint: "Duplicatas removidas? Datas convertidas?"

\trans{"Resolveram estrutura. Agora problemas de significado: dados que estão lá mas podem enganar."}

## Bloco 2B — Limpeza Semântica | 10:25–11:00

- \demo{Mostrar missings de review\_score $\times$ preço + um outlier (7 min)}
- "Limpeza vai ser questionada daqui a 6 meses. Se não documentou, vai refazer."
- \exercicio{Missings, outliers, categorias/scaffold (23 min). Circular.}
- \atencao{Maior travamento é aqui (decisão sobre missings). Guiar por consequências:}
    - "Dropar = perder 6% dos pedidos mais caros"
    - "Imputar mediana = assumir que quem não avaliou daria nota mediana"
    - "Manter NaN = preservar tudo, lidar caso a caso"
    - NÃO dar a resposta. "Qual consequência você aceita?"
- Se fillna(0): "Zero não é sem avaliação. Puxa todas as médias pra baixo."
    - \conceito{Suporte da distribuição — review\_score vai de 1 a 5. Colocar 0 introduz um valor que não existe na escala original. Muda a distribuição inteira, não só a média.}
- \tangencia{Outliers:}
    - "B2B misturado com B2C. Cortar 5% da receita ou descobrir segmento novo?"
    - "Flag em vez de remover = opção mais segura"
    - \conceito{Mistura de distribuições — os dados vêm de dois processos geradores diferentes (B2C e B2B). Tratar como uma distribuição só é modelar errado. Separar as populações antes de analisar.}
    - \conceito{Estatística robusta — média é sensível a outliers, mediana não. Se o público perguntar qual usar: mediana pra resumir, média só se filtrar outliers antes. Winsorização é o meio-termo.}
- Checkpoint final

\trans{"Dados limpos o suficiente. Hora de gerar intuição, procurar as perguntas certas."}

## Intervalo | 11:00–11:10

## Bloco 3 — Exploração Visual | 11:10–11:40

- \demo{Interpretar distribuição bimodal de review\_score (5 min):}
    - "Maioria é 5, depois 4, depois 1. Quase ninguém 2 ou 3. Média engana — bimodal."
    - "Dois picos = dois grupos. Quem são os do pico da esquerda?"
    - \conceito{Subpopulações latentes — bimodal = provavelmente duas populações misturadas. Formalmente é um mixture model. A pergunta prática: qual variável separa os dois grupos? Atraso? Categoria? Região?}
- \exercicio{Executam vizs com scaffold, documentam observações (20 min). Circular.}
- Ao circular, pra cada tipo:
    - Bimodal: "Quem são os dois grupos?"
    - Assimétrica: "Cauda longa, mediana melhor como centro"
        - \conceito{Log-transform — distribuições de preço/receita geralmente ficam normais em log. Se alguém perguntar "como lidar com a cauda", log é a resposta padrão.}
    - Tendência: "Picos coincidem com datas comerciais?"
- Se muitos gráficos sem interpretação: "Pra cada viz, escreva uma frase. Se não consegue, o gráfico não serviu."
- Checkpoint

\trans{"Observações prontas. Transformar em perguntas de negócio que a Marina consegue usar."}

## Intervalo | 11:40–11:50

## Bloco 4 — Perguntas + Cliffhanger | 11:50–13:00

### Demo: perguntas analíticas (10 min)

- Transformar observação em pergunta na frente deles:
    - Vaga: "Os dados são bons?"
    - Melhor: "A satisfação é boa?"
    - Específica: "Em quais categorias nota abaixo de 3.5, com 100+ avaliações?"
- 3 critérios: **respondível** (com estes dados), **acionável** (Marina muda algo), **específica** (sabe qual coluna)
- Ruim: "O frete causa insatisfação?" $\rightarrow$ "causa" é causal
    - \conceito{Linguagem causal vs associativa (Pearl) — "causa", "impacta", "gera" são termos causais. EDA só sustenta "está associado a", "correlaciona com". A escada da causalidade: associação $\rightarrow$ intervenção $\rightarrow$ contrafactual.}
- Bom: "Nota média por faixa de frete, diferença entre mais barata e mais cara?"

### Exercício + Revisão (40 min)

- \exercicio{Formulam 3+ perguntas, incluindo 1 não-respondível por EDA (20 min)}
- \atencao{Ao iniciar revisão: "Rodem esta célula — salva dados limpos pra amanhã. No Colab baixa automaticamente. Não pulem."}
- \exercicio{Revisão entre pares (20 min). Circular, identificar melhor pergunta pro cliffhanger.}
- Se dupla concordando sem fricção: "Estão sendo gentis demais. Onde pode falhar?"
- Discussão grupo: 2–3 duplas compartilham

### Cliffhanger (10–15 min)

- "Deixa eu pegar uma pergunta que me chamou atenção..." (parecer espontâneo)
- \atencao{Se não achou boa, usar reserva: "categorias com nota abaixo da mediana $\times$ tempo de entrega"}
- \demo{Abrir notebook, groupby ao vivo, verbalizar enquanto digita}
- Resultado aparece. Correlação clara.
- \atencao{Parar. Silêncio 2–3 segundos. Olhar pra sala.}
- **"Isso prova que X causa Y?"**
- Não responder.
- **"Isso tem um nome. Amanhã a gente enfrenta."**
- Fechar notebook. Encerrar.
- Se insistirem: "Deixar sem resposta é proposital. Boa análise levanta mais perguntas do que resolve."

\newpage

# DIA 2 — Análise e Comunicação (4h)

## Abertura + Demo Margem de Erro | 09:00–09:20

- Recap: \textasciitilde{}100k pedidos, 5 problemas, decisões documentadas, bimodal, correlação
- "Ficou uma pergunta no ar ontem sobre correlação e causalidade. Vamos voltar nela."
- Upload CSVs limpos no Colab. "Se perderam, notebook carrega versão pronta."
- \demo{Groupby ao vivo: ranking por média. "Parece claro, certo?"}
- \atencao{Votação: "Levantem a mão quem acha que audio é pior que a média geral."}
- \demo{Executar célula de IC. Barras de erro. Ranking colapsa.}
- \atencao{"Vocês votaram num ranking que não existe."}
- Analogia: "Margem de erro como pesquisa eleitoral."
- \atencao{Frase-âncora: "Média sem margem de erro é opinião, não é evidência."}
- "Guardem isso. Tudo que fizerem hoje: qual o n?"
- \conceito{Intervalo de confiança / erro padrão — margem encolhe com raiz de n. De 50 pra 5000 avaliações, margem cai 10x.}

\trans{"Vocês viram o que a margem de erro faz com um ranking. Agora vamos responder as perguntas da Marina."}

## Bloco 1 — Análise Estatística | 09:20–10:20

- \demo{groupby + agg ao vivo (15 min):}
    - "Nota média por categoria. Mas média sozinha engana, preciso de volume."
    - Resultado: "Nota 1.5, incrível. Mas volume: 3 avaliações. Não dá."
    - \atencao{Volume mínimo: "Menos de 100 avaliações, não tiro conclusão."}
    - \conceito{Lei dos grandes números / variância amostral — com 5 avaliações a média oscila absurdamente. Com 100, estabiliza. O "30" da estatística clássica assume normalidade; avaliações 1-5 são tudo menos normais. Por isso 100.}
    - Filtrar: "Agora sim, as 10 piores têm volume suficiente."
- \exercicio{3 análises: categoria, atraso $\times$ satisfação, sazonalidade (40 min). Circular.}
- Resultados esperados pra orientar circulação:
    - Categoria: eletrônicos/telefonia piores, approx 1 ponto diferença
        - \conceito{Significância prática vs estatística — 1 ponto numa escala de 1-5 é enorme (20\% da escala). Com 100k pedidos quase tudo é estatisticamente significativo. A pergunta que importa: o efeito é grande o suficiente pra justificar ação?}
    - Atraso: correlação approx -0.3, no prazo approx 4.3, atraso >14d approx 2.0
    - Sazonalidade: volume cresce 2017–18, picos novembro
- \tangencia{Causalidade (na correlação -0.3):}
    - "Correlação não é causalidade. Regiões distantes: mais atraso E mais insatisfação."
    - \conceito{Variável confundidora / DAGs — distância geográfica confunde a relação atraso-nota. Num DAG: distância $\rightarrow$ atraso e distância $\rightarrow$ insatisfação. Sem controlar distância, o efeito do atraso está inflado.}
    - \conceito{Simpson's paradox — a satisfação geral pode ser estável enquanto piora nas categorias que crescem. A composição do mix muda o agregado. Sempre desagregar antes de concluir.}
    - "Pra Marina, evidência útil. Se diretoria perguntar: temos evidência consistente, não certeza."
- Checkpoint

\trans{"Têm os números. Comunicar de forma que Marina apresente sem vocês do lado."}

## Intervalo | 10:20–10:30

## Bloco 2 — Visualizações Finais | 10:30–11:30

- \demo{Transformar gráfico exploratório em gráfico de apresentação (10 min):}
    1. Histograma $\rightarrow$ barras horizontais top 5 + bottom 5
    2. Título: "Categorias com Melhor e Pior Satisfação" (não "Nota por Categoria")
    3. Eixos com unidades
    4. Linha de referência (média geral)
    5. Anotar insight
- "Exploratório é pra vocês. Final é pra quem não viu os dados."
- \exercicio{4 vizs: categoria, atraso, temporal, heatmap/scaffold (45 min). Circular.}
- Viz 4 (heatmap): cruza dimensões que viram separadas — verificar se entenderam
    - \conceito{Efeito de interação — o impacto do atraso na nota pode ser diferente por categoria. Eletrônicos com atraso = desastre. Decoração com atraso = tolerável. O heatmap mostra isso. Sem cruzar, você perde a interação.}
- Ao circular: Título = insight? Eixos com unidades? Eixo Y do zero? Anotação?
    - \conceito{Lie factor (Tufte) — eixo Y cortado exagera diferenças. Barras que começam em 3.5 fazem 0.5 ponto parecer abismo. A razão entre o efeito visual e o efeito real nos dados deveria ser 1:1.}
- Se cores aleatórias: "Mensagem é boas vs. ruins. Vermelho piores, verde melhores."
- Checkpoint

\trans{"Gráficos sem contexto são decoração. Resumo executivo é o que a diretoria lê."}

## Intervalo | 11:30–11:40

## Bloco 3 — Storytelling | 11:40–12:25

- \demo{Estrutura: contexto $\rightarrow$ problema $\rightarrow$ descoberta $\rightarrow$ recomendação (10 min)}
- \demo{Escrever resumo executivo ao vivo:}
    - Contexto (99k, período) $\rightarrow$ padrão (concentrado) $\rightarrow$ quantificar (2.5 pts, 22% receita) $\rightarrow$ ação
- "Diretoria decide algo com esse parágrafo sem olhar gráfico."
- "Limitações = honestidade intelectual. Diretoria confia mais."
- Limitações: correlação $\neq$ causalidade, MAR, período 2017–18, sem controle região/peso
    - \conceito{Validade externa — dados de 2017-18 podem não representar o marketplace de hoje. Mudou o mix de categorias? Mudou a logística? A conclusão é válida pra aquele período, extrapolar é premissa, não fato.}
- \exercicio{Preenchem documento de análise (35 min). Circular.}
- Se resumo = lista de gráficos: "Não é resumo, é legenda."
- Se recomendação genérica: "'Melhorar logística' não é acionável."
- Perguntar se preencheram limitações

\trans{"Empacotar num documento que se sustenta sozinho."}

## Bloco 4 — Documento Final | 12:25–12:45

- "Executem célula de exportação."
- \exercicio{Exportam HTML, autoavaliam (20 min):}
    - Resumo sem gráficos? 3+ descobertas? Recomendações com evidência? Limitações? Títulos/labels?
    - "4 de 5 = no nível. Menos = completem agora."
- Mostrar 2–3 docs de participantes. Destacar o que ficou bom.

## CTA | 12:45–13:00

- "Fizeram em 2 dias o que muita gente com dados não sabe. Não é pouco."
- "Esse documento já é melhor que maioria dos relatórios que vejo em empresas."
- Pausa.
- "Mas quero ser honesto. Lembram correlação $\neq$ causalidade?"
- "Se Marina perguntar 'reduzo prazo em 2 dias, quanto a nota sobe?' — conseguem responder?"
- Pausa. "Não. Tudo bem. Pra isso: inferência causal, modelagem, experimentação."
- \demo{Mostrar roadmap visual}
- "Diferença entre quem faz gráfico e quem toma decisão: degraus seguintes."
- Oferta: CDO 20% off (R\$3.200), Zero a Analista 15% off, 72h, link por email
- "Não vou repetir. Se fizer sentido, ótimo. Se não, workshop já valeu."
- "Material acessível por 7 dias. Obrigado, pessoal."
