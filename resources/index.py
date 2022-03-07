from flask_restful import Resource


class index(Resource):
    def get(self):
        return '<h1>Hello World!</h1>'
