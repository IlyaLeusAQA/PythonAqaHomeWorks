import datetime

import httpx
from jsonschema import validate
from core.contracts import UPDATE_USER_SCHEME
import allure

BASE_URL = "https://reqres.in/api/users/2"


@allure.suite('Обновление тестового юзера')
@allure.title('Обновление у юзера имени и работы')
def test_update_user_name_and_job():
    body = {
        "name": "ilya",
        "job": "QA"
    }
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL}'):
        response = httpx.put(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    update_date = response_json['updatedAt'].replace('T', ' ')

    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step(f'Получаем структуру объекта с id: {BASE_URL[-1]}'):
        validate(response_json, UPDATE_USER_SCHEME)
    with allure.step(f'Проверяем,что {response_json["name"]} равен {body["name"]}'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем,что {response_json["job"]} равен {body["job"]}'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем,что {update_date[0:16]} равен {current_date[0:16]}'):
        assert update_date[0:16] == current_date[0:16]


@allure.suite('Обновление тестового юзера')
@allure.title('Обновление у юзера имени')
def test_partial_update_user_data_only_name():
    body = {
        "name": "ilya"
    }
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL}'):
        response = httpx.patch(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    update_date = response_json['updatedAt'].replace('T', ' ')

    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step(f'Получаем структуру объекта с id: {BASE_URL[-1]}'):
        validate(response_json, UPDATE_USER_SCHEME)
    with allure.step(f'Проверяем,что {response_json["name"]} равен {body["name"]}'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем,что {update_date[0:16]} равен {current_date[0:16]}'):
        assert update_date[0:16] == current_date[0:16]


@allure.suite('Обновление тестового юзера')
@allure.title('Обновление у юзера работы')
def test_partial_update_user_data_only_job():
    body = {
        "job": "Meta"
    }
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL}'):
        response = httpx.patch(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    update_date = response_json['updatedAt'].replace('T', ' ')

    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200

    with allure.step(f'Получаем структуру объекта с id: {BASE_URL[-1]}'):
        validate(response_json, UPDATE_USER_SCHEME)
    with allure.step(f'Проверяем,что {response_json["job"]} равен {body["job"]}'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем,что {update_date[0:16]} равен {current_date[0:16]}'):
        assert update_date[0:16] == current_date[0:16]
