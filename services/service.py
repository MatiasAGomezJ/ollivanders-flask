from repository.db_atlas import db_atlas


class service:

    ## ! TODO: Marshalizar todo

    @staticmethod
    def inventario():

        ## ! TODO: crear db en g
        documentos = db_atlas.get_stock()

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    def item_by_name(name):
        documentos = db_atlas.get_name(name)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    def items(name, quality, sell_in):
        documentos = db_atlas.get_item(name, quality, sell_in)

        items = []
        for item in documentos:
            items.append(item)

        return items
    
    @staticmethod
    def items_by_quality(quality):
        documentos = db_atlas.get_quality(quality)

        items = []
        for item in documentos:
            items.append(item)

        return items

    @staticmethod
    def items_by_sell_in(sell_in):
        documentos = db_atlas.get_sell_in(sell_in)

        items = []
        for item in documentos:
            items.append(item)

        return items
