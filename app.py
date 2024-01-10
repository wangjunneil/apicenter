from flask import Flask
from dotenv import load_dotenv, find_dotenv

from tools.kms import get_secret

# 初始化
app = Flask(__name__)

@app.route('/')
def status():
    """
    查看服务健康状态
    """    
    
    print(get_secret('OPEN_API_KEY'))
    
    return 'The Api Server is Running.'

if __name__ == '__main__':
    
    # 加载配置
    load_dotenv(find_dotenv(), override=True)
    
    app.run(debug=False, host='0.0.0.0', port=5678)