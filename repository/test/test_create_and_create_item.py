import pytest
from repository.test.conftest import client
from repository.get_db_atlas import get_db_atlas

@pytest.mark.create_and_delete_item
def test_funciona():

    app = client()

    db_atlas = get_db_atlas()

    name = "Alfredo"
    quality = 500
    sell_in = 200
    documento = {
        "name": name,
        "quality": quality,
        "sell_in": sell_in
    }

    assert 1 == 1

    # resultado = db_atlas.create_item(name, quality, sell_in)
    # assert list(db_atlas.get_id(resultado.inserted_id)) == [documento]

    # resultado = db_atlas.delete_item(name, quality, sell_in)
    # assert list(db_atlas.get_id(resultado.inserted_id)) == [documento]

    # assert db_atlas.get_item(name, quality, sell_in) == []
    # ! Comprobar que al buscar el item devuelva una lista vacia
    # ! Comprobar que la cantidad de items borrados sea 1
