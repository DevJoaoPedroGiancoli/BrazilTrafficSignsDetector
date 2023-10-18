import os

destination_dir =r"Resultado_de_dados\previsao_modelo_txt"

# Caminho completo do arquivo image0.txt no diretório de destino
destination_file_path = os.path.join(destination_dir, 'image0.txt')

# Verifique se o arquivo existe no caminho especificado
if os.path.exists(destination_file_path):
    # Adicione uma linha de cabeçalho ao arquivo
    with open(destination_file_path, 'r') as file:
        content = file.read()

    # Se o arquivo já contiver o cabeçalho, não o adicione novamente
    if not content.startswith("Sign_class x1 y1 x2 y2 ID"):
        with open(destination_file_path, 'w') as file:
            file.write("Sign_class x1 y1 x2 y2 ID\n" + content)

    print('Cabeçalho adicionado com sucesso.')
else:
    print(f'Arquivo {destination_file_path} não encontrado.')
