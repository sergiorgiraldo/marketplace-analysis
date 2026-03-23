## ADDED Requirements

### Requirement: Notebook guiado com scaffold
O notebook principal SHALL conter células pré-preenchidas com estrutura (markdown headers, comentários, imports) que o participante completa durante o workshop. Cada seção MUST ter: (1) célula markdown com objetivo do bloco, (2) célula de código com imports e setup, (3) células vazias ou parcialmente preenchidas para o participante completar, (4) célula de checkpoint.

#### Scenario: Participante sem experiência em Python
- **WHEN** um participante com pouca experiência em Python abre o notebook
- **THEN** as células scaffold contêm código parcial com comentários indicando o que alterar (ex: `# Altere o nome da coluna abaixo`), permitindo execução mesmo com modificações mínimas

#### Scenario: Participante com experiência em Python
- **WHEN** um participante experiente quer ir além do scaffold
- **THEN** existem células extras marcadas como "Desafio" com problemas abertos que não têm scaffold, permitindo exploração livre

### Requirement: Checklist de análise exploratória
O workshop MUST fornecer checklist reutilizável (em markdown) que o participante pode usar em qualquer análise futura. O checklist SHALL cobrir: diagnóstico de dados, limpeza, exploração univariada, exploração bivariada, formulação de perguntas, análise direcionada, visualização e comunicação.

#### Scenario: Uso do checklist durante o workshop
- **WHEN** o participante está em qualquer bloco do workshop
- **THEN** o checklist indica em qual etapa da análise está e quais passos restam, funcionando como mapa de progresso

#### Scenario: Uso do checklist após o workshop
- **WHEN** o participante inicia uma nova análise por conta própria
- **THEN** o checklist é genérico o suficiente para aplicar a qualquer dataset, com perguntas-guia em cada etapa

### Requirement: Documento final de análise
Ao final do Dia 2, o participante MUST ter um documento exportável (markdown ou HTML) contendo: resumo executivo (3-5 parágrafos), metodologia resumida, descobertas principais com visualizações embutidas e recomendações acionáveis.

#### Scenario: Exportação do documento
- **WHEN** o participante completa o Dia 2
- **THEN** uma célula de exportação gera versão limpa do notebook sem células de código, apenas markdown e outputs visuais, em formato apresentável para um portfólio

#### Scenario: Qualidade mínima do documento
- **WHEN** o documento final é gerado
- **THEN** ele contém pelo menos: 1 resumo executivo, 3 descobertas com visualizações, 2 recomendações baseadas nos dados, e é compreensível para alguém que não participou do workshop

### Requirement: Material de referência pós-workshop
O participante MUST receber acesso por 7 dias ao material completo: notebook com solução do instrutor (todas as células preenchidas), notebook do participante com seu progresso, dataset, checklist e documento final.

#### Scenario: Acesso pós-evento
- **WHEN** o workshop termina
- **THEN** o participante recebe link para pasta com todos os materiais e tem 7 dias para finalizar a análise se não terminou ao vivo
