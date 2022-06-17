from flask_restful import Resource, abort
from services.service import service


class quality(Resource):
    def get(self, quality):
        
        if quality.isnumeric():
            quality = int(quality)

        if not quality:
            abort(404, message="No se han pasado los argumentos necesarios")
        
        return service.items_by_quality(quality)