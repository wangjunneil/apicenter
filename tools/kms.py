import os
import requests

def get_secret(key: str) -> (str):    
    """
    根据指定的key获取对应的密钥配置信息
    
    参数:
    key (str): 要查询的key
    
    返回值：
    str: 对应key的value
    """
    INFISICAL_URL       = os.getenv('INFISICAL_URL')
    INFISICAL_TOKEN     = os.getenv('INFISICAL_TOKEN')
    INFISICAL_API_KEY   = os.getenv('INFISICAL_API_KEY')
    print(f">>> {INFISICAL_URL}, {INFISICAL_TOKEN}, {INFISICAL_API_KEY}")
    headers = {
        'User-Agent':'PostmanRuntime/7.36.0',
        "X-API-Key": INFISICAL_API_KEY,
        "Authorization": f"Bearer {INFISICAL_TOKEN}"
    }
        
    URL = (
        f"https://{INFISICAL_URL}/api/v3/secrets/raw/{key}"
        f"?workspaceId=659e5516f2957fd1520bda17&environment=prod&type=shared"
    )
    
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    