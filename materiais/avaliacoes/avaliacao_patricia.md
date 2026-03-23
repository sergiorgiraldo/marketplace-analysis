# Avaliacao do Workshop - Patricia Souza

Gerente de compras, 41 anos, 14 anos de empresa. Nao sou de dados, nao quero ser de dados. Vim entender o que o time de dados faz para conseguir pedir melhor e questionar o que me entregam.

---

## 1. Antes do workshop

Eu me inscrevi por um motivo bem pratico. Faz seis meses que a empresa contratou um "time de dados" e desde entao eu recebo dashboards que nao entendo, com metricas que ninguem me explicou, e todo mundo na reuniao faz cara de quem sabe o que esta olhando. Eu nao sei. Eu finjo. E isso me incomoda porque eu tenho 14 anos de empresa, conhego meus fornecedores, conhego a operacao, mas quando aparece um grafico de dispersao na tela, eu viro figurante.

Minha expectativa era: entender o suficiente para parar de fingir. Saber que perguntas fazer quando me mostram um relatorio. Talvez entender o que significa quando alguem fala "a correlacao e fraca" ou "os dados tem outliers". Nao quero virar analista, quero virar uma gestora que nao e enganada por grafico bonito.

Meu medo principal: parecer burra. Eu sei que sou mais velha que a maioria dos participantes. Sei que nunca abri Python na vida. Tenho medo de ser a unica que nao acompanha e de todo mundo fingir que esta tudo bem enquanto eu fico para tras.

Meu medo secundario: perder tempo. Tenho reuniao com fornecedor segunda-feira de manha, preciso preparar a negociacao. Se o workshop for enrolacao, eu vou me arrepender profundamente de ter vindo.

O que me fez vir: o preco era acessivel, o instrutor tem curriculo pesado (Amazon, Nubank, Magalu), e a promessa de sair com algo concreto. "Analise real no portfolio" nao me interessa como portfolio, mas se eu sair entendendo como uma analise e feita de verdade, ja valeu.

---

## 2. Setup

Aqui comecou o pesadelo. E preciso ser honesta sobre isso.

Meu laptop e um Dell corporativo com Windows 10, administrado pelo TI. Eu nao consigo instalar nada sem abrir chamado, e chamado demora de 3 a 5 dias uteis. Quando o instrutor pediu para abrir o Jupyter e executar a primeira celula, eu nao tinha Jupyter. Nao tinha Python. Nao tinha nada. O notebook pedia para rodar `import pandas as pd` e eu nao tinha pandas instalado. Na verdade, eu nao tinha nem o conceito de o que e um "ambiente virtual".

O roteiro do instrutor preve isso de maneira generica: "Verificar que todos conseguem abrir o Jupyter" e lista tres problemas comuns. Mas o meu problema nao era nenhum dos tres. O meu problema era anterior: eu nao consigo instalar software no meu computador. Ponto. O roteiro fala em `source .venv/bin/activate` e `pip install pandas numpy matplotlib seaborn`, mas eu nao tenho permissao para rodar nenhum desses comandos.

Perdi uns 15 minutos tentando entender o que fazer. O monitor tentou me ajudar, mas quando viu que o problema era bloqueio corporativo, nao tinha muito o que fazer. No final, fiz pair com um rapaz do meu lado que tinha tudo instalado. Ele rodava as celulas, eu olhava a tela dele e tentava acompanhar. Funcionou mais ou menos, mas eu perdi a autonomia. Toda vez que o notebook pedia "execute a celula abaixo", eu precisava esperar ele terminar a dele para pedir que rodasse a minha.

Sinceramente, esse foi o momento em que quase desisti. Eu pensei: "pronto, e curso para programador, eu nao devia estar aqui." Se o instrutor nao tivesse, na abertura, dito aquela frase sobre ser o mesmo processo que ele usa no dia a dia, acho que eu teria ido embora. Aquilo me deu um motivo para ficar: se e o que o CAIO do Magalu faz, eu preciso pelo menos entender o processo, mesmo sem rodar eu mesma.

Uma sugestao concreta: deveria ter uma alternativa para gente como eu. Um Google Colab pre-configurado, por exemplo. Algo que roda no navegador sem instalar nada. O roteiro nao preve isso e deveria, porque em qualquer turma com publico heterogeneo vai ter pelo menos 2 ou 3 pessoas com laptop bloqueado.

---

## 3. Dia 1 - bloco a bloco

### Abertura (15 min)

A apresentacao do instrutor foi rapida e eficiente. "Sou Caio Gomes, trabalho com dados ha 20 anos, passei por Amazon, Nubank, Booking, hoje sou CAIO do Magalu." Duas frases e pronto. Gostei. Gente que precisa de 10 minutos para se apresentar geralmente nao tem o que dizer.

Quando ele mostrou o produto final (o notebook executado do Dia 2, com os graficos e o documento de analise), eu entendi para onde estavamos indo. Isso reduziu minha ansiedade. Eu pensei: "ok, e um relatorio com graficos e recomendacoes. Isso eu sei ler. Talvez eu nao consiga fazer sozinha, mas se eu entender o processo, ja serve."

O briefing da Marina foi o ponto alto da abertura para mim. "Precisamos entender melhor o que esta acontecendo com a satisfacao dos clientes." Isso eu entendo. A Marina e eu somos parecidas: gestoras que precisam de respostas, nao de codigo. Quando o instrutor disse "as perguntas da Marina sao abertas de proposito, porque no mundo real o gestor nunca sabe exatamente o que procurar", eu me senti representada. Eu faco isso com o meu time de compras o tempo todo: dou uma direcao e espero que eles voltem com algo concreto.

### Bloco 1: Diagnostico do Dataset (45 min)

A demonstracao ao vivo com o dataset separado (iris ou tips) foi boa didaticamente. O instrutor verbalizou o raciocinio: "Primeiro eu olho o shape... depois os tipos... depois os missings..." Isso e exatamente o que eu queria aprender: o fluxo mental de quem trabalha com dados. Nao o codigo, mas a sequencia de perguntas.

A frase "Diagnostico antes de acao. Assim como medico nao receita sem examinar, analista nao limpa dado sem diagnosticar" ficou comigo. Vou usar essa analogia na proxima reuniao quando alguem me mostrar um dashboard sem explicar de onde vieram os dados.

Quando os participantes foram para o exercicio, eu fiquei olhando a tela do meu colega de pair. Ele executou as celulas de carregamento (cell-3 e cell-4 do notebook), e eu vi os numeros: Orders com ~100k linhas, Items com ~113k linhas, Reviews com ~99k linhas. Ate ai tudo bem, sao numeros, eu entendo.

O momento que me travou foi a celula de missings (cell-9). O codigo mostra `df.isnull().sum()` e a porcentagem. Eu entendi o resultado (6% dos review_scores estao faltando), mas nao entendi o codigo. E quando chegou na celula seguinte (cell-10), que compara o preco medio com e sem score, ai eu entendi a logica: os pedidos mais caros tem mais ausencia de avaliacao. Isso e uma descoberta de negocio, nao de programacao. E eu entendi o conceito sem precisar entender o `reviews_items[reviews_items['review_score'].isna()]['price'].mean()`.

O tangenciamento sobre Missing At Random foi o primeiro momento em que eu pensei: "ah, entao tem gente que estuda isso a serio." O instrutor explicou que "a probabilidade de estar missing depende de outra variavel observada" e que "se voces simplesmente jogarem fora esses registros, vao subestimar o preco medio do marketplace." Isso e o tipo de coisa que eu preciso saber para questionar um relatorio. Se alguem no meu time de dados jogou fora 6% dos dados sem pensar, eu agora sei que preciso perguntar "esses 6% que voce tirou tinham algum padrao?"

O checkpoint foi bom (cell-18). Deu a sensacao de progresso. Meu colega rodou, deu tudo OK. Eu nao rodei nada, mas vi que o processo tem pontos de verificacao. Isso e gestao basica, eu faco o mesmo com meus processos de compra.

### Bloco 2: Limpeza Estruturada (60 min)

Esse bloco foi denso. A frase central do instrutor foi: "Limpeza sem justificativa nao e limpeza, e destruicao de dados." Essa eu anotei no caderno. Vou usar literalmente. Quando o time de dados me mostrar um numero, vou perguntar: "o que voces limparam e por que?"

A demonstracao de duplicatas (cell-23) foi clara. Mesmo sem entender o codigo, eu entendi a decisao: tem pedidos que aparecem mais de uma vez com timestamps diferentes, provavelmente o sistema registrou duas vezes, e a escolha e manter o mais recente. O instrutor mostrou que nao e so apertar um botao, e uma decisao que precisa de justificativa. Isso me surpreendeu. Eu achava que limpeza de dados era mecanico.

A parte de datas com formato misto (cell-25 e cell-26) foi onde eu travei de novo. O instrutor explicou que `2017-10-02` e `02/10/2017` sao o mesmo dia, mas o computador pode interpretar errado. "Outubro vira fevereiro." Isso eu entendi intelectualmente, mas o codigo `pd.to_datetime(orders_clean[col], format='mixed', dayfirst=True)` para mim era chines.

O momento dos outliers (cell-33 e cell-34) foi interessante. O instrutor falou: "Esses precos extremos podem ser B2B misturado com B2C. No mundo real, isso e a diferenca entre cortar 5% da receita ou descobrir um segmento novo." Isso e a minha vida. Eu trabalho com fornecedores B2B. Se alguem no time de dados removesse compras de alto valor dos meus dados de compra sem me perguntar, eu iria ficar furiosa. A ideia de criar um flag em vez de remover fez todo sentido para mim.

A parte sobre typos em categorias (cell-30 e cell-31) tambem foi reveladora. `health_beauty` aparecendo como `heath_beauty` e `health_beuty`. Isso e o tipo de problema que eu vejo nas planilhas de Excel o tempo todo: gente escrevendo "parafuso allen" de 8 jeitos diferentes. Agora sei que existe um nome para isso e que analistas precisam padronizar antes de contar.

### Bloco 3: Analise Exploratoria Inicial (60 min)

Aqui eu comecei a gostar de verdade. Quando o instrutor mostrou o histograma de review_score e explicou que a distribuicao e bimodal ("as pessoas ou amam ou odeiam, o meio e raro"), eu tive um insight: a media engana. Se eu recebo um relatorio dizendo "nota media 4.0", parece bom. Mas se a maioria e 5 e 1, com quase ninguem no meio, a situacao e muito diferente. A media esconde o conflito.

Essa descoberta sozinha ja pagou o workshop para mim. Da proxima vez que alguem me mostrar uma media, eu vou perguntar: "Qual e a distribuicao?"

As celulas de visualizacao (cell-41 a cell-47) geraram graficos que eu consegui ler mesmo sem ter rodado. Meu colega de pair me mostrava cada um e eu tentava interpretar. O scatter plot de preco vs. frete (cell-46), por exemplo, mostra que frete nao depende so de preco. "Tem produto de R$50 com frete de R$40 e produto de R$200 com frete de R$15." Isso faz sentido para mim: frete depende de peso e regiao, nao de preco. E o tipo de coisa que eu sei da minha experiencia de compras.

A frase "Gerar grafico e facil. O valor esta na interpretacao. Para cada visualizacao, escrevam uma frase: o que isso me diz? Se nao conseguem escrever a frase, o grafico nao serviu para nada" foi outro momento de virada. Eu vejo dashboards no trabalho que sao bonitos e nao dizem nada. Agora sei articular por que me incomodam.

### Bloco 4: Perguntas Analiticas (45 min)

O melhor bloco do Dia 1. A transformacao de pergunta vaga em pergunta especifica foi excelente. O instrutor pegou "Os dados sao bons?" e transformou em "Em quais categorias a nota media esta abaixo de 3.5, com pelo menos 100 avaliacoes?" Isso e exatamente o que eu preciso aprender a fazer: quando o time de dados me mandar um relatorio vago, eu preciso devolver com perguntas especificas.

Os 3 criterios de uma boa pergunta (respondivel, acionavel, especifica) sao simples o suficiente para eu guardar e usar. Vou aplicar isso nas minhas reunioes. Quando alguem da minha equipe vier com "precisamos renegociar com o fornecedor X", eu vou perguntar: "Respondivel com os dados que temos? Acionavel? Especifica o suficiente?"

O tangenciamento sobre causalidade no fechamento foi o terceiro momento revelador: "EDA e o diagnostico. Inferencia causal e o tratamento." Simples, poderoso, memoravel. Agora eu sei que quando alguem diz "frete caro causa insatisfacao", eu posso questionar: "voce esta dizendo que causa, ou que os dois andam juntos?"

---

## 4. Dia 2 - bloco a bloco

### Abertura Dia 2 (10 min)

Voltei no segundo dia. O meu colega de pair tambem, entao consegui manter o arranjo. O recap foi util, especialmente os numeros (100k pedidos, 5 problemas encontrados, decisoes de limpeza). Senti que o instrutor se dirigia a turma toda, nao so aos programadores.

### Bloco 1: Analise Estatistica Aplicada (60 min)

A demonstracao de `groupby + agg` (solucao_dia2, cell-3) foi densa. Eu nao entendi o codigo, mas entendi o resultado: uma tabela mostrando nota media, mediana, volume e receita por categoria. E ai o instrutor disse a frase que mais me marcou no workshop inteiro: "Tem uma categoria com nota 1.5, incrivel, pior do marketplace inteiro. Mas olhem o volume: 3 avaliacoes. Nao da para concluir nada com 3 avaliacoes."

Eu quase levantei da cadeira. Quantas vezes eu ja vi apresentacao na empresa com conclusoes tiradas de 5 respostas de pesquisa? "Os clientes preferem o fornecedor Y." Baseado em quantas respostas? Tres. O conceito de volume minimo e algo que eu vou carregar para sempre.

A parte de correlacao entre atraso e nota (correlacao de -0.3) me pareceu abstrata a principio, mas o instrutor contextualizou: "Para o briefing da Marina, a correlacao ja e evidencia util. Mas se alguem na diretoria perguntar 'tem certeza que e o atraso que causa a nota baixa?', a resposta honesta e: nao temos certeza. Temos evidencia consistente." Isso e honestidade intelectual. E raro. E eu gostei.

### Bloco 2: Visualizacoes Interpretativas (60 min)

A transformacao de grafico exploratorio para grafico final foi excelente (solucao_dia2, cell-9 a cell-12). A diferenca entre "Nota por Categoria" e "Categorias com Melhor e Pior Satisfacao" e obvia quando alguem aponta, mas eu nunca tinha pensado nisso. Titulo que diz o insight, nao so o eixo. Cores com significado (vermelho para piores, verde para melhores). Anotacao que resume o ponto.

A tabela comparando grafico exploratorio vs. grafico final (nas notas de aula) e um material que eu quero imprimir e colar no monitor. Publico, titulo, labels, anotacoes, escala, cores. Tudo diferente dependendo de se o grafico e para voce ou para o stakeholder.

O heatmap de satisfacao por categoria e faixa de atraso (solucao_dia2, cell-12) foi o grafico mais bonito e mais informativo do workshop. Eu consegui ler sem ajuda: vermelho escuro no canto inferior direito (categorias de moveis com atraso grave) e verde no canto superior esquerdo (categorias leves com entrega antecipada). Contou a historia inteira em uma imagem.

### Bloco 3: Storytelling com Dados (45 min)

Esse bloco foi feito para gente como eu. A estrutura contexto > problema > descoberta > recomendacao e o que eu uso intuitivamente quando apresento para o diretor de supply chain. Nunca ninguem tinha me ensinado que analise de dados segue a mesma logica.

O resumo executivo que o instrutor escreveu ao vivo foi bom. "A analise de 99 mil pedidos do marketplace revela que a insatisfacao nao e generalizada: esta concentrada em categorias especificas (eletronicos e telefonia) e fortemente correlacionada com atraso na entrega." Uma frase, e a diretoria ja sabe o que importa. Eu sei fazer isso com relatorios de compras, agora sei que analise de dados deveria chegar no mesmo formato.

A secao de limitacoes ("correlacao nao e causalidade", "missings nao aleatorios", "periodo limitado") foi o ponto que mais me surpreendeu. O instrutor ensinou que admitir o que nao sabe e parte da honestidade intelectual da analise. Na minha experiencia, ninguem faz isso. Os relatorios que eu recebo do time de dados nunca dizem "isso e o que nao sabemos." A partir de agora eu vou cobrar.

### Bloco 4: Documento Final (30 min)

Aqui eu nao consegui fazer nada sozinha, obviamente. Meu colega de pair exportou o HTML dele e me mostrou no navegador. Era bonito: graficos, texto, recomendacoes, tudo num documento limpo sem codigo aparente. O `--no-input` do nbconvert remove todo o Python e deixa so o resultado.

Eu entendi que o documento e o produto final: o que vai para a mao do stakeholder. E que o notebook inteiro (com todo o codigo sujo) fica por baixo. Isso me ajudou a entender o que o time de dados deveria estar me entregando no trabalho, e por que os dashboards sem contexto nao servem.

---

## 5. Momentos marcantes

### Positivos

1. **Volume minimo**: "Nao da para concluir nada com 3 avaliacoes." Esse conceito sozinho mudou a forma como eu vou ler qualquer relatorio pelo resto da minha carreira. Simples, poderoso, imediatamente aplicavel.

2. **"Limpeza sem justificativa nao e limpeza, e destruicao de dados."** Anotei no caderno, sublinhei, coloquei estrela. Vou usar essa frase literalmente na proxima reuniao em que alguem me mostrar numeros sem explicar o tratamento.

3. **Distribuicao bimodal vs. media**: Entender que nota media 4.0 pode esconder uma realidade de muitos 5 e muitos 1 foi uma revelacao. Eu achava que media era suficiente. Nao e. Agora sei perguntar "qual e a distribuicao?"

### Negativos

1. **Setup**: Eu nao consegui instalar nada no meu laptop corporativo. Fiquei 15 minutos tentando, sentindo uma vergonha que nao precisava sentir. O roteiro nao preve solucao para isso. Se eu nao tivesse encontrado um colega de pair disposto, teria ido embora. Esse e o maior risco do workshop para publico heterogeneo.

2. **Vocabulario tecnico sem glossario**: Palavras como `DataFrame`, `merge`, `groupby`, `quantile`, `dtypes` apareciam sem traducao. O instrutor verbalizava o raciocinio ("estou juntando as tabelas"), mas o notebook assumia que eu sabia o que `pd.qcut` significa. Nao sei. Um glossario de 20 termos entregue junto com o checklist de EDA teria feito diferenca enorme.

3. **Ritmo do Bloco 2 no Dia 1**: A limpeza estruturada teve 60 minutos com 5 problemas diferentes (duplicatas, datas, missings, categorias, outliers). Para quem esta olhando pela primeira vez, foi rapido demais. Eu entendi as decisoes, mas nao tive tempo de digerir cada uma. Se o bloco tivesse 75 minutos, ou se tivesse dividido em dois, eu teria absorvido melhor.

---

## 6. O HTML final

Eu nao gerei o HTML sozinha. Meu colega de pair rodou o comando de exportacao e me mostrou no navegador do laptop dele. O resultado era impressionante: um documento limpo, com graficos coloridos, texto estruturado, recomendacoes claras. Parecia profissional.

O que eu senti foi um misto. Orgulho, porque eu entendi o que estava ali, mesmo sem ter escrito uma linha de codigo. E frustracaoo, porque eu nao conseguiria reproduzir isso sozinha. Nao pelo conteudo, eu sei estruturar um relatorio, eu sei escrever recomendacoes. Mas pela parte tecnica: rodar celulas, gerar graficos, exportar HTML.

Se me dessem os graficos prontos e pedissem para eu escrever o resumo executivo e as recomendacoes, eu faria um trabalho tao bom quanto o gabarito. Essa e a parte que o workshop me mostrou que eu ja sei fazer. A parte que nao sei e o meio: transformar dados brutos em graficos.

---

## 7. CTA e oferta

O pitch foi bem construido. A transicao do reconhecimento ("voces acabaram de fazer em 2 dias o que muita gente que trabalha com dados nao sabe fazer") para a lacuna ("se a Marina perguntasse 'quanto a nota sobe se eu reduzir o prazo em 2 dias', voces conseguiriam responder?") foi natural. Nao pareceu forcado.

O roadmap visual com os degraus (EDA > Inferencia > Modelagem > Experimentacao > Causalidade) fez sentido como mapa. Eu entendi onde estou e o que falta.

Vou comprar? Nao. Nem o CDO (R$3.200), nem o Zero a Analista. Por dois motivos. Primeiro, eu nao quero virar analista. Eu quero ser uma gestora melhor, e o workshop ja me deu o suficiente para isso. Segundo, eu nao tenho infraestrutura para acompanhar um curso tecnico. Meu laptop e bloqueado, meu tempo e curto, e eu nao vou pedir para o TI instalar Python para fazer um curso pessoal.

Mas a oferta nao me incomodou. O instrutor disse "se nao fizer sentido, sem problema" e eu acreditei. Nao foi pressao. Nao foi "restam poucas vagas." Nao foi urgencia artificial. Isso me fez confiar mais nele, nao menos.

Vou indicar? Sim, e com entusiasmo. Eu tenho pelo menos tres colegas gestoras em situacao parecida com a minha: recebem dashboards que nao entendem, tem medo de perguntar, e acham que dados e coisa de programador. Esse workshop mostra que nao e. Mostra que a parte mais importante da analise de dados nao e o codigo, e o raciocinio: que perguntas fazer, como limpar com criterio, como interpretar uma distribuicao, como comunicar o resultado.

Vou indicar tambem porque o instrutor em nenhum momento me fez sentir que eu estava no lugar errado. O tom era respeitoso, as analogias eram acessiveis (medico que nao receita sem examinar), e os conceitos de negocio eram reais (a Marina e um gestor real, nao um boneco de palha).

---

## 8. O que diria para uma colega

"Vai, mas resolve o problema do computador antes. Pergunta se pode fazer no Google Colab ou se precisa de alguma coisa instalada. Se voce nao resolver isso, voce vai gastar a primeira meia hora frustrada e vai querer ir embora."

"Nao se preocupe em entender o codigo. Eu nao entendi e mesmo assim aprendi coisas que vou usar toda semana no trabalho. O importante e entender o processo e os conceitos. A parte de limpeza documentada, volume minimo, distribuicao vs. media, correlacao vs. causalidade, tudo isso e util mesmo se voce nunca abrir Python na vida."

"Se voce tem medo de parecer burra, relaxa. O instrutor sabe que tem gente de todo nivel na sala e nao faz voce se sentir mal por nao saber. Mas aviso: vai ter momentos em que voce nao entende nada do que esta na tela. Respira e presta atencao no que ele fala, nao no que esta escrito no codigo."

"Nao vai te transformar em analista. Vai te transformar numa gestora que sabe conversar com analista. E isso vale mais do que voce imagina."

---

## 9. Nota geral: 7.5/10

O workshop entrega muito valor conceitual. Os momentos de insight (volume minimo, limpeza documentada, distribuicao bimodal, correlacao vs. causalidade) sao genuinamente uteis para qualquer gestor que trabalha com times de dados. O material de storytelling, a estrutura contexto > problema > descoberta > recomendacao, e a enfase na honestidade intelectual (documentar limitacoes, admitir o que nao sabe) sao diferenciadores reais. Eu saio sabendo questionar relatorios de um jeito que nao sabia antes.

O que impede a nota de ser 9 e a experiencia tecnica para quem nao e tecnico. O setup sem alternativa para laptops bloqueados e um risco real de perder participantes nos primeiros 20 minutos. A ausencia de um glossario de termos basicos faz com que o notebook, que deveria ser acessivel, se torne parcialmente incompreensivel para quem nunca viu pandas. E o ritmo do Bloco 2 no Dia 1 pressupoe uma familiaridade com manipulacao de dados que nem todo mundo tem.

Se o publico-alvo inclui gestores e migrantes de carreira (e inclui, segundo a proposta), o workshop precisa de uma camada de acessibilidade que nao esta la: Colab como fallback, glossario impresso, e talvez 15 minutos extras no Bloco 2 do Dia 1. Com esses ajustes, seria 9. Sem eles, e 7.5: excelente em conteudo, fragil em inclusao tecnica.
