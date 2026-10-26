# %%[Sprint 1] -  Leitura e diagnóstico
import pandas as pd

# Leitura do arquivo CSV
df = pd.read_csv("data/Base Varejo.csv", sep=";", encoding="latin-1")

# Verificação inicial do DataFrame
df.head()
print("\nDimensões (linhas, colunas):", df.shape)
print("\nColunas:", df.columns)
print("\nInfo:")
df.info()

# Quantidade de nulos por coluna
nulos = df.isnull().sum()
print("\nQuantidade de nulos por coluna:")
print(nulos)

# Linhas duplicadas
duplicadas = df.duplicated().sum()
print("\nQuantidade de linhas duplicadas:", duplicadas)

# Inconsistências nos tipos de dados
tipos_inconsistentes = df.dtypes[df.dtypes == 'object']
print("\nColunas com tipos de dados inconsistentes:")
print(tipos_inconsistentes)

# %%[Sprint 2] -  Limpeza e padronização
# Cópia de segurança da base bruta
df_clean = df.copy()

# Remoção de colunas vazias ('Unnamed') identificadas na Sprint 1
colunas_vazias = [c for c in df_clean.columns if str(c).startswith("Unnamed") and df_clean[c].isna().all()]
df_clean = df_clean.drop(columns=colunas_vazias)

colunas_texto = ["CL_GENERO", "CL_SEG", "PR_CAT", "PR_NOME"]
textos_nulos = ["", "#n/d", "#n/a", "n/d", "nan", "null"]

for coluna in colunas_texto:
    if coluna in df_clean.columns:
        df_clean[coluna] = (
            df_clean[coluna]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.lower()
            .replace(textos_nulos, pd.NA)
        )

# Remoção de duplicatas confirmadas
linhas_antes = len(df_clean)
df_clean = df_clean.drop_duplicates()
linhas_removidas_dup = linhas_antes - len(df_clean)

# Antes vs Depois
print("=== DIAGNÓSTICO COMPARATIVO (ANTES vs DEPOIS) ===")
print(f"Linhas: {len(df)} ➔ {len(df_clean)} (Removidas: {linhas_removidas_dup} duplicatas)")
print(f"Colunas: {df.shape[1]} ➔ {df_clean.shape[1]}")
print(f"\nNulos antes:\n{df.isnull().sum()}")
print(f"\nNulos depois:\n{df_clean.isnull().sum()}")
print(f"\nDuplicatas restantes: {df_clean.duplicated().sum()}")

# Criação dos dados limpos na pasta data/
df_clean.to_csv("data/dados_limpos.csv", index=False)
print("\nBase limpa exportada com sucesso para 'data/dados_limpos.csv'!")

# %%[Sprint 3] -  Funções e organização
# Definição das funções
def tratar_dados(tabela):
    tratado = tabela.copy()
    colunas_vazias = [c for c in tratado.columns if str(c).startswith("Unnamed") and tratado[c].isna().all()]
    tratado = tratado.drop(columns=colunas_vazias)
    
    colunas_texto = ["CL_GENERO", "CL_SEG", "PR_CAT", "PR_NOME"]
    textos_nulos = ["", "#n/d", "#n/a", "n/d", "nan", "null"]
    
    for coluna in colunas_texto:
        if coluna in tratado.columns:
            tratado[coluna] = (
                tratado[coluna]
                .astype("string")
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
                .str.lower()
                .replace(textos_nulos, pd.NA)
            )
            
    tratado = tratado.drop_duplicates().copy()
    return tratado

def resumo_numerico(serie):
    return {
        "contagem_valida": serie.count(),
        "media": serie.mean(),
        "minimo": serie.min(),
        "maximo": serie.max()
    }

# Execução limpa do pipeline modularizado na Sprint 3
df_original_s3 = pd.read_csv("data/Base Varejo.csv", sep=";", encoding="latin-1")
df_limpo_s3 = tratar_dados(df_original_s3)

df_limpo_s3.to_csv("data/dados_limpos.csv", index=False)
print("Pipeline da Sprint 3 executado via funções com sucesso!")

# %%[Sprint 4] -  Análise 
import pandas as pd

# Garantindo a disponibilidade da função de resumo numérico (definida na Sprint 3)
def resumo_numerico(serie):
    return {
        "contagem_valida": serie.count(),
        "media": serie.mean(),
        "minimo": serie.min(),
        "maximo": serie.max()
    }

# Carregamento dos dados limpos
df_analise = pd.read_csv("data/dados_limpos.csv")

# Aplicação do resumo numérico na coluna escolhida (CL_FHL)
coluna_numerica_escolhida = "CL_FHL"

if coluna_numerica_escolhida in df_analise.columns:
    resultado_estatistico = resumo_numerico(df_analise[coluna_numerica_escolhida])
    print(f"=== RESUMO NUMÉRICO DA COLUNA: {coluna_numerica_escolhida} ===")
    for chave, valor in resultado_estatistico.items():
        print(f"  - {chave}: {valor}")
else:
    print(f"\nAviso: A coluna '{coluna_numerica_escolhida}' não foi encontrada.")

# Aplicação de um filtro com Significado
# Filtro de negócio: isolando apenas os registros da categoria de produtos 'alimentos'
df_alimentos = df_analise[df_analise['PR_CAT'] == 'alimentos'].copy()
print(f"\n=== FILTRO APLICADO ===")
print(f"Total de registros na categoria 'alimentos': {len(df_alimentos)}")

# Dois groupby diferentes com explicações de negócio
# Groupby 1: Agrupando por Categoria de Produto (PR_CAT) para medir o volume de itens comercializados por categoria
print("\n=== GROUPBY 1: Volume de itens por Categoria de Produto (PR_CAT) ===")
agrupado_categoria = df_analise.groupby("PR_CAT").size().reset_index(name="quantidade_itens")
print(agrupado_categoria)

# Groupby 2: Agrupando por Segmento de Cliente (CL_SEG) para medir a distribuição de compras/registros por segmento de consumidor
print("\n=== GROUPBY 2: Volume de registros por Segmento de Cliente (CL_SEG) ===")
agrupado_segmento = df_analise.groupby("CL_SEG").size().reset_index(name="total_registros")
print(agrupado_segmento)

# %%[Sprint 5] -  Exportação e comunicação


# %%[Sprint 6] - Previsão e entrega
