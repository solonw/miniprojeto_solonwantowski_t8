# Sprint 1 - Leitura e Diagnóstico

- **Tamanho do arquivo:** 47 MB (`Base Varejo.csv`)
- **Volume da base:** 830.000 linhas e 14 colunas.
- **Estrutura e Tipos de Dados:**
  - Carregamento bem-sucedido utilizando o separador ponto e vírgula (`;`) e codificação `latin-1`.
  - A base é composta por colunas de identificação de transação, cliente, gênero, estado civil, faixa etária, segmento, além de dados do produto comprado.
- **Inconsistências e Achados Encontrados:**
  - **Colunas Vazias:** Identificação de 4 colunas extras indesejadas no final do dataset (`Unnamed: 10` a `Unnamed: 13`), todas com 100% de valores nulos (0 valores preenchidos). Elas serão removidas na Sprint 2.
  - **Valores Nulos:** Com exceção das colunas `Unnamed`, as demais colunas principais não apresentam valores ausentes na base.
  - **Linhas Duplicadas:** Foram detectadas **96.553 linhas duplicadas** no total, que precisarão ser avaliadas e tratadas na próxima etapa de limpeza.
# Sprint 2 - 