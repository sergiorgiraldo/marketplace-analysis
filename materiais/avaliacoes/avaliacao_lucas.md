# Avaliacao do Workshop - Lucas Pereira, 22 anos

## 1. Antes do workshop

Vou ser sincero: eu me inscrevi com uma mistura de esperanca e panico. Formei em Administracao faz uns meses, fiz estagio em controladoria, nao me efetivaram, e agora to mandando curriculo para tudo que e vaga de analista jr. So que toda vaga pede Python e SQL. E eu tenho no curriculo "30% de um curso do Coursera que eu abandonei". Nao e exatamente um diferencial.

O que me fez clicar no link foi a promessa de sair com algo pro portfolio. Porque esse e o meu problema real. Nas entrevistas, quando o cara pergunta "me mostra um projeto que voce fez", eu fico olhando pro nada. Nao tenho nada pra mostrar. E o workshop prometia que em dois dias eu ia ter uma analise real, com dados reais, que eu podia colocar no LinkedIn no dia seguinte. Isso me pegou.

O medo, claro, era travar. Eu sei o que e variavel, sei o que e for, sei o que e if. Nunca abri um pandas na vida. Nunca vi um DataFrame. E meu notebook e um Positivo com 4GB de RAM e HD mecanico que demora 40 segundos pra abrir o Chrome. A possibilidade de eu passar o workshop inteiro tentando instalar coisa enquanto todo mundo ja tava fazendo grafico era muito real.

## 2. Setup

O setup foi a parte que mais me deu medo, e ao mesmo tempo a que mais me aliviou. No roteiro do instrutor ta escrito que ele da 3-4 minutos pra setup e ja antecipa os problemas mais comuns: "Nao abre o Jupyter", "ModuleNotFoundError", "FileNotFoundError nos CSVs". So de ler isso eu ja imagino que nao fui o unico que ia ter problema.

No meu caso, como to no Windows, provavelmente ia precisar daquele `.venv\Scripts\activate` que ele menciona nas notas de aula. Se tivesse monitor pra me ajudar em paralelo (o roteiro fala em 1 monitor a cada 20 participantes), eu ia sobreviver. Se nao tivesse, eu ia perder facil 10 minutos so nisso. E 10 minutos num workshop de 4 horas e muito.

A celula de setup (cell-3 do notebook do Dia 1) e simples: importa pandas, numpy, matplotlib, seaborn, configura visual, e printa "Setup completo!". Aquele "Setup completo!" provavelmente seria o momento mais feliz do meu workshop, porque significa que meu computador nao me traiu. Na celula seguinte (cell-4) ja carrega os 3 CSVs e mostra o shape. Se ate aqui deu certo, to no jogo.

Com meu PC, o que me preocupava era o tamanho dos dados. Orders com ~100k linhas, items com ~113k linhas, reviews com ~99k linhas. Nao e big data, mas num notebook com 4GB de RAM e HD mecanico, qualquer operacao ia ser mais lenta que pro pessoal com Mac. Cada plt.show() ia demorar um tiquinho a mais. Nada que impossibilitasse, mas o suficiente pra eu ficar sempre um passo atras.

## 3. Dia 1 - bloco a bloco

### Abertura (15 min)

Quando o Caio abre com "Sou Caio Gomes, trabalho com dados ha 20 anos, passei por Amazon, Nubank, Booking, hoje sou CAIO do Magalu", a primeira reacao e intimidacao. Mas a frase seguinte salva: "Mas o que importa para voces e que eu faco no dia a dia exatamente o que voces vao fazer agora." Isso baixa a guarda.

Mostrar o produto final (o notebook executado do Dia 2) antes de comecar foi muito inteligente. As notas de aula dizem "isso ancora a expectativa e reduz ansiedade", e e exatamente o que aconteceu comigo. Eu vi os graficos, vi o documento de analise, e pensei: "ok, se eu chegar nisso, eu tenho algo pra mostrar". Visualizar o ponto de chegada faz diferenca pra quem ta perdido feito eu.

O briefing da Marina eu achei genial. Eu nunca pensei que analise de dados comeca com alguem te mandando um email pedindo algo. Parece obvio, mas no Coursera o exercicio era "calcule a media desse array". Aqui nao. Aqui tem uma gestora com nome, cargo, e um problema real: o NPS caiu e ela precisa de diagnostico visual pra diretoria. Isso me fez sentir que eu tava fazendo algo que importa, nao so exercicio de faculdade.

### Bloco 1: Diagnostico do Dataset (45 min)

A demonstracao ao vivo com um dataset diferente (iris ou tips) foi uma sacada que eu so entendi depois. Nas notas de aula, ele explica: "se usar o dataset do exercicio, os participantes copiam em vez de pensar." Verdade. Se ele mostrasse no dataset real, eu ia so reproduzir igual. Com um dataset diferente, eu tive que transferir o raciocinio.

O fluxo mental que ele verbaliza (shape, dtypes, head/tail, describe, isnull) parece simples, mas pra mim foi uma revelacao. Eu nao sabia que existia uma ordem logica pra olhar dados. No Coursera era "rode isso, agora rode aquilo". Aqui ele explicou o por que de cada passo: "Se uma coluna que deveria ser numerica aparece como object, ja sei que tem sujeira." Essa logica eu nunca tinha visto.

Quando fui pro exercicio (cells 4 a 15 do notebook), consegui executar tudo. O notebook guiado e muito bem feito nesse sentido: cada celula tem o codigo pronto, com comentarios que explicam o que esperar. A cell-9 que conta missings ja imprime a porcentagem, e a cell-10 que investiga se os missings sao aleatorios ja traz o merge pronto e pede que eu compare o preco medio com e sem score.

Onde eu brilhei: quando vi que o preco medio dos pedidos SEM review_score era maior que o dos COM review_score, eu entendi que tinha algo errado. Nao sabia o nome tecnico, mas a intuicao tava certa. Quando o Caio disse "isso e Missing At Random", eu pensei "ah, entao tem nome pra isso". Foi o primeiro momento em que eu senti que minha cabeca funcionava pra dados.

Onde eu travei: na cell-12, sobre duplicatas. O notebook mostra que duplicatas exatas sao zero, mas order_ids duplicados sao ~500. Eu nao entendia a diferenca. A frase do instrutor nas notas ajuda: "Executam .duplicated() e concluem 'sem duplicatas' porque as linhas nao sao identicas. Orientar para checar por order_id." Precisei dessa orientacao.

O checkpoint (cell-18) foi tranquilizante. Apareceram 4 OKs. Saber que estou no caminho certo depois de 45 minutos de incerteza faz toda a diferenca pra quem ta comecando.

### Bloco 2: Limpeza Estruturada (60 min)

Esse foi o bloco mais dificil e mais importante pra mim. A frase que grudou na cabeca: "Limpeza sem justificativa nao e limpeza, e destruicao de dados." Eu nunca tinha pensado que deletar uma linha de um Excel precisava de justificativa. Mas faz total sentido: se daqui a 6 meses alguem perguntar por que eu removi 500 linhas, a resposta precisa estar la.

A cell-23 (tratamento de duplicatas) me deu seguranca porque o codigo ja tava basicamente pronto. O `sort_values('purchase_date').drop_duplicates(subset='order_id', keep='last')` eu nao saberia escrever do zero, mas entendi o que faz: ordena por data e fica com o ultimo registro de cada pedido. A justificativa ("o registro mais recente provavelmente reflete o estado final") me ensinou que toda decisao tecnica tem que ter uma razao de negocio.

Na cell-26 (correcao de datas), o momento mais tenso. O Caio explica nas notas: "Tem '2017-10-02' e '02/10/2017' no mesmo campo. Se eu converter sem cuidado, outubro vira fevereiro." Isso eu nunca teria percebido sozinho. O `pd.to_datetime com format='mixed' e dayfirst=True` resolve, mas se eu nao tivesse o scaffold do notebook, ia converter errado e nem saber.

A decisao sobre os missings de review_score (cell-28) foi onde eu quase travei de verdade. O notebook oferece 3 opcoes: dropar, imputar pela mediana, ou manter como NaN. A opcao C ja vem como "recomendada", mas o exercicio de pensar por que fez diferenca. Se eu dropo, perco os pedidos mais caros (que sao justamente os com missing). Se imputo pela mediana, to assumindo que quem nao avaliou daria nota "media", o que provavelmente nao e verdade. Manter como NaN e filtrar nas analises que usam score preserva tudo. Essa logica de "qual e a consequencia de cada opcao" e o tipo de raciocinio que ninguem me ensinou na faculdade.

A padronizacao de categorias (cells 30-31) foi mais mecanica, mas me surpreendeu. Tinha "heath_beauty" e "health_beuty" como categorias separadas. Eu pensei: "quem digitou isso errado?" E ai lembrei que no mundo real os dados vem de gente, e gente erra. O dicionario de typos (typo_fixes) me pareceu artesanal, e eu achei bom. Mostra que nao tem magica, tem trabalho.

O tratamento de outliers (cells 33-34) introduziu a ideia de flag em vez de remocao. Criar uma coluna `is_high_value` em vez de deletar os precos extremos me pareceu elegante. Nas notas, o Caio diz que esses precos podem ser B2B misturado com B2C, e que remover pode ser "cortar 5% da receita ou descobrir um segmento novo". Isso me fez pensar em dados de um jeito diferente: nem tudo que parece errado e erro.

### Bloco 3: Analise Exploratoria Inicial (60 min)

Esse foi o bloco mais divertido. Finalmente eu tava fazendo grafico. A cell-41 gera dois graficos lado a lado: distribuicao de notas e distribuicao de precos. Ver a distribuicao bimodal das notas (concentracao em 5 e 1, quase ninguem em 2 ou 3) foi um daqueles momentos de "ah, entao e por isso que a media engana". Nas notas, o Caio explica: "as pessoas ou amam ou odeiam, o meio e raro."

A serie temporal (cell-42) mostra o volume crescendo ao longo do tempo com picos. Eu achei bonito, sinceramente. Foi a primeira vez que eu gerei um grafico que parecia profissional.

Onde travei: na cell-44 (top 15 por receita), eu precisava completar o groupby. O scaffold ja trazia o `items_clean.groupby('category')['price'].sum().nlargest(15)`, mas eu fiquei uns minutos olhando sem saber se era pra mudar algo. No final, era so executar. Mas a inseguranca de "sera que eu deveria alterar alguma coisa?" me pegou.

A observacao que o notebook pede pra documentar ("as categorias que vendem mais sao as que geram mais receita?") me fez perceber que volume e receita nao sao a mesma coisa. Uma categoria pode vender muito item barato e ter receita menor que outra que vende pouco item caro. Isso e basico, mas eu nunca tinha pensado com dados na frente.

O scatter plot de preco vs. frete (cell-46) e o calculo de correlacao me apresentaram a ideia de que duas variaveis podem andar juntas sem uma causar a outra. Mas isso ficou mais claro so no Dia 2.

### Bloco 4: Perguntas Analiticas (45 min)

Esse bloco me tirou da zona de conforto. Ate aqui eu tava executando codigo. Agora o notebook pede que eu escreva perguntas. Texto. Em Markdown. E nao e "escreva qualquer coisa": tem 3 criterios (respondivel, acionavel, especifica) e uma tabela de priorizacao.

A demonstracao ao vivo da transformacao de observacao em pergunta me ajudou muito. A sequencia "Os dados sao bons?" -> "A satisfacao do marketplace e boa?" -> "Em quais categorias a nota media esta abaixo de 3.5, com pelo menos 100 avaliacoes?" mostra claramente a diferenca entre pergunta de bar e pergunta de analista. Eu nao sabia formular perguntas desse jeito, e saiu do workshop sabendo.

Consegui formular 3 perguntas. Nenhuma era genial, mas eram especificas. Uma sobre satisfacao por categoria, uma sobre atraso, uma sobre sazonalidade. Basicamente alinhadas com o briefing da Marina.

O fechamento do Dia 1 me deixou ansioso pelo Dia 2, mas num sentido bom. Salvar os dados limpos (cell-59) e ver os 3 CSVs salvos com os shapes corretos me deu uma sensacao de "eu fiz alguma coisa hoje". Os checkpoints todos passaram. Eu sabia que no dia seguinte ia ter que responder as perguntas e montar o documento, e pela primeira vez eu senti que talvez conseguisse.

O tangenciamento sobre causalidade no final ("Notem que a pergunta mais interessante que voces formularam provavelmente nao pode ser respondida so com EDA") me incomodou produtivamente. Ele nao resolveu, e eu fiquei com aquilo na cabeca. Isso foi calculado, eu sei.

## 4. Dia 2 - bloco a bloco

### Abertura Dia 2 (10 min)

Cheguei mais confiante. Carregar os dados limpos do Dia 1 (cell-1 do notebook do Dia 2) e ver tudo funcionando foi um alivio. O recap foi rapido: 5 problemas encontrados, decisoes de limpeza documentadas, observacoes da exploracao. A frase "Ontem voces fizeram o trabalho que ninguem ve mas que sustenta toda analise" me fez sentir que o dia anterior tinha sido importante, nao so preparacao.

A cell-2, que monta o dataset consolidado com o merge triplo (orders + items + reviews) e cria colunas derivadas (total_item, delivery_days, delay_days, purchase_month), foi o momento em que eu entendi o poder do merge. Juntar 3 tabelas numa so com uma linha de codigo e ter 113 mil linhas com todas as informacoes cruzadas. Eu sabia que SQL fazia isso, mas ver em pandas ao vivo foi diferente.

### Bloco 1: Analise Estatistica Aplicada (60 min)

A analise por categoria (cell-5) me ensinou algo crucial: filtro de volume minimo. O `cat_stats[cat_stats['volume'] >= 100]` elimina categorias com poucas avaliacoes. Nas notas, o Caio explica: "Categoria com nota 1.5 e 3 avaliacoes nao significa que e a pior." Isso e o tipo de armadilha que eu cairia com certeza sem a orientacao. Eu ia olhar a nota mais baixa e sair correndo pra falar que era a pior categoria.

A analise de atraso (cell-8) foi a mais impactante. Criar faixas com `pd.cut` e ver a nota media caindo monotonicamente de ~4.3 (entrega antecipada) para ~2.0 (atraso grave acima de 14 dias) me fez entender uma relacao real nos dados. Cada faixa de atraso derruba a nota em ~0.5 pontos. E visual, e claro, e eu consegui interpretar sozinho.

A cell-10 (correlacao) me apresentou os numeros: atraso vs. nota = -0.3, frete vs. nota = algo menor. Nas notas, o instrutor comenta que "o problema nao e o preco do frete, e o cumprimento do prazo." Isso refuta a hipotese da equipe de logistica da Marina. A gente encontrou algo que contradiz o que eles pensavam. Isso me fez sentir que analise de dados nao e so confirmar o que o chefe ja acha, e as vezes o dado discorda.

A analise de sazonalidade (cell-12) mostrou crescimento com picos em novembro/dezembro. Eu associei com Black Friday na hora. O fato de a nota nao cair proporcionalmente ao volume (como as notas de aula comentam) me surpreendeu. Eu esperava que mais pedidos = mais problemas = nota pior, mas nao e bem assim.

O tangenciamento sobre causalidade nesse bloco ("correlacao nao e causalidade... pode ser que regioes distantes tenham mais atraso E mais insatisfacao por outros motivos") me incomodou de novo. E exatamente a pergunta que eu nao sei responder. E isso que o CDO ensina?

### Bloco 2: Visualizacoes Interpretativas (60 min)

Aqui eu precisei me concentrar. A diferenca entre grafico exploratorio e grafico final que ele mostra na tabela das notas de aula (publico, titulo, labels, anotacoes, escala, cores) fez sentido na pratica quando vi os graficos do notebook.

A Visualizacao 1 (cell-20) com barras vermelhas e verdes pras piores e melhores categorias ficou bonita. As cores comunicam sem precisar de legenda: vermelho = ruim, verde = bom. A linha tracejada da media geral como referencia me pareceu profissional. Eu mudei o texto do insight (que vem como placeholder "descreva o padrao que encontrou") pra algo como "categorias de itens grandes concentram a insatisfacao".

A Visualizacao 2 (cell-22) com as barras de atraso foi a que mais gostei. As cores degradando de verde para vermelho, os n= em cima de cada barra, o titulo "Quanto Mais Atraso, Pior a Avaliacao". Eu nunca pensei que um titulo de grafico deveria dizer o insight, nao so o que o eixo mostra. Essa diferenca entre "Nota vs Atraso" e "Quanto Mais Atraso, Pior a Avaliacao" e sutil mas muda tudo.

A Visualizacao 3 (cell-24) com dual axis me deu mais trabalho. Dois eixos Y, barras e linhas sobrepostas, legendas combinadas. O codigo e mais longo e eu nao entendi cada detalhe do twinx(). Mas executou, gerou o grafico, e ficou bonito. Provavelmente eu nao conseguiria reproduzir sem o scaffold, mas entendi o que o grafico comunica.

A Visualizacao 4 (cell-26) era livre. Eu fiquei uns 5 minutos sem saber o que fazer. A dica diz "heatmaps funcionam bem para cruzar duas variaveis categoricas", mas eu nunca usei heatmap. Olhando a solucao do instrutor (cell-12 do solucao_dia2), ele fez um heatmap de nota media por categoria vs. faixa de atraso, que ficou muito bom. Eu tentei algo parecido, nao ficou tao limpo, mas gerou.

### Bloco 3: Storytelling com Dados (45 min)

Esse bloco me assustou. Escrever um resumo executivo? Eu sou de Administracao, devia saber escrever relatorio, mas nunca com dados. A estrutura "contexto > problema > descoberta > recomendacao" me deu um norte.

O exemplo de resumo executivo que o Caio escreve ao vivo nas notas de aula e muito bom: "A analise de 99 mil pedidos do marketplace no periodo 2017-2018 revela que a insatisfacao nao e generalizada: esta concentrada em categorias especificas (eletronicos e telefonia) e fortemente correlacionada com atraso na entrega. Pedidos entregues com mais de 7 dias de atraso tem nota media 2.5 pontos abaixo dos entregues no prazo." Ele comenta que esse paragrafo da contexto, identifica o padrao, quantifica e direciona acao. Eu tentei reproduzir essa estrutura no meu.

Onde eu travei: na secao de limitacoes. O notebook pede que eu escreva "o que esta analise NAO responde". Eu nao sabia o que escrever. Depois de pensar, coloquei "correlacao nao e causalidade" e "os missings nao sao aleatorios". Sao as duas coisas que o instrutor repetiu tantas vezes que ficaram.

As recomendacoes foram a parte mais dificil de formular. O Caio diz nas notas que "'Melhorar a logistica' nao e acionavel. 'Investigar a causa do atraso nas categorias eletronicos e telefonia, que concentram 35% das notas abaixo de 3' e acionavel." Eu tentei ser especifico, mas provavelmente ficou generico demais.

### Bloco 4: Documento Final (30 min)

A cell-36 (exportacao para HTML) funcionou. Fiquei com medo de dar erro por causa do nbconvert, mas passou. Quando abri o HTML no navegador e vi as visualizacoes, os textos que eu escrevi, o resumo executivo, tudo formatado como um documento profissional sem mostrar nenhum codigo... eu senti algo. Tipo: "isso eu fiz. Isso existe agora. Isso eu posso mostrar."

O checkpoint final (cell-38) deu tudo OK. 8/8. Eu olhei pro resultado e pensei: "ha dois dias eu nao sabia o que era pandas."

## 5. Momentos marcantes

### Positivos

1. **O momento do MAR (Bloco 1, Dia 1)**: Quando eu vi que o preco medio dos pedidos sem review_score era maior, e o Caio deu nome ao fenomeno (Missing At Random), eu senti que meu raciocinio tava certo antes de saber o conceito. Isso e raro pra quem ta comecando. Me deu confianca de que eu consigo pensar sobre dados, nao so executar codigo.

2. **A frase "Limpeza sem justificativa nao e limpeza, e destruicao de dados" (Bloco 2, Dia 1)**: Mudou minha cabeca sobre o que significa trabalhar com dados. Nao e so rodar funcao. E documentar cada decisao. Isso e algo que eu posso falar numa entrevista: "eu documento minhas decisoes de limpeza com justificativa". Soa profissional.

3. **O HTML final (Bloco 4, Dia 2)**: Abrir o documento no navegador e ver algo que parece um relatorio real de consultoria foi o ponto alto. Eu tenho algo concreto. Eu posso mandar o link pro recrutador. Isso era exatamente o que eu precisava.

### Negativos

1. **A Visualizacao 4 livre (Bloco 2, Dia 2)**: Ficar 5-10 minutos sem saber o que fazer num exercicio livre quando todo mundo ao redor parece saber e horrivel. O notebook da uma dica ("heatmaps funcionam bem"), mas eu nao sabia usar sns.heatmap. Teria ajudado ter um exemplo minimo de heatmap no proprio notebook, tipo um scaffold mais basico pra quem nunca usou.

2. **A velocidade do Bloco 2 do Dia 1 (60 min pra 5 tarefas de limpeza)**: Eu terminei no limite. Padronizar categorias, tratar missings, criar flag de outlier, converter datas, remover duplicatas, tudo em 60 minutos. Se meu PC travasse ou se eu errasse uma celula e precisasse voltar, nao daria tempo. Pra quem e mais rapido, ok. Pra quem e lento e inseguro como eu, foi apertado.

3. **O tangenciamento sobre causalidade ficou um pouco frustrante**: O instrutor fala 3-4 vezes que "correlacao nao e causalidade" e que "para responder isso voce precisa de inferencia causal". Na terceira vez, eu ja tinha entendido que nao consigo resolver isso agora. Cada vez que ele repetia, eu sentia mais o tamanho do que eu nao sei. Acho que uma vez basta pra plantar a semente, mais que isso comeca a parecer venda.

## 6. O HTML final

Consegui gerar. Funcionou na primeira tentativa. Abri no Chrome e fiquei scrollando por uns 5 minutos. Os graficos estavam la, os textos que eu escrevi estavam la, nao tinha codigo aparecendo. Parecia um documento de verdade.

O que eu senti foi uma mistura de orgulho e impostor. Orgulho porque eu produzi aquilo. Impostor porque boa parte do codigo ja estava no scaffold e eu so executei e preenchi os espacos. Mas dai eu pensei: o resumo executivo fui eu que escrevi. As interpretacoes fui eu que escrevi. As recomendacoes fui eu que formulei. O codigo era ferramenta, o raciocinio foi meu.

Se eu mandar esse HTML pra um recrutador com um texto tipo "Aqui esta uma analise exploratoria que eu fiz num dataset de marketplace real, identificando que a insatisfacao esta concentrada em categorias especificas e fortemente correlacionada com atraso na entrega", isso ja e melhor que 90% dos portfolios de quem ta comecando. Eu sei porque eu olhei o portfolio de outros candidatos no LinkedIn. A maioria e Titanic ou iris.

## 7. CTA e oferta

O CTA comeca com reconhecimento: "Voces acabaram de fazer em 2 dias o que muita gente que trabalha com dados nao sabe fazer." Isso e verdade? Nao sei. Mas depois de 8 horas de trabalho, eu queria acreditar. E o fato de eu ter o HTML na mao dava credibilidade.

A lacuna que ele apresenta e precisa. "Se a Marina chegasse e perguntasse: 'Se eu reduzir o prazo de entrega em 2 dias, quanto a nota sobe?' Voces conseguiriam responder com o que fizeram hoje?" Nao. Eu nao consigo. E eu sinto que deveria conseguir.

O roadmap visual e bom porque mostra que o que eu fiz (EDA e Limpeza) e o primeiro degrau de 6. Nao me faz sentir burro, me faz sentir que comecei. E o Zero a Analista cobre os 3 primeiros degraus (EDA, Inferencia, Modelagem), que e exatamente o que eu precisaria pra virar analista jr.

Sobre a oferta em si: CDO a R$3.200/ano (20% off) ta fora da minha realidade. R$3.200 e quase dois meses do que meus pais gastam comigo. O Zero a Analista com 15% de desconto sobre R$1.500-2.000 seria mais viavel. Se der pra parcelar em 10x ou 12x, to falando de R$100-140/mes. Isso eu consigo convencer meus pais.

O que me incomodou: o documento de oferta exclusiva diz explicitamente "Nao oferecer parcelamento diferente do padrao". Se o padrao for 3x, nao funciona pra mim. Se for 12x, ai sim. Essa informacao faz toda a diferenca e nao aparece no CTA nem no script. Pra alguem na minha situacao, parcelamento e a variavel decisiva. O desconto de 15% e legal, mas R$1.500 a vista ou em 3x eu nao tenho.

O prazo de 72 horas me pressionou, mas nao de um jeito ruim. O script diz "Nao vou ficar repetindo isso." Eu gostei dessa postura. Nao parece aquelas vendas de "ULTIMAS VAGAS!!! CORRE!!!". E mais tipo "esta aqui, decide voce, a gente nao vai ficar te enchendo." Ai o email de D+1 conta a historia da categoria de moveis e da pergunta causal. O de D+3 e so lembrete. Nao e agressivo.

Vou comprar? Se meus pais toparem, provavelmente sim, o Zero a Analista. Nao pelo desconto em si, mas porque eu ja senti o metodo. Se o curso inteiro for como o workshop, com scaffolding que me guia sem me dar a resposta, com justificativa pra cada decisao, com dados reais em vez de iris e Titanic, entao vale. O que me convenceu nao foi o pitch, foi o HTML na minha mao.

## 8. O que diria para um amigo

"Cara, faz o workshop. Serio. Eu sei que voce acha que nao sabe Python o suficiente, eu tambem nao sabia. O notebook ja vem com a maior parte do codigo pronto, voce vai executando e preenchendo os pedacos que faltam. Nao e aula de Python, e aula de como pensar sobre dados usando Python.

Em dois dias eu sai com um relatorio HTML que parece coisa de consultoria, analisando dados reais de um marketplace brasileiro. Isso ja ta no meu GitHub e no meu LinkedIn. Antes eu nao tinha NADA pra mostrar em entrevista. Agora eu tenho uma analise onde eu limpo dados sujos, descubro que atraso na entrega destrói a satisfacao do cliente, e recomendo acoes especificas. E eu consigo explicar cada decisao que tomei.

Unica coisa: se seu computador for muito ruim, se prepara pra ter paciencia. Meu Positivo sofreu um pouco mas deu conta. E se voce for lento com codigo, o Bloco 2 do Dia 1 e apertado no tempo. Mas o pior que acontece e voce nao terminar um exercicio opcional, e tudo bem.

Ah, e no final ele faz CTA pro curso pago. Nao e forcado, nao e chateia, mas e claro que o workshop funciona como vitrine. Se voce tiver como pagar, o Zero a Analista parece valer. Se nao tiver, o workshop sozinho ja te da o portfolio."

## 9. Nota geral: 8/10

O workshop entrega o que promete. Eu entrei sem portfolio e sai com um. Eu entrei sem saber o que era pandas e sai sabendo fazer merge, groupby, agg, visualizacoes com matplotlib, e exportar um notebook pra HTML. Eu entrei achando que analise de dados era "fazer grafico bonito" e sai entendendo que e sobre tomar decisoes documentadas com base em evidencia. A estrutura do notebook guiado (scaffolding com espacos pra preencher) e perfeita pra quem ta comecando: segura a mao sem dar a resposta.

Tiro 2 pontos por tres motivos. Primeiro, o tempo e apertado pro perfil iniciante. 60 minutos pro Bloco 2 do Dia 1, com 5 tarefas de limpeza diferentes, presupoe que o participante executa rapido e nao trava. Quem trava (e iniciante trava) fica pra tras, e o sentimento de "to atrasado enquanto todo mundo ja terminou" e desmotivante. Segundo, o exercicio livre da Visualizacao 4 no Dia 2 precisa de mais scaffold pra quem nunca usou heatmap ou nao sabe por onde comecar uma analise sem roteiro. Terceiro, a questao de parcelamento na oferta nao esta resolvida pro meu perfil. R$1.500 sem opcao de parcelamento longo simplesmente nao acontece pra quem mora com os pais e ta desempregado. Se tiver 12x de R$125, e provavel que eu compre. Se for 3x de R$500, nao vai rolar. Essa informacao deveria estar clara no CTA.

Fora isso, e o melhor investimento de 8 horas que eu ja fiz em aprendizado. O Caio sabe conduzir, os materiais sao completos (o dicionario de dados, o checklist de EDA, o briefing da Marina, tudo se complementa), e o resultado e tangivel. Se eu tivesse que recomendar uma coisa so pra alguem na minha situacao, seria esse workshop.
