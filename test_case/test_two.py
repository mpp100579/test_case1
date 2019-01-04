import requests
import unittest
import json

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.login_url = 'http://192.168.1.15/'
        cls.info_url = 'http://bkcyun.org:9002/default/Home'
        cls.username = 'yujian'
        cls.password = 'Bkc123456'

    def test_login(self):
        """
        测试登录
        """
        data = {
            'username': self.username,
            'password': self.password
        }

        response = requests.post(self.login_url, data=data).json()

        assert response['code'] == 200
        assert response['msg'] == 'success'

    def test_info(self):
        """
        测试info接口
        """

        data = {
            'username': self.username,
            'password': self.password
        }

        response_cookies = requests.post(self.login_url, data=data).cookies
        session = response_cookies.get('session')
        assert session

        info_cookies = {
            'session': session
        }

        response = requests.get(self.info_url, cookies=info_cookies).json()
        assert response['code'] == 200
        assert response['msg'] == 'success'
        assert response['data'] == 'info'

if __name__ == '__main__':
      unittest.main()