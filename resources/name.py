from flask_restful import Resource, abort, request
from services.service import service


class name(Resource):
    def get(self):
        args = request.args
        name = args.get("name")

        if not name:
            abort(404, message="No se han pasado los argumentos necesarios")

        return service.item_by_name(name)
