import requests 

BASE = "http://127.0.0.1:5000/"

response1 = requests.get(BASE + "allLocations")
print(response1.json())

response2 = requests.put(BASE + "bookSpot",{"vehicle" : "scooter", "station" : "Marine Lines"})
print(response2.json())

response3 = requests.get(BASE + "nearestLocations/Churchgate")
print(response3.json())