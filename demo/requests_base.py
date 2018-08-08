import requests
# import json

# def get():
#     url = "https://www.baidu.com"
#     response = requests.get(url)
#     response.encoding = "utf-8"
#     print("text->" + response.text)   #网页内容
#     print("status_code->" + response.status_code)  #状态码
#     print("url->" + response.url)  #URL
#     print("headers->" + response.headers)  #header
#     print("cookies->" + response.cookies) #cookies


# def get_interface():
#     url = "http://www.itblacklist.top/goto_detail/"
#     res = requests.get(url)
#     print("text->" + res.text)#网页内容
#     print("status_code->" + res.status_code)  #状态码
#     print("url->" + res.url)  #URL
#     print("headers->" + res.headers)  #header
#     print("cookies->" + res.cookies) #cookies


# def post():
#     url = ""
#     data = {}
#     data["username"] = "admin"
#     data["password"] = "123456"
#     # json = json.dumps(data)
#     # print(type(json))
#     response = requests.post(url=url, data=data)
#     print(response)

# def get1():
#     url = "http://www.itblacklist.top/"
#     response = requests.get(url)
#     response.encoding = "utf-8"
#     print(response.status_code)
#     print(response.text)


def post1():
    url = "http://www.itblacklist.top:2333/login"
    data = {}
    data["username"] = "admin"
    data["password"] = "123456"
    response = requests.post(url, data=data)
    code = eval(response.text)
    print(code)
    if(code['code'] == 200):
        # print(code['code'])
        return code['data']
    else:
        return None


def post2():
    url = "http://www.itblacklist.top:2333/chicktoken"
    token = post1()
    data = {}
    data["token"] = token
    res = requests.post(url, data)
    print(res.text)
    code = eval(res.text)
    if(code['code'] == 200):
        print("成功->%s" % code['msg'])


if __name__ == "__main__":
    post2()
