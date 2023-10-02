from flask import Flask, request, render_template
from predictRain import predict_Precipitation
from predictCrop import predict_Crop

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("my_index.html")
    
@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

# Form Function --------------------------------
@app.route("/predict" ,methods = ['POST'])
def predict():
    parameters = [float(x) for x in request.form.values()]
    crop=predict_Crop(parameters)
    return render_template("my_index.html" ,prediction_text = "The Crop is {}".format(crop))

# Api Function --------------------------------
@app.route("/predict_api",methods=['GET','POST'])
def predict_api():
    parameters = []
    lati=request.args.get('lat')
    longi=request.args.get('lon')
    prec=predict_Precipitation(lati,longi)
    print(prec)
    parameters.append(request.args.get('N'))
    parameters.append(request.args.get('P'))
    parameters.append(request.args.get('K'))
    parameters.append(request.args.get('temp'))
    parameters.append(request.args.get('hum'))
    parameters.append(request.args.get('ph'))
    parameters.append(prec)
    crop=predict_Crop(parameters)
    return crop

if  __name__=='__main__':
    app.run(debug='True',host='0.0.0.0')