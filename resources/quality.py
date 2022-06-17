from flask_restful import Resource
from services.service import service
from resources.checking import check_quality_param

class quality(Resource):
    def get(self, quality):

        check_quality_param(quality)

        quality = int(quality)
        
        return service.items_by_quality(quality)