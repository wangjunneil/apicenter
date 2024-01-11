from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv

from tools.auth import auth
from modules.chat_gpt import GPTAnswer

# 初始化
app = Flask(__name__)
api = Api(app)

# Restful 路由
api.add_resource(GPTAnswer, '/v1/gpt')

@app.route('/')
def status():
    """
    查看服务健康状态
    """    
    return {'message':'The API Server is Running.'}, 200

@app.before_request
@auth.login_required
def before_request():
    """
    拦截所有业务请求，本函数不做处理，递交到 auth.verify_password 中处理
    """
    pass

if __name__ == '__main__':
    
    # .env 配置加载
    load_dotenv(find_dotenv(), override=True)
    
    app.run(debug=False, host='0.0.0.0', port=5678)