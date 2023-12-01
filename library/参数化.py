# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：参数化.py
@Date      ：2023/11/24 19:29
@Author    ：ChenGH
"""

# def test_args(*agres):
#     for i in agres:
#         print(i)
#
#
# arg = ['yasoob', 'python', 'eggs', 'test']
# test_args(*arg)
# 解包
a, b, *c = ['yasoob', 'python', 'eggs', 'test']
print(a, b, c)
a, b, c = ['yasoob', 'eggs', 'test']
print(a, b, c)
print(type(a))
