from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

stations = ["Churchgate", "Marine Lines","Charni Road","Grant Road", "Mumbai Central", "Mahalaxshmi","Lower Parel","Elphinstone Road","Dadar","Matunga","Bandra","Khar Road","Santacruz","Vile Parle","Andheri","Jogeshwari","Goregoan","Malad","Kandivali","Borivali","Dahisar","Mira Road","Bhayandar","Naigoan","Vasai Road","Nala Sopara","Virar"]
distance = [0,2,3,4,5,6,8,9,11,11.5,12,15,17,18,20,22,24,27,30,32,34,37,40,44,48,52,56,60]
has_charging_station = [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0]


class AllLocations(Resource):
    def get(self):
        return {"data":"All Locations"}

class NearestLocations(Resource):
    def get(self):
        return {"data":"Nearest Locations"}

class ReachableLocations(Resource):
    def get(self,battery,vehicle):
        return {"data":"Reachable Locations","battery" : battery,"Vehicle" : vehicle}


api.add_resource(AllLocations, "/allLocations")
api.add_resource(NearestLocations, "/nearestLocations")
api.add_resource(ReachableLocations, "/reachableLocations/<int:battery>/<string:vehicle>")

if __name__ == "__main__":
    app.run(debug=True)