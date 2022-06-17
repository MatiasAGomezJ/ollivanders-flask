from flask_restful import Resource
from services.service import service
from resources.checking import check_sell_in_param


class sell_in(Resource):
    def get(self, sell_in):

        check_sell_in_param(sell_in)

        sell_in = int(sell_in)

        return service.items_by_sell_in(sell_in)
