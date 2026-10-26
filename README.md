# Miniprojeto de Análise de Varejo

## Identificação
* **Autor:** Sólon Wantowski
* **Turma:** T8

---

# Sprint 1 - Leitura e Diagnóstico

- **Tamanho do arquivo:** 47 MB (`Base Varejo.csv`)
- **Volume da base:** 830.000 linhas e 14 colunas.
- **Estrutura e Tipos de Dados:**
  - Carregamento bem-sucedido utilizando o separador ponto e vírgula (`;`) e codificação `latin-1`.
  - A base é composta por colunas de identificação de transação, cliente, gênero, estado civil, faixa etária, segmento, além de dados do produto comprado.
- **Inconsistências e Achados Encontrados:**
  - **Colunas Vazias:** Identificação de 4 colunas extras indesejadas no final do dataset (`Unnamed: 10` a `Unnamed: 13`), todas com 100% de valores nulos (0 valores preenchidos). Elas foram removidas na Sprint 2.
  - **Valores Nulos:** Com exceção das colunas `Unnamed`, as demais colunas principais não apresentam valores ausentes na base.
  - **Linhas Duplicadas:** Foram detectadas **96.553 linhas duplicadas** no total, que precisaram ser avaliadas e tratadas na etapa de limpeza.

# Sprint 2 - Limpeza e Tratamento

- **Remoção de Colunas Vazias:** Eliminação automática das 4 colunas extras indesejadas no final do dataset (`Unnamed: 10` a `Unnamed: 13`), que continham 100% de valores nulos.
- **Padronização Textual:** 
  - Conversão de todas as colunas de texto (`CL_GENERO`, `CL_SEG`, `PR_CAT`, `PR_NOME`) para letras minúsculas (*lowercase*).
  - Remoção de espaços em branco excedentes no início e fim dos textos.
  - Substituição de strings nulas ou inconsistentes dispersas na base (como `""`, `"#n/d"`, `"#n/a"`, `"n/d"`, `"nan"`, `"null"`) para o padrão nulo oficial do Pandas (`NaN`).
- **Tratamento de Linhas Duplicadas:** 
  - Exclusão das **96.553 linhas duplicadas** identificadas na base, garantindo a integridade analítica dos dados.
- **Volume Resultante:** 
  - A base limpa foi reduzida de 830.000 para **733.447 linhas** válidas, mantendo as colunas essenciais tratadas e prontas para as próximas etapas.

# Sprint 3 - Funções e Modularização

- **Criação da Função `tratar_dados(tabela)`:** 
  - Pipeline automatizado que engloba a remoção de colunas `Unnamed` vazias, a padronização de textos e a eliminação de duplicatas de forma reutilizável.
- **Criação da Função `resumo_numerico(serie)`:** 
  - Função modular projetada para calcular métricas estatísticas essenciais (`contagem_valida`, `media`, `minimo`, `maximo`) em colunas numéricas elegíveis.
- **Persistência dos Dados:** 
  - Exportação oficial da base tratada para o arquivo `data/dados_limpos.csv`, garantindo a separação limpa entre os dados brutos e os dados processados.

# Sprint 4 - Análise, Filtros e Agrupamentos

- **Resumo Estatístico:** 
  - Aplicado na coluna numérica `CL_FHL`, retornando uma contagem válida de 733.447 registros, média de ~1.15, valor mínimo de 0 e máximo de 4.
- **Filtro Aplicado:** 
  - Isolamento da categoria de produtos `alimentos`, totalizando 384.197 registros para análises focadas de negócio.
- **Groupby 1 (`PR_CAT`):** 
  - Agrupamento por Categoria de Produto para medir o volume de itens comercializados por setor (com forte destaque para os setores de alimentos e bebidas).
- **Groupby 2 (`CL_SEG`):** 
  - Agrupamento por Segmento de Cliente para medir o volume de registros por perfil de consumidor (destaque para o segmento `b` com 468.505 registros).

# Sprint 5 - Exportação, Conclusões e Fechamento

- **Exportação Final:** 
  - Geração do arquivo definitivo `varejo_limpo.csv` na raiz do repositório.
- **Arquitetura do Pipeline:** 
  - A **leitura** ocorre a partir da base bruta, a **transformação** é executada pelas funções dedicadas e agrupamentos do Pandas, e a **gravação** consolida os datasets limpos e os artefatos visuais gerados.
- **Conclusões baseadas em números reais:**
  1. O volume total de registros válidos na base tratada consolida um total robusto de 733.447 linhas.
  2. A categoria de produtos 'alimentos' lidera o volume de registros com 384.197 ocorrências, representando a maior fatia da base.
  3. A categoria 'bebidas' vem logo em seguida com 382.643 registros, demonstrando alta sinergia e proximidade de consumo com o setor de alimentos.
  4. O segmento de clientes 'b' concentra o maior volume de registros comerciais (468.505 ocorrências), superando os segmentos 'a' e 'c'.
  5. A coluna numérica 'CL_FHL' apresentou uma média de aproximadamente 1.15 dependentes/núcleo familiar por cliente válido.
- **Recomendação:** 
  - Focar campanhas de marketing cruzado (*cross-selling*) combinando ofertas entre as categorias de alimentos e bebidas direcionadas especialmente ao segmento de clientes 'b'.
- **Limitação:** 
  - A base de dados possui ausência de carimbos temporais (datas e horários de transação), limitando análises preditivas de sazonalidade e tendências de longo prazo.

---

## Como Executar
1. Certifique-se de ter o Python e a biblioteca Pandas instaladas (`pip3 install pandas`).
2. Abra o projeto no VS Code.
3. Execute as Sprints sequencialmente no terminal interativo para validar o pipeline e gerar os arquivos de saída.