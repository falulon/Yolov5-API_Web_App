import io

from numpy import imag
import torch
import base64
from io import BytesIO
from PIL import Image

# Model
# model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True, force_reload=True)

model_path = "../custom.pt" #@param ["yolov5s", "yolov5/runs/train/exp/weights/best.pt", "custom.pt"] {allow-input: true}
    # model_conf = 0.25 #@param {type:"slider", min:0, max:1, step:0.01}
    # model_iou = .45 #@param {type:"slider", min:0, max:1, step:0.01}

model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
# img = Image.open("zidane.jpg")  # PIL image direct open

# Read from bytes as we do in app
with open("35.jpg", "rb") as file:
    img_bytes = file.read()
img = Image.open(io.BytesIO(img_bytes))

results = model(img, size=640)  # includes NMS
# image_as_string = base64.b64encode(cv2.imencode('.jpg', results)[1]).decode()
#     # return image_as_string
# print(image_as_string)
# with open('./image_as_string', 'wb') as f:
#                         f.write(image_as_string)
# results.save()

results.imgs # array of original images (as np array) passed to model for inference
results.render()  # updates results.imgs with boxes and labels
for im in results.imgs:
    buffered = BytesIO()
    im_base64 = Image.fromarray(im)
    im_base64.save(buffered, format="JPEG")
    print(base64.b64encode(buffered.getvalue()).decode('utf-8'))  # base64 encoded image with results
# print(results.pandas().xyxy[0])
