from flask import Flask
from flask_restful import Api
from resources.index import index
from resources.inventario import inventario
from resources.item import item
from resources.name import name
from resources.quality import quality
from resources.sell_in import sell_in

# Cambio
app = Flask(__name__)
api = Api(app, catch_all_404s=True)


api.add_resource(index, '/')
api.add_resource(inventario, '/inventario')
api.add_resource(item, '/item')
api.add_resource(name, '/name')
api.add_resource(quality, '/quality')
api.add_resource(sell_in, '/sell_in')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)