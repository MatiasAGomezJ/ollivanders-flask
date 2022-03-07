from flask_restful import Resource
from get_documents import get_datos


class datos(Resource):
    def get(self):
        return get_datos()
