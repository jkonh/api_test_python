# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：handle_path.py
@Date      ：2023/7/21 11:27
@Author    ：ChenGH
"""
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目根路径
LOG_PATH = os.path.join(BASE_PATH, 'logs')  # 获取项目日志路径
PAGE_PATH = os.path.join(BASE_PATH, "page")  # 获取项目page路径
RESOURCE_PATH = os.path.join(BASE_PATH, "resource")  # 获取项目资源存放路径
TEST_DATA_PATH = os.path.join(BASE_PATH, "testData")  # 获取项目测试数据路径
TEST_SCRIPT_PATH = os.path.join(BASE_PATH, "testScript")  # 获取项目测试脚本路径
CONFIG_PATH = os.path.join(BASE_PATH, "config")
if __name__ == '__main__':
    print(f"项目根路径为:{BASE_PATH}")
    print(f"日志路径为:{LOG_PATH}")
    print(f"项目page路径为:{PAGE_PATH}")
    print(f"项目资源存放路径为:{RESOURCE_PATH}")
    print(f"项目测试数据路径为:{TEST_DATA_PATH}")
    print(f"项目测试脚本路径为:{TEST_SCRIPT_PATH}")
    print(f"项目配置文件路径为:{CONFIG_PATH}")

