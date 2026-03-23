## Why

O Dia 1 está com muita informação e o tempo de aula está excessivamente apertado. Estamos usando no limite as 4 horas disponíveis. Mas o problema central não é operacional: é de narrativa.

A estrutura narrativa de um bom dia de curso segue uma curva assimétrica: começo forte o suficiente para criar expectativa e engajamento, barriga no meio onde fica o conteúdo denso e técnico, e final mais alto que o início — não apenas "também bom", mas emocionalmente mais intenso do que quando o dia começou. O Dia 1 atual falha nas duas extremidades e por razões diferentes.

**Início fraco:** o Bloco 1 abre com iris ou tips do seaborn. O participante acabou de ouvir a promessa "você vai analisar um dataset de marketplace real brasileiro" e a primeira coisa que vê é dado de flores ou gorjetas de restaurante americano. A quebra de expectativa vai na direção errada: em vez de ampliar o senso de possibilidade, reduz. O primeiro contato não tem gancho — e gancho no início serve para sustentar a barriga do meio, quando o conteúdo fica denso e o cansaço aparece.

**Final fraco (e abaixo do início):** o encerramento termina em logística (salvar arquivos, checkpoint, preview do Dia 2). Não é só que o final é ruim — ele é mais baixo do que o início, o que inverte a curva e deixa a memória afetiva do dia num ponto descendente. Ninguém sai animado de um dia que terminou em instrução de download.

## What Changes

- **Redesenha o início** do Dia 1: os primeiros minutos são no dataset Olist real — 99 mil pedidos de um marketplace que eles conhecem. O instrutor abre `orders` na demonstração sem nenhum dataset intermediário. A abertura estabelece o gancho que vai sustentar a barriga técnica dos blocos do meio.
- **Remove** a demonstração com iris/tips do Bloco 1; demonstração passa a ser feita diretamente no Olist desde o primeiro minuto
- **Reduz** o Bloco 1 de 45 para ~30 min (demo parcial em `orders` + exercício em `items` e `reviews`)
- **Move** o salvamento de arquivos (save + download CSV) para acontecer em paralelo durante a revisão entre pares no Bloco 4, liberando os 10 min finais
- **Redesenha** o encerramento do Dia 1 (últimos 10-15 min) como cliffhanger: instrutor pega a melhor pergunta da sala, começa a responder com EDA ao vivo, chega perto da resposta, mostra a ambiguidade (correlação vs. causalidade), e para sem resolver — "isso tem um nome. Amanhã a gente enfrenta."
- O tempo liberado pelo Bloco 1 (~15 min) é redistribuído: ~5 min absorvidos na revisão entre pares (Bloco 4), ~10 min para o novo encerramento

## Capabilities

### New Capabilities

_(nenhuma)_

### Modified Capabilities

- `workshop-conteudo`: O Bloco 1 do Dia 1 muda de 45 min com demo em dataset separado para ~30 min com demo direto no Olist. O encerramento do Bloco 4 muda de logística de fechamento para sequência de cliffhanger.
- `notas-dia1`: As notas do Bloco 1 precisam descrever a nova demo (direto no Olist, só a tabela `orders`, raciocínio verbal sobre o que mostrar). As notas do Bloco 4 precisam incluir o script do novo encerramento: seleção da melhor pergunta, análise parcial ao vivo, revelação da ambiguidade, parada deliberada sem resolução.

## Impact

- `materiais/roteiro_instrutor.md` — tabela de tempos do Bloco 1 e sequência do Bloco 4
- `materiais/notas_aula.md` — fala do Bloco 1 (remove referência ao iris/tips) e script do encerramento do Dia 1
- `notebooks/dia1_fundamentos_cleaning.ipynb` — remover células de demo com iris/tips; mover célula de save para dentro do bloco de revisão entre pares
