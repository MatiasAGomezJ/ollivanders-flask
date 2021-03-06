import pytest
import api
import json

@pytest.mark.item_endpoint
def test_get():
    app = api.app.test_client()

    name = "Sulfuras"
    quality = 50
    sell_in = 7

    resp = app.get(f"/item/{name}/{quality}/{sell_in}")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == name
    assert resp_dict.get("quality") == quality
    assert resp_dict.get("sell_in") == sell_in

    assert resp.get_data(True) == '[{"name": "' + name + '", "quality": ' + str(
        quality) + ', "sell_in": ' + str(sell_in) + '}]\n'


def test_post_delete():
    app = api.app.test_client()

    # Post

    name = "Time-Turner"
    quality = 25
    sell_in = 13

    resp = app.post(f"/item/{name}/{quality}/{sell_in}")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == name
    assert resp_dict.get("quality") == quality
    assert resp_dict.get("sell_in") == sell_in

    assert resp.get_data(True) == '[{"name": "' + name + '", "quality": ' + str(quality) + ', "sell_in": ' + str(sell_in) + '}]\n'

    # Delete

    resp = app.delete(f"/item/{name}/{quality}/{sell_in}")

    assert resp.status_code == 200

    assert not json.loads(resp.data.decode())

    assert resp.get_data(True) != '[{"name": "' + name + '", "quality": ' + str(
        quality) + ', "sell_in": ' + str(sell_in) + '}]\n'


def test_post_put():
    app = api.app.test_client()

    # Post

    name = "Time-Turner"
    quality = 25
    sell_in = 13

    resp = app.post(f"/item/{name}/{quality}/{sell_in}")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == name
    assert resp_dict.get("quality") == quality
    assert resp_dict.get("sell_in") == sell_in

    assert resp.get_data(True) == '[{"name": "' + name + '", "quality": ' + str(
        quality) + ', "sell_in": ' + str(sell_in) + '}]\n'

    new_name = "Wand"
    new_quality = 3
    new_sell_in = 5

    resp = app.put(
        f"/item/{name}/{quality}/{sell_in}/{new_name}/{new_quality}/{new_sell_in}")

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == new_name
    assert resp_dict.get("quality") == new_quality
    assert resp_dict.get("sell_in") == new_sell_in

    assert resp.get_data(True) == '[{"name": "' + new_name + '", "quality": ' + str(
        new_quality) + ', "sell_in": ' + str(new_sell_in) + '}]\n'
