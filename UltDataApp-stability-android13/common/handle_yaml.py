# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：handle_yaml.py
@Date      ：2023/7/21 11:38
@Author    ：ChenGH
"""
import os

import yaml

from common.handle_path import TEST_DATA_PATH


class Handle_yaml(object):
    def __init__(self, yaml_file_name):
        """

        :param yaml_file_name: 传入要解析的yaml文件名称
        """
        self.yaml_path = os.path.join(TEST_DATA_PATH, yaml_file_name)

    def read_data(self):
        with open(self.yaml_path, 'r', encoding='utf-8') as f:
            dict_yaml = yaml.load(f.read(), Loader=yaml.FullLoader)
            return dict_yaml


if __name__ == '__main__':
    data = Handle_yaml('uielements.yml').read_data()
    print(data['authLicense_page']['license_agree'])
    print(Handle_yaml("cmdCommand.yml").read_data()['photo_path']['cleanFile'])
