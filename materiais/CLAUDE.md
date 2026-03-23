# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que e este repositorio

Workshop presencial de 2 dias (4h/dia) sobre Analise de Dados com Python. Publico heterogeneo: migrantes de carreira, juniores, curiosos. O workshop funciona como topo de funil para os cursos pagos (CDO, Zero a Analista).

O dataset e o Olist (Brazilian E-Commerce) do Kaggle, com 5 problemas injetados propositalmente pelo script de preparacao: duplicatas parciais, datas em formato misto, missings MAR em review_score, outliers B2B, e typos em categorias.

## Sobre regras do Workshop 

Eu vou seguir o formato que usamos em aulas muito grandes. Temos que garantir que o inicio seja forte e interessante, e o final seja forte, interessante, engraçado, empolgante. Isto garante que cada dia o aluno depois se lembre dos pontos máximos do curso com prazer. Se o dia começa ou termina fraco, isso garante uma situação pior.

## Comandos

```bash
# Setup inicial (requer kaggle API key em ~/.kaggle/kaggle.json)
uv sync
uv run python scripts/download_olist.py
uv run python scripts/prepare_dataset.py

# Jupyter (para desenvolvimento dos notebooks)
uv run jupyter notebook --notebook-dir=notebooks

# Exportar notebook do Dia 2 como HTML (documento final do aluno)
uv run jupyter nbconvert --to html --no-input notebooks/dia2_analise_comunicacao.ipynb --output ../materiais/analise_marketplace
```

## Estrutura

- `data/raw/` - CSVs originais do Olist (9 arquivos, ~180MB total). Nao versionados.
- `data/prepared/` - 3 tabelas com problemas injetados (orders, items, reviews) + versoes _clean geradas pelo notebook do Dia 1.
- `notebooks/` - 4 notebooks: dia1 e dia2 (exercicio do aluno com scaffolding), solucao_dia1 e solucao_dia2 (gabarito do instrutor).
- `materiais/` - Roteiro do instrutor, notas de aula, script de CTA, checklist de EDA, briefing da Marina, dicionario de dados, visualizacoes geradas, e o HTML final exportado.
- `scripts/` - download_olist.py (baixa do Kaggle) e prepare_dataset.py (injeta os 5 problemas).

## Pipeline de dados

`data/raw/` (Olist original) → `scripts/prepare_dataset.py` (injeta problemas, seed=42) → `data/prepared/*.csv` (dataset do workshop) → notebook dia1 (limpeza) → `data/prepared/*_clean.csv` → notebook dia2 (analise e visualizacoes) → `materiais/analise_marketplace.html`

## Os 5 problemas injetados no dataset

Definidos em `scripts/prepare_dataset.py` com seed fixa (42). Qualquer alteracao muda os problemas e quebra a referencia nos notebooks e nas notas de aula.

1. **Missings MAR**: ~6% de review_score removido em pedidos >R$300 e categorias tech
2. **Duplicatas parciais**: 500 orders duplicados com timestamps levemente diferentes
3. **Datas mistas**: 20% de purchase_date convertido para formato dd/mm/yyyy
4. **Outliers B2B**: 200 itens com preco multiplicado por 10-50x
5. **Typos em categorias**: 15% de 8 categorias com variacoes de grafia

## Materiais do instrutor

O roteiro (`materiais/roteiro_instrutor.md`) define tempos e logistica. As notas de aula (`materiais/notas_aula.md`) definem o conteudo discursivo: o que falar, que conceitos explicar, que erros antecipar, como fazer as transicoes. O script de CTA (`materiais/script_cta.md`) cobre os 15 minutos finais de encerramento e oferta. Os tres se complementam sem sobreposicao.

## OpenSpec

O projeto usa OpenSpec para gestao de mudancas. Specs em `openspec/specs/` cobrem 4 dominios: conteudo do workshop, dataset, entregaveis, e funil de conversao. Changes ativas ficam em `openspec/changes/`. Usar os comandos `/opsx:*` para interagir.
