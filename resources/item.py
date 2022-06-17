from flask_restful import Resource
from services.service import service
from resources.checking import check_item_params


class item(Resource):
    def get(self, name, quality, sell_in):

        check_item_params(name, quality, sell_in)

        return service.items(name, int(quality), int(sell_in))

    def post(self, name, quality, sell_in):

        check_item_params(name, quality, sell_in)

        quality = int(quality)
        sell_in = int(sell_in)

        service.create_item(name, quality, sell_in)
        return service.items(name, quality, sell_in)

    def delete(self, name, quality, sell_in):

        check_item_params(name, quality, sell_in)

        quality = int(quality)
        sell_in = int(sell_in)

        service.delete_item(name, quality, sell_in)
        return service.items(name, quality, sell_in)

    def put(self, name, quality, sell_in, new_name, new_quality, new_sell_in):

        check_item_params(name, quality, sell_in)
        check_item_params(new_name, new_quality, new_sell_in)

        quality = int(quality)
        sell_in = int(sell_in)

        new_quality = int(new_quality)
        new_sell_in = int(new_sell_in)

        service.update_item(name, quality, sell_in,
                            new_name, new_quality, new_sell_in)
        return service.items(new_name, new_quality, new_sell_in)
