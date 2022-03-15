from repository.db_atlas import db_atlas
from bson.objectid import ObjectId
import pytest


@pytest.mark.get_id
def test_funciona():
    id_item = ObjectId("62285950522af60258662c1d")
    documento = {
        "name": "Aged_brie",
        "quality": 3,
        "sell_in": 4
    }
    assert list(db_atlas.get__id(id_item)) == [documento]
