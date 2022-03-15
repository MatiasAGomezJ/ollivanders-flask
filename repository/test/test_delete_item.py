from repository.db_atlas import db_atlas
import pytest


@pytest.mark.delete_item
def funciona():
    name = "Alfredo"
    quality = 500
    sell_in = 200
    documento = {
        "name": name,
        "quality": quality,
        "sell_in": sell_in
    }

    # ! Crear un item para borrar
    resultado = db_atlas.delete_item()
    # ! Comprobar que al buscar el item devuelva una lista vacia
    # ! Comprobar que la cantidad de items borrados sea 1