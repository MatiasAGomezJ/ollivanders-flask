from mongoengine import connect
from repository.uri import uri


class db:
    @staticmethod
    def connectar_db():
        conexion = connect(host=uri)
        return conexion["ollivanders"]["ollivanders"]
