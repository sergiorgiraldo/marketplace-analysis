# Avaliacao do Workshop - Thiago Nakamura

## 1. Antes do workshop

Vou ser sincero: eu quase nao me inscrevi. Vi o anuncio e meu primeiro pensamento foi "mais um workshop de pandas para iniciante". Eu ja sei fazer groupby, ja sei plotar histograma, ja subi modelo em producao (com ajuda, mas subi). Meu problema nao e tecnico, e que faz tres meses que o Lucas saiu da empresa e eu virei "o cara de dados" de uma fintech de credito sem ter metade da experiencia que ele tinha. Toda semana chega alguem pedindo "uma analise" e eu nao sei nem por onde priorizar.

O que me fez clicar no link de inscricao foram duas coisas. Primeiro, o Caio e CAIO do Magalu, e eu acompanho o Fisico Turista. Segundo, a descricao mencionava "comunicar resultado para stakeholder" e "formular perguntas de negocio". Isso e exatamente o que me falta. Eu consigo rodar o codigo. O que eu nao consigo e olhar pro resultado e saber se ta bom o suficiente pra mandar pro diretor.

Meu medo real, o que eu nao falo pra ninguem: eu to fingindo. Toda vez que mando um relatorio, fico esperando alguem perguntar algo que eu nao sei responder. E a pergunta sempre vem. "Mas isso e causal?" "Essa diferenca e significativa?" E eu desconverso.

## 2. Setup

Setup foi zero problema pra mim. MacBook da empresa, Jupyter ja instalado, rodei a primeira celula (cell-3 do dia1) e apareceu "Setup completo!" em 10 segundos. Mas eu vi que metade da sala travou. Tinha gente que nao sabia ativar ambiente virtual, gente que abriu o notebook de fora da pasta `notebooks/` e os caminhos relativos quebraram. As notas de aula preveem exatamente esses problemas (o trecho sobre "Problemas mais comuns"), e o instrutor resolveu rapido, mas deu pra ver que sem monitor auxiliar isso ia travar uns 15 minutos.

Uma coisa que notei: o notebook ja vem com as celulas de import e read_csv prontas, o que faz sentido pro publico. Se fosse eu sozinho, ia preferir escrever do zero, mas entendo que num workshop com gente que nunca abriu Jupyter, deixar isso pronto poupa tempo. O scaffold e bem pensado. Tem codigo suficiente pra ninguem ficar parado, mas tem espacos em branco pra voce preencher. Cell-10, por exemplo, ja faz o merge de reviews com items e calcula preco medio com e sem score, mas o campo "Sua observacao:" ta vazio pra voce escrever. Isso e melhor que dar tudo pronto ou nao dar nada.

## 3. Dia 1 - bloco a bloco

### Abertura (15 min)

A apresentacao pessoal foi curta e no ponto. "Sou Caio Gomes, trabalho com dados ha 20 anos, passei por Amazon, Nubank, Booking, hoje sou CAIO do Magalu. Mas o que importa para voces e que eu faco no dia a dia exatamente o que voces vao fazer agora." Duas frases, sem PowerPoint, sem humildade falsa. As notas de aula dizem explicitamente "Duas frases, nao mais", e funcionou.

A jogada de mostrar o produto final (o HTML exportado do Dia 2) logo no comeco foi boa. Ancora a expectativa. Voce ve onde vai chegar e a ansiedade diminui. E a promessa de "analise real no portfolio" nao soou como marketing vazio, porque ele abriu o notebook na frente de todo mundo e scrollou as visualizacoes.

O briefing da Marina e o que mais me chamou atencao nessa abertura. O documento simula um pedido real de gestor, com perguntas abertas e restricoes praticas ("preciso de algo visual que eu consiga mostrar para a diretoria"). Na fintech, eu recebo coisa assim toda semana, so que menos bem escrita. A frase das notas de aula, "No mundo real voces nunca comecam uma analise sem entender o que o stakeholder quer", parece obvia, mas eu ja comecei analise sem ler o pedido direito varias vezes. Vergonhoso, mas verdade.

### Bloco 1: Diagnostico do Dataset (45 min)

O conteudo tecnico aqui eu ja sabia. Shape, dtypes, head, describe, isnull. Faco isso toda semana. Mas o que eu nunca tinha feito com disciplina e a sequencia que o instrutor demonstra: shape primeiro, depois dtypes, depois head/tail, depois describe, depois isnull. Eu sempre pulo direto pro describe e depois volto quando encontro problema. A verbalizacao ao vivo do raciocinio foi o diferencial. Ele diz coisas como "Hmm, por que essa coluna esta como object?" enquanto executa, e isso nao e o tipo de coisa que voce aprende lendo documentacao.

A investigacao dos missings em review_score (cell-10) foi onde comecou a ficar interessante. O notebook pede que voce compare o preco medio dos pedidos com e sem score. Quando vi que pedidos sem avaliacao tinham preco medio significativamente mais alto, eu pensei "ah, faz sentido, cliente que gastou mais tem menos paciencia pra avaliar". Mas ai veio o tangenciamento sobre Missing At Random. As notas de aula dizem: "Notem que os missings aqui nao sao aleatorios: pedidos caros tem mais ausencia de avaliacao. Isso e o que em estatistica chamamos de Missing At Random, que apesar do nome quer dizer que a probabilidade de estar missing depende de outra variavel observada."

Eu sabia o que era MAR por nome, mas nunca tinha visto na pratica com dados reais. A ficha caiu. Na fintech, a gente tem um problema parecido: clientes que dao default tem menos dados de comportamento de pagamento, e a gente trata como MCAR. Provavelmente estamos errados.

O checkpoint (cell-18) e pratico e rapido. Verifica se os DataFrames estao carregados e com o tamanho esperado. Nao e sofisticado, mas serve pra sincronizar a turma.

### Bloco 2: Limpeza Estruturada (60 min)

Aqui teve o momento que mais mudou minha perspectiva no dia inteiro. A frase "Limpeza sem justificativa nao e limpeza, e destruicao de dados" me acertou. No trabalho, eu rodo `drop_duplicates()`, `dropna()`, e sigo em frente. Nunca documento por que tomei cada decisao. As notas de aula insistem que "cada decisao de limpeza precisa de uma razao documentada" e que "a limpeza que voces fazem hoje vai ser questionada daqui a 6 meses". Na fintech, eu ja passei por isso: o Lucas tinha um pipeline de limpeza que ninguem entendia, e quando ele saiu, tivemos que refazer tudo do zero porque nao tinha documentacao.

A demonstracao de duplicatas parciais (cell-12 e cell-23) foi bem construida. O dataset tem duplicatas de order_id com timestamps diferentes, nao duplicatas exatas. Se voce roda `.duplicated()` sem pensar, nao encontra nada. Tem que checar por chave. Eu teria caido nessa se nao tivesse visto a demonstracao.

A conversao de datas com formato misto (cell-25 e cell-26) e daquelas coisas que todo mundo aprende da pior maneira possivel. A explicacao de que `pd.to_datetime` sem `dayfirst=True` interpreta 02/10/2017 como 10 de fevereiro em vez de 2 de outubro e o tipo de armadilha que voce so descobre quando alguem percebe que os numeros nao batem.

A decisao sobre missings de review_score (cell-28) foi o momento onde mais gente travou. O notebook apresenta tres opcoes (dropar, imputar mediana, manter NaN) e a orientacao das notas de aula e nao dar a resposta, mas guiar pelo raciocinio de consequencias: "Qual e a consequencia de cada opcao?" Isso e exatamente o que eu preciso aprender a fazer: em vez de perguntar "o que faco", perguntar "o que acontece se eu fizer X vs Y vs Z".

O tangenciamento sobre outliers ("Decidir o que e outlier vs. dado legitimo e uma decisao que depende do contexto de negocio") conectou com algo que me aconteceu mes passado. Eu removi outliers de um modelo de credito sem pensar e depois descobri que aqueles "outliers" eram clientes PJ misturados com PF. Cortei um segmento inteiro da analise.

A criacao da flag `is_high_value` em vez de remover os outliers (cell-34) e uma abordagem que eu nunca tinha usado. Preserva os dados e permite analisar separadamente. Simples, mas muda tudo.

### Bloco 3: Analise Exploratoria Inicial (60 min)

Aqui eu achei que ia ser o bloco mais entediante, e tecnicamente foi o mais "basico". Histogramas, scatter plots, series temporais. Mas duas coisas me surpreenderam.

Primeira: a insistencia em interpretar cada grafico antes de fazer o proximo. As notas de aula dizem: "Gerar grafico e facil. O valor esta na interpretacao. Para cada visualizacao, escrevam uma frase: o que isso me diz? Se nao conseguem escrever a frase, o grafico nao serviu para nada." No meu trabalho, eu gero 15 graficos, coloco num slide e mando pro diretor. Nenhum tem interpretacao escrita. O diretor olha, nao entende, e pede uma reuniao pra eu explicar. Agora eu entendo por que.

Segunda: a explicacao sobre distribuicao bimodal do review_score. As notas dizem "A maioria e 5, depois 4, depois 1. Quase ninguem da 2 ou 3. Isso e tipico de avaliacoes: as pessoas ou amam ou odeiam, o meio e raro. A media aqui engana, porque sugere que a experiencia e razoavel, quando na verdade e bimodal." Eu ja sabia que distribuicoes de avaliacao sao assim, mas nunca tinha conectado com o fato de que a media se torna uma metrica ruim para esse tipo de dado. No meu trabalho, a gente usa NPS (que tambem e bimodal) e reporta media. Provavelmente estamos enganando a diretoria sem saber.

A transicao do Bloco 3 pro 4 foi uma das melhores: "Voces geraram graficos, viram distribuicoes, notaram padroes. Tudo isso e observacao. Agora vamos transformar observacoes em perguntas de negocio que a Marina consegue usar."

### Bloco 4: Perguntas Analiticas (45 min)

Esse bloco valeu a inscricao. A demonstracao da diferenca entre pergunta vaga e pergunta analitica foi a coisa mais util que eu vi em meses. "A satisfacao do marketplace e boa?" versus "Em quais categorias a nota media esta abaixo de 3.5, com pelo menos 100 avaliacoes?" Eu formulava perguntas do primeiro tipo e ficava frustrado quando a analise nao ia a lugar nenhum.

Os 3 criterios (respondivel, acionavel, especifica) viraram meu checklist mental. Na segunda-feira apos o workshop, peguei um pedido do diretor de credito ("preciso entender a inadimplencia"), reformulei como "Em quais faixas de renda a taxa de default no primeiro pagamento ultrapassou a media do portfolio nos ultimos 3 meses, considerando apenas produtos com mais de 200 contratos?" e pela primeira vez ele respondeu "e exatamente isso que eu quero saber" sem pedir reuniao de alinhamento.

O tangenciamento sobre causalidade no fechamento ("Notem que a pergunta mais interessante que voces formularam provavelmente nao pode ser respondida so com EDA") foi honesto e bem colocado. A analogia "EDA e o diagnostico, inferencia causal e o tratamento" e simples, mas gruda.

O desafio do Bloco 4 (cell-62), pedindo pra formular uma pergunta que nao da pra responder com EDA, foi o exercicio que mais me fez pensar. Eu escrevi: "Reduzir o tempo de aprovacao de credito em X horas aumenta a taxa de conversao em quanto?" E percebi que na fintech a gente trata isso como se fosse respondivel com dados historicos, quando na verdade e uma pergunta causal que exigiria um experimento.

## 4. Dia 2 - bloco a bloco

### Abertura Dia 2 (10 min)

O recap foi rapido e eficiente. Reconectar com o briefing da Marina e com as perguntas formuladas no dia anterior deu foco. A frase "Ontem voces fizeram o trabalho que ninguem ve mas que sustenta toda analise" valida uma verdade que me incomoda: no trabalho, ninguem agradece limpeza de dados. Mas sem ela nada funciona.

### Bloco 1: Analise Estatistica Aplicada (60 min)

O conceito de volume minimo (cell-5 do dia2) foi revelador na pratica. O notebook filtra categorias com menos de 100 avaliacoes antes de ranquear por nota media. A solucao do instrutor (solucao_dia2, cell-3) comenta: "Tem uma categoria com nota 1.5, incrivel, pior do marketplace inteiro. Mas olhem o volume: 3 avaliacoes. Nao da para concluir nada com 3 avaliacoes." Eu ja cometi esse erro varias vezes. A fintech tem segmentos pequenos com taxas de default aparentemente altissimas, e eu ja flagei eles como "problema" sendo que tinha 8 contratos no segmento.

A analise de atraso vs satisfacao (cell-8) foi o momento mais forte do Dia 2 do ponto de vista analitico. O notebook cria faixas de atraso (antecipado, no prazo, leve atraso, atraso, atraso grave) e calcula nota media por faixa. O padrao e brutal e monotonico: a cada faixa, a nota cai ~0.5 pontos. De 4.3 para 2.0. O comentario do instrutor na solucao ("O impacto e grande e monotonico. A cada faixa de atraso, a nota cai ~0.5 pontos. Isso e evidencia forte") mostra como apresentar uma descoberta sem afirmar causalidade.

O tangenciamento 4 foi o mais sofisticado: "A correlacao aqui e -0.3, moderada. Mas cuidado: correlacao nao e causalidade. Pode ser que regioes distantes tenham mais atraso E mais insatisfacao por outros motivos." E depois: "Para o briefing da Marina, a correlacao ja e evidencia util. Ela nao precisa de prova causal para justificar investir em logistica. Mas se alguem na diretoria perguntar 'tem certeza que e o atraso que causa a nota baixa e nao outra coisa?', a resposta honesta e: nao temos certeza. Temos evidencia consistente."

Essa frase e exatamente o que eu precisava aprender a dizer. No trabalho, ou eu afirmo causalidade sem ter (e alguem me pega), ou eu coloco tanta ressalva que o diretor descarta a analise inteira. O equilibrio entre "evidencia consistente" e "nao temos prova causal" e o tom correto.

A observacao da solucao sobre frete ("Atraso tem correlacao muito mais forte com insatisfacao do que frete. Isso refuta parcialmente a hipotese da equipe de logistica: o problema nao e o preco do frete, e o cumprimento do prazo") mostra algo que eu raramente faco: confrontar a hipotese do stakeholder com os dados e dizer que a hipotese esta parcialmente errada. Eu teria medo de falar isso pra Marina.

### Bloco 2: Visualizacoes Interpretativas (60 min)

A tabela comparativa entre grafico exploratorio e grafico final (nas notas de aula) deveria ser colada na parede de todo time de dados. "Publico: voce vs stakeholder", "Titulo: descritivo tecnico vs comunicativo (diz o insight)", "Anotacoes: nenhuma vs destaque do ponto principal". Eu nunca fiz essa distincao. Meus graficos de apresentacao sao iguais aos meus graficos de exploracao, so que com fonte maior.

A transformacao ao vivo de histograma para barras horizontais com top 5 e bottom 5 (cell-20 do dia2) foi pratica e visual. O uso de cores intencionais (vermelho para piores, verde para melhores) parece trivial, mas a maioria dos graficos que eu vejo em reuniao usa a paleta default do matplotlib, que nao comunica nada.

O gráfico de dual axis (cell-24) com volume em barras e nota em linha e um formato que eu conhecia, mas a anotacao do instrutor na solucao ("Volume cresce com sazonalidade clara, mas nota media permanece relativamente estavel") mostra como o insight esta na relacao entre as duas series, nao em cada uma isolada. Isso eu nao fazia.

O heatmap da solucao (solucao_dia2, cell-12) cruzando categoria com faixa de atraso usando nota media como cor foi a visualizacao mais sofisticada do workshop. Mostra ao mesmo tempo dois eixos de analise e permite ver interacoes. Essa celula sozinha me deu uma ideia pra um relatorio que preciso entregar na semana que vem.

### Bloco 3: Storytelling com Dados (45 min)

Esse bloco foi o que mais valor gerou pra mim em termos de carreira. A estrutura "contexto > problema > descoberta > recomendacao" das notas de aula e simples de entender, mas a demonstracao de escrever o resumo executivo ao vivo foi transformadora.

O paragrafo que o instrutor escreve na frente de todos: "A analise de 99 mil pedidos do marketplace no periodo 2017-2018 revela que a insatisfacao nao e generalizada: esta concentrada em categorias especificas (eletronicos e telefonia) e fortemente correlacionada com atraso na entrega. Pedidos entregues com mais de 7 dias de atraso tem nota media 2.5 pontos abaixo dos entregues no prazo. As 5 categorias com pior avaliacao representam 22% da receita total, o que justifica investigacao direcionada."

E depois a explicacao: "Notem o que esse paragrafo faz: da contexto (99k pedidos, periodo), identifica o padrao (concentrado, nao generalizado), quantifica (2.5 pontos, 22% da receita) e direciona acao (investigacao nas categorias especificas). A diretoria consegue decidir algo com essa informacao sem olhar um unico grafico."

Eu nunca escrevi um resumo executivo assim. Os meus sao listas de graficos: "No grafico 1 vemos que... No grafico 2 vemos que..." As notas de aula chamam isso de "legenda, nao resumo". Doeu, mas e verdade.

A secao sobre limitacoes ("A secao de limitacoes e onde mora a honestidade intelectual da analise") tambem me pegou. Eu nunca coloco limitacoes nos meus relatorios. Tenho medo de que isso enfraqueça a analise. Mas o argumento de que "a diretoria confia mais numa analise que diz 'isso e o que sabemos, isso e o que nao sabemos' do que numa que finge certeza" faz sentido. Confianca vem de transparencia, nao de omissao.

A solucao completa do instrutor no storytelling (solucao_dia2, cell-13) e o melhor documento de analise que eu ja vi como referencia didatica. As tres descobertas sao hierarquizadas (concentracao por categoria, impacto do atraso, estabilidade temporal), as recomendacoes sao especificas e conectadas aos dados, e as limitacoes sao honestas sem enfraquecer as conclusoes. A recomendacao "Prometer um prazo mais longo e entregar antes tem efeito positivo maior do que prometer prazo curto e atrasar" e o tipo de insight que faz um diretor parar e pensar.

### Bloco 4: Documento Final (30 min)

Exportar pra HTML e ver o documento completo no navegador, sem codigo, so texto e graficos, foi o momento de "cara, eu fiz isso". O formato e profissional. Da pra mandar pro diretor sem vergonha. Comparado com os slides de 3 bullets que eu faco no trabalho, e outro nivel.

## 5. Momentos marcantes

### Positivos

1. **O tangenciamento sobre MAR no Bloco 1 do Dia 1.** Nao foi so a informacao tecnica. Foi o fato de eu perceber que tenho um problema analogo no trabalho e nao sabia. Isso e o tipo de coisa que voce nao encontra num tutorial de YouTube.

2. **"Limpeza sem justificativa nao e limpeza, e destruicao de dados."** Virou mantra. Na segunda-feira eu abri meu pipeline de limpeza e comecei a documentar cada drop. Demorou 2 horas. Vai economizar semanas quando alguem questionar.

3. **A escrita do resumo executivo ao vivo no Bloco 3 do Dia 2.** Eu vi um profissional sênior transformar numeros em narrativa na minha frente, explicando cada escolha. Isso e mentoria, nao aula.

4. **O equilibrio entre "evidencia consistente" e "nao temos prova causal" no tangenciamento 4.** Esse e o tom que eu procurava. Nem covarde nem irresponsavel.

### Negativos

1. **O Bloco 3 do Dia 1 (exploracao) e o mais fraco do workshop.** Os graficos gerados sao basicos (histograma, scatter, serie temporal) e a maioria dos participantes de nivel intermediario ja sabe fazer isso. O valor esta na interpretacao, mas o notebook guiado nao forca a interpretacao o suficiente: cell-44 tem um "Sua observacao:" no final, mas muita gente pula porque nao e obrigatorio. Se fosse checkpoint, mais gente faria.

2. **O tempo do Dia 1 e apertado.** 45 minutos pro Bloco 4 (perguntas analiticas) e pouco. E o bloco mais importante do dia e eu tive que correr no final. Se o Bloco 3 fosse encurtado em 15 minutos e esse tempo fosse pro Bloco 4, ficaria melhor equilibrado.

3. **O desafio do Bloco 2 do Dia 2 (small multiples) parece descolado do fluxo.** O notebook sugere criar um grid 2x3 de distribuicoes por categoria, mas ninguem fez porque ja estavam correndo pra terminar as 4 visualizacoes obrigatorias. Desafios opcionais so funcionam se o tempo base for confortavel, e nao e.

## 6. O HTML final

O documento HTML exportado e a melhor coisa que eu ja coloquei no meu portfolio (que ate agora nao existia formalmente). Tem titulo, resumo executivo, contexto, tres descobertas com visualizacoes, recomendacoes e limitacoes. E tudo isso feito por mim, com dados reais, em formato que eu posso mandar pra qualquer recrutador.

Comparando com os relatorios que eu faco no trabalho: nao tem comparacao. Os meus sao um slide com 5 bullets e 3 graficos sem titulo. O HTML tem narrativa, quantificacao, cor intencional, anotacao nos graficos e secao de limitacoes. Se eu passasse a fazer relatorios nesse formato na fintech, provavelmente o diretor pararia de pedir reuniao de alinhamento pra entender o que eu quis dizer.

## 7. CTA e oferta

O CTA foi o menos agressivo que eu ja vi num workshop pago. Nao teve "restam poucas vagas", nao teve urgencia artificial, nao teve bonus inventado. O script de CTA diz explicitamente "NAO criar urgencia artificial" e "o tom deve ser informativo, nao vendedor". E isso que eu senti.

A parte da lacuna ("Se a Marina chegasse e perguntasse: 'Se eu reduzir o prazo de entrega em 2 dias, quanto a nota sobe?' Voces conseguiriam responder com o que fizeram hoje?") me pegou porque essa e literalmente uma pergunta que eu recebo no trabalho e nao sei responder. A transicao pro roadmap foi natural. Vi o mapa de "EDA e Limpeza" ate "Inferencia Causal" e "Lideranca em Dados" e pensei: "Eu to no degrau 1 e meu cargo exige que eu esteja no degrau 3."

Sobre a oferta: CDO a R$3.200 com 20% de desconto. Sao R$267 por mes, que e menos do que eu gasto com cafe no mes. A questao nao e se vale a pena, e se eu vou usar. Mas o formato do workshop me mostrou que o Caio pensa em processo e mentalidade, nao em ferramenta. Se o CDO mantiver esse nivel, sim, eu vou comprar. Se virar videoaula de "como fazer groupby no pandas", eu cancelo no primeiro mes.

Vou comprar o CDO. Nao pela oferta em si, mas porque em 8 horas eu aprendi mais sobre como pensar uma analise do que em 1.5 ano trabalhando. O modulo de inferencia causal e o que mais me interessa, porque e a pergunta que eu recebo toda semana e nao sei responder.

## 8. O que diria para um colega de trabalho

"Se voce ja sabe pandas basico, o workshop nao vai te ensinar codigo novo. Mas se voce, igual eu, fica perdido entre 'rodar o codigo' e 'convencer o diretor', vai valer a pena. O Dia 1 e solido mas previsivel. O Dia 2 e onde o bicho pega: a parte de storytelling e comunicacao de dados e a melhor que eu ja vi, e eu ja fiz uns 5 cursos online. O cara escreve um resumo executivo ao vivo e explica cada decisao de escrita. Isso nao existe em curso gravado. Vai preparado pra ter seus habitos questionados, especialmente se voce, igual eu, acha que 'gerar o grafico' e o mesmo que 'comunicar o resultado'."

## 9. Nota geral: 8/10

O workshop entrega o que promete. Voce sai com uma analise real no portfolio, e o processo que ele ensina (diagnostico > limpeza documentada > exploracao > perguntas > analise > comunicacao) e genuinamente util. A parte de comunicacao e storytelling no Dia 2 e excepcional e seria suficiente pra justificar a inscricao sozinha. As notas de aula mostram que o instrutor antecipou os erros mais comuns com precisao cirurgica, e os tangenciamentos sobre causalidade, MAR e modelagem sao feitos com honestidade e profundidade suficiente pra voce sentir a lacuna sem se sentir vendido.

O que impede de ser 9 ou 10 e o equilibrio do Dia 1. O Bloco 3 (exploracao) e o menos denso e poderia perder 15 minutos pro Bloco 4 (perguntas), que e onde o framework de processo realmente se constroi. Alem disso, os desafios opcionais dos notebooks sao boas ideias que ninguem tem tempo de fazer, porque o tempo base ja e justo. Se os desafios fossem integrados ao fluxo principal em vez de opcionais, o resultado final de cada aluno seria mais consistente.

Pra quem e intermediario como eu, o workshop nao muda sua vida tecnica, mas muda sua perspectiva profissional. Eu entrei achando que meu problema era nao saber codigo suficiente. Sai entendendo que meu problema e nao saber pensar a analise como processo e nao saber comunicar resultado com a clareza que o stakeholder precisa. Isso vale mais do que aprender mais uma biblioteca.
