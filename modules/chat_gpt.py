from flask_restful import Resource, request
from openai import OpenAI
import httpx
from tools.kms import get_secret

class GPTAnswer(Resource):
    """ GPT 服务类 """
    
    def __init__(self) -> None:
        """ 默认构造 """
        super().__init__()
        
        # 读取 kms 中 openai 的配置信息
        openai_api_key = get_secret('OPENAI_API_KEY')
        openai_proxy_url = get_secret('OPENAI_PROXY_URL')
        
        # 初始化 openai client
        self.client = OpenAI(
            api_key=openai_api_key,
            http_client=httpx.Client(proxy=openai_proxy_url)
        )
        
    def get(self):
        """ GET 请求 """
        request_data = request.get_json()
        content = request_data['content']
        result = self.__chat([
            { "role":"user", "content":content }
        ])
        return result, 200
        
    def __chat(self, message):
        """ 私有调用GPT服务方法 """
        chat_completion = self.client.completions.create(
            message=message,
            model="gpt-3.5-turbo",
            temperature=0.8,
            max_tokens=120,
            top_p=1.0,
            frequency_penalty=0.5,
            presence_penalty=0.0
        )
        return chat_completion['choices'][0].message.content