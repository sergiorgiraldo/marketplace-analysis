## ADDED Requirements

### Requirement: Notas da Abertura Dia 2
As notas SHALL conter: recap do Dia 1 (o que fizemos, onde paramos), recontextualização das perguntas formuladas, e objetivo claro do Dia 2 (responder, visualizar, comunicar).

#### Scenario: Recap do Dia 1
- **WHEN** o Dia 2 inicia
- **THEN** as notas contêm pontos-chave para relembrar (dataset, problemas encontrados, perguntas formuladas) e frase de transição para o trabalho do dia

### Requirement: Notas do Bloco 1 - Análise Estatística
As notas MUST conter: demonstração de groupby+agg ao vivo, conceito de volume mínimo para tirar conclusões, como interpretar correlações sem confundir com causalidade, os resultados esperados de cada análise (satisfação por categoria, atraso vs nota, sazonalidade), e tangenciamento sobre inferência causal.

#### Scenario: Demonstração ao vivo da análise
- **WHEN** o instrutor conduz a demonstração do Bloco 1 Dia 2
- **THEN** as notas descrevem os resultados esperados de cada análise e como interpretar os números para a audiência

#### Scenario: Erros comuns na análise
- **WHEN** participantes executam as análises
- **THEN** as notas listam erros comuns (conclusão de amostra pequena, confundir correlação com causalidade, ignorar composição do dado)

### Requirement: Notas do Bloco 2 - Visualizações
As notas MUST conter: diferença entre gráfico exploratório e gráfico final, checklist de qualidade visual (título, labels, anotação, escala), erros comuns de visualização (eixo cortado, cores enganosas, excesso de informação).

#### Scenario: Demonstração de visualização final
- **WHEN** o instrutor cria visualização ao vivo
- **THEN** as notas descrevem o passo a passo de transformar gráfico exploratório em gráfico de apresentação, com critérios explícitos

### Requirement: Notas do Bloco 3 - Storytelling
As notas MUST conter: estrutura contexto-problema-descoberta-recomendação explicada com exemplo, como escrever um resumo executivo (o que incluir, o que omitir), e a importância de documentar limitações.

#### Scenario: Demonstração de storytelling
- **WHEN** o instrutor demonstra storytelling
- **THEN** as notas contêm exemplo de parágrafo de resumo executivo escrito ao vivo, com raciocínio sobre escolha de palavras e nível de detalhe

### Requirement: Notas do Bloco 4 - Documento Final e Encerramento
As notas MUST cobrir: instrução de exportação, como avaliar qualidade do documento final, transição para o CTA (referência ao script_cta.md).

#### Scenario: Transição para CTA
- **WHEN** o checkpoint final é concluído
- **THEN** as notas contêm frase de transição do momento técnico para o momento de encerramento/oferta
