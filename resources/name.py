from flask_restful import Resource
from services.service import service


class name(Resource):
    def get(self, name):
        return service.item_by_name(name)