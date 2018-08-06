import requests


def get(url=""):
    try:
        response = requests.get(url)
    except Exception as e:
        print(e)

    return response


def post(url="", data={}, headers={}):
    try:
        response = requests.post(url, data=data, headers=headers)
    except Exception as e:
        print(e)

    return response


def add_cases():
    url_index = "http://www.itblacklist.top:5000/index"
    res_index = get(url=url_index)
    print(res_index.text)

    url_userRegist = "http://www.itblacklist.top:5000/userRegist/"
    data = {"username": "user3322", "password": "123", "nickname": "user33"}
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"
    headers["Content-Type"] = "application/json"
    res_regist = post(url=url_userRegist, data=data, headers=headers)
    print(res_regist.text)
    # 实际工作中需要通过对返回值的status_code&&参数返回值&&数据库数据比对进行结果验证。


if __name__ == '__main__':
    add_cases()
