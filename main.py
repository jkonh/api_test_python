import unittest

from BeautifulReport import BeautifulReport

from common.handle_logging import log
from common.handle_path import CASE_DIR, REPORT_DIR

log.info('开始执行测试用例....')

suite1 = unittest.TestSuite()
# 加载测试用例到套件
suite1.addTest(unittest.TestLoader().discover(CASE_DIR))
# 执行用例生成报告
BeautifulReport(suite1).report('登录&充值&注册接口自动化测试', filename='test_result.html', report_dir=REPORT_DIR)
log.info('用例执行完毕')
