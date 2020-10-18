import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'T':21.7, 'TM':30.0, 'Tm':12.2,'SLP':1014.5,'H':52.0,'W':1.1,'V':6.3,'VM':16.5})

print(r.json())

##T	TM	Tm	SLP	H	VV	V	VM
##21.7,30.0,12.2,1014.5,52.0,1.1,6.3,16.5