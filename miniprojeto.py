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


# %%[Sprint 3] -  Funções e organização


# %%[Sprint 4] -  Análise 


# %%[Sprint 5] -  Exportação e comunicação


# %%[Sprint 6] - Previsão e entrega
