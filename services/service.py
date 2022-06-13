from repository.db_atlas import db_atlas
from flask_restful import fields, marshal_with

class service:

    item_schema = {
        'name': fields.String,
        'quality': fields.Integer,
        'sell_in': fields.Integer
    }

    @staticmethod
    @marshal_with(item_schema)
    def inventario():

        ## ! TODO: crear db en g
        documentos = db_atlas.get_stock()

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    @marshal_with(item_schema)
    def item_by_name(name):
        documentos = db_atlas.get_name(name)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    @marshal_with(item_schema)
    def items(name, quality, sell_in):
        documentos = db_atlas.get_item(name, quality, sell_in)

        items = []
        for item in documentos:
            items.append(item)

        return items
    
    @staticmethod
    @marshal_with(item_schema)
    def items_by_quality(quality):
        documentos = db_atlas.get_quality(quality)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    @marshal_with(item_schema)
    def items_by_sell_in(sell_in):
        documentos = db_atlas.get_sell_in(sell_in)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    def create_item(name, quality, sell_in):
        db_atlas.create_item(name, quality, sell_in)
