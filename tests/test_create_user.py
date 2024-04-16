import datetime

import httpx
from jsonschema import validate
from core.contracts import CREATED_USER_SCHEME
import allure

BASE_URL = "https://reqres.in/api/users"


@allure.suite('Создание тестового юзера')
@allure.title('Создание юзера с именем и работой')
def test_create_user_with_name_and_job():
    body = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL}'):
        response = httpx.post(BASE_URL, json=body)
    response_json = response.json()
    current_date = str(datetime.datetime.utcnow())
    creation_date = response_json['createdAt'].replace('T', ' ')

    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 201

    with allure.step(f'Получаем структуру объекта с id: {response_json["id"]}'):
        validate(response_json, CREATED_USER_SCHEME)
    with allure.step(f'Проверяем,что {response_json["name"]} равен {body["name"]}'):
        assert response_json['name'] == body['name']
    with allure.step(f'Проверяем,что {response_json["job"]} равен {body["job"]}'):
        assert response_json['job'] == body['job']
    with allure.step(f'Проверяем,что {creation_date[0:16]} равен {current_date[0:16]}'):
        assert creation_date[0:16] == current_date[0:16]
    with allure.step(f'Проверяем,что id : {int(response_json["id"])} не равен 0'):
        assert int(response_json['id']) != 0


@allure.suite('Создание тестового юзера')
@allure.title('Создание юзера без имени и без работы')
def test_create_user_without_name_and_without_job():
    body = {

    }
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL}'):
        response = httpx.post(BASE_URL, json=body)

    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 400



