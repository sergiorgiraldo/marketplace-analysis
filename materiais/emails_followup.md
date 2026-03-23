# Sequência de Emails de Follow-up

## Email 1: D+0 (Imediatamente após o workshop)

**Assunto:** Seus materiais do Workshop + condição exclusiva

**Corpo:**

Oi [nome],

Acabamos de terminar o workshop e aqui estão seus materiais:

- Notebook Dia 1 (seu progresso)
- Notebook Dia 2 (seu progresso)
- Notebook com solução do instrutor (Dia 1 e 2)
- Dataset completo
- Checklist de EDA reutilizável
- Dicionário de dados

[LINK PARA PASTA DE MATERIAIS]

Você tem 7 dias de acesso para finalizar o que ficou pendente.

Como prometido, aqui está a condição exclusiva para quem participou do workshop:

**CDO (De Analista a CDO):** R$3.200/ano (20% off do preço normal)
**Zero a Analista:** [preço com 15% off]

[LINK CDO] | [LINK ZERO A ANALISTA]

A condição é válida por 72 horas (até [data/hora]).

Qualquer dúvida, responda este email.

Caio

---

## Email 2: D+1 (24 horas depois)

**Assunto:** Uma coisa que ficou de fora do workshop

**Corpo:**

Oi [nome],

Lembra quando a gente descobriu que categorias de itens grandes (móveis, decoração) concentram a insatisfação do marketplace? E que o atraso na entrega tem correlação forte com notas baixas?

A pergunta natural que surge é: se a operação reduzisse o prazo de entrega em 3 dias nessas categorias, quanto a nota subiria?

Para responder isso com confiança, você precisaria isolar o efeito do atraso de outros fatores (região, preço, categoria). Correlação mostra que andam juntos; causalidade mostra se um causa o outro.

Esse é exatamente o tipo de raciocínio que se constrói nos módulos de inferência e modelagem.

Se isso faz sentido para você, a condição exclusiva do workshop ainda está ativa por mais 48 horas:

[LINK CDO] | [LINK ZERO A ANALISTA]

Caio

---

## Email 3: D+3 (72 horas depois, encerramento)

**Assunto:** Última chance: condição do workshop expira hoje

**Corpo:**

Oi [nome],

Passando para avisar que a condição exclusiva do workshop expira hoje à meia-noite.

- CDO: R$3.200/ano (20% off)
- Zero a Analista: [preço com 15% off]

[LINK CDO] | [LINK ZERO A ANALISTA]

Se não fizer sentido agora, sem problema. O workshop e os materiais já são seus.

Caio

---

## Notas de implementação

- Usar plataforma de email com tracking de abertura e cliques
- Segmentar: quem clicou no link do CDO recebe D+1 e D+3 focados em CDO; quem clicou em Zero a Analista, idem
- Se alguém comprar após D+0, remover da sequência
- Todos os links devem ter UTM: `utm_source=workshop&utm_medium=email&utm_campaign=followup_d[0|1|3]`
