import pandas as pd

# Ler o arquivo CSV de horários
data_horarios = pd.read_csv(r'Resultado_de_dados\arquivos_csv\horarios_por_id.csv')

# Criar uma nova coluna 'HoraMinSeg' com o formato desejado
data_horarios['HoraMinSeg'] = data_horarios.apply(lambda row: f"{row['Horas']}:{row['Minutos']}:{row['Segundos']}", axis=1)

# Exibir o novo DataFrame
print(data_horarios)