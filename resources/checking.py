from flask_restful import abort


def check_item_params(name, quality, sell_in):
    if not name or not quality.isnumeric() or not sell_in.isnumeric():
        abort(404, message="No se han pasado los argumentos correctos")
