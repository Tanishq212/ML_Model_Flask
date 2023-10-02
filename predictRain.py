import requests
from datetime import datetime

def predict_Precipitation(lat,lon):
    currMonth = datetime.now().month
    rainApi="https://api.weatherbit.io/v2.0/normals?lat="+str(lat)+"&lon="+str(lon)+"&start_day=01-01&end_day=12-31&tp=monthly&key=171c09c40311442fa7fae09e9576f152"
    response = requests.get(rainApi)
    prec=-1
    if(response.status_code==200):
        jsonFile=response.json()
        prec=jsonFile["data"][currMonth-1]["precip"]
    return prec 