from PIL import Image
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO(r'Modelos\Deploys_Ultralytics_Hub\detector_de_placas_yolov8_nano.pt')

# Run inference on 'bus.jpg'
results = model(r'Images')  # results list

""" # Show the results
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
    im.show()  # show image
    im.save('results.jpg')  # save image """
    

for item in results:
    print(item)