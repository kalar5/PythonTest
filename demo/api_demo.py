from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>测试网站</h1>'


@app.route('/getinfo', methods=["GET"])
def getinfo():
    info = {}
    info["姓名"] = "阿绿"
    info["性别"] = "女"
    return jsonify(info)


@app.route('/login', methods=['POST'])
def login():
    hdict = request.get_json()
    username = hdict.get("username")
    password = hdict.get("password")
    response = {}
    if username == "admin" and password == "123456":
        response['code'] = 200
        response['data'] = {"token": "adjkasjdkdjkasjdklajskldja23135dgsgd"}
        response['msg'] = "登陆成功"
        return jsonify(response)
    elif username == "" and password == "":
        response['code'] = 400
        response['msg'] = "账号或密码不能为空"
        return jsonify(response)
    else:
        response['code'] = 400
        response['msg'] = "账号或密码错误"
        return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
