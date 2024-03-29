from flask import Flask, request
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv

from tools.auth import auth
from tools.log import logger
from modules.chat_gpt import GPTAnswer
from modules.send_email import MailService

# 初始化
app = Flask(__name__)
api = Api(app, prefix='/api/v1')

# Restful 路由
api.add_resource(GPTAnswer, '/gpt')
api.add_resource(MailService, '/mail')

@app.route('/')
def status():
    """
    查看服务健康状态
    """
    return {'success':True, 'message':'The API Server is Running.'}, 200

@app.before_request
@auth.login_required
def before_request():
    """
    拦截所有业务请求，本函数不做处理，递交到 auth.verify_password 中处理
    """
    pass

@app.errorhandler(Exception)
def handler_error(e):
    logger.error(e)
    return {'success':False, 'message': "An internal error occurred"}, 500

if __name__ == '__main__':
    
    # 在序列化JSON时不要将其编码为ASCII，避免非ASCII字符转义成\uXXXX格式
    app.config['JSON_AS_ASCII'] = False
    # 设置返回的JSON响应的MIME类型及字符集编码
    app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8"

    # .env 配置加载
    load_dotenv(find_dotenv(), override=True)

    app.run(debug=False, host='0.0.0.0', port=5000)