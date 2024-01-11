from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv

from tools.auth import auth
from modules.chat_gpt import GptAnswer

# 初始化
app = Flask(__name__)
api = Api(app)

# Restful路由
api.add_resource(GptAnswer, '/v1/gpt')


@app.route('/')
def status():
    """
    查看服务健康状态
    """    
    return {'message':'The API Server is Running.'}, 200


@app.before_request
@auth.login_required
def before_request():
    # 每个请求处理之前执行
    # 在这个函数中不需要做任何事情，因为认证逻辑在 auth.verify_password 中处理
    pass

if __name__ == '__main__':
    # 加载配置
    load_dotenv(find_dotenv(), override=True)
    
    app.run(debug=False, host='0.0.0.0', port=5678)