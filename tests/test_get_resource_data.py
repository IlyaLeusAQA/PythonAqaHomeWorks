import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
RESOURCE_NOT_FOUND = "api/unknown/23"
MINIMAL_ENTER_YEAR = 2000
FIRST_SYMBOL_IN_COLOR = "#"


def test_get_list_resource():
    response = httpx.get(BASE_URL + LIST_RESOURCE)
    assert response.status_code == 200

    resource_data = response.json()['data']
    for item in resource_data:
        validate(item, RESOURCE_DATA_SCHEMA)
        assert item['year'] >= MINIMAL_ENTER_YEAR
        assert item['color'][0] == FIRST_SYMBOL_IN_COLOR


def test_get_single_resource():
    response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    assert response.status_code == 200

    resource_single_data = response.json()['data']
    validate(resource_single_data, RESOURCE_DATA_SCHEMA)
    assert resource_single_data['year'] >= MINIMAL_ENTER_YEAR
    assert resource_single_data['color'][0] == FIRST_SYMBOL_IN_COLOR

def test_resource_not_found():
    response = httpx.get(BASE_URL + RESOURCE_NOT_FOUND)
    assert response.status_code == 404

