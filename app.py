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
    data.append(request.args.get('ph'))
    data.append(request.args.get('rainfall'))
    features = [np.array(data)]
    prediction = model.predict(features)
    print(prediction)
    output = prediction[0]
    return output

if  __name__=='__main__':
    app.run()