from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

stations = ["Churchgate", "Marine Lines","Charni Road","Grant Road", "Mumbai Central", "Mahalaxshmi","Lower Parel","Elphinstone Road","Dadar","Matunga","Bandra","Khar Road","Santacruz","Vile Parle","Andheri","Jogeshwari","Goregoan","Malad","Kandivali","Borivali","Dahisar","Mira Road","Bhayandar","Naigoan","Vasai Road","Nala Sopara","Virar"]
distance = [0,2,3,4,5,6,8,9,11,12,14,15,17,18,20,22,24,27,30,32,34,37,40,44,48,52,56,60]
has_charging_station = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]
waiting_cars = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
waiting_trucks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
waiting_scooters = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

put_args = reqparse.RequestParser()
put_args.add_argument("vehicle", type=str,help="You forgot to put ur vehicle",required=True)
put_args.add_argument("station", type=str,help="You forgot to put ur station",required=True)

def getVehiclesWaiting(station):
    cars = waiting_cars[stations.index(station)]
    trucks = waiting_trucks[stations.index(station)]
    scooters = waiting_scooters[stations.index(station)]
    print(station)
    return {"cars" : cars, "trucks" : trucks, "scooters" : scooters}

def getWaitingTime(station):
    vehicles = getVehiclesWaiting(station)
    truck_time = vehicles['trucks']*120
    car_time = vehicles['cars']*45
    scooter_time = vehicles['scooters']*18
    return {"waitTime" : truck_time+car_time+scooter_time}
    

class AllLocations(Resource):
    def get(self):
        return {"data": stations}

class NearestLocations(Resource):
    def get(self,station):
        dislis=[]
        chdislis=[]
        near4=[]
        z = station
        x =stations.index(z)
        for i in range(0,len(stations)):
            dis=abs(distance[x]-distance[i])
            dislis.append(dis)
        for i in range(0,len(stations)):
            chdis=dislis[i]*has_charging_station[i]
            if chdis==0:
                chdis=chdis+100
            chdislis.append(chdis)
        for i in range(4):
            p=min(chdislis)
            a=chdislis.index(p)
            near4.append(stations[a])
            chdislis[a]=100
        nearest = {}
        for i in near4:
            nearest[i] = {
                "station" : i,
                "waiting_vehicles" : getVehiclesWaiting(i),
                "waitTime" : getWaitingTime(i)["waitTime"]
            }
        return {"nearest":nearest}

class BookSpot(Resource):
    def put(self):
        args = put_args.parse_args()
        vehicle = args.vehicle
        station = args.station
        if vehicle == 'car':
            waiting_cars[stations.index(station)] += 1
        elif vehicle == 'scooter':
            waiting_scooters[stations.index(station)] += 1
        elif vehicle == 'truck':
            waiting_trucks[stations.index(station)] += 1
        return {"vehicles" : getVehiclesWaiting(station),"waitTime" : getWaitingTime(station)["waitTime"]}

api.add_resource(AllLocations, "/allLocations")
api.add_resource(NearestLocations, "/nearestLocations/<string:station>")
api.add_resource(BookSpot, "/bookSpot")

if __name__ == "__main__":
    app.run(debug=True)