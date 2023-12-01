# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：handle_config.py
@Date      ：2023/11/23 14:18
@Author    ：ChenGH
"""
from configparser import ConfigParser

from common.handle_path import CONF_FILE


class ConfigHandle(ConfigParser):
    def __init__(self, filename):
        # super().__init__() 就是调用父类的__init__()方法,初始化filename
        super().__init__()
        self.read(filename, encoding='utf-8')


conf = ConfigHandle(CONF_FILE)

if __name__ == '__main__':
    conf = ConfigHandle(CONF_FILE)
    print(conf['mysql']['host'])
    print(conf['test_data']['admin_phone'])

