import httpx
from jsonschema import validate
from core.contracts import RESOURCE_DATA_SCHEMA
import allure

BASE_URL = "https://reqres.in/"
LIST_RESOURCE = "api/unknown"
SINGLE_RESOURCE = "api/unknown/2"
RESOURCE_NOT_FOUND = "api/unknown/23"
FIRST_SYMBOL_IN_COLOR = "#"
FIND_ID = 2


@allure.suite('Получение различных данных ресурсов')
@allure.title('Получение списка ресурсов')
def test_get_list_resource():
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL + LIST_RESOURCE}'):
        response = httpx.get(BASE_URL + LIST_RESOURCE)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    resource_data = response.json()['data']
    for item in resource_data:
        with allure.step(f'Получаем структуру объекта с id: {item["id"]}'):
            validate(item, RESOURCE_DATA_SCHEMA)
            with allure.step(f'Проверяем, что {item["year"] % 10} меньше {item["id"]} на 1'):
                assert item['year'] % 10 == item['id'] - 1
            with allure.step(f'Проверяем, что первый символ цвета {item["color"]} начинается с {FIRST_SYMBOL_IN_COLOR}'):
                assert item['color'][0] == FIRST_SYMBOL_IN_COLOR


@allure.suite('Получение различных данных ресурсов')
@allure.title('Получение данных одного ресурса')
def test_get_single_resource():
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL + SINGLE_RESOURCE}'):
        response = httpx.get(BASE_URL + SINGLE_RESOURCE)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    resource_single_data = response.json()['data']
    with allure.step(f'Получаем структуру объекта с id: {resource_single_data["id"]}'):
        validate(resource_single_data, RESOURCE_DATA_SCHEMA)
    with allure.step(f'Проверяем, что {resource_single_data["year"] % 10} меньше {resource_single_data["id"]} на 1'):
        assert resource_single_data['year'] % 10 == resource_single_data['id'] - 1
    with allure.step(f'Проверяем, что первый символ цвета {resource_single_data["color"]} начинается с {FIRST_SYMBOL_IN_COLOR}'):
        assert resource_single_data['color'][0] == FIRST_SYMBOL_IN_COLOR
    with allure.step(f'Проверяем, что id ресурса {resource_single_data["id"]}  равен искомому id = {FIND_ID} '):
        assert resource_single_data['id'] == FIND_ID


@allure.suite('Получение различных данных ресурсов')
@allure.title('Попытка запроса на получение несуществующего ресурса')
def test_resource_not_found():
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL + RESOURCE_NOT_FOUND}'):
        response = httpx.get(BASE_URL + RESOURCE_NOT_FOUND)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 404

