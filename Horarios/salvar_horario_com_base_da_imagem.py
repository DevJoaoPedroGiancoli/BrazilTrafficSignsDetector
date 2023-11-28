import os
import re
import csv

# Diretório onde estão os arquivos
diretorio = "Resultado_de_dados\imagens_inteiras"

diretorio_de_saida = r"Resultado_de_dados\arquivos_csv"

# Lista para armazenar os dados a serem escritos no CSV
dados = []

# Padrão para extrair o ID e o horário dos nomes dos arquivos
padrao = r'foto_inteira_do_id_(\d+)_horario_(\d+-\d+-\d+).jpg'

# Iterar pelos arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    caminho_completo = os.path.join(diretorio, nome_arquivo)
    
    # Verificar se é um arquivo e se corresponde ao padrão
    if os.path.isfile(caminho_completo) and re.match(padrao, nome_arquivo):
        # Extrair ID e horário do nome do arquivo
        match = re.search(padrao, nome_arquivo)
        id_foto = match.group(1)
        horario = match.group(2)
        
        # Formatar o horário para "XX:XX:XX"
        horario_formatado = ":".join(horario.split('-'))
        
        # Adicionar os dados à lista
        dados.append([id_foto, horario_formatado])

# Nome do arquivo CSV de saída
nome_arquivo_csv = os.path.join(diretorio_de_saida, "dados_fotos.csv")

# Escrever os dados no arquivo CSV
with open(nome_arquivo_csv, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    escritor_csv.writerow(["ID", "Horário"])
    escritor_csv.writerows(dados)

print(f"Arquivo CSV criado com sucesso: {nome_arquivo_csv}")