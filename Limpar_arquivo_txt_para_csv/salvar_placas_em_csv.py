import csv
import pandas as pd
import os

# Ler o arquivo de dados
data = pd.read_csv(r"Resultado_de_dados\previsao_modelo_txt\image0.txt", sep=' ')

# Defina o caminho do diretório onde você deseja salvar o arquivo
output_directory = r"Resultado_de_dados\arquivos_csv"

# Verifique se o diretório de saída existe, senão crie-o
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Filtrar linhas que possuem um valor no campo 'ID'
filtered_data = data[data['ID'].notnull()]

# Remover linhas duplicadas com base no ID
unique_data = filtered_data.drop_duplicates(subset='ID', keep='first')

# Adicionar um cabeçalho
unique_data.columns = ['Sign_class', 'x1', 'y1', 'x2', 'y2', 'ID']

# Construa o caminho completo para o arquivo de saída no diretório de saída
output_path = os.path.join(output_directory, 'classe_de_placas_por_id.csv')

# Salvar o resultado em um novo arquivo CSV
unique_data.to_csv(output_path, index=False)