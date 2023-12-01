# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：rsa_token.py
@Date      ：2023/11/30 19:05
@Author    ：ChenGH
"""
import base64
import time

import rsa
from requests import request


def rsa_encrypt(msg: str, pub_key: str):
    '''
    公钥加密
    :param msg: 要加密的内容 str
    :param pub_key: pem格式的公钥字符串
    :return:
    '''
    # 1.生成公钥对象
    # 把公钥字符串转换为字节数据
    pub_key_bytes = pub_key.encode()
    pub = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key_bytes)
    # 待加密的数据转换为字节数据
    content = msg.encode('utf-8')
    # 2.加密
    crypt_msg = rsa.encrypt(content, pub)
    # 3.base64编码并转换成字符串格式
    return base64.b64encode(crypt_msg).decode()


def generate_sign(token, pub_key):
    '''
    生成签名
    :param token: token字符串
    :param pub_key: pem格式的公钥
    :return:
    '''
    # 1.获取token的前50位
    token_50 = token[:50]
    # 获取timestamp
    timestamp = int(time.time())
    # 拼接token的前50位和生成的时间戳，转换成整数
    msg = token_50 + str(timestamp)

    # 进行rsa加密
    sign = rsa_encrypt(msg, pub_key)
    return sign, timestamp


if __name__ == '__main__':

    headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
    data ={
        'mobile_phone':"15512345678",
        'pwd':'12345678'
    }
    resp = request(method='post', url='http://api.lemonban.com/futureloan/member/login', headers=headers, json=data)
    res = resp.json()
    token = res['token_info']['token']
    sign, timestamp = generate_sign(token, settings.SERVER_RSA_PUB_KEY)
    headers = {
        "X-Lemonban-Media-Type": "lemonban.v3",
        "Authorization": "Bearer " + token
    }
    data = {
        'member_id': res['id'],
        'amount': 5000,
        'timestamp': timestamp,
        'sign': sign
    }
    url = settings.PROJECT_HOST + settings.INTERFACES['recharge']
    res = requests.post(url=url, json=data, headers=headers)
    print(res.status_code)
    print(res.text)
# # 日志配置
# LOG_CONFIG = {
#     'name': 'pylog',
#     'mode': 'a',
#     'encoding': 'utf-8',
#     'debug': True
# }
#
# # 测试数据配置
# TEST_DATA_FILE = 'test_data/test_data.xlsx'
#
# # 测试报告
# REPORT_CONFIG = {
#     'filename': 'reports/测试报告.html',
#     'description': '一个练手项目'
# }
# 项目域名
PROJECT_HOST = 'http://test.lemonban.com/futureloan/mvc/api'

# 接口地址，将/符号放在接口地址中
INTERFACES = {
    'register': '/member/register',
    'login': '/member/login',
    'recharge': '/member/recharge'
}