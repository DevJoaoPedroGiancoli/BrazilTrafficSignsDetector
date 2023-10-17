import csv

import pandas as pd

# Ler o arquivo de dados
data = pd.read_csv(r"runs\detect\predict29\labels\image0.txt", sep=' ')


# Filtrar linhas que possuem um valor no campo 'ID'
filtered_data = data[data['ID'].notnull()]

# Remover linhas duplicadas com base no ID
unique_data = filtered_data.drop_duplicates(subset='ID', keep='first')

# Salvar o resultado em um novo arquivo CSV
unique_data.to_csv('seusassaasarquivo_unico.csv', index=False)