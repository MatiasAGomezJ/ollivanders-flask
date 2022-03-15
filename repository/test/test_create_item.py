from repository.db_atlas import db_atlas
import pytest


@pytest.mark.create_item
def test_funciona():
    name = "Alfredo"
    quality = 500
    sell_in = 200
    documento = {
        "name": name,
        "quality": quality,
        "sell_in": sell_in
    }
    resultado = db_atlas.create_item(name, quality, sell_in)
    assert list(db_atlas.get_id(resultado.inserted_id)) == [documento]
