from flask_restful import Resource, abort, request
from services.service import service


class item(Resource):
    def get(self):
        args = request.args
        name = args.get("name")
        quality = args.get("quality")
        sell_in = args.get("sell_in")

        if not name or not quality or not sell_in:
            abort(404, message="No se han pasado los argumentos necesarios")

        return service.items(name, int(quality), int(sell_in))
