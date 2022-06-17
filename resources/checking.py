from flask_restful import abort


def check_item_params(name, quality, sell_in):
    if not name or not quality.isnumeric() or not sell_in.isnumeric():
        abort(404, message="No se han pasado los argumentos correctos")


def check_quality_param(quality):
    if not quality.isnumeric():
        abort(404, message="El parametro 'quality' tiene que ser un número")


def check_sell_in_param(sell_in):
    if not sell_in.isnumeric():
        abort(404, message="El parametro 'sell_in' tiene que ser un número")
