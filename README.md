# YOLOv5 Object Detection model api/app with Flask (Python / JS)
Based on : https://github.com/ultralytics/yolov5/tree/master/utils/flask_rest_api
           https://github.com/falulon/moles-classifier
           
This repo contains example apps for exposing the [YOLOv5](https://github.com/ultralytics/yolov5) object detection model from [Pytorch hub](https://pytorch.org/hub/ultralytics_yolov5/) via a [Flask](https://flask.palletsprojects.com/en/1.1.x/) api/app.

## Web app
Simple app consisting of a form where you can upload an image, and see the inference result of the model in the browser. Run:

Visit http://localhost:5000/ in your browser

![image](https://user-images.githubusercontent.com/79255543/168185163-c87e4bcf-1d18-4164-a54e-e0c86a199eed.png)
Image by Elena Joland (https://unsplash.com/@labf)

## Rest API
Simple rest API exposing the model for consumption by another service. 

The model inference results are returned as JSON consist of the result image and xyxy boxes coordinations :

```
[{'class': 0,
  'confidence': 0.8197850585,
  'name': 'person',
  'xmax': 1159.1403808594,
  'xmin': 750.912902832,
  'ymax': 711.2583007812,
  'ymin': 44.0350036621},
 {'class': 0,
  'confidence': 0.5667674541,
  'name': 'person',
  'xmax': 1065.5523681641,
  'xmin': 116.0448303223,
  'ymax': 713.8904418945,
  'ymin': 198.4603881836},
 {'class': 27,
  'confidence': 0.5661227107,
  'name': 'tie',
  'xmax': 516.7975463867,
  'xmin': 416.6880187988,
  'ymax': 717.0524902344,
  'ymin': 429.2020568848}]
```

## Docker
The example dockerfile shows how to expose the rest API.
You can test your changes locally by installing Docker and using the following command:

```
docker build -t moles-classifier . && docker run --rm -it -p 5000:5000 moles-classifier
```

It will run a container and initiate server.py and serve app/view/index.html on your localhost:5000

# You'd like to do the following: 

1. Replace _custom.pt_ (YOLOv5 model) in /app/ with your _best.pt_ trained model. 
2. Customize the UI of _app/view/index.html_
                   and _app/static/style.css_

3.  [Deploying to Heroku](https://github.com/falulon/moles-classifier/issues/1) 

##### **A. Install Heroku, log in and make sure it is connected to your Github account**

##### **B. Create a new pipeline**
- choose the repo from github, connect and create a Pipeline.

![image](https://user-images.githubusercontent.com/79255543/161379274-05585c2c-2e3b-4b68-9597-60f740f2957c.png)
##### **C. Under Staging, New app, create new App.**

![image](https://user-images.githubusercontent.com/79255543/161379308-6acfe51d-e2c9-4da3-b421-e193d9ad7ed4.png)
##### **D. Edit App Settings**
- Change the stack from heroku to container by running this command in your terminal:
`heroku stack:set container --app my-detection-app-name`
– Enable Automatic deploys (still in App settings) 
– Deploy

![image](https://user-images.githubusercontent.com/79255543/161379353-f350c3fe-9651-4037-98c8-89027264e693.png)


If there is some error, find it by running: 
`heroku logs --tail`

You may like to run also
```
heroku git:remote -a my-detection-app-name
heroku addons:add heroku-postgresql:hobby-dev --app my-detection-app-name
```

### **The app is up and updates on every time you make some changes and push to Github.**


## reference
https://github.com/ultralytics/yolov5/tree/master/utils/flask_rest_api
