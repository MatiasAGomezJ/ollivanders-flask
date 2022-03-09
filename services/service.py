from repository.db import db


class service:

    @staticmethod
    def inventario():

        documentos = db.get_stock()

        items = []
        for item in documentos:
            items.append(item)

        return items
