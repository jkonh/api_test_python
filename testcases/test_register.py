# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：test_register.py
@Date      ：2023/12/1 19:09
@Author    ：ChenGH
"""

import unittest
from random import randint

from requests import request

from common.handle_config import conf
from common.handle_db import MySQLHandler
from common.handle_excel import HandleExcel
from common.handle_logging import log
from common.handle_path import TEST_DATA_FILE
from library.myddt import ddt, data

excel = HandleExcel(filename=TEST_DATA_FILE, sheet_name='register')
cases = excel.read_data()


@ddt
class TestRegister(unittest.TestCase):
    # 1.读取用例
    excel = HandleExcel(filename=TEST_DATA_FILE, sheet_name='register')
    cases = excel.read_data()

    # 前置操作，连接数据库
    @classmethod
    def setUpClass(cls) -> None:
        cls.db = MySQLHandler()

    @data(*cases)
    def test_register(self, case):
        # 替换用例中的#phone#
        phone = self.random_phone()
        if '#phone#' in case['data']:
            case['data'] = case['data'].replace("#phone#", phone)
        sql = case.get('check_sql')
        if sql:
            sql = case['check_sql'].replace("#phone#", phone)
        url = conf['env']['url'] + case['url']
        resp = request(method=case['method'], url=url, json=eval(case['data']), headers=eval(conf['env']['headers']))
        expected = eval(case['expected'])
        res = resp.json()
        # 3. 断言
        test_result = 'pass'
        # 判断是否需要验证sql语句的执行

        try:
            if sql:
                r = self.db.find_count(sql)
                self.assertEqual(1, r)
            self.assertEqual(expected['code'], res['code'])
        except AssertionError as e:
            test_result = 'fail'
            log.error('用例---{0}---执行未通过,注册手机号是{1}'.format(case['title'], self.phone))
            log.exception('e')
            raise e

        finally:
            self.excel.write_data(row=case['case_id'] + 1, column=8, value=test_result)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.db.close()

    @classmethod
    def random_phone(cls):
        phone = '188'
        while True:
            # 随机生成8个字符
            s = []
            for i in range(8):
                n = randint(0, 9)
                s.append(str(n))
            phone += ''.join(s)
            sql = 'SELECT reg_name FROM member where mobile_phone={}'.format(phone)
            res = cls.db.find_count(sql)
            if res:
                continue
            else:
                return phone


if __name__ == '__main__':
    unittest.main()
