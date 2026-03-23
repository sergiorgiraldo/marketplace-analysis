## ADDED Requirements

### Requirement: Momentos de demonstração de profundidade
O workshop SHALL ter pelo menos 4 momentos onde o conteúdo tangencia temas avançados (teste de hipótese, modelagem, causalidade, feature engineering) que são cobertos nos cursos pagos. Cada momento MUST ser orgânico ao fluxo da análise, não uma pausa para propaganda.

#### Scenario: Tangenciamento natural durante análise
- **WHEN** o participante encontra uma situação que pede análise mais avançada (ex: "essa diferença entre categorias é significativa?")
- **THEN** o Caio mostra brevemente o que seria possível (ex: teste estatístico, modelo preditivo), explica por que isso importa, e menciona que isso é parte do CDO/Zero a Analista sem interromper o fluxo da análise por mais de 2 minutos

### Requirement: CTA formal apenas no encerramento
O workshop MUST ter apenas um CTA formal (oferta comercial explícita) e ele SHALL acontecer nos últimos 15 minutos do Dia 2, após a entrega de valor estar completa.

#### Scenario: Encerramento com oferta
- **WHEN** o documento final está pronto e o workshop está nos últimos 15 minutos
- **THEN** o Caio apresenta oferta exclusiva para participantes do workshop com desconto limitado para CDO ou Zero a Analista, mostrando o roadmap de aprendizado e onde o workshop se encaixa na jornada completa

#### Scenario: Sem pitch antes do encerramento
- **WHEN** o workshop está em qualquer momento antes dos 15 minutos finais
- **THEN** não há menção a preço, oferta ou urgência de compra; apenas demonstrações de profundidade integradas ao conteúdo

### Requirement: Ponte entre workshop e cursos
O conteúdo do workshop MUST ser estruturado para que o participante perceba naturalmente as lacunas que os cursos pagos preenchem, sem que isso seja dito explicitamente.

#### Scenario: Percepção de lacuna via dataset
- **WHEN** o participante termina a análise exploratória
- **THEN** pelo menos 2 perguntas de negócio formuladas durante o workshop não podem ser respondidas apenas com EDA (exigiriam inferência, modelagem ou experimentação), criando curiosidade genuína sobre os próximos passos

#### Scenario: Roadmap de aprendizado
- **WHEN** o CTA formal é apresentado no encerramento
- **THEN** o participante vê um mapa visual mostrando: "Você está aqui (EDA)" → "Próximo passo: Inferência/Modelagem (CDO)" → "Carreira em dados (formação completa)", conectando a experiência do workshop ao percurso dos cursos

### Requirement: Oferta exclusiva para participantes
A oferta no encerramento SHALL incluir condição exclusiva (desconto ou bônus) disponível apenas para quem participou do workshop, com prazo limitado (48-72h após o evento).

#### Scenario: Condição exclusiva
- **WHEN** o participante recebe a oferta no encerramento
- **THEN** a condição é melhor do que o preço público dos cursos e tem prazo claro de expiração, criando urgência sem manipulação

### Requirement: Follow-up pós-workshop
O sistema MUST enviar sequência de follow-up por email: (1) imediatamente após o evento com materiais e link da oferta, (2) D+1 com destaque de um insight da análise e lembrete da oferta, (3) D+3 com encerramento da oferta.

#### Scenario: Sequência de emails
- **WHEN** o workshop termina
- **THEN** 3 emails são enviados na sequência definida, cada um agregando valor (material, insight, próximos passos) além de lembrar a oferta
