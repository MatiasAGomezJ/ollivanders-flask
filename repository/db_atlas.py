from repository.stock import stock
from repository.db import db


class db_atlas:
    @staticmethod
    def get_stock():
        return db.connectar_db().find({}, {"_id": False})

    @staticmethod
    def get_item(name, quality, sell_in):
        return db.connectar_db().find({"name": name, "quality": quality, "sell_in": sell_in}, {"_id": False})

    @staticmethod
    def get_name(name):
        return db.connectar_db().find({"name": name}, {"_id": False})

    @staticmethod
    def get_quality(quality):
        return db.connectar_db().find({"quality": quality}, {"_id": False})

    @staticmethod
    def get_sell_in(sell_in):
        return db.connectar_db().find({"sell_in": sell_in}, {"_id": False})

    @staticmethod
    def create_item(name, quality, sell_in):
        db.connectar_db().insert_one({"name": name, "quality": quality, "sell_in": sell_in})
