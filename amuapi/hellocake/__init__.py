from flask import Blueprint
from flask_restful import Resource, Api

bp = Blueprint("hellocake", __name__, url_prefix="/hello-cake")
api = Api(bp)


class Cake(Resource):
    def get(self):
        return {
            "msg": "Hello! It's my favorite cake!",
            "cake": "Red Velvet",
        }


api.add_resource(Cake, "/cake")

