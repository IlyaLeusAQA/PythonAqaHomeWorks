import httpx
import allure

BASE_URL = "https://reqres.in/api/users/2"


@allure.suite('Удаление тестового юзера')
@allure.title('Удаление тестового юзера по id')
def test_delete_user_data():
    with allure.step(f'Отправляем запрос по адресу: {BASE_URL}'):
        response = httpx.patch(BASE_URL, json=body)

    with allure.step(f'Проверяем код ответа'):
        assert response.status_code == 200
