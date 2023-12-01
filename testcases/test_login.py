# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：test_login.py
@Date      ：2023/11/23 20:31
@Author    ：ChenGH
"""
import unittest

from requests import request

from common.handle_config import conf
from common.handle_excel import HandleExcel
from common.handle_logging import log
from common.handle_path import TEST_DATA_FILE
from library.myddt import data, ddt


@ddt
class LoginTestCase(unittest.TestCase):
    excel = HandleExcel(filename=TEST_DATA_FILE, sheet_name='login')
    cases = excel.read_data()

    @data(*cases)
    def test_login(self, case):
        method = case['method']
        data = eval(case['data'])
        headers = eval(conf['env']['headers'])  # 将类似于字典的字符串转化为字典
        url = conf['env']['url']+case['url']
        resp = request(method=method, url=url, headers=headers, json=data)
        expected = eval(case['expected'])  # {'code': 0, 'msg': 'OK'}
        # 实际结果
        actual = resp.json()
        row = case['case_id'] + 1
        test_result = ''

        try:
            self.assertEqual(expected['code'], actual['code'])
            self.assertEqual(expected['msg'], actual['msg'])
        except AssertionError as e:

            log.error(f"用例{case['title']}测试不通过")
            # ac=[actual['code'],actual['msg']]

            test_result = 'fail'
        else:
            log.info(f"用例{case['title']}测试通过")

            test_result = 'pass'
        finally:
            self.excel.write_data(row, 8, test_result)


if __name__ == '__main__':
    unittest.main()
