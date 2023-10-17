from ultralytics import YOLO

# Carregue um modelo
model = YOLO("Placas de Transito BR.v3i.yolov8\yolov8n.pt")  # carregue um modelo pré-treinado (recomendado para treinamento)

# Use o modelo
model.train(data="Placas de Transito BR.v3i.yolov8\data.yaml", epochs=3)  # treine o modelo com seu arquivo data.yaml encontrado no dataset do roboflow
metrics = model.val()  # avalie o desempenho do modelo no conjunto de validação

#path = model.export(format="onnx")  # exporte o modelo para o formato ONNX por exemplo