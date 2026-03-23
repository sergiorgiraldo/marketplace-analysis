## 1. Preparação do Dataset

- [x] 1.1 Baixar dataset público do Olist e selecionar tabelas: orders, order_items, reviews
- [x] 1.2 Criar script de preparação que introduz problemas realistas: missings não-aleatórios em avaliações, duplicatas parciais com timestamps diferentes, mix de formatos de data, outliers B2B/B2C, categorias com grafia inconsistente
- [x] 1.3 Validar que o dataset final tem entre 50k-120k registros na tabela principal e que os problemas inseridos são detectáveis mas não triviais
- [x] 1.4 Escrever dicionário de dados em markdown: nome, tipo, descrição de negócio e exemplo para cada coluna de cada tabela
- [x] 1.5 Criar briefing fictício do gestor com 2-3 perguntas de negócio abertas (satisfação, performance por categoria, sazonalidade)

## 2. Notebook Guiado - Dia 1

- [x] 2.1 Criar estrutura do notebook com seções markdown para cada bloco: Diagnóstico, Limpeza, Exploração Inicial, Perguntas Analíticas
- [x] 2.2 Implementar células scaffold do Bloco 1 (Diagnóstico): imports, carga de dados, células de shape/dtypes/describe/missings/duplicatas com comentários guia
- [x] 2.3 Implementar células scaffold do Bloco 2 (Limpeza): tratamento de missings, duplicatas, tipos, outliers com espaços para o participante preencher justificativas
- [x] 2.4 Implementar células scaffold do Bloco 3 (Exploração): histogramas, boxplots, countplots com código parcial para participante completar
- [x] 2.5 Implementar células scaffold do Bloco 4 (Perguntas): template markdown para formulação e priorização de perguntas de negócio
- [x] 2.6 Adicionar células de checkpoint ao final de cada bloco (verificações automáticas: nº de linhas após limpeza, nº de perguntas documentadas, etc.)
- [x] 2.7 Adicionar células "Desafio" opcionais para participantes avançados em cada bloco

## 3. Notebook Guiado - Dia 2

- [x] 3.1 Criar estrutura do notebook Dia 2 com seções: Análise Estatística, Visualizações, Storytelling, Documento Final
- [x] 3.2 Implementar células scaffold do Bloco 1 (Análise): agrupamentos, correlações, comparações entre segmentos com espaço para interpretação textual
- [x] 3.3 Implementar células scaffold do Bloco 2 (Visualizações): template para 4 visualizações finais com título descritivo, labels e anotação de insight
- [x] 3.4 Implementar células scaffold do Bloco 3 (Storytelling): template markdown com estrutura contexto → problema → descoberta → recomendação
- [x] 3.5 Implementar célula de exportação do Bloco 4: geração de versão limpa sem código (markdown/HTML) com resumo executivo, descobertas e recomendações
- [x] 3.6 Adicionar células de checkpoint e desafios opcionais para Dia 2

## 4. Notebook Solução do Instrutor

- [x] 4.1 Criar versão completa do notebook Dia 1 com todas as células preenchidas e comentários sobre decisões
- [x] 4.2 Criar versão completa do notebook Dia 2 com análise finalizada, visualizações e documento exportável
- [x] 4.3 Validar que a solução do instrutor cobre todos os checkpoints e produz documento final de qualidade

## 5. Materiais de Apoio

- [x] 5.1 Criar checklist reutilizável de análise exploratória em markdown (genérico para qualquer dataset)
- [x] 5.2 Criar roteiro do instrutor com tempos por bloco, pontos de demonstração ao vivo e transições entre blocos
- [x] 5.3 Definir e documentar os 4+ momentos de tangenciamento com temas avançados (quais temas, em qual bloco, frase de transição)

## 6. Estratégia de Conversão

- [x] 6.1 Criar script do CTA de encerramento (últimos 15min do Dia 2): oferta, roadmap visual, condição exclusiva e prazo
- [x] 6.2 Criar mapa visual do roadmap de aprendizado: "EDA (Workshop)" → "Inferência/Modelagem (CDO)" → "Carreira (formação completa)"
- [x] 6.3 Redigir sequência de 3 emails de follow-up: D+0 (materiais + oferta), D+1 (insight + lembrete), D+3 (encerramento da oferta)
- [x] 6.4 Definir condições da oferta exclusiva (desconto % ou bônus, prazo 48-72h)

## 7. Validação e Teste

- [x] 7.1 Executar notebooks de ponta a ponta (Dia 1 + Dia 2) simulando participante sem experiência para verificar que scaffold funciona
- [x] 7.2 Verificar que todos os checkpoints produzem output correto
- [x] 7.3 Verificar que documento final exportado está apresentável e compreensível para não-participante
- [x] 7.4 Revisar tempos do roteiro com dry run das demonstrações ao vivo
