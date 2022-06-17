import pytest
import api
import json

@pytest.mark.item_endpoint
def test_get():
    app = api.app.test_client()
    resp = app.get('/item/Sulfuras/50/7')

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == "Sulfuras"
    assert resp_dict.get("quality") == 50
    assert resp_dict.get("sell_in") == 7

    assert resp.get_data() == b'[{"name": "Sulfuras", "quality": 50, "sell_in": 7}]\n'


def test_post_delete():
    app = api.app.test_client()

    name = "Time-Turner"
    quality = 25
    sell_in = 13
    document = {
        name: name,
        quality: quality,
        sell_in: sell_in
    }

    resp = app.post(f"/item/{name}/{quality}/{sell_in}")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == name
    assert resp_dict.get("quality") == quality
    assert resp_dict.get("sell_in") == sell_in

    assert resp.get_data(True) == '[{"name": "' + name + '", "quality": ' + str(quality) + ', "sell_in": ' + str(sell_in) + '}]\n'
