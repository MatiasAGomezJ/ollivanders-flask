from flask_restful import Resource
from services.service import service
from resources.checking import check_item_params


class item(Resource):
    def get(self, name, quality, sell_in):

        check_item_params(name, quality, sell_in)

        return service.items(name, int(quality), int(sell_in))

    def post(self, name, quality, sell_in):

        check_item_params(name, quality, sell_in)
        
        service.create_item(name, quality, sell_in)
        return service.items(name, int(quality), int(sell_in)), 201
