import requests
import json

city = input("Enter your city name : \n")
url = "http://api.weatherapi.com/v1/current.json?key=c7f78941de6a457ca1983336231606&q={city}"
r=requests.get(url)
print(r.text)
wdic = json.loads(r.text)
#print(wdic["current"]["temp_c"])

