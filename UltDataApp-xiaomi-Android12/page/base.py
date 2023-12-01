# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：base.py
@Date      ：2023/7/21 11:53
@Author    ：ChenGH
"""
import os
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.handle_yaml import Handle_yaml
from common.logger import get_log
# from config.config import Config
from config import config


def deCache(page_name, del_path):
    cmdCommand_yml = Handle_yaml(yaml_file_name="cmdCommand.yml").read_data()
    # 获取cmdCommand中的cleanFile下的路径page_name传入对应需要删除的类型如：photo_path，element_name传入cleanFile
    command = cmdCommand_yml.get(page_name).get(del_path)
    try:
        os.popen(command).read()
    except Exception:
        get_log().info('当前要删除的路径不存在，不需删除')


class base(object):
    """读取页面元素，并封装对应的操作方法"""

    def __init__(self, page_name, element_name):
        """

        :param page_name: yml文件对应的page_name
        :param element_name: yml文件对应的element_name
        """
        self.driver = config.driver
        self.page_name = page_name
        self.element_name = element_name
        yaml_data = Handle_yaml(yaml_file_name="uielements.yml").read_data()
        self.elements = yaml_data.get(page_name).get(element_name)
        self.type = self.elements.get('type')
        self.value = self.elements.get('value')
        self.text = self.elements.get('text')
        self.attribute = self.elements.get('attribute')

    """通过查uielements.yaml文件，获取元素属性，等待界面元素出现"""

    def waitElement(self):
        if self.type == "xpath":
            element = WebDriverWait(self.driver, timeout=10000, poll_frequency=0.2).until(
                lambda x: x.find_element(By.XPATH, self.value))
            return element
        elif self.type == 'id':
            element = WebDriverWait(self.driver, timeout=10000, poll_frequency=0.2).until(
                lambda x: x.find_element(By.ID, self.value))
            return element
        else:
            get_log().error(f"waitElement方法未找到{self.page_name}下的{self.element_name}元素")

    '''通过查uielements.yaml文件，获取控件属性，再调用selenium对应的方法获取控件'''

    def getElement(self):

        if self.type == "xpath":
            element = WebDriverWait(self.driver, timeout=1000, poll_frequency=0.1).until(
                lambda x: x.find_element(By.XPATH, self.value))
            return element
        elif self.type == 'id':
            element = WebDriverWait(self.driver, timeout=1000, poll_frequency=0.1).until(
                lambda x: x.find_element(By.ID, self.value))
            return element
        elif self.type == 'swipe':
            element = self.driver.swipe(*self.value)
            return element
        elif self.type == 'tap':
            element = self.driver.tap(self.value)
            return element
        elif self.type == 'class':
            element = self.driver.find_element(By.CLASS_NAME, self.value)
            return element
        else:
            get_log().error(f"getElement方法未找到{self.page_name}下的{self.element_name}元素")

    def get_version_element(self):
        if self.type == 'id':
            element = WebDriverWait(self.driver, timeout=10, poll_frequency=0.1).until(
                lambda x: x.find_element(By.ID, self.value))
            return element
        else:
            get_log().error(f"getElement方法未找到{self.page_name}下的{self.element_name}元素")

    def clickElement(self):
        if self.type == "xpath":
            element = WebDriverWait(self.driver, timeout=1000, poll_frequency=0.1).until(
                lambda x: x.find_element(By.XPATH, self.value))
            return element.click()
        elif self.type == 'id':
            element = WebDriverWait(self.driver, timeout=1000, poll_frequency=0.1).until(
                lambda x: x.find_element(By.ID, self.value))
            return element.click()
        elif self.type == 'class':
            element = self.driver.find_element(By.CLASS_NAME, self.value)
            return element.click()
        else:
            get_log().error(f"clickElement方法未找到{self.page_name}下的{self.element_name}元素")

    def get_activity_element(self):
        if self.type == 'id':
            element = WebDriverWait(self.driver, timeout=5, poll_frequency=0.1).until(
                lambda x: x.find_element(By.ID, self.value))
            return element
        else:
            get_log.error(f"未封装{self.page_name}下的{self.element_name}元素对应activity的{self.type}方法")

    """使用find_elements定位一组元素，并通过text属性定位需要的元素"""

    def getElement_by_elements(self):

        if self.type == 'id':
            elements = self.driver.find_elements(By.ID, self.attribute)
            for element in elements:
                if element.get_attribute('text') == self.text:
                    element.click()
                    break
        elif self.type == 'class':
            elements = self.driver.find_elements(By.CLASS_NAME, self.attribute)
            for element in elements:
                if element.get_attribute('text') == self.text:
                    element.click()
                    break
        elif self.type == 'xpath':
            elements = self.driver.find_elements(By.XPATH, self.attribute)
            for element in elements:
                if element.get_attribute('text') == self.text:
                    element.click()
                    break
        else:
            get_log().error(f"getElement_by_elements 未找到{self.page_name}下的{self.element_name}元素")

    """通过adb命令获取指定路径下的文件数量"""

    def getFileCount(self, path):
        # 获取指定路径下对应的文件数量
        file_count = os.popen(path).read()
        return file_count

    def isAcitivityExist1(self):
        try:
            self.get_activity_element()
            return True
        except Exception as e:
            get_log().error(f"控件不存在，异常为{e},未找到{self.page_name}页面的{self.element_name}元素！")
            return False

    def isAcitivityExist(self):
        try:
            if self.driver.query_app_state('com.tenorshare.recovery') == 3:
                # 1表示app未启动，3表示启动成功
                return True
        except Exception as e:
            get_log().error(f"控件不存在，异常为{e},未找到{self.page_name}页面的{self.element_name}元素！")
            return False

    """通过adb命令清空指定文件夹"""

    '''
    判断控件是否存在
    '''

    def isExist(self):
        try:
            self.getElement()
            return True
        except Exception as e:
            get_log().error(f"控件不存在，异常为{e},未找到{self.page_name}页面的{self.element_name}元素！")
            return False

    '''
    判断控件是否不存在
    '''

    def isnotExist(self):
        try:
            self.getElement()
            return False
        except Exception:
            get_log().info(f"isnotExist方法未找到{self.page_name}页面的{self.element_name}元素！")
            return True

    def get_element_text(self):
        if self.type == "xpath":
            element = WebDriverWait(self.driver, timeout=10, poll_frequency=0.1).until(
                lambda x: x.find_element(By.XPATH, self.value))
            text = element.text
            return text
        elif self.type == 'id':
            element = WebDriverWait(self.driver, timeout=10, poll_frequency=0.1).until(
                lambda x: x.find_element(By.ID, self.value))
            text = element.text
            return text

        else:
            get_log().error(f"未封装{self.page_name}下的{self.element_name}元素{type}类型定位方法")
