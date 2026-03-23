# Checklist de Análise Exploratória de Dados

> **Dica:** Consulte o glossário (`glossario_python.md`) para explicação dos termos técnicos de Python e pandas usados neste checklist e nos notebooks.

Use este checklist em qualquer análise nova. Cada etapa tem perguntas-guia para não esquecer nada.

---

## 1. Diagnóstico

- [ ] Carregar dados e verificar shape (linhas x colunas)
- [ ] Examinar tipos de cada coluna (dtypes) - algum tipo parece errado?
- [ ] Olhar primeiras e últimas linhas (head/tail) para ver formato real
- [ ] Contar valores ausentes por coluna - qual % de missings?
- [ ] Verificar se os missings são aleatórios ou seguem padrão
- [ ] Procurar duplicatas (exatas e parciais por chave)
- [ ] Checar estatísticas descritivas (describe) - min/max fazem sentido?
- [ ] Listar valores únicos de colunas categóricas

**Perguntas-guia:**
O dataset tem o tamanho esperado? Alguma coluna deveria ser numérica mas está como texto? Existem missings que parecem depender de outra variável?

## 2. Limpeza

- [ ] Tratar duplicatas (decidir qual manter, documentar critério)
- [ ] Padronizar formatos (datas, categorias, strings)
- [ ] Decidir sobre missings: dropar, imputar, ou manter? Documentar por quê
- [ ] Identificar outliers - são erros ou dados legítimos?
- [ ] Se outliers legítimos: criar flag ou segmentar
- [ ] Converter tipos quando necessário (strings para datas, etc.)
- [ ] Validar que a limpeza não removeu dados demais

**Perguntas-guia:**
A decisão sobre cada problema está documentada com justificativa? A limpeza alterou significativamente a distribuição dos dados?

## 3. Exploração Univariada

- [ ] Distribuição de cada variável numérica (histogramas)
- [ ] Contagem de cada variável categórica (barplots)
- [ ] Identificar assimetrias, bimodalidade, concentrações
- [ ] Série temporal se houver componente de tempo

**Perguntas-guia:**
Alguma distribuição surpreende? Alguma variável é dominada por um único valor?

## 4. Exploração Bivariada

- [ ] Scatter plots para pares de variáveis numéricas
- [ ] Boxplots de variáveis numéricas por categorias
- [ ] Correlações entre variáveis numéricas
- [ ] Crosstabs entre variáveis categóricas

**Perguntas-guia:**
Existem relações fortes entre variáveis? Alguma correlação é inesperada?

## 5. Formulação de Perguntas

- [ ] Formular perguntas que sejam respondíveis com os dados
- [ ] Cada pergunta é acionável? (a resposta muda uma decisão?)
- [ ] Cada pergunta é específica? (vira uma análise concreta?)
- [ ] Priorizar por impacto x viabilidade

## 6. Análise Direcionada

- [ ] Para cada pergunta: calcular métrica principal
- [ ] Segmentar por grupos relevantes
- [ ] Documentar interpretação numérica

## 7. Visualização Final

- [ ] Cada gráfico tem título descritivo
- [ ] Eixos rotulados com unidades
- [ ] Anotação com insight principal
- [ ] Gráficos salvos em alta resolução

## 8. Comunicação

- [ ] Resumo executivo (compreensível sem ver gráficos)
- [ ] Contexto + Descobertas + Recomendações
- [ ] Limitações documentadas
- [ ] Próximos passos sugeridos
