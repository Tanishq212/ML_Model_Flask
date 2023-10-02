import numpy 
import pickle

model = pickle.load(open("crop_predic_model.pkl","rb"))

def predict_Crop(parameters):
    paraArr = [numpy.array(parameters)]
    cropPredict = model.predict(paraArr)
    crop = cropPredict[0]
    print(crop)
    return crop