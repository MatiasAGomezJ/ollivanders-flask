import json

with open("datos.json") as json_file:
    stock = json.load(json_file)


def get_datos():
    return stock
