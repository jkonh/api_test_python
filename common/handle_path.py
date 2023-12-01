# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：handle_path.py
@Date      ：2023/11/23 14:38
@Author    ：ChenGH
"""
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目跟目录
CASE_DIR = os.path.join(BASE_DIR, 'testcases')  # 用例脚本所在目录
DATA_DIR = os.path.join(BASE_DIR, 'data')  # 用例数据目录
CONF_DIR = os.path.join(BASE_DIR, 'conf')  # 配置文件路径
REPORT_DIR = os.path.join(BASE_DIR, 'reports')  # 测试报告路径
LOG_DIR = os.path.join(BASE_DIR, 'logs')  # 日志目录路径
CONF_FILE = os.path.join(CONF_DIR, 'config.ini')  # 配置文件路径
TEST_DATA_FILE = os.path.join(DATA_DIR, 'apicases.xlsx')
if __name__ == '__main__':
    print(BASE_DIR)
    print(CASE_DIR)
    print(DATA_DIR)
    print(CONF_DIR)
    print(REPORT_DIR)
    print(LOG_DIR)
    print(CONF_FILE)
    print(TEST_DATA_FILE)
