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


# %%[Sprint 4] -  Análise 


# %%[Sprint 5] -  Exportação e comunicação


# %%[Sprint 6] - Previsão e entrega
