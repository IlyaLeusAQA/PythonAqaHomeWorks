import json
import httpx
import pytest
from jsonschema import validate
from core.contracts import SUCCESSFUL_LOGIN_USER_SCHEME, ERROR_RESPONSE_SCHEME
import allure

BASE_URL = 'https://reqres.in/'
LOGIN_ENDPOINT = 'api/login'
json_file = open('/Users/ilyaleus/PycharmProjects/lessonPython/core/data_providers/test_login_data.json')
login_data = json.load(json_file)
MISSED_EMAIL = 'Missing email or username'
MISSED_PASSWORD = 'Missing password'


@allure.suite('Авторизация пользователя')
@allure.title('Авторизация с различными входными даннными')
@pytest.mark.parametrize('body', login_data)
def test_login_users(body):
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL + LOGIN_ENDPOINT}'):
        response = httpx.post(BASE_URL + LOGIN_ENDPOINT, json=body)

    response_json = response.json()
    email = body['email']
    password = body['password']

    if len(email) > 0 and len(password) > 0:
        with allure.step(f'Итог валидации входных данных: {response_json}'):
            validate(response_json, SUCCESSFUL_LOGIN_USER_SCHEME)
        with allure.step(f'Проверяем код ответа'):
            assert response.status_code == 200
    elif len(email) > 0:
        with allure.step(f'Итог валидации входных данных: {response_json}'):
            validate(response_json, ERROR_RESPONSE_SCHEME)
        with allure.step(f'Проверяем код ответа'):
            assert response.status_code == 400
        with allure.step(f'Проверяем, что ошибка {response_json["error"]}'):
            assert response_json['error'] == MISSED_PASSWORD
    else:
        with allure.step(f'Итог валидации входных данных: {response_json}'):
            validate(response_json, ERROR_RESPONSE_SCHEME)
        with allure.step(f'Проверяем код ответа'):
            assert response.status_code == 400
        with allure.step(f'Проверяем, что ошибка {response_json["error"]}'):
            assert response_json['error'] == MISSED_EMAIL
