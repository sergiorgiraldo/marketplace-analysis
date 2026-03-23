---
title: "Checklist de Análise Exploratória de Dados"
subtitle: "Workshop de Análise de Dados com Python"
author: ""
date: ""
geometry: margin=2cm
fontsize: 11pt
mainfont: "Helvetica Neue"
monofont: "Menlo"
linestretch: 1.2
colorlinks: true
header-includes:
  - \usepackage{fancyhdr}
  - \pagestyle{fancy}
  - \fancyhead[L]{\small Workshop de Análise de Dados}
  - \fancyhead[R]{\small Checklist EDA}
  - \fancyfoot[C]{}
  - \usepackage{amssymb}
  - \usepackage{enumitem}
  - \newcommand{\checkbox}{$\square$\hspace{6pt}}
---

\begin{center}
\textit{Use este checklist em qualquer análise nova. Cada etapa tem perguntas-guia para não esquecer nada.\\Consulte o glossário para explicação dos termos técnicos.}
\end{center}

\vspace{0.5em}

## 1. Diagnóstico

\checkbox Carregar dados e verificar shape (linhas x colunas)

\checkbox Examinar tipos de cada coluna (dtypes) --- algum tipo parece errado?

\checkbox Olhar primeiras e últimas linhas (head/tail) para ver formato real

\checkbox Contar valores ausentes por coluna --- qual \% de missings?

\checkbox Verificar se os missings são aleatórios ou seguem padrão

\checkbox Procurar duplicatas (exatas e parciais por chave)

\checkbox Checar estatísticas descritivas (describe) --- min/max fazem sentido?

\checkbox Listar valores únicos de colunas categóricas

**Perguntas-guia:** O dataset tem o tamanho esperado? Alguma coluna deveria ser numérica mas está como texto? Existem missings que parecem depender de outra variável?

## 2. Limpeza

\checkbox Tratar duplicatas (decidir qual manter, documentar critério)

\checkbox Padronizar formatos (datas, categorias, strings)

\checkbox Decidir sobre missings: dropar, imputar ou manter? Documentar por quê

\checkbox Identificar outliers --- são erros ou dados legítimos?

\checkbox Se outliers legítimos: criar flag ou segmentar

\checkbox Converter tipos quando necessário (strings para datas, etc.)

\checkbox Validar que a limpeza não removeu dados demais

**Perguntas-guia:** A decisão sobre cada problema está documentada com justificativa? A limpeza alterou significativamente a distribuição dos dados?

## 3. Exploração Univariada

\checkbox Distribuição de cada variável numérica (histogramas)

\checkbox Contagem de cada variável categórica (barplots)

\checkbox Identificar assimetrias, bimodalidade, concentrações

\checkbox Série temporal se houver componente de tempo

**Perguntas-guia:** Alguma distribuição surpreende? Alguma variável é dominada por um único valor?

## 4. Exploração Bivariada

\checkbox Scatter plots para pares de variáveis numéricas

\checkbox Boxplots de variáveis numéricas por categorias

\checkbox Correlações entre variáveis numéricas

\checkbox Crosstabs entre variáveis categóricas

**Perguntas-guia:** Existem relações fortes entre variáveis? Alguma correlação é inesperada?

## 5. Formulação de Perguntas

\checkbox Formular perguntas que sejam respondíveis com os dados

\checkbox Cada pergunta é acionável? (a resposta muda uma decisão?)

\checkbox Cada pergunta é específica? (vira uma análise concreta?)

\checkbox Priorizar por impacto x viabilidade

## 6. Análise Direcionada

\checkbox Para cada pergunta: calcular métrica principal

\checkbox Segmentar por grupos relevantes

\checkbox Documentar interpretação numérica

## 7. Visualização Final

\checkbox Cada gráfico tem título descritivo (diz o insight, não só o eixo)

\checkbox Eixos rotulados com unidades

\checkbox Anotação com insight principal

\checkbox Gráficos salvos em alta resolução (dpi $\geq$ 150)

## 8. Comunicação

\checkbox Resumo executivo (compreensível sem ver gráficos)

\checkbox Estrutura: Contexto + Descobertas + Recomendações

\checkbox Limitações documentadas

\checkbox Próximos passos sugeridos
