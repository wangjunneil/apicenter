from flask_restful import Resource, request
from tools.kms import get_secret
import requests

class MailService(Resource):
    """ GPT 服务类 """

    def __init__(self) -> None:
        """ 默认构造 """
        super().__init__()
        
        # 读取 kms 中的配置信息
        self.MAILGUN_API_KEY = get_secret('MAILGUN_API_KEY')

    def get(self):
        """ GET 请求 """
        request_data = request.get_json()
        
        mailfrom = request_data['from']
        mailto = request_data['to']
        subject = request_data['subject']
        content = request_data['content']
        
        result = self.__mailgun(mailfrom, mailto, subject, content)
        return {'success': result}, 200
    
    def __mailgun(self, mailfrom: str, mailto:[], subject: str, content: str ) -> (bool):
        response = requests.post("https://api.mailgun.net/v3/wangjun.dev/messages",
            auth=("api", self.MAILGUN_API_KEY),
            data={"from": mailfrom,
                    "to": mailto,
                    "subject": subject,
                    "text": content})
        return response.status_code == 200