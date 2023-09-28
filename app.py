# import uvicorn
# from fastapi import FastAPI
# from manage import manage 

import numpy as np
from flask import Flask, request ,jsonify, render_template
import pickle

app = Flask(__name__)
  
model = pickle.load(open("crop_predic_model.pkl","rb"))

@app.route("/")
def Home():
    return render_template("my_index.html")
    
@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/predict" ,methods = ['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    print(prediction)
    return render_template("my_index.html" , prediction_text = "The Crop is {}".format(prediction))
    # return render_template(prediction)

@app.route("/predict_api",methods=['GET','POST'])
def predict_api():
    data = []
    data.append(request.args.get('N'))
    data.append(request.args.get('P'))
    data.append(request.args.get('K'))
    data.append(request.args.get('temperature'))
    data.append(request.args.get('humidity'))
    # data.append(5)
    # data.append(300)
    data.append(request.args.get('ph'))
    data.append(request.args.get('rainfall'))
    features = [np.array(data)]
    prediction = model.predict(features)
    print(prediction)
    output = prediction[0]
    return output
# if in host parameter,we don't provide any ip address then by defalut it will run on 
# ip address "127.0.0.1:5000" but if we specify host parameter with ip address
# "0.0.0.0:5000" then it will run on th ip address through which local system is connected
if  __name__=='__main__':
    app.run(debug=True)


# import uvicorn
# from fastapi import FastAPI
# from manage import manage 

# import json
# import requests
# from datetime import datetime
# import numpy as np
# from flask import Flask, request ,jsonify, render_template
# import pickle

# app = Flask(__name__)
  
# model = pickle.load(open("crop_predic_model.pkl","rb"))

# latitude=28.6692 
# longitude=77.4538
# currentMonth = datetime.now().month
# access_key = 'e3c993d2-a441-4695-8762-76e2f70c46f7'
# headers = {
#     'X-Meteum-API-Key': access_key
# }
# rain_url="https://api.meteum.ai/v1/climate?lat="+str(latitude)+"&lon="+str(longitude)
# response = requests.get(rain_url, headers=headers)
# if(response.status_code==200):
#     response=response.json()
#     print(currentMonth)
#     data=response[currentMonth-1]
#     rain=data["prec"]

# @app.route("/")
# def Home():
#     return render_template("my_index.html")
    
# @app.route("/login")
# def login():
#     return render_template("login.html")



# @app.route("/register")
# def register():
#     return render_template("register.html")


# @app.route("/predict" ,methods = ['POST'])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     print(prediction)
#     return render_template("my_index.html" , prediction_text = "The Crop is {}".format(prediction))
#     # return render_template(prediction)

# @app.route("/predict_api",methods=['GET','POST'])
# def predict_api():
#     data = []
#     data.append(request.args.get('N'))
#     data.append(request.args.get('P'))
#     data.append(request.args.get('K'))
#     data.append(request.args.get('temperature'))
#     data.append(request.args.get('humidity'))
#     data.append(request.args.get('ph'))
#     data.append(request.args.get('rainfall'))
#     # data.append(rain)
#     print(rain)
#     features = [np.array(data)]
#     prediction = model.predict(features)
#     print(prediction)
#     output = prediction[0]
#     return output

# if  __name__=='__main__':
#     app.run(debug='True',host='192.168.29.248')