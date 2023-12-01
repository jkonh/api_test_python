import os
import unittest
import decimal

import jsonpath
from requests import request

from common.handle_config import conf
from common.handle_db import MySQLHandler
from common.handle_excel import HandleExcel
from common.handle_logging import log
from common.handle_path import DATA_DIR,TEST_DATA_FILE
from library.myddt import ddt, data


@ddt
class TestRecharge(unittest.TestCase):
    # excel = HandleExcel(os.path.join(DATA_DIR, 'apicases.xlsx'), 'recharge')
    excel =HandleExcel(filename=TEST_DATA_FILE,sheet_name='recharge')
    cases = excel.read_data()

    @classmethod
    def setUpClass(cls) -> None:
        """用例执行的前置条件：登录成功"""
        # 1. 登录成功，获得response
        url = conf['env']['url'] + '/member/login'  # 登录接口的完整地址
        data = {
            'mobile_phone': conf['test_data']['phone'],
            'pwd': conf['test_data']['pwd']
        }
        headers = eval(conf['env']['headers'])
        resp = request(method='post', url=url, json=data, headers=headers)
        res = resp.json()
        # 2. 获取token，并把token设置为类属性   cls.token  = ....
        cls.token = 'Bearer' + ' ' + jsonpath.jsonpath(res, '$..token')[0]
        # 3. 获取member_id，并把member_id设置为类属性  cls.member_id = ....
        cls.member_id = jsonpath.jsonpath(res, '$..id')[0]
        # 4. 连接数据库
        cls.db = MySQLHandler()

    @data(*cases)
    def test_recharge(self, case):
        print(case)
        url = conf['env']['url'] + case['url']
        data = eval(case['data'].replace('#member_id#', str(self.member_id)))
        headers = eval(conf['env']['headers'])
        headers['Authorization'] = self.token
        expected = eval(case['expected'])

        # 判断用例是否需要数据库校验
        sql = case.get('check_sql')
        after_money = befor_money = 0
        #  充值前
        if sql:  # 如果有sql语句，就校验数据库
            sql = sql.format(self.member_id)  # 把sql语句中的id={}  替换为  id = 15511
            # 充值业务 如何校验数据库？  充值前余额 + 充值金额 =   充值后余额
            befor_money = self.db.find_one(sql)['leave_amount']

        # 发送请求，获得实际结果, 为了普通的校验 ，预期结果和实际结果
        resp = request(method=case['method'], url=url, json=data, headers=headers)  # 充值操作
        res = resp.json()

        # 获得充值后的余额
        if sql:
            after_money = self.db.find_one(sql)['leave_amount']
        # 断言
        test_result = '通过'
        try:
            self.assertEqual(expected['code'], res['code'])
            self.assertEqual(expected['msg'], res['msg'])
            if sql:
                money = decimal.Decimal(str(data['amount']))  # 把充值的钱转换为 Decimal类型
                self.assertEqual(money, after_money - befor_money)
                pass
            print('...')
        except AssertionError as e:
            log.error('用例---{}---执行未通过'.format(case['title']))
            log.debug('预期结果：{}'.format(expected))
            log.debug('实际结果：{}'.format(res))
            log.exception(e)
            test_result = '不通过'
            raise e
        finally:
            self.excel.write_data(row=case['case_id'] + 1, column=8, value=test_result)

    @classmethod
    def tearDownClass(cls) -> None:
        # 5. 关闭数据库
        cls.db.close()


if __name__ == '__main__':
    unittest.main()
