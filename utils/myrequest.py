import requests


# 对request进行二次封装
class requestUtils:
    def __init__(self, url, data={}):
        self.url = url
        self.data = data

    def get(self):
        try:
            response = requests.get(self.url)
            response.encoding = "utf-8"
        except Exception as e:
            print(e)

        return response

    def post(self):
        try:
            response = requests.post(self.url, data=self.data)
        except Exception as e:
            print(e)

        return response


if __name__ == "__main__":
    # req = requestUtils(url="http://www.baidu.com")
    # response = req.get()

    url = "http://www.itblacklist.top:2333/chicktoken"
    data = {}
    data["username"] = "admin"
    data["password"] = "123456"
    req = requestUtils(url=url, data=data)
    response = req.post()
    print(response.text)
