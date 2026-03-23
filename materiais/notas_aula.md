# Notas de Aula - Workshop de Análise de Dados

Documento pessoal de condução. Não é material do aluno, não substitui o roteiro de tempos. É o que consultar quando esquecer a sequência ou o ponto que não pode pular.

---

# DIA 1: Fundamentos e Data Cleaning

## Abertura (15 min)

### Apresentação pessoal

Duas frases, não mais. "Sou Caio Gomes, trabalho com dados há 20 anos, passei por Amazon, Nubank, Booking, hoje sou CAIO do Magalu. Mas o que importa para vocês é que eu faço no dia a dia exatamente o que vocês vão fazer agora."

O ponto é: isso não é exercício acadêmico. O processo que vamos seguir é o mesmo que eu uso quando chega um dataset novo na minha mesa.

### A promessa

"Em dois dias vocês vão sair daqui com uma análise real, feita por vocês, que podem colocar no portfólio hoje. Não é simulação, não é dados inventados. É um dataset de marketplace real com problemas reais."

Mostrar o produto final: abrir o notebook executado do Dia 2, scrollar as visualizações, mostrar o documento de análise exportado. Deixar a audiência ver onde vai chegar. Isso ancora a expectativa e reduz ansiedade.

"Isso aqui é o que vocês vão construir. Passo a passo, começando do zero."

### Setup técnico

Distribuir glossário (`glossario_python.md`) + checklist de EDA junto com o notebook.

**Instrução principal: Google Colab.** Pedir que abram o link do notebook no Colab e executem a primeira célula. O Colab instala dependências e baixa os dados automaticamente. Isso elimina 90% dos problemas de setup.

**Fallback local:** para quem insistir no ambiente local, os notebooks detectam automaticamente e ajustam os caminhos. Os problemas típicos do local são:

1. **"Não abre o Jupyter"** - Verificar se ativaram o ambiente virtual. No terminal: `source .venv/bin/activate` (Mac/Linux) ou `.venv\Scripts\activate` (Windows), depois `jupyter notebook`.
2. **"ModuleNotFoundError"** - Falta instalar dependências. `pip install pandas numpy matplotlib seaborn` dentro do venv.
3. **"FileNotFoundError nos CSVs"** - O notebook assume que está na pasta `notebooks/`. Se abriram de outro lugar, os caminhos relativos quebram.

Dar 3-4 minutos para setup. Pedir que levantem a mão (ou mandem no chat) quando aparecer "Setup completo!". Se alguém travar, o monitor resolve em paralelo.

### Briefing da Marina

"Antes de tocar nos dados, leiam o briefing. No mundo real vocês nunca começam uma análise sem entender o que o stakeholder quer. A Marina é gerente de operações, o NPS do marketplace caiu, e ela precisa de diagnóstico visual para a diretoria."

Dar 2 minutos para lerem. Depois: "Notem que as perguntas da Marina são abertas de propósito. Ela não sabe exatamente o que procurar. Parte do trabalho de quem analisa dados é transformar perguntas vagas em perguntas respondíveis. Vamos chegar lá no Bloco 4."

---

## Bloco 1: Diagnóstico do Dataset (30 min)

### Script de abertura — os primeiros minutos

Antes de qualquer código, abrir `orders` e dizer:

"Isso aqui são 99 mil pedidos de um marketplace brasileiro. Vocês já compraram num marketplace assim. A Marina, que é gerente de operações, está vendo o NPS cair e não sabe por quê. Em dois dias vocês vão ter uma análise que ela pode levar para a diretoria."

Pausa. Deixar o peso disso pousar.

"Mas antes de fazer qualquer análise, a gente precisa entender com o que está lidando. Nunca confie num dataset sem olhar para dentro dele primeiro."

O objetivo dos primeiros minutos não é contextualizar — é criar a tensão que vai sustentar os blocos técnicos do meio. O participante entra no exercício querendo descobrir o que está escondido nos dados, não apenas executar células.

### Demonstração ao vivo (10 min)

Abrir diretamente a tabela `orders` do Olist. O exercício vai cobrir `items` e `reviews` — a demo usa `orders` para não antecipar o que os alunos vão descobrir.

Sequência da demonstração, verbalizando o raciocínio:

1. **Shape**: "Primeiro eu olho quantas linhas e colunas. Isso me diz o tamanho do problema. 99 mil pedidos, 8 colunas."
2. **dtypes**: "Depois os tipos. Se uma coluna que deveria ser numérica aparece como object, já sei que tem sujeira. Se datas estão como string, vou precisar converter."
3. **head/tail**: "Olho as primeiras e últimas linhas. O head me mostra o formato, o tail me mostra se o final do arquivo tem lixo."
4. **describe**: "Estatísticas descritivas. Olho especialmente min e max. Se o preço mínimo é negativo, tem problema. Se o máximo parece absurdo para um marketplace generalista, pode ser outlier ou segmento diferente."
5. **isnull**: "Conto os missings por coluna. Não apenas quantos, mas onde estão. Missings concentrados numa coluna é diferente de missings espalhados."

Frase-chave: "Diagnóstico antes de ação. Assim como médico não receita sem examinar, analista não limpa dado sem diagnosticar."

### Os 5 problemas que vão encontrar

Os participantes vão trabalhar no dataset real. Os problemas plantados são:

1. **Duplicatas em orders** - Mesmo order_id com timestamps diferentes. Não são duplicatas exatas, o que força uma decisão sobre qual registro manter.
2. **Datas em formato misto** - purchase_date mistura ISO (2017-10-02) com formato brasileiro (02/10/2017). pd.to_datetime sem parâmetros vai interpretar errado.
3. **Missings em review_score que não são aleatórios** - Pedidos com preço mais alto têm mais ausência de avaliação. Isso é Missing At Random (MAR), e tratar como se fosse aleatório distorce a análise.
4. **Categorias com typos** - health_beauty aparece como heath_beauty e health_beuty. Sem padronizar, as contagens ficam erradas.
5. **Outliers de preço** - Valores extremos que provavelmente são B2B misturado com B2C. Não são erros, mas distorcem médias.

### Erros comuns dos participantes

O exercício cobre as tabelas `items` e `reviews`. Os erros mais comuns nessas tabelas:

- **Não investigar os missings em reviews**: Olham o .isnull().sum(), veem que é "pouco" (6%), e seguem. Perguntar: "Pouco em relação a quê? E se os 6% forem sistematicamente os clientes mais valiosos?"
- **Não cruzar missings com outras variáveis**: Enxergam a quantidade de missing mas não pensam em investigar se o padrão de missing depende de outra variável (ex: preço alto → mais missing em review_score).
- **Não olhar o describe de price em items com atenção**: Passam direto pelo max de preço sem questionar se R$6.000+ num marketplace genérico faz sentido. Guiar: "Isso é outlier ou dado legítimo? O que muda na sua análise se for cada um deles?"

### Tangenciamento: Missing At Random

Momento: quando os participantes estiverem investigando por que o preço médio dos pedidos sem review_score é maior.

"Notem que os missings aqui não são aleatórios: pedidos caros têm mais ausência de avaliação. Isso é o que em estatística chamamos de Missing At Random, que apesar do nome quer dizer que a probabilidade de estar missing depende de outra variável observada. Se vocês simplesmente jogarem fora esses registros, vão subestimar o preço médio do marketplace. Se imputarem pela mediana geral, vão diluir o efeito."

Pausa.

"A decisão de dropar versus imputar é uma das que mais impacto tem no resultado final de qualquer análise. No CDO a gente dedica uma aula inteira só a mecanismos de missing e suas consequências."

Tom: informativo, não vendedor. Mostrar que existe profundidade sem insistir.

---

## Bloco 2A: Limpeza Estrutural (30 min)

### Demonstração ao vivo (8 min)

Abrir o notebook do exercício agora (não o demo). Mostrar a limpeza de duplicatas passo a passo.

Sequência:

1. **Identificar**: "Primeiro, quantas duplicatas de order_id existem? Não vou tratar antes de entender."
2. **Investigar**: "Vou olhar um exemplo. Esse pedido aparece duas vezes com timestamps diferentes. Provavelmente o sistema registrou duas vezes, ou o status mudou e gerou novo registro."
3. **Decidir**: "Vou manter o registro mais recente, porque provavelmente reflete o estado final do pedido."
4. **Documentar**: "Escrevo a justificativa no próprio código. Daqui a 3 meses quando alguém perguntar 'por que removeu 300 linhas', a resposta está aqui."

Frase-chave: **"Limpeza sem justificativa não é limpeza, é destruição de dados."**

Repetir essa frase. É o conceito mais importante do bloco.

Demonstrar a conversão de datas com formato misto:
"Olhem esse campo. Tem '2017-10-02' e '02/10/2017' no mesmo campo. Se eu converter sem cuidado, outubro vira fevereiro. pd.to_datetime com format='mixed' e dayfirst=True resolve, mas vocês precisam saber que esse risco existe."

### Mini-checkpoint e transição 2A → 2B

Após o exercício de duplicatas e datas, pedir que executem o mini-checkpoint. Verificar que a maioria passou.

Transição:
"Vocês resolveram os problemas de estrutura: registros duplicados e datas inconsistentes. Agora vamos para os problemas de significado: dados que estão lá mas podem enganar. Missings que não são aleatórios, categorias escritas errado, e preços que parecem de outro planeta."

---

## Bloco 2B: Limpeza Semântica (35 min)

### Demonstração ao vivo (7 min)

Mostrar que os missings em review_score dependem do preço (MAR). Mostrar um outlier e perguntar: "Isso é erro ou dado legítimo?"

### Conceito: limpeza documentada

O ponto central não é técnico. Todo mundo consegue rodar .drop_duplicates(). O ponto é a disciplina de documentar cada decisão.

"No mundo real, a limpeza que vocês fazem hoje vai ser questionada daqui a 6 meses. Se não está documentada, vocês vão ter que refazer tudo. Pior: alguém vai refazer diferente e chegar em números diferentes, e ninguém vai saber qual está certo."

### Guia para participantes travados

O momento de maior travamento é na decisão sobre missings de review_score. Muita gente fica paralisada entre dropar, imputar ou manter.

Se alguém perguntar "o que faço com os missings?":
"Qual é a consequência de cada opção? Se dropar, você perde 6% dos dados, e são justamente os pedidos mais caros. Se imputar pela mediana, está assumindo que os clientes que não avaliaram teriam dado uma nota mediana, o que provavelmente não é verdade. Se manter como NaN e filtrar nas análises que usam score, preserva tudo e lida com isso caso a caso. Qual dessas consequências você aceita?"

Não dar a resposta. Guiar pelo raciocínio das consequências.

### Erros comuns dos participantes

- **Aplicar fillna(0) em review_score**: Zero não é "sem avaliação", é uma nota que não existe na escala. Isso puxa todas as médias para baixo.
- **Não verificar o resultado da limpeza**: Limpam e seguem sem checar se o shape faz sentido, se os tipos converteram corretamente, se não perderam dados demais.
- **Esquecer de salvar os DataFrames limpos**: No final do dia precisam dos dados limpos para o Dia 2. Se não salvarem, perdem o trabalho. No Colab, o notebook oferece download automático dos CSVs limpos.

### Tangenciamento: outliers e modelagem

Momento: na discussão sobre preços extremos, quando estiverem decidindo o que fazer com os valores acima do P99.

"Decidir o que é outlier versus dado legítimo é uma decisão que depende do contexto de negócio. Esses preços extremos podem ser B2B misturado com B2C. No mundo real, isso é a diferença entre cortar 5% da receita ou descobrir um segmento novo."

"A opção de criar um flag em vez de remover é a mais segura: preserva os dados e permite analisar separadamente. Em modelagem preditiva, outliers não tratados podem dominar o erro do modelo. A gente cobre isso em profundidade na formação, porque a decisão certa depende do que você vai fazer com os dados depois."

---

## Bloco 3: Análise Exploratória Inicial (30 min)

### Demonstração ao vivo (5 min)

Demo mais curta, focada na leitura da distribuição bimodal:

"Olhem essa distribuição de review_score. A maioria é 5, depois 4, depois 1. Quase ninguém dá 2 ou 3. Isso é típico de avaliações: as pessoas ou amam ou odeiam, o meio é raro. A média aqui engana, porque sugere que a experiência é razoável, quando na verdade é bimodal. Dois picos significam dois grupos distintos. Quem são os do pico da esquerda e quem são os do pico da direita?"

Não precisa construir o histograma na frente deles. O notebook já tem o código pronto. Foco na interpretação, não na construção.

### Interpretação de distribuições

Os participantes vão gerar vários gráficos. O risco é que gerem e não interpretem. Para cada tipo de distribuição, ter uma explicação pronta:

- **Bimodal** (review_score): "Dois picos. Significa que existem dois grupos distintos no dado. Perguntem: quem são os do pico da esquerda e quem são os do pico da direita? O que os separa?"
- **Assimétrica à direita** (preço): "A maioria dos valores está concentrada na esquerda, com uma cauda longa à direita. A média é puxada pela cauda, por isso a mediana é melhor como medida de centro aqui."
- **Tendência com sazonalidade** (volume mensal): "O volume cresce ao longo do tempo, com picos pontuais. Os picos coincidem com datas comerciais? Se sim, é sazonalidade. Se não, pode ser efeito de campanha ou mudança no mix."

### Ênfase: documentar observações

"Gerar gráfico é fácil. O valor está na interpretação. Para cada visualização, escrevam uma frase: o que isso me diz? Se não conseguem escrever a frase, o gráfico não serviu para nada."

Isso prepara para o Bloco 4, onde as observações viram perguntas.

### Erros comuns dos participantes

- **Gerar 15 gráficos sem interpretar nenhum**: Quantidade não é qualidade. Melhor 4 gráficos com interpretação do que 15 sem.
- **Pular para bivariada sem fazer univariada**: Cruzam preço com nota sem antes entender a distribuição de cada um. Resultado: interpretam uma correlação que é artefato de outlier.
- **Não filtrar outliers nas visualizações**: O histograma de preço fica achatado por causa dos extremos. Precisam aprender que filtrar para visualização não é o mesmo que remover do dataset.

---

## Bloco 4: Perguntas Analíticas (55 min)

### Demonstração ao vivo (10 min)

Transformar uma observação em pergunta analítica na frente de todos:

"Vamos pegar uma observação da exploração. Digamos que notamos que eletrônicos têm nota mais baixa que a média. A observação é: 'eletrônicos têm nota baixa'. Mas isso não é uma pergunta. A pergunta é: 'Em quais categorias de eletrônicos a nota média está abaixo da mediana geral, e qual o volume de pedidos dessas categorias?'"

Mostrar a transformação:

- Pergunta vaga: "Os dados são bons?"
- Melhor: "A satisfação do marketplace é boa?"
- Específica: "Em quais categorias a nota média está abaixo de 3.5, com pelo menos 100 avaliações?"

### Os 3 critérios de uma boa pergunta

1. **Respondível** com os dados disponíveis. "Se a resposta depende de dados que não temos, não é uma boa pergunta para agora. Guardem para depois."
2. **Acionável** para o negócio. "Se a Marina não pode fazer nada com a resposta, a pergunta é curiosidade, não análise. Curiosidade é válida, mas o briefing pede ação."
3. **Específica** o suficiente para virar uma análise concreta. "Se você não consegue visualizar qual tabela/coluna vai usar para responder, a pergunta ainda está vaga demais."

### Exemplos bons e ruins usando o dataset

**Ruim:** "Os clientes estão satisfeitos?"
Problema: vaga demais, não é acionável.

**Ruim:** "O frete causa insatisfação?"
Problema: "causa" é causal, e EDA mostra correlação, não causalidade.

**Bom:** "Qual a nota média por faixa de valor de frete, e existe diferença estatisticamente relevante entre a faixa mais barata e a mais cara?"
Por que funciona: específica, respondível com groupby + agg, e acionável (se frete caro correlaciona com nota baixa, pode-se subsidiar frete em categorias críticas).

**Bom:** "Em quais meses do ano o volume de pedidos cresce mais de 30% em relação à média, e a nota média cai nesses meses?"
Por que funciona: específica, respondível com série temporal, e acionável (se picos pioram a nota, escalar operação nos picos).

### Revisão entre pares (20 min)

Ao iniciar a revisão, antes de os participantes trocarem perguntas:

"Enquanto vocês revisam as perguntas do colega, rodem esta célula — ela salva os dados limpos que vão precisar amanhã. No Colab ela baixa automaticamente para o seu computador. Não pule isso."

Deixar a célula de save rodando em paralelo. Depois, conduzir a revisão normalmente.

Durante a revisão, **identificar a melhor pergunta para o cliffhanger**. Critério: uma pergunta que envolva nota × outra variável com correlação evidente nos dados (atraso de entrega é o caso mais óbvio, mas frete, categoria e sazonalidade funcionam). A pergunta ideal tem correlação clara e ambiguidade causal aberta.

**Pergunta-padrão de reserva:** "Em quais categorias a nota média está abaixo da mediana geral, e isso tem relação com o tempo de entrega?" — usar se nenhuma pergunta da sala for adequada.

Orientação ao circular:
- Se a dupla está concordando com tudo sem fricção, intervir: "Vocês estão sendo gentis demais. Onde essa pergunta pode falhar?"
- Se travam na avaliação, dar exemplo concreto: "Essa pergunta é respondível? Com qual coluna?"
- Guardar 5 minutos para discussão em grupo: pedir que 2-3 duplas compartilhem a melhor pergunta e o feedback que deram/receberam

### Cliffhanger — seleção da pergunta

Após a discussão em grupo, você já deve ter a pergunta selecionada. Não anunciar antes — a transição precisa parecer espontânea.

Se ainda não escolheu: use a pergunta de reserva. Não improvisar com uma pergunta ruim.

### Cliffhanger — condução ao vivo (10-15 min)

"Deixa eu pegar uma pergunta aqui que me chamou atenção..."

Anunciar a pergunta para a sala. Abrir o notebook. Fazer o groupby ao vivo sem pressa — verbalizar o raciocínio enquanto digita. Chegar no resultado: a correlação vai aparecer clara nos números.

Parar. Silêncio de 2-3 segundos.

Olhar para a sala. "Isso prova que X causa Y?"

Não responder. Deixar a pergunta no ar.

"Isso tem um nome. Amanhã a gente enfrenta."

Fechar o notebook. Encerrar o dia.

**Não ceder à pressão da sala.** A abertura é deliberada. Se alguém insistir em ter a resposta: "Deixar sem resposta é proposital. Boa análise de dados levanta mais perguntas do que resolve. Amanhã vocês entendem por quê." — e encerrar. Não entrar na discussão.

---

## Transições do Dia 1

**Abertura → Bloco 1 (Diagnóstico):**
"Vocês leram o briefing da Marina. Agora a pergunta é: os dados que temos permitem responder o que ela quer? Para saber, primeiro precisamos entender o que tem nesses dados. Vamos diagnosticar."

**Bloco 1 → Bloco 2A (Limpeza Estrutural):**
"Vocês encontraram os problemas. Duplicatas, datas misturadas, missings suspeitos, categorias com typos, preços estranhos. Vamos começar pelos problemas de estrutura: registros duplicados e formatos inconsistentes."

**Bloco 2A → Bloco 2B (Limpeza Semântica):**
"Vocês resolveram os problemas de estrutura: registros duplicados e datas inconsistentes. Agora vamos para os problemas de significado: dados que estão lá mas podem enganar."

**Bloco 2B → Bloco 3 (Exploração):**
"Os dados estão limpos. Ou melhor: estão limpos o suficiente para começar a explorar. Agora é hora de gerar intuição. Não estamos respondendo perguntas ainda, estamos procurando as perguntas certas para fazer."

**Bloco 3 → Bloco 4 (Perguntas):**
"Vocês geraram gráficos, viram distribuições, notaram padrões. Tudo isso é observação. Agora vamos transformar observações em perguntas de negócio que a Marina consegue usar. Perguntas específicas, respondíveis, acionáveis."

**Fechamento do Dia 1:**
"Hoje vocês pegaram um dataset sujo, diagnosticaram, limparam com justificativa, exploraram e formularam perguntas. Amanhã, vocês respondem essas perguntas, criam as visualizações finais e montam o documento que a Marina pediu. Salvem seus dados limpos, e amanhã a gente começa de onde parou."

---

# DIA 2: Análise e Comunicação

## Abertura Dia 2 (20 min)

### Recap do Dia 1 (5 min)

"Ontem vocês fizeram o trabalho que ninguém vê mas que sustenta toda análise: diagnóstico, limpeza, exploração. Vamos relembrar rapidamente."

Pontos para recap (consultar enquanto fala):

- Dataset de marketplace com ~100k pedidos, 113k itens, 99k reviews
- 5 problemas encontrados: duplicatas, datas mistas, MAR em reviews, typos em categorias, outliers de preço
- Decisões de limpeza documentadas (manter NaN, criar flag de alto valor, padronizar categorias)
- Observações da exploração: distribuição bimodal de notas, concentração de receita em poucas categorias, correlação preço-frete com dispersão

Sobre o cliffhanger: "Ficou uma pergunta no ar ontem sobre se correlação prova causalidade. Vamos voltar nela quando analisarmos atraso vs nota."

### Carregamento dos dados no Dia 2

No Colab, o notebook pede upload dos CSVs limpos que baixaram ontem. Se alguém perdeu os arquivos, há fallback automático para versões pré-limpas hospedadas. Explicar: "Se vocês baixaram os arquivos ontem, façam upload. Se não, o notebook carrega uma versão pronta. O resultado é o mesmo, mas quem usa os próprios dados limpos carrega também as decisões que tomou ontem."

### Reveal de Margem de Erro (10 min)

Transição do recap para a demo:

"Antes de começarmos a responder as perguntas, eu quero mostrar algo sobre os dados que vocês limparam ontem. Algo que muda como vocês vão olhar para cada número que produzirem hoje."

Abrir o notebook de solução (projetado na tela). Fazer o groupby rápido de satisfação por categoria. Mostrar o ranking ordenado.

"Olhem esse ranking. Parece claro: office_furniture é a pior, books_general_interest é a melhor."

**Votação:** "Levantem a mão quem acha que audio é significativamente pior que a média geral."

Esperar. Maioria levanta.

Executar a célula de IC. O mesmo gráfico aparece com barras de erro (bigodes).

Silêncio de 3-4 segundos. Deixar a sala processar.

"Olhem os bigodes. O bigode é a margem de erro. Vocês já viram margem de erro em pesquisa de eleição? '48% dos votos, com margem de 2 pontos.' Aqui é a mesma ideia."

Apontar para categorias com bigodes grandes:

"fashion_underwear_beach: média 3.93, mas com 120 avaliações o bigode vai de 3.7 a 4.2. Pode ser uma das piores ou uma das melhores. A gente não sabe."

Apontar para categorias com bigodes pequenos:

"health_beauty: média 4.17, com 7 mil avaliações o bigode é minúsculo. Essa nota a gente confia."

"Quando os bigodes se cruzam, a diferença pode ser ruído. Quando não se cruzam, aí vocês têm algo real."

Pausa. Frase de âncora:

**"Média sem margem de erro é opinião, não é evidência. O bigode é o que separa 'eu acho' de 'os dados mostram'."**

Generalização rápida (só se houver tempo):

"Isso chama intervalo de confiança. Quanto mais dados, menor a margem. Quanto menos dados, maior a incerteza. O filtro de 100 que a gente usa é uma regra prática. O certo seria mostrar a margem de erro e deixar o leitor ver onde tem certeza e onde não tem."

Reframe para o exercício:

"Pra agora, vamos com o filtro de 100. É suficiente pro briefing da Marina. Mas guardem esse gráfico na cabeça. Tudo que fizerem hoje, perguntem: qual o n?"

### Erros a evitar na demo de margem de erro

- **Não chamar de "intervalo de confiança" logo de cara.** Usar "margem de erro" (que o público conhece de pesquisa eleitoral). Só no final dar o nome técnico.
- **Não mostrar fórmulas.** O ponto é visual e intuitivo, não matemático.
- **Se alguém perguntar "como calcula?":** "São 3 linhas de código com numpy. Mando por email depois." Satisfaz sem abrir tangente.
- **Se passar de 10 minutos:** Cortar a generalização. Ir direto para "guardem isso, qual o n?" e seguir para o Bloco 1.
- **Se alguém pedir IC no notebook dele:** "Ótimo instinto. Pro briefing da Marina o filtro de volume mínimo resolve. O código eu mando por email."
- **Reforço informal ao circular durante o exercício:** Se alguém rankear categorias sem mencionar volume, perguntar: "Cadê o bigode?"

### Recontextualização das perguntas

"Vocês formularam perguntas no final de ontem. O briefing da Marina pede três coisas: satisfação por categoria, relação entre frete e satisfação, e sazonalidade. Hoje vamos responder isso com números e com gráficos que ela possa mostrar na diretoria."

### Objetivo do dia

"Hoje o ciclo completa, mas antes, uma revelação sobre o que significa confiar num número. Vocês vão: (1) responder as perguntas com análise estatística, (2) criar visualizações que comuniquem as descobertas, e (3) montar o documento de análise. No final do dia, o que vocês têm em mãos é um projeto real de portfólio."

---

## Bloco 1: Análise Estatística Aplicada (60 min)

### Demonstração ao vivo (15 min)

Mostrar como responder uma pergunta com groupby + agg:

"Vou pegar a primeira pergunta da Marina: satisfação por categoria. O que preciso? Nota média por categoria. Mas nota média sozinha engana, preciso de volume também."

```python
df.groupby('category').agg(
    nota_media=('review_score', 'mean'),
    volume=('review_score', 'count')
)
```

"Olhem esse resultado. Tem uma categoria com nota 1.5, incrível, pior do marketplace inteiro. Mas olhem o volume: 3 avaliações. Não dá para concluir nada com 3 avaliações."

### Conceito: volume mínimo

"Regra prática: se a categoria tem menos de 100 avaliações, eu não tiro conclusão sobre satisfação. É pouco para separar padrão de ruído. 30 é o mínimo da estatística clássica, mas em dados de avaliação, com distribuição tão concentrada nos extremos, 100 é mais seguro."

Filtrar e mostrar: "Agora sim. Com esse filtro, as 10 piores categorias têm volume suficiente para a conclusão ter peso."

### Resultados esperados de cada análise

Para orientar a circulação durante o exercício, saber o que esperar:

1. **Satisfação por categoria**: Categorias de eletrônicos e telefonia tendem a ter notas piores. Categorias de decoração e cama/mesa/banho tendem a ter notas melhores. A diferença entre melhor e pior é de ~1 ponto na nota média.

2. **Atraso vs satisfação**: Correlação negativa moderada (~-0.3). Pedidos entregues antes do prazo têm nota média ~4.3. Pedidos com atraso grave (>14 dias) caem para ~2.0. O padrão é claro: atraso destrói satisfação.

3. **Sazonalidade**: Volume cresce ao longo de 2017-2018 (marketplace em crescimento). Picos em novembro (Black Friday) e períodos festivos. Nota média não cai necessariamente nos picos, mas volume de reclamações absolutas sobe.

### Tangenciamento: causalidade e inferência

Momento: quando analisarem a correlação de -0.3 entre atraso e nota.

"A correlação aqui é -0.3, moderada. Mas cuidado: correlação não é causalidade. Pode ser que regiões distantes tenham mais atraso E mais insatisfação por outros motivos. A distância pode ser o confundidor que explica ambos."

"Para separar o efeito do atraso dos confundidores geográficos, precisaríamos de regressão controlada ou matching. É o tipo de pergunta que a gente ataca no módulo de inferência causal do CDO."

"Para o briefing da Marina, a correlação já é evidência útil. Ela não precisa de prova causal para justificar investir em logística. Mas se alguém na diretoria perguntar 'tem certeza que é o atraso que causa a nota baixa e não outra coisa?', a resposta honesta é: não temos certeza. Temos evidência consistente."

### Erros comuns dos participantes

- **Concluir de amostra pequena**: Categoria com 5 avaliações e nota 1.0 não significa que é a pior. Insistir no filtro de volume mínimo.
- **Confundir correlação com causalidade**: "Frete caro causa nota baixa" é uma afirmação causal. O que os dados mostram é que frete caro está associado a nota mais baixa. A diferença importa.
- **Ignorar composição do dado**: A média geral de satisfação pode ser estável enquanto a satisfação piora nas categorias que crescem. Simpson's paradox em ação.

---

## Bloco 2: Visualizações Interpretativas (60 min)

### Demonstração ao vivo (10 min)

Criar uma visualização final ao vivo, mostrando a transformação de gráfico exploratório para gráfico de apresentação.

"Vou pegar esse histograma exploratório que fizemos ontem. Ele serve para mim entender o dado. Mas se eu coloco isso numa apresentação para a diretoria, ninguém entende nada."

Transformação passo a passo:
1. Trocar histograma por barras horizontais com as 5 melhores e 5 piores categorias
2. Adicionar título descritivo: não "Nota por Categoria" mas "Categorias com Melhor e Pior Satisfação"
3. Rotular eixos com unidades
4. Adicionar linha de referência (média geral)
5. Anotar o insight: a frase que resume o que o gráfico mostra

"Gráfico exploratório é para vocês. Gráfico final é para quem não viu os dados. A diferença é contexto: título, labels, anotação, referência."

### Viz 4: Heatmap guiado

A quarta visualização agora é um heatmap de satisfação cruzando categoria com faixa de atraso. O código está ~60% pronto: pivot_table e sns.heatmap estruturados, o aluno executa e escreve a interpretação.

Ao circular, verificar se entenderam que o heatmap cruza duas dimensões que viram separadas (Viz 1 = categorias, Viz 2 = atrasos). O valor pedagógico é integrar os achados anteriores numa visualização que mostra a interação entre os dois fatores.

Se alguém terminar rápido, sugerir que altere o número de categorias ou experimente outro colormap.

### Diferença: gráfico exploratório vs. gráfico final

| Aspecto | Exploratório | Final |
|---------|-------------|-------|
| Público | Você | Stakeholder |
| Título | Descritivo técnico | Comunicativo (diz o insight) |
| Labels | Opcional | Obrigatório com unidades |
| Anotações | Nenhuma | Destaque do ponto principal |
| Escala | Automática | Ajustada para comparação justa |
| Cores | Default | Intencionais (vermelho=ruim, verde=bom) |

### Checklist de qualidade visual

Para cada visualização que os participantes criarem, devem verificar:

1. **Título diz o insight, não apenas o eixo** - "Quanto Mais Atraso, Pior a Avaliação" > "Nota vs Atraso"
2. **Eixos rotulados com unidades** - "Preço (R$)", não "price"
3. **Anotação com o número-chave** - n=1.500 em cada barra, ou a correlação no scatter
4. **Escala que não engana** - eixo Y começa no zero para barras, legenda presente se usar cores
5. **Salvou em alta resolução** - dpi=150 mínimo, bbox_inches='tight'

### Erros comuns de visualização

- **Eixo Y cortado**: Barras que começam em 3.0 em vez de 0 exageram diferenças pequenas. Para notas de 1-5, sempre começar do zero.
- **Cores sem significado**: Usar 10 cores aleatórias para 10 categorias quando a mensagem é "boas vs ruins". Melhor: vermelho para as piores, verde para as melhores.
- **Excesso de informação**: Gráfico com 50 categorias é ilegível. Top 5 + Bottom 5 comunica melhor que todas juntas.
- **Dual axis mal usado**: Dois eixos Y com escalas diferentes podem sugerir correlações que não existem. Usar com cuidado e sempre explicar.

---

## Bloco 3: Storytelling com Dados (45 min)

### Demonstração ao vivo (10 min)

Mostrar a estrutura narrativa e escrever um parágrafo de resumo executivo ao vivo.

"A estrutura que funciona para documento de análise é simples: contexto, problema, descoberta, recomendação. Não é receita de bolo, é lógica de argumentação."

**Contexto:** O que motivou a análise? Qual o cenário?
**Problema:** O que está acontecendo de diferente do esperado?
**Descoberta:** O que os dados revelam sobre o problema?
**Recomendação:** O que fazer com base no que descobrimos?

Escrever ao vivo um parágrafo de resumo executivo:

"Vou escrever isso na frente de vocês. A análise de 99 mil pedidos do marketplace no período 2017-2018 revela que a insatisfação não é generalizada: está concentrada em categorias específicas (eletrônicos e telefonia) e fortemente correlacionada com atraso na entrega. Pedidos entregues com mais de 7 dias de atraso têm nota média 2.5 pontos abaixo dos entregues no prazo. As 5 categorias com pior avaliação representam 22% da receita total, o que justifica investigação direcionada."

"Notem o que esse parágrafo faz: dá contexto (99k pedidos, período), identifica o padrão (concentrado, não generalizado), quantifica (2.5 pontos, 22% da receita) e direciona ação (investigação nas categorias específicas). A diretoria consegue decidir algo com essa informação sem olhar um único gráfico."

### Como escrever um resumo executivo

O que incluir:
- Período e volume analisado (números concretos)
- O achado principal em uma frase
- Quantificação do impacto
- Direção de ação (não ação detalhada, mas para onde olhar)

O que omitir:
- Detalhes metodológicos (ninguém na diretoria quer saber que usou groupby)
- Ressalvas sobre tamanho amostral (coloque nas limitações)
- Gráficos (o resumo deve funcionar como texto puro)

### Importância de documentar limitações

"A seção de limitações é onde mora a honestidade intelectual da análise. Todo mundo quer mostrar resultados, ninguém quer mostrar o que não sabe. Mas a diretoria confia mais numa análise que diz 'isso é o que sabemos, isso é o que não sabemos' do que numa que finge certeza."

Limitações que os participantes devem documentar:
- Correlação ≠ causalidade (a maior)
- Missings em review_score não são aleatórios (os pedidos sem avaliação são sistematicamente diferentes)
- Período limitado (2017-2018, pode não refletir o marketplace atual)
- Não controlamos para região, peso do produto, ou outros confundidores

### Erros comuns dos participantes

- **Resumo executivo que é lista de gráficos**: "No gráfico 1 vemos que... No gráfico 2 vemos que..." Isso não é resumo, é legenda.
- **Recomendações genéricas**: "Melhorar a logística" não é acionável. "Investigar a causa do atraso nas categorias eletrônicos e telefonia, que concentram 35% das notas abaixo de 3" é acionável.
- **Pular a seção de limitações**: Perguntar diretamente se preencheram.

---

## Bloco 4: Documento Final e Encerramento (20 min)

### Exportação

Instrução prática: executar a célula de exportação que gera o HTML. Se der erro, provavelmente é porque nbconvert não está instalado. Solução rápida: `pip install nbconvert`.

"O HTML que vocês geraram é o documento final. Abram no navegador, leiam do começo ao fim como se fossem a Marina. Faz sentido? Está convincente? Os gráficos contam uma história coerente?"

### Avaliação de qualidade

Pedir que cada participante faça uma autoavaliação rápida:

- Resumo executivo compreensível sem gráficos? Sim/Não
- Pelo menos 3 descobertas com visualização? Sim/Não
- Recomendações baseadas em evidência dos dados? Sim/Não
- Limitações documentadas? Sim/Não
- Gráficos com título, labels e anotação? Sim/Não

Se 4/5 sim: o documento está no nível. Se menos, usar os próximos minutos para completar.

### Transição para CTA

"Vocês acabaram de fazer em 2 dias o que muita gente que trabalha com dados não sabe fazer: pegar um dataset sujo, limpar com critério, formular perguntas de negócio, responder com dados e comunicar os resultados de forma clara."

Pausa. Deixar o peso da realização ser sentido.

"Esse documento que vocês produziram já é melhor que a maioria dos relatórios que eu vejo em empresas. E vocês podem usar no portfólio a partir de agora."

Mostrar 2-3 documentos de participantes que ficaram bons. Destacar o que fizeram bem.

Depois, seguir o script de CTA em `materiais/script_cta.md`. A transição natural é do reconhecimento para a lacuna: "Mas eu quero ser honesto com vocês sobre uma coisa..."

---

## Transições do Dia 2

**Abertura → Bloco 1 (Análise Estatística):**
"Vocês viram o que a margem de erro faz com um ranking. Guardem isso. Agora vamos responder as perguntas da Marina, começando por satisfação por categoria."

**Bloco 1 → Bloco 2 (Visualizações):**
"Vocês têm os números. Agora precisam comunicar esses números de forma que a Marina consiga apresentar para a diretoria sem precisar de vocês do lado explicando. Isso é o que as visualizações finais fazem."

**Bloco 2 → Bloco 3 (Storytelling):**
"Gráficos bonitos sem contexto são decoração. Agora vocês vão amarrar tudo numa narrativa: contexto, problema, descoberta, recomendação. O resumo executivo é a parte mais importante do documento: é o que a diretoria lê."

**Bloco 3 → Bloco 4 (Documento Final):**
"A narrativa está escrita, os gráficos estão prontos. Agora é empacotar tudo num documento que se sustenta sozinho, sem vocês do lado. Exportar, revisar, e garantir que quando a Marina abrir, ela encontre o que precisa."

**Bloco 4 → CTA:**
A transição está no script de CTA. O ponto de virada é o reconhecimento do que fizeram, seguido da honestidade sobre o que falta. Não forçar a transição: o trabalho de dois dias já fez o marketing.
