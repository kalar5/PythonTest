import unittest
from utils.pyrequest import get, post
from utils.readExcel import getTestdata


class test_login(unittest.TestCase):
    def test_01(self):
        url = "http://127.0.0.1:8080/login"

        payload = {"username": "admin", "password": "123456"}
        headers = {"Content-Type": "application/json"}

        response = post(url, headers=headers, json=payload)
        print(response)
        code = response.json()["code"]
        self.assertEqual(code, 200)

    def test_02(self):
        res = get("http://127.0.0.1:8080/info")
        code = res.json()['code']
        self.assertEqual(code, 200)

    def test_03(self):
        url_login = "http://127.0.0.1:8080/login"
        data = {}
        data["username"] = "admin"
        data["password"] = "123456"
        headers = {
            "Content-Type": "application/json"
        }
        res = post(url=url_login, data=data, headers=headers)
        code = res.json['code']
        self.assertEqual(code, 200)

    def test_04(self):
        url_login1 = "http://127.0.0.1:8080/login"
        data = {}
        for i in range(7):
            username = getTestdata(i, 0)
            for j in range(1):
                password = getTestdata(i, j)

                data["username"] = username
                data["password"] = password
                headers = {
                    "Content-Type": "application/json"
                }
                res = get(url_login1, data, headers)
                data = res.json['data']
                token = data['token']
                self.assertEqual(token, 200)
