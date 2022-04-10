from flask_restful import Resource
from services.service import service


class inventario(Resource):
    def get(self):
        return service.inventario()
