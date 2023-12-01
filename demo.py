# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：demo.py
@Date      ：2023/11/30 17:29
@Author    ：ChenGH
"""
# import jsonpath
# from requests import request
#
# data = {"mobile_phone": "15512345678", "pwd": "12345678"}
# headers = {"X-Lemonban-Media-Type": "lemonban.v2"}
# resp = request(method='post', url='http://api.lemonban.com/futureloan/member/login', headers=headers, json=data)
# res = resp.json()
# print(res)
# print(res['data']['token_info']['token'])
# # 1.设置Authorization请求头，值为Bearertoken值
# Authorization = 'Bearer' + ' ' + jsonpath.jsonpath(res, '$..token')[0]
# print('Authorization:',Authorization)
# # V3版本的token鉴权,取token前50位拼接timestamp,timestamp值为1567342860
# token = jsonpath.jsonpath(res, '$..token')[0][:50] + '1567342860'
# print(len(token))
# print(token)
# # 对token进行RSA加密，得到加密的签名字符串
#
#
# # 3.获取member_id，并把member_id设置为类属性:jsonpath.jsonpath(res, '$..id')是去res中查找包含id的数据
# member_id = jsonpath.jsonpath(res, '$..id')[0]
# print(member_id)
import rsa

# 1.生成密钥对
# 返回数据为元祖
(pub, pri) = rsa.newkeys(1024)
# 打印公钥
print(pub)
# 打印私钥
print(pri)

# 2.加密
# 2.1需要把待加密的数据转换为字节
# 消息加密前需要转换成字节数据
# 转换为字节数据
message = '测试'.encode('utf-8')
# 加密，返回二进制格式
res = rsa.encrypt(message, pub)
print(res)
# 加密后的数据一般会转换成字符串传输
# 二进制数据转换为字符串，使用base64编码  a-z A-Z 0-9 + =
import base64

# 2.2一般需要把加密后的字节转换为base64编码
b64_res = base64.b64encode(res)  # 字节，但是都是ascii码
print(b64_res)
# 要转换为字符串
# 2.3将base64编码字节转换为字符串
b64_str_res = b64_res.decode()
print(b64_str_res)

# 3.解密
# 一般拿到的加密数据都是base64编码的字符串
# 3.1将base64编码字节转换为字符串
# 转换为字节数据
b64_bytes = b64_str_res.encode()

# 3.2将base64字节数据解码为密文
# 把b64解码
r = base64.b64decode(b64_bytes)

# 3.3解密
d_res = rsa.decrypt(r, pri)
print(d_res)  # 字节数据
# 3.4如果你加密的是字符串，需要对应的字符编码进行解码为字符串
print(d_res.decode('utf-8'))  # 解码

pub_key = '''
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE
O3F7gs+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr
tuPorOc42+gLnFfyhJAwdZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S
kKlZFc8Br7SHtbL2tQIDAQAB
-----END PUBLIC KEY-----
'''
# 一般提供的公钥格式都是上面这种pem格式
# 1.先转换成字节数据
pub_key = pub_key.encode()  # 因为都是ascii码所以不用指定特定的字符编码
# 2.调用方法加载
pub = rsa.PublicKey.load_pkcs1_openssl_pem(pub_key)
print(type(pub), pub)