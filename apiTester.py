import requests 

BASE = "http://127.0.0.1:5000/"

response1 = requests.get(BASE + "allLocations")
print(response1.json())

response2 = requests.get(BASE + "nearestLocations")
print(response2.json())

response3 = requests.get(BASE + "reachableLocations/30/car")
print(response3.json())