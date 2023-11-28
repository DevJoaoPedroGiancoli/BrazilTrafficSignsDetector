import cv2
import os
from ultralytics import YOLO
from datetime import datetime, timedelta

# Load the YOLOv8 model
modelo_pt = r'Modelos\Deploys_Ultralytics_Hub\detector_de_placas_yolov8_nano.pt'
model = YOLO(f'{modelo_pt}')

# Open the video file
video_path = r"Video\Video_teste.mp4"
cap = cv2.VideoCapture(video_path)

# Certifique-se de que o diretório de saída existe, senão crie-o
save_path_cortadas = r"Resultado_de_dados\imagens_cortadas"
if not os.path.exists(save_path_cortadas):
    os.makedirs(save_path_cortadas)

save_path_inteiras = r"Resultado_de_dados\imagens_inteiras"
if not os.path.exists(save_path_inteiras):
    os.makedirs(save_path_inteiras)

# Defina manualmente o horário de início da gravação IMPORTANTISSIMO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
start_time = datetime(2023, 10, 30, 17, 35, 9)

# Loop through the video frames
file_num = 0
unique_id = set()

# Define a nova largura e altura desejada
new_width, new_height = 1100, 600

while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Resize the frame to 640x640
        frame = cv2.resize(frame, (new_width, new_height))

        # Run YOLOv8 inference on the frame
        results = model.track(frame, persist=True, conf=0.95, save_txt=True)
        #results = model.predict(frame, conf=0.95, save_txt=True)

        if results[0].boxes.id is not None:
            boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
            ids = results[0].boxes.id.cpu().numpy().astype(int)

            for box, id in zip(boxes, ids):
                int_id = int(id)

                if int_id not in unique_id:
                    unique_id.add(int_id)
                    box = box[:4]

                    # Crop the image using the bounding box coordinates
                    cropped_img = frame[box[1]:box[3], box[0]:box[2]]
                    class_id = int(id)

                    # Calcular o horário de detecção somando os segundos desde o início do vídeo ao horário de início
                    seconds_elapsed = cap.get(cv2.CAP_PROP_POS_FRAMES) / cap.get(cv2.CAP_PROP_FPS)
                    detection_time = start_time + timedelta(seconds=seconds_elapsed)


                    # Salvar a imagem recortada com o horário relativo
                    filename = f"imagem_destacada_do_id_{int_id}_horario_{detection_time.strftime('%H-%M-%S')}.jpg"
                    filepath = os.path.join(save_path_cortadas, filename)
                    cv2.imwrite(filepath, cropped_img)

                    filename_inteira = f"foto_inteira_do_id_{int_id}_horario_{detection_time.strftime('%H-%M-%S')}.jpg"
                    filepath_inteira = os.path.join(save_path_inteiras, filename_inteira)
                    cv2.imwrite(filepath_inteira, frame)

                frame = results[0].plot()

        # Display the annotated frame
        cv2.imshow(f"Detectando pelo modelo: {modelo_pt}", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()