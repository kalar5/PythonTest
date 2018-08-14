import requests
from pyrequest import post


def postToken():
    url = "http://www.itblacklist.top:2333/login"
    data = {}
    data["username"] = "admin"
    data["password"] = "123456"
    response = post(url, data=data)
    code = eval(response.text)
    print(code)
    if(code['code'] == 200):
        # print(code['code'])
        return code['data']
    else:
        return None


def postChickToken():
    url = "http://www.itblacklist.top:2333/chicktoken"
    token = postToken()
    data = {}
    data["token"] = token
    res = post(url, data)
    print(res.text)
    code = eval(res.text)
    if(code['code'] == 200):
        print("成功->%s" % code['msg'])


if __name__ == "__main__":
    postChickToken()
