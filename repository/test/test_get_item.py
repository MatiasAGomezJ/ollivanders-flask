from repository.db_atlas import db_atlas
import pytest


@pytest.mark.get_item
def test_funciona():
    name = "Aged_brie"
    quality = 10
    sell_in = 15
    documento = {"name": name, "quality": quality, "sell_in": sell_in}
    assert list(db_atlas.get_item(name, quality, sell_in)) == [documento]
