from flask_restful import Resource, abort, request
from services.service import service


class sell_in(Resource):
    def get(self):
        args = request.args
        sell_in = args.get("sell_in")
        if sell_in.isnumeric():
            sell_in = int(sell_in)

        if not sell_in:
            abort(404, message="No se han pasado los argumentos necesarios")

        return service.items_by_sell_in(sell_in)