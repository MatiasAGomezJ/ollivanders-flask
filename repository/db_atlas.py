from repository.stock import stock
from repository.get_db import get_db


class db_atlas:
    @staticmethod
    def get_stock():
        db = get_db()
        return db.connectar_db().find({}, {"_id": False})

    @staticmethod
    def get_item(name, quality, sell_in):
        db = get_db()
        return db.connectar_db().find({"name": name, "quality": quality, "sell_in": sell_in}, {"_id": False})

    @staticmethod
    def get_id(id_item):
        db = get_db()
        return db.connectar_db().find({"_id": id_item}, {"_id": False})

    @staticmethod
    def get_name(name):
        db = get_db()
        return db.connectar_db().find({"name": name}, {"_id": False})

    @staticmethod
    def get_quality(quality):
        db = get_db()
        return db.connectar_db().find({"quality": quality}, {"_id": False})

    @staticmethod
    def get_sell_in(sell_in):
        db = get_db()
        return db.connectar_db().find({"sell_in": sell_in}, {"_id": False})

    @staticmethod
    def create_item(name, quality, sell_in):
        db = get_db()
        return db.connectar_db().insert_one({"name": name, "quality": quality, "sell_in": sell_in})

    @staticmethod
    def delete_item(name, quality, sell_in):
        db = get_db()
        return db.connectar_db().delete_one({"name": name, "quality": quality, "sell_in": sell_in})
