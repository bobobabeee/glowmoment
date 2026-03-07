from flask import Flask, request, jsonify

# 初始化 Flask 应用
app = Flask(__name__)

# 模拟一个数据库，存储用户数据
users = [
    {"id": 1, "username": "test", "password": "123456"}
]

# 第一个接口：测试连接（不用登录就能访问）
@app.route('/')
def hello():
    return "你的后端服务器跑起来了！"

# 第二个接口：用户登录（APP 登录时调用）
@app.route('/login', methods=['POST'])
def login():
    # 获取 APP 传过来的账号密码
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # 检查是否匹配
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({
                "success": True,
                "message": "登录成功",
                "token": "fake_jwt_token_123" # 这里先模拟一个 Token
            })
    
    return jsonify({
        "success": False,
        "message": "账号或密码错误"
    })

# 启动服务器
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)