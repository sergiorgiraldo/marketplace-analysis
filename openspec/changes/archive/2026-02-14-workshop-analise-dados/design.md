## Context

O Workshop de Análise de Dados é um evento de 2 dias (~4h/dia) que funciona como topo de funil para os cursos CDO e Zero a Analista. O público-alvo são pessoas em transição de carreira ou início na área de dados que já viram tutoriais mas não conseguem fazer uma análise real sozinhas. O workshop precisa entregar valor genuíno (uma análise completa no portfólio) ao mesmo tempo que demonstra a profundidade do método de ensino, gerando demanda qualificada para os cursos pagos.

O conteúdo é ministrado ao vivo pelo Caio, com demonstrações em tempo real e acompanhamento dos participantes via notebook compartilhado. Não é um curso gravado; a interação e o diagnóstico ao vivo são parte central da proposta.

## Goals / Non-Goals

**Goals:**
- Participante sai com uma análise exploratória completa, documentada e apresentável
- Exposição ao método real de trabalho de um analista (não o método de tutorial)
- Criar conexão natural com os cursos CDO e Zero a Analista sem transformar o workshop em propaganda
- Dataset com sujeira real que force o participante a tomar decisões (não dados toy)
- Roteiro com tempos definidos para cada bloco, incluindo margens para dúvidas

**Non-Goals:**
- Não vai ensinar programação do zero (Python básico é pré-requisito ou será fornecido notebook guiado)
- Não vai cobrir modelagem preditiva ou machine learning
- Não vai aprofundar estatística inferencial (isso é conteúdo do CDO)
- Não é um curso completo de pandas/matplotlib; as ferramentas são meio, não fim

## Decisions

**1. Dataset: e-commerce brasileiro (Olist adaptado) vs. dataset sintético**

Usar dataset real (baseado no Olist público, com modificações para introduzir problemas realistas). Razão: dataset sintético não gera as surpresas e decisões que um analista enfrenta de verdade. O Olist tem variedade de tipos (datas, categorias, valores monetários, texto), volume adequado (~100k registros) e uma história de negócio compreensível (marketplace). As modificações incluem: introdução de missings não-aleatórios, duplicatas parciais, inconsistências de formato de data, e outliers reais.

Alternativa descartada: criar dataset do zero. Custo alto de preparação e risco de parecer artificial.

**2. Formato de entrega: Jupyter Notebook vs. script Python + relatório separado**

Jupyter Notebook como artefato principal, com documento final em markdown exportado. Razão: notebook permite narrativa + código + output visual no mesmo lugar, que é o formato mais próximo de como analistas reais documentam exploração. O documento final é uma versão limpa (sem código) para "stakeholders".

**3. Nível de pré-requisito: zero absoluto vs. Python básico**

Fornecer notebook com células pré-preenchidas que o participante executa e modifica. Quem sabe Python avança mais rápido; quem não sabe consegue acompanhar executando e alterando parâmetros. Razão: ampliar o público sem nivelar por baixo. O notebook guiado funciona como scaffold.

Alternativa descartada: exigir Python como pré-requisito duro. Reduziria muito o público-alvo de um evento de topo de funil.

**4. Estrutura pedagógica: linear vs. espiral**

Abordagem em espiral com dois passes no dataset. Dia 1: passe exploratório (entender, limpar, perguntar). Dia 2: passe analítico (responder, visualizar, comunicar). Razão: o participante vê o mesmo dado duas vezes com lentes diferentes, o que reforça aprendizado e simula o ciclo real de análise.

**5. Conversão: CTAs explícitos vs. demonstração de profundidade**

Conversão por demonstração, não por pitch. Nos momentos em que o conteúdo toca algo mais profundo (teste de hipótese, modelagem, causalidade), o Caio menciona que isso é parte do CDO/Zero a Analista e mostra brevemente o que seria possível. O CTA formal acontece apenas no encerramento do Dia 2, com oferta exclusiva para participantes do workshop.

## Risks / Trade-offs

[Público muito heterogêneo em nível técnico] → Notebook guiado com células scaffold mitiga parcialmente. Monitores/assistentes no chat ajudam quem trava. Aceitar que haverá dispersão e calibrar expectativa.

[Dataset muito complexo para 2 dias] → Pré-selecionar subconjunto de tabelas do Olist (pedidos, itens, avaliações). Não usar todas as tabelas. Manter scope gerenciável.

[Workshop gratuito/barato atrai público que não converte] → Cobrar valor simbólico (R$47-97) para filtrar. Participantes que pagam, mesmo pouco, têm mais compromisso e convertem melhor.

[Tempo insuficiente para participantes terminarem] → Definir checkpoints claros e versão "mínima viável" da análise. Quem não terminar ao vivo recebe acesso ao material por 7 dias para finalizar.

## Open Questions

- Preço exato do workshop (gratuito vs. R$47 vs. R$97)
- Plataforma de transmissão (Zoom vs. YouTube Live vs. plataforma própria)
- Se haverá certificado de participação (pode ajudar na conversão mas adiciona operação)
- Quantidade de monitores necessários por número de participantes
