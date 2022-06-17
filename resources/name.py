from flask_restful import Resource, abort
from services.service import service


class name(Resource):
    def get(self, name):

        if not name:
            abort(404, message="No se han pasado los argumentos necesarios")

        return service.item_by_name(name)

    def post(self, name):
        quality = 1
        sell_in = 1

        if not name:
            abort(404, message="No se han pasado los argumentos necesarios")

        service.create_item(name, quality, sell_in)
        return service.items(name, int(quality), int(sell_in)), 201
