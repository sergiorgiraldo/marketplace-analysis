---
title: "Briefing: Análise do Marketplace"
subtitle: "Workshop de Análise de Dados com Python"
author: ""
date: ""
geometry: margin=2.5cm
fontsize: 12pt
mainfont: "Helvetica Neue"
monofont: "Menlo"
linestretch: 1.3
colorlinks: true
linkcolor: NavyBlue
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\small Workshop de Análise de Dados}
  - \fancyhead[R]{\small Briefing}
  - \fancyfoot[C]{}
  - \usepackage{xcolor}
  - \definecolor{accentblue}{HTML}{2563EB}
  - \usepackage{tcolorbox}
  - \newtcolorbox{briefingbox}{colback=gray!5, colframe=gray!40, boxrule=0.5pt, arc=3pt, left=10pt, right=10pt, top=8pt, bottom=8pt}
---

\begin{center}
\textbf{\Large De:} Marina Silva, Gerente de Operações\\[4pt]
\textbf{\Large Para:} Time de Dados\\[4pt]
\textbf{\Large Assunto:} Diagnóstico de satisfação dos clientes do marketplace
\end{center}

\vspace{1em}
\noindent\rule{\textwidth}{0.4pt}
\vspace{1em}

Pessoal,

Nos últimos meses percebemos uma queda no NPS do marketplace, mas os números agregados não estão nos ajudando a entender o que está por trás disso. Preciso que vocês mergulhem nos dados de pedidos, itens e avaliações para responder algumas perguntas que estão travando decisões aqui.

## O que preciso de vocês

### 1. Satisfação por categoria

Existem categorias de produto onde a insatisfação é sistematicamente pior? Precisamos saber se o problema é generalizado ou concentrado em segmentos específicos. Se for concentrado, quero entender o tamanho de cada segmento (volume de vendas e receita) para priorizar onde atacar primeiro.

### 2. Relação entre frete/entrega e satisfação

A hipótese da equipe de logística é que pedidos com frete caro ou entrega atrasada geram mais avaliações negativas. Quero evidência. Consigam olhar para a relação entre valor de frete, tempo de entrega (estimado vs. real) e nota de avaliação.

### 3. Sazonalidade e tendência

Nosso volume de vendas tem sazonalidade? As notas de avaliação pioram em períodos de pico (Black Friday, Natal)? Precisamos saber se devemos ajustar a operação em datas específicas ou se o problema é estrutural.

## Restrições

- Preciso de algo **visual** que eu consiga mostrar para a diretoria na próxima reunião.
- **Não** preciso de modelo preditivo agora, preciso de **diagnóstico**.
- Se encontrarem algo inesperado nos dados (inconsistências, padrões estranhos), **documentem**. Eu quero saber.

\vspace{2em}

Conto com vocês. Temos uma semana.

\vspace{1em}

\noindent\textbf{Marina}
