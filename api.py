from flask import Flask
from flask_restful import Api
from resources.index import index
from resources.inventario import inventario
from resources.item import item
from resources.name import name
from resources.quality import quality
from resources.sell_in import sell_in
from create_app import create_app
# Cambio

app = create_app()

api = Api(app, catch_all_404s=True)

# curl localhost:5000
api.add_resource(index, '/')

# curl localhost:5000/inventario
api.add_resource(inventario, '/inventario')

# curl localhost:5000/item/Aged_brie/22/8
api.add_resource(item, '/item/<name>/<quality>/<sell_in>',
                 '/item/<name>/<quality>/<sell_in>/<new_name>/<new_quality>/<new_sell_in>')

# curl localhost:5000/name/Aged_brie
api.add_resource(name, '/name/<name>')

# curl localhost:5000/quality/22
api.add_resource(quality, '/quality/<quality>')

# curl localhost:5000/sell_in/8
api.add_resource(sell_in, '/sell_in/<sell_in>')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
