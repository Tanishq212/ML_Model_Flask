import requests 

url = "http://localhost:5000/predict_api"
r = requests.post(url,json={'N': 8, 'P':80 ,'K':18, 'temperature':19.2369 , 'humidity':23.8995 , 'ph':6.2147 , 'rainfall':145.4284 })

print (r.json())