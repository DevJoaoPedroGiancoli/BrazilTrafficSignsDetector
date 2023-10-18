import os
import shutil

# Diretório base onde os diretórios "predictX" estão localizados
base_dir = r'runs\detect'

# Diretório de destino para mover o arquivo
destination_dir = r'Resultado_de_dados\previsao_modelo_txt'

# Encontre todos os diretórios que começam com "predict" em ordem alfabética reversa
predict_directories = sorted([d for d in os.listdir(base_dir) if d.startswith('predict')], reverse=True)

# Verifique se há pelo menos um diretório "predictX"
if predict_directories:
    # Obtenha o diretório mais recente (o primeiro da lista ordenada)
    most_recent_predict_dir = predict_directories[0]

    # Crie o caminho completo para o arquivo image0.txt
    source_file_path = os.path.join(base_dir, most_recent_predict_dir, 'labels', 'image0.txt')

    # Crie o caminho completo de destino para o nova pasta
    destination_file_path = os.path.join(destination_dir, 'image0.txt')

    # Mova o arquivo para o diretório de destino
    shutil.move(source_file_path, destination_file_path)

    print(f'Arquivo movido com sucesso para {destination_file_path}')
else:
    print('Nenhum diretório "predictX" encontrado.')
    


