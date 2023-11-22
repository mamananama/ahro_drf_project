from django.test import TestCase, Client
import requests

HOST = 'http://localhost:8000'
LOGIN_URL = HOST + '/account/login/'

# 사용자가 본 HTML파일에 입력 form에서 입력한 데이터
LOGIN_INFO = {
    "username": "test_account",
    "password": "whoareyou!",
}


class TestAccounts(TestCase):
    def setUp(self):
        print("----- accounts app test -----")
        self.client = Client()
        self.token = ""

    def test_login(self):
        print("----- accounts: login test -----")
        response = requests.post(LOGIN_URL, data=LOGIN_INFO)
        self.assertEqual(response.status_code, 200)
        print(response.status_code)
        print(response.json())
        print(response.json()['access_token'])
        self.token = response.json()['access_token']
