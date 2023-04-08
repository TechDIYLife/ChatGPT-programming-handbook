import requests
import json
import sys

opt=sys.argv[1]

# 设置身份验证密钥
_SERVICE_AUTH_KEY = "758e9ef7984b415688972d749f8aa58e"

# 设置请求头
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {_SERVICE_AUTH_KEY}"
}

if opt=="add":
    todo=sys.argv[2]
    # 准备数据
    data = {
        "todo": todo
    }
    # 发送POST请求
    response = requests.post("http://127.0.0.1:5002/todos/john", headers=headers, data=json.dumps(data))

if opt=="list":
    # 发送POST请求
    response = requests.get("http://127.0.0.1:5002/todos/john", headers=headers)
    
if opt=="del":
    _id=int(sys.argv[2])
    data = {
        "todo_idx": _id
    }
    response = requests.delete("http://127.0.0.1:5002/todos/john", headers=headers, data=json.dumps(data))


# 打印响应结果
print(response.status_code)
print(response.content)
print(response)