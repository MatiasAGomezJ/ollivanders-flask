from flask_restful import fields, marshal_with
from repository.get_db_atlas import get_db_atlas
from flask import g


class service:

    item_schema = {
        'name': fields.String,
        'quality': fields.Integer,
        'sell_in': fields.Integer
    }

    @staticmethod
    @marshal_with(item_schema)
    def inventario():
        db_atlas = get_db_atlas()
        documentos = db_atlas.get_stock()

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    @marshal_with(item_schema)
    def item_by_name(name):
        db_atlas = get_db_atlas()
        documentos = db_atlas.get_name(name)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    @marshal_with(item_schema)
    def items(name, quality, sell_in):
        db_atlas = get_db_atlas()
        documentos = db_atlas.get_item(name, quality, sell_in)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    @marshal_with(item_schema)
    def items_by_quality(quality):
        db_atlas = get_db_atlas()
        documentos = db_atlas.get_quality(quality)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    @marshal_with(item_schema)
    def items_by_sell_in(sell_in):
        db_atlas = get_db_atlas()
        documentos = db_atlas.get_sell_in(sell_in)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    def create_item(name, quality, sell_in):
        db_atlas = get_db_atlas()
        db_atlas.create_item(name, quality, sell_in)

    @staticmethod
    def delete_item(name, quality, sell_in):
        db_atlas = get_db_atlas()
        db_atlas.delete_item(name, quality, sell_in)

    @staticmethod
    def update_item(name, quality, sell_in, new_name, new_quality, new_sell_in):
        db_atlas = get_db_atlas()
        db_atlas.update_item(name, quality, sell_in,
                             new_name, new_quality, new_sell_in)
