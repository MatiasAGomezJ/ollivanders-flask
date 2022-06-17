import pytest
import api
import json

@pytest.mark.get_resource
def test_funciona():
    app = api.app.test_client()
    resp = app.get('/item/Sulfuras/50/7')

    assert resp.status_code == 200

    resp_dict = json.loads(resp.data.decode())[0]

    assert resp_dict.get("name") == "Sulfuras"
    assert resp_dict.get("quality") == 50
    assert resp_dict.get("sell_in") == 7

    assert resp.get_data() == b'[{"name": "Sulfuras", "quality": 50, "sell_in": 7}]\n'
