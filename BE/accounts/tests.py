from django.test import TestCase, Client
import requests


HOST = 'http://localhost:8000'
LOGIN_URL = HOST + '/account/login/'

LOGIN_INFO = {
    "username": "test_account",
    "password": "whoareyou!",
}
PROFILE_URL = HOST + '/account/profile/test_account/'


class TestAccounts(TestCase):
    def setUp(self):
        print("----- accounts app test start -----")
        self.client = Client()
        self.token = ""

    def test_login(self):
        '''
        정상적인 로그인 POST가 성공적으로 이루어졌는지 테스트합니다.
        '''
        print("----- accounts: LOGIN test -----")
        response = requests.post(LOGIN_URL, data=LOGIN_INFO)
        print(f'login status: {response.status_code}')
        self.assertEqual(response.status_code, 200)
        print('\n')
        self.token = response.json()['access_token']

    def test_profile(self):
        '''
        자신의 프로필 페이지를 성공적으로 GET할 수 있는지 테스트합니다.
        '''
        print("----- accounts: PROFILE test -----")
        self.test_login()
        header = {
            'Authorization': 'Bearer ' + self.token
        }
        response = requests.get(PROFILE_URL, headers=header, data='')
        self.assertEqual(response.status_code, 200)
        print(response.content)
        print('\n')
