# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：eval的使用.py
@Date      ：2023/11/24 16:04
@Author    ：ChenGH
"""
import requests

str1 = "{'type':'content-type'}"
str2 = "['a','b','c']"
str3 = '(1,23,3)'


def use_eval(s):
    print('转换前', s)
    print('转换前的类型', type(s))
    print('转换后', eval(s))
    print('转换后的类型', type(eval(s)))
    print("\n")


use_eval(str1)
use_eval(str2)
use_eval(str3)
data = {"mobile_phone": "15512345678", "pwd": "12345678"}
res = requests.request(method='post', url='http://api.lemonban.com/futureloan/member/login',
                       headers={"X-Lemonban-Media-Type": "lemonban.v2"}, json=data)
print(res.json())


def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)


arg = ['yasoob', 'python', 'eggs', 'test']
test_var_args(*arg)
