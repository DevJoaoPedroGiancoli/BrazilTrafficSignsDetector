import cv2
import os
from ultralytics import YOLO
from datetime import datetime, timedelta

# Load the YOLOv8 model
modelo_pt = r'Modelos\Deploys_Ultralytics_Hub\detector_de_placas_yolov8_nano.pt'

model = YOLO(f'{modelo_pt}')

# Open the video file
video_path = r"Video\Video_teste.mp4"

#model.predict(video_path, save=True, imzs=640, conf=0.7, save_txt = True)
# project=r"Resultado_de_dados\previsao_modelo_txt", name="arquivo_txt"

cap = cv2.VideoCapture(video_path)

# Certifique-se de que o diretório de saída existe, senão crie-o
save_path_cortadas = r"Resultado_de_dados\imagens_cortadas"

if not os.path.exists(save_path_cortadas ):
    os.makedirs(save_path_cortadas )
    
save_path_inteiras = r"Resultado_de_dados\imagens_inteiras"

if not os.path.exists(save_path_inteiras ):
    os.makedirs(save_path_inteiras )

# Loop through the video frames
file_num = 0
unique_id=set()
unique_id_to_class = {}  # Mapeia IDs únicos para classes
# Define a nova largura e altura desejada
new_width, new_height = 1100, 600
#project=r"Resultado_de_dados\previsao_modelo_txt", name="arquivo_txt"

start_time = datetime.now()  # Horário de início da gravação


# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        
        # Resize the frame to 640x640
        frame = cv2.resize(frame, (new_width, new_height))
                  
        # Run YOLOv8 inference on the frameaaa
        #results = model(frame)
        results = model.track(frame, persist=True,conf=0.95, save_txt=True)
        # Visualize the results on the frame

        if  results[0].boxes.id !=  None:
            
            boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
    
            ids = results[0].boxes.id.cpu().numpy().astype(int)
            
            for box, id in zip(boxes, ids):
                # Check if the id is unique
                int_id = int(id)
                if  int_id  not  in  unique_id:
                    unique_id.add(int_id)
                    
                    box = box[:4]  # Coordenadas da caixa
    
                    # Crop the image using the bounding box coordinates
                    cropped_img = frame[box[1]:box[3], box[0]:box[2]]
                    # Acesse a classe usando o índice apropriado em 'ids'
                    class_id = int(id)
                    # Calcular a diferença de tempo em relação ao início da gravação
                    current_time = datetime.now()
                    time_difference = current_time - start_time

    
                    # Save the cropped image with a unique filename
                    filename = f"imagem_destacada_do_id_{int_id}.jpg"
                    filepath = os.path.join(save_path_cortadas, filename)
                    cv2.imwrite(filepath, cropped_img)
                    filename_inteira = f"foto_inteira_do_id_{int_id}.jpg"
                    filepath_inteira = os.path.join(save_path_inteiras, filename_inteira)
                    cv2.imwrite(filepath_inteira, frame)
                    
                # Draw the bounding box and id on the frame
                
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