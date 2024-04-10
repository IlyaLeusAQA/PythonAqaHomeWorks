import httpx
from jsonschema import validate
from core.contracts import USER_DATA_SCHEMA
import allure

BASE_URL = "https://reqres.in/"
LIST_USERS = "api/users?page=2"
SINGLE_USER = "api/users/2"
EMAIL_ENDS = "@reqres.in"
USER_NOT_FOUND = "api/users/23"

@allure.suite('Получение различных данных пользователей')
@allure.title('Получение списка пользователей')
def test_get_list_users():
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL + LIST_USERS}'):
        response = httpx.get(BASE_URL + LIST_USERS)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    users_data = response.json()['data']
    for item in users_data:
        with allure.step(f'Проверяем структура объекта c id: {item["id"]}'):
            validate(item, USER_DATA_SCHEMA)
            with allure.step(f'Проверяем, что email оканчивается на {EMAIL_ENDS}'):
                assert item['email'].endswith(EMAIL_ENDS)
            with allure.step(f'Проверяем ссылку на аватар'):
                assert item['avatar'] == f'{BASE_URL}img/faces/{item["id"]}-image.jpg'

@allure.suite('Получение различных данных пользователей')
@allure.title('Получение данных одного пользователя')
def test_get_single_user():
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL + SINGLE_USER}'):
        response = httpx.get(BASE_URL + SINGLE_USER)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    users_data = response.json()['data']
    with allure.step(f'Проверяем структура объекта c id: {users_data["id"]}'):
        validate(users_data, USER_DATA_SCHEMA)
    with allure.step(f'Проверяем, что email оканчивается на {EMAIL_ENDS}'):
        assert users_data['email'].endswith(EMAIL_ENDS)
    with allure.step(f'Проверяем ссылку на аватар'):
        assert users_data['avatar'] == f'{BASE_URL}img/faces/{users_data["id"]}-image.jpg'

@allure.suite('Получение различных данных пользователей')
@allure.title('Попытка получения данных по несуществующему пользователю')
def test_user_not_found():
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL + USER_NOT_FOUND}'):
        response = httpx.get(BASE_URL + USER_NOT_FOUND)
    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 404


