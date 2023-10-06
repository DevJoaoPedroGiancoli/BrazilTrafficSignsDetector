from ultralytics import YOLO
import cv2

# Carregue o modelo
model = YOLO(r"C:\Users\joao.giancoli.PLANOSENG\Desktop\Codigos\RoboflowPlacas\runs\detect\train3\weights\best.pt")

# Abra o vídeo
cap = cv2.VideoCapture(r'#caminho_absoluto')  # substitua '/content/ERS122_teste.mp4' pelo caminho para o seu vídeo

# Defina o codec e crie um objeto VideoWriter
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('saida.mp4', fourcc, 20.0, (640,480))  # substitua 'saida.mp4' pelo nome do arquivo de saída

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # Faça a previsão
        results = model.predict(frame)

        # Escreva o quadro no arquivo de saída
        out.write(frame)

    else:
        break

# Libere tudo se o trabalho estiver terminado
cap.release()
out.release()