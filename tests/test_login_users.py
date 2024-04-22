import datetime

import httpx
import pytest
from jsonschema import validate
from core.contracts import UPDATE_USER_SCHEME
import allure

BASE_URL = 'https://reqres.in/'
LOGIN_ENDPOINT = 'api/login'

@pytest.mark.parametrize('')
def test_login_users():
    response = httpx.post(BASE_URL + LOGIN_ENDPOINT,json=body)
