import argparse
import io
from io import BytesIO
import base64
from PIL import Image

import torch
from flask import Flask, request, render_template

app = Flask(__name__)
DETECTION_URL = "/analyze"

@app.route("/", methods=["GET"])
def serve_index(): 
    return render_template("index.html")


@app.route(DETECTION_URL, methods=["POST"])
def predict():
    print("image recieved")
    if request.files.get("image"):
        image_file = request.files["image"]
        image_bytes = image_file.read()
        img = Image.open(io.BytesIO(image_bytes))
        
        results = model(img, size=640) # call the model
        data = img_as_text(results)
        return {'image_data': data, 'xyxy': results.pandas().xyxy[0].to_json(orient="records")}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask api exposing yolov5 model")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model_path = "./custom.pt" 
    # model_conf = 0.25 #@param {type:"slider", min:0, max:1, step:0.01}
    # model_iou = .45 #@param {type:"slider", min:0, max:1, step:0.01}
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)
    # .autoshape()  # force_reload = recache latest code 

def img_as_text(results):
    results.imgs # array of original images (as np array) passed to model for inference
    results.render()  # updates results.imgs with boxes and labels
    
    buffered = BytesIO()
    im_base64 = Image.fromarray(results.imgs[0])
    im_base64.save(buffered, format="JPEG")
    return (base64.b64encode(buffered.getvalue()).decode('utf-8'))  # base64 encoded image with results
    # model.eval()
    
app.run(host="0.0.0.0", port=args.port)  # debug=True causes Restarting with stat
