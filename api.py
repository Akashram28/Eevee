from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

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