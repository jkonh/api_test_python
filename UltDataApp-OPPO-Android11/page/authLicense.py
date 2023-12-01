# encoding:utf-8
'''
测试函数封装文件，可按照模块写多个测试函数封装文件
可直接在测试函数封装文件里调试运行
'''
import time

from common.logger import get_log
from config import config
from page.base import base


class AuthLicense(object):
    def __init__(self):
        self.driver = config.Config.driver

    def disagreeLicense(self):
        self.driver.start_activity('com.tenorshare.recovery', '.WelcomeActivity')
        disagree = base('authLicense_page', 'license_cancel').get_activity_element()
        disagree.click()

    def agreeLicense(self):
        """启动APP-->通过封装的getElement方法获取控件"""

        self.driver.start_activity('com.tenorshare.recovery', '.WelcomeActivity')
        time.sleep(2)
        agree = base("authLicense_page", "license_agree").getElement()
        agree.click()
        try:
            time.sleep(2)
            base('main_page', 'version_dialog').get_version_element().click()
            # self.driver.find_element(By.ID, 'com.tenorshare.recovery:id/version_dialog_close').click()
            get_log().info("存在升级提示弹框，关闭成功")
        except Exception as e:
            get_log().info(f"升级提示弹框不存在，错误码为{e}")
            pass


if __name__ == "__main__":
    AuthLicense().disagreeLicense()
    AuthLicense().agreeLicense()
