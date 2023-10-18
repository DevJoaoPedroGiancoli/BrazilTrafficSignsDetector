import easyocr
import numpy as np
from PIL import Image
import os
import glob
import csv

# Crie um objeto EasyOCR
reader = easyocr.Reader(['en', 'pt'])

# Diretório onde as imagens estão armazenadas
directory_path = r"Resultado_de_dados\imagens_inteiras"

# Defina o caminho do diretório onde você deseja salvar o arquivo
output_directory = r"Resultado_de_dados\arquivos_csv"

# Verifique se o diretório de saída existe, senão crie-o
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Nome do arquivo onde você deseja salvar os resultados em formato CSV
output_file = os.path.join(output_directory, "horarios_por_id.csv")

# Use o módulo glob para listar todas as imagens no diretório
image_files = glob.glob(os.path.join(directory_path, 'foto_inteira_do_id_*.jpg'))

# Abra o arquivo CSV de saída para escrita
with open(output_file, mode="w", newline="") as file:
    # Crie um escritor CSV
    writer = csv.writer(file)

    # Escreva a linha de cabeçalho
    writer.writerow(["ID", "Horas", "Minutos", "Segundos"])

    for image_file in image_files:
        # Extrair o ID da imagem do nome do arquivo
        image_id = int(os.path.basename(image_file).split('_')[-1].split('.')[0])

        # Carregue a imagem
        image = Image.open(image_file)

        # Defina as coordenadas da região de interesse (ROI)
        x1, y1, x2, y2 = 369, 3, 523, 400  # Coordenadas de uma imagem de 1100x600, coordenadas obtidas através de recorte.py

        # Recorte a região de interesse da imagem original
        roi_image = image.crop((x1, y1, x2, y2))

        # Converta a imagem em uma matriz numpy
        roi_image_np = np.array(roi_image)

        # Realize a detecção de texto na região recortada
        results = reader.readtext(roi_image_np)

        # Inicialize uma lista para armazenar as detecções que correspondem ao que você procura
        dados_interessantes = []

        # Procure por palavras-chave ou padrões específicos nos resultados
        for result in results:
            texto = result[1]
            if "HORÁRIO" in texto:
                # Se "HORÁRIO" for encontrado, procure os dados à direita dela
                index_horario = texto.index("HORÁRIO")
                dados_interessantes.append(texto[index_horario + len("HORÁRIO"):])

        # Escreva os dados interessantes no arquivo CSV
        for dado in dados_interessantes:
            texto_limpo = dado
            horas = texto_limpo[2:4].zfill(2)
            minutos = texto_limpo[5:7].zfill(2)
            segundos = texto_limpo[8:].zfill(2)

            # Escreva os resultados no arquivo CSV
            writer.writerow([image_id, horas, minutos, segundos])
            
            
""" 
            # Adicione um zero à esquerda se o valor for menor que 10
            if int(horas) < 10:
                horas = f"0{horas}"
            if int(minutos) < 10:
                minutos = f"0{minutos}"
            #if int(segundos) < 10:
                #segundos = f"0{segundos}"
                """