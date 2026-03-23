# Avaliacao do Workshop de Analise de Dados

**Persona:** Renata Oliveira, 34 anos, advogada tributarista, migrando para dados.

---

## 1. Antes do workshop

Eu vi um anuncio do workshop no Instagram, acho. Ou foi no YouTube, depois de assistir um video do Caio sobre como ele saiu da fisica e foi parar na Amazon. Nao lembro exatamente. O que lembro e que a descricao dizia algo como "sem pre-requisito, voce sai com uma analise real no portfolio". E eu pensei: bom, ou isso e verdade e eu descubro que consigo, ou e mentira e eu descubro que nao e para mim. Nos dois casos, saio com uma resposta.

Meus medos eram concretos. Primeiro: nunca abri o Terminal do meu Mac. Nunca. Sei que ele existe, sei que tem uma telinha preta, sei que gente de TI usa, e so. Segundo: achei que ia chegar la e todo mundo ia saber Python menos eu. Terceiro, e mais fundo: tenho 34 anos, 8 anos de tributario, e estava me perguntando se nao era tarde demais para virar a mesa. Existe uma diferenca entre pensar "quero mudar de carreira" e sentar numa sala para fazer isso de verdade. O workshop era o teste.

Paguei, me inscrevi, e passei a semana anterior tentando nao desistir.

---

## 2. Setup

Essa foi a primeira prova de fogo. O roteiro do instrutor menciona que o setup e para levar 3-4 minutos e que os problemas mais comuns sao "nao abre o Jupyter", "ModuleNotFoundError" e "FileNotFoundError nos CSVs". Lendo isso, eu sei que ele previu que gente como eu ia travar. E eu travei.

Quando ele pediu para executar a primeira celula de setup (cell-3 do notebook dia1), aquela que importa pandas, numpy, matplotlib, seaborn e imprime "Setup completo!", eu nao sabia nem onde estava o Jupyter. Provavelmente o pessoal do suporte tecnico ja tinha deixado o ambiente preparado, porque o roteiro fala em monitores (1 a cada 20 participantes). Mesmo assim, a sensacao de abrir uma interface que parece uma pagina web com celulas de codigo e nao entender direito o que e aquilo... nao vou mentir, meu estomago embrulhou. Shift+Enter para executar? Tive que perguntar. Vi uma menina do meu lado executando tudo rapido e me senti atrasada.

Mas a celula rodou. "Setup completo!" apareceu. E isso, por bobo que pareca, foi o primeiro micro-alivio do dia.

---

## 3. Dia 1 -- bloco a bloco

### Abertura (15 min)

A apresentacao pessoal dele foi curta. Duas frases, como ele planejou nas notas de aula: "Sou Caio Gomes, trabalho com dados ha 20 anos, passei por Amazon, Nubank, Booking, hoje sou CAIO do Magalu." E depois a parte que me pegou: "O que importa para voces e que eu faco no dia a dia exatamente o que voces vao fazer agora." Isso desarmou a parte do meu cerebro que estava dizendo "isso e para engenheiro, nao para advogada".

Quando ele mostrou o produto final, o notebook do Dia 2 todo executado com graficos e o documento de analise exportado, pensei: "isso e bonito, mas nao tem como eu fazer isso." E ai ele disse: "Passo a passo, comecando do zero." Eu me segurei na cadeira.

O briefing da Marina foi interessante porque me colocou num papel que eu entendo. No direito tributario, o cliente manda um email vago pedindo "me explica como reduzir a carga tributaria". A gente tem que transformar isso em perguntas especificas, pesquisar jurisprudencia, e montar um parecer. O email da Marina ("Precisamos entender melhor o que esta acontecendo com a satisfacao dos clientes") e exatamente isso: vago de proposito, e meu trabalho e destrinchar. Quando ele disse "no mundo real voces nunca comecam uma analise sem entender o que o stakeholder quer", eu pensei: isso eu ja faco, so que com outro nome.

### Bloco 1: Diagnostico do Dataset (45 min)

A demonstracao ao vivo com o dataset iris me ajudou. Ele verbalizou o raciocinio: "Primeiro eu olho o shape... depois os tipos... depois os missings..." Isso me deu uma sequencia mental. Nao era "senta e ve o que acontece". Existia um metodo, e ele estava transparente.

Quando fui para o exercicio no dataset real (cell-4, carregando os 3 CSVs), a tela mostrou "Orders: 99.441 linhas, 7 colunas", "Items: 113.180 linhas, 6 colunas", "Reviews: 99.224 linhas, 6 colunas". Cem mil linhas. Nunca trabalhei com cem mil linhas no Excel sem o computador travar. Aqui demorou menos de um segundo. Esse momento me impressionou.

Na celula de missings (cell-9), quando apareceu que review_score tinha missings e ele pediu para investigar se eram aleatorios, eu travei. Nao sabia o que "aleatorio" significava nesse contexto. Mas a celula seguinte (cell-10) ja dava o scaffold: comparar preco medio de pedidos COM score versus SEM score. Executei, vi que o preco medio dos sem score era maior, e o instrutor explicou o conceito de Missing At Random. A frase das notas de aula e perfeita: "apesar do nome quer dizer que a probabilidade de estar missing depende de outra variavel observada." Eu entendi. Nao de forma tecnica profunda, mas entendi o mecanismo: gente que compra caro avalia menos, entao se jogar fora esses registros, distorce o resultado.

A parte de duplicatas (cell-12) me surpreendeu. Achei que duplicata era duplicata. Mas o notebook mostrou que o mesmo order_id aparecia duas vezes com timestamps diferentes. O conceito de "duplicata parcial" nunca tinha me ocorrido, e no entanto faz todo sentido: num sistema, o mesmo registro pode ser processado mais de uma vez.

O checkpoint (cell-18) dando tudo OK foi satisfatorio. Pequena vitoria.

### Bloco 2: Limpeza Estruturada (60 min)

"Limpeza sem justificativa nao e limpeza, e destruicao de dados." Essa frase ficou na minha cabeca o dia inteiro. Ele repetiu varias vezes, como planejado nas notas de aula, e funcionou. Porque na advocacia e a mesma coisa: voce nao muda uma estrategia processual sem fundamentar. Todo ato tem que ter motivacao escrita.

A conversao de datas (cell-26) me deu um no. O conceito de que "02/10/2017" pode ser 2 de outubro ou 10 de fevereiro dependendo do formato era novo para mim. No Excel eu nunca tinha me preocupado com isso porque o software decidia por mim (e provavelmente decidia errado em alguns casos, agora percebo). Quando ele explicou que pd.to_datetime com format='mixed' e dayfirst=True resolve, eu copiei a linha e tentei entender cada pedaco. Nao entendi tudo, mas entendi a logica: voce precisa dizer ao programa qual e o dia e qual e o mes, senao ele chuta.

Na decisao sobre missings de review_score (cell-28), eu fiquei travada. O notebook dava tres opcoes: dropar, imputar pela mediana, ou manter como NaN. Eu queria uma resposta certa. Quando o instrutor circulou e alguem perguntou "o que faco com os missings?", ele nao respondeu direto. Ele perguntou: "Qual e a consequencia de cada opcao?" Isso me forcou a pensar. Se dropar, perco os pedidos caros. Se imputar, estou inventando uma nota. Se manter, preservo tudo mas tenho que lembrar de filtrar depois. Escolhi manter (opcao C, a recomendada). Mas o processo de chegar la foi mais importante que a resposta.

Os typos em categorias (cell-30, cell-31) foram quase divertidos. "heath_beauty" em vez de "health_beauty". No direito eu lido com erros de grafia em contratos o tempo todo. A ideia de criar um dicionario de correcao (typo_fixes) me pareceu elegante: voce lista cada erro e a versao correta, e o programa aplica em tudo de uma vez. Isso seria util em tanta coisa que eu faco no Excel manualmente...

Os outliers de preco (cell-33, cell-34) geraram uma discussao interessante na sala. O instrutor falou nas notas de aula que "decidir o que e outlier versus dado legitimo e uma decisao que depende do contexto de negocio." Fiquei pensando em como isso se aplica a tributario: uma empresa com faturamento 10x maior que as concorrentes nao e necessariamente fraude, pode ser um player diferente no mercado. O conceito de criar um flag em vez de remover me agradou muito.

### Bloco 3: Analise Exploratoria Inicial (60 min)

Aqui os graficos comecaram a aparecer. O histograma de review_score (cell-41) mostrou aquela distribuicao que o instrutor chamou de bimodal: muita nota 5, bastante nota 1, quase nada no meio. Ele explicou nas notas de aula: "as pessoas ou amam ou odeiam, o meio e raro." Faz sentido. Quando eu avalio um restaurante no Google, ou dou 5 ou dou 1. Nunca penso "foi 3 estrelas, razoavel."

O volume de pedidos ao longo do tempo (cell-42) foi o primeiro grafico onde eu vi algo e pensei: "ah, isso eu consigo interpretar sem ajuda." A linha subia, tinha uns picos, dava para ver que em novembro tinha mais vendas. Black Friday. Obvia, mas foi a primeira vez que eu extraia uma informacao de um grafico que eu mesma gerei. Momento importante.

O scatter plot de preco versus frete (cell-46) foi mais confuso. Muitos pontos, muita dispersao. O instrutor explicou que frete depende mais de peso e regiao do que de preco, o que faz sentido logisticamente. Mas interpretar scatter plots nao e intuitivo para mim. Vou precisar de mais pratica.

A frase que mais me marcou no bloco foi: "Gerar grafico e facil. O valor esta na interpretacao. Para cada visualizacao, escrevam uma frase: o que isso me diz? Se nao conseguem escrever a frase, o grafico nao serviu para nada." Isso e tao parecido com o que eu digo para estagiarios sobre peticoes: "Se voce nao consegue resumir o argumento em uma frase, voce nao entendeu o argumento."

### Bloco 4: Perguntas Analiticas (45 min)

Esse foi o bloco onde eu me senti mais em casa. A diferenca entre pergunta vaga ("Os clientes estao satisfeitos?") e pergunta especifica ("Em quais categorias a nota media esta abaixo de 3.5, com pelo menos 100 avaliacoes?") e exatamente o que eu faco quando pego um caso novo. Cliente diz "quero pagar menos imposto", eu transformo em "qual a aliquota efetiva de ICMS por estado para esta operacao especifica e onde existe beneficio fiscal aplicavel?"

Os tres criterios de uma boa pergunta (respondivel, acionavel, especifica) me pareceram tao uteis que anotei num post-it e colei no notebook. Vou usar isso fora de dados tambem.

Quando o instrutor fez o tangenciamento sobre causalidade ("EDA e o diagnostico. Inferencia causal e o tratamento"), eu entendi a limitacao do que estavamos fazendo. Nao e que a analise seja ruim. E que ela responde "o que esta acontecendo", mas nao "por que esta acontecendo" nem "o que fazer para mudar". E essa honestidade me passou confianca, nao inseguranca. Ele nao estava vendendo a ideia de que dois dias de workshop resolvem tudo. Estava dizendo: isso aqui e a base, e a base e solida.

O fechamento do Dia 1 me deixou satisfeita. Salvei os dados limpos (cell-59), todos os checkpoints passaram. Fui para casa pensando: "eu consegui."

---

## 4. Dia 2 -- bloco a bloco

### Abertura Dia 2 (10 min)

Cheguei no segundo dia com menos medo e mais curiosidade. O recap das notas de aula e bem feito: "Ontem voces fizeram o trabalho que ninguem ve mas que sustenta toda analise." Isso valida o esforco do Dia 1, que foi pesado.

Quando a celula de setup do Dia 2 (cell-1) carregou os dados limpos que eu mesma salvei no dia anterior, senti uma continuidade que me agradou. Nao foi "joga fora o que fez e comeca de novo". Foi "pega o que voce construiu e avanca."

### Bloco 1: Analise Estatistica Aplicada (60 min)

O merge das tres tabelas (cell-2) criou um dataset consolidado com mais de 100 mil linhas e varias colunas derivadas (total_item, delivery_days, delay_days, purchase_month). Eu nao teria conseguido fazer isso sozinha, mas o scaffold estava la. Executei, funcionou, e quando vi o head() do resultado, pensei: "agora sim, tudo junto."

A analise de satisfacao por categoria (cell-5) com o filtro de volume minimo de 100 avaliacoes me mostrou uma coisa que eu nunca teria pensado sozinha: que uma categoria com nota 1.5 baseada em 3 avaliacoes nao significa nada. O conceito de "nao tire conclusao de categoria com 5 avaliacoes" e contra-intuitivo. No direito, um unico precedente do STF ja muda tudo. Em dados, 5 casos nao mudam nada. Essa inversao de logica foi um dos aprendizados mais valiosos dos dois dias.

A analise de atraso versus satisfacao (cell-8) foi reveladora. Os buckets de atraso mostraram um padrao claro: quanto mais atraso, pior a nota. De 4.3 para entregas antecipadas a 2.0 para atrasos graves. Monotonico, como ele falou. Esse e o tipo de resultado que mesmo eu, sem background tecnico, consigo olhar e dizer: "isso e obvio, mas agora esta quantificado." E quantificar muda tudo. No direito tributario, a diferenca entre "a aliquota e alta" e "a aliquota e 3 pontos percentuais acima da media do setor" e a diferenca entre reclamacao e argumento.

A correlacao de -0.3 entre atraso e nota (cell-10) gerou a discussao sobre causalidade que o roteiro previa. O instrutor foi claro: "a correlacao ja e evidencia util, mas se alguem na diretoria perguntar 'tem certeza que e o atraso que causa a nota baixa e nao outra coisa?', a resposta honesta e: nao temos certeza. Temos evidencia consistente." Gostei dessa honestidade. Num parecer juridico, eu nunca escreveria "com certeza absoluta o tribunal vai decidir X." Escrevo "a jurisprudencia prevalecente aponta para X." Mesma logica.

### Bloco 2: Visualizacoes Interpretativas (60 min)

A demonstracao da diferenca entre grafico exploratorio e grafico final foi um dos momentos mais didaticos do workshop. O instrutor pegou um histograma bruto e transformou em barras horizontais com as 5 melhores e 5 piores categorias, titulo descritivo, eixos rotulados, linha de referencia e anotacao de insight. A tabela comparativa das notas de aula (exploratorio vs. final, "publico: voce" vs. "publico: stakeholder") organizou isso na minha cabeca.

O scaffold do notebook para a Visualizacao 1 (cell-20) ja trazia a estrutura: barras coloridas (vermelho para piores, verde para melhores), titulo, media geral como linha de referencia. Mas o espaco para eu escrever a anotacao do insight estava em branco: "Insight: [descreva o padrao que encontrou]". Eu tive que pensar e escrever. Nao era so executar codigo.

A Visualizacao 2 de atraso versus satisfacao (cell-22) ficou bonita. As barras com cores indo do verde ao vermelho, os volumes escritos em cima de cada barra (n=X.XXX). Esse e o tipo de grafico que eu mostraria para alguem e a pessoa entenderia sem eu precisar explicar. Que e exatamente o ponto: a Marina precisa mostrar para a diretoria.

A Visualizacao 3 com dual axis (cell-24) foi a mais complicada para mim. Dois eixos Y com escalas diferentes, um com barras (volume) e outro com linha (nota media). O instrutor alertou nas notas de aula que dual axis pode sugerir correlacoes que nao existem. Entendi a ressalva, mas confesso que nao teria conseguido criar esse grafico do zero. O scaffold salvou.

A Visualizacao 4 de escolha livre (cell-26) foi onde eu travei de verdade. O notebook dava uma dica ("heatmaps funcionam bem para cruzar duas variaveis categoricas") e o espaco em branco. Eu nao sabia o que fazer. Fiquei uns 10 minutos olhando para a celula vazia. Acho que o instrutor percebeu que varias pessoas estavam travadas, porque circulou sugerindo opcoes. Acabei fazendo algo simples, um barplot de frete medio por faixa de atraso, e nao ficou incrivel, mas ficou funcional.

### Bloco 3: Storytelling com Dados (45 min)

Esse bloco foi onde a advogada em mim se sentiu mais confortavel. A estrutura contexto > problema > descoberta > recomendacao e basicamente a estrutura de um parecer juridico: fatos > direito > analise > conclusao. Quando o instrutor escreveu o paragrafo de resumo executivo ao vivo, eu pensei: "isso eu sei fazer, so nunca fiz com numeros."

O scaffold do documento de analise (cell-32) tinha tudo: resumo executivo, contexto, 3 descobertas com espaco para imagem, recomendacoes, limitacoes. Eu tive que preencher. E aqui aconteceu algo interessante: eu escrevi mais rapido que a maioria da sala. Porque a habilidade de sintetizar informacao em texto claro e exatamente o que eu faco ha 8 anos. So que agora, em vez de citar jurisprudencia, eu estava citando dados. O mecanismo e o mesmo: evidencia + argumento + implicacao pratica.

A secao de limitacoes me agradou especialmente. "A secao de limitacoes e onde mora a honestidade intelectual da analise." Isso e verdade em qualquer area. Um parecer que nao reconhece riscos nao e um bom parecer.

### Bloco 4: Documento Final (30 min)

A exportacao para HTML (cell-36) foi o gran finale. Quando executei a celula e ela disse "Documento exportado", abri o arquivo no navegador e... vi um documento bonito, sem codigo, so texto e graficos, com cara de relatorio profissional. Com o meu texto. Com os meus graficos (ok, muitos deles vieram do scaffold, mas eu executei, eu preenchi, eu interpretei).

O checkpoint final (cell-38) deu quase tudo OK. Faltou uma visualizacao (a quarta, que eu nao consegui fazer direito). Mas 7 de 8. Fiquei satisfeita.

---

## 5. Momentos marcantes

### Positivos

1. **O primeiro "Setup completo!" (cell-3, Dia 1).** Parece bobo, mas para quem nunca executou uma linha de codigo na vida, ver o computador obedecendo ao que eu pedi foi uma sensacao real. O fato de o notebook ja ter o codigo pronto e eu so precisar apertar Shift+Enter nao diminui isso. Eu precisava sentir que a maquina nao era hostil.

2. **A frase "Limpeza sem justificativa nao e limpeza, e destruicao de dados."** Isso conectou o workshop com minha experiencia profissional de uma forma que nenhum tutorial de Python faria. Nao era sobre codigo. Era sobre disciplina de raciocinio. Fundamentar decisoes e o que eu faco todo dia.

3. **A analise de atraso versus satisfacao mostrando queda monotonica (cell-8, Dia 2).** Foi o momento em que eu "vi" dados funcionando para responder uma pergunta de negocio. Nao um exercicio academico. Uma gerente real perguntou, e os dados responderam com clareza. Entrega atrasada destroi satisfacao. Quantificado.

4. **O documento HTML final.** Abrir no navegador e ver algo que parecia um relatorio da McKinsey (com todo respeito a McKinsey, provavelmente o deles e melhor, mas o meu existia) foi o momento de maior satisfacao dos dois dias. Eu pensei: "isso eu posso mostrar para alguem."

### Negativos

1. **A Visualizacao 4 de escolha livre (cell-26, Dia 2).** Esse foi o momento de maior frustracao. O notebook dava um espaco em branco e uma dica vaga. Eu nao tinha repertorio para criar algo do zero. O contraste com os blocos anteriores, onde o scaffold era generoso, foi grande. Entendo que a intencao era empurrar para a autonomia, mas para quem esta no primeiro contato com Python, o salto foi abrupto demais.

2. **O scatter plot de preco versus frete (cell-46, Dia 1).** Muitos pontos, muita dispersao, e eu nao sabia o que estava olhando. O instrutor interpretou bem na demonstracao, mas quando tentei escrever minha observacao, travei. Scatter plots nao sao intuitivos para quem vem de tabelas e graficos de barras no Excel. Senti que faltou mais tempo ou mais explicacao sobre como ler esse tipo de grafico.

3. **O ritmo do Bloco 2 do Dia 1 (limpeza, 60 min).** Foram muitas decisoes em sequencia: duplicatas, datas, missings, categorias, outliers. Cada uma com conceitos novos. Eu consegui acompanhar, mas no final do bloco estava mentalmente exausta. Um intervalo extra ou 15 minutos a mais teriam ajudado. O roteiro preve 60 minutos, e foi apertado.

---

## 6. O HTML final

Consegui gerar. A celula de exportacao (cell-36 do Dia 2) rodou sem erro. Abri o arquivo no Safari e vi um documento com titulo, texto, graficos coloridos, e nenhuma linha de codigo. Parecia feito por alguem que sabe o que esta fazendo.

O que senti? Orgulho e incredulidade, nessa ordem. Orgulho porque eu fiz (com muito scaffold, mas fiz). Incredulidade porque 48 horas antes eu nunca tinha aberto o Terminal. A distancia entre "nao sei nada de Python" e "tenho um documento de analise exportado" era menor do que eu imaginava. Nao porque seja facil: nao e. Mas porque o caminho estava claro.

Vi que o meu documento nao era tao bom quanto o gabarito do instrutor (a solucao_dia2 com aquele heatmap por categoria e faixa de atraso, que eu nao soube fazer). Mas era funcional. E a Marina poderia abrir aquilo e tomar uma decisao.

---

## 7. CTA e oferta

O script de CTA e bem construido. A transicao do reconhecimento ("Voces acabaram de fazer em 2 dias o que muita gente que trabalha com dados nao sabe fazer") para a lacuna ("Se a Marina perguntasse 'se eu reduzir o prazo em 2 dias, quanto a nota sobe?', voces conseguiriam responder?") e precisa. Eu senti a lacuna. Nao de forma manipulada, mas genuina. Porque durante os dois dias os tangenciamentos ja tinham plantado a semente: "correlacao nao e causalidade", "no CDO a gente dedica uma aula inteira a isso", "para separar esses efeitos, precisariamos de regressao controlada."

O roadmap visual ajudou. Eu me vi no primeiro degrau (EDA e Limpeza) e entendi que existem mais cinco. Nao como ameaca ("voce nao sabe nada"), mas como mapa ("voce esta aqui, e o caminho e esse"). A tabela de apoio com exemplos do workshop foi inteligente: "Quando a Marina perguntar 'essa queda na nota e significativa?', voce vai precisar de inferencia estatistica." Eu pensei: faz sentido, isso apareceu durante o workshop e eu nao soube responder.

A oferta em si: CDO a R$3.200 (20% off) ou Zero a Analista com 15% off. Janela de 72 horas. Ele nao insistiu, nao repetiu, nao criou urgencia falsa. Disse: "Se fizer sentido para voces, otimo. Se nao fizer, o workshop ja valeu pelo que voces produziram."

Vou comprar? Sim, provavelmente o Zero a Analista. Porque o CDO parece completo demais para onde eu estou. Ele vai ate lideranca em dados, e eu ainda nao sei se vou de fato migrar de carreira. O Zero a Analista cobre os tres primeiros degraus (EDA, inferencia, modelagem preditiva) e e o "caminho mais curto para quem quer entrar na area", como ele descreveu. Isso e o que eu preciso agora: validar se consigo aprender o suficiente para mudar de area. Se der certo, depois penso no CDO.

O email de follow-up do D+1, aquele que retoma a pergunta sobre o efeito do atraso na entrega e conecta com inferencia causal, vai me pegar. Sei que vai. Porque aquela pergunta ficou aberta na minha cabeca e eu quero saber a resposta.

---

## 8. O que diria para uma amiga

"Carol, fiz um workshop de analise de dados fim de semana passado. Dois dias, 4 horas por dia. O instrutor e o Caio Gomes, aquele do Magalu. Olha, eu cheguei morrendo de medo. Nunca tinha aberto o Terminal, nunca tinha escrito uma linha de Python, e achei que ia fazer papel de idiota. Nao fiz. O material vem mastigado: voce executa celulas de codigo que ja estao prontas, interpreta os resultados, e escreve suas observacoes. Nao e ctrl+C ctrl+V: voce precisa pensar, decidir, justificar. Mas nao precisa inventar codigo do zero.

Sai de la com um documento bonito de analise de marketplace que posso colocar no LinkedIn. E mais que isso: sai entendendo o processo. Diagnosticar, limpar, explorar, formular perguntas, responder com dados, comunicar. Isso eu consigo fazer de novo com outro dataset.

Tem coisas que nao entendi. Scatter plot ainda me confunde, Python ainda parece outra lingua, e no final ele mostrou que o que a gente fez e so o primeiro degrau. Mas o primeiro degrau ta feito, e isso muda tudo.

Se voce ta pensando em migrar para dados e nao sabe se e para voce: faz o workshop. No pior dos casos voce descobre que nao gostou. No meu caso, descobri que gostei mais do que esperava."

---

## 9. Nota geral: 8.5 / 10

O workshop cumpre a promessa central: uma pessoa sem nenhuma experiencia em Python sai com uma analise real feita por ela. Nao e fake, nao e so "siga os passos e aperte Enter". O scaffold e generoso (e precisa ser, para o publico), mas os momentos de decisao sao reais. Escolher o que fazer com os missings, decidir o que e outlier, formular perguntas de negocio, escrever o resumo executivo: tudo isso exige raciocinio proprio. O notebook nao faz por voce. Ele te coloca no caminho e deixa voce caminhar.

O que funciona muito bem: a estrutura narrativa dos dois dias (diagnosticar, limpar, explorar, perguntar, responder, comunicar) e logica e progressiva. O briefing da Marina cria um contexto real que sustenta o workshop inteiro. Os checkpoints dao seguranca de que voce esta no caminho certo. Os tangenciamentos para conteudo mais avancado (MAR, causalidade, modelagem) sao feitos com honestidade, sem tom de venda forcada. O instrutor sabe a hora de mostrar profundidade sem assustar.

O que tiraria meio ponto: o Bloco 2 do Dia 1 e denso demais para 60 minutos. Cinco decisoes de limpeza em sequencia, cada uma com conceitos novos, sem intervalo no meio. Para quem ja programa, deve ser tranquilo. Para mim, foi no limite. A Visualizacao 4 de escolha livre no Dia 2 e um salto de autonomia grande demais sem transicao. E o scatter plot do Bloco 3 mereceria mais tempo de interpretacao guiada. O outro meio ponto que tiraria e por um ponto que nao e culpa do workshop, mas do formato: 8 horas em dois dias e pouco para sedimentar. Na segunda-feira, eu ja nao lembrava a sintaxe do pd.to_datetime. Mas lembrava do raciocinio por tras da decisao, e acho que e isso que importa.
