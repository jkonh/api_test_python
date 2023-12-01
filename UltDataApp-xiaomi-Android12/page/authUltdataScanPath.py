# encoding:utf-8
import time

from page.authLicense import AuthLicense
from config import config
from page.scanfuncSelect import ScanfuncSelect

from page.base import base


class AuthUltdataScanpath(object):
    def __init__(self):
        self.driver = config.driver

    def dis_access_Auth_Ultdata(self):
        # 同意许可协议-->选择扫描功能-->关闭隐私声明弹框
        # AuthLicense().agreeLicense()
        # self.driver.start_activity('com.tenorshare.recovery', '.WelcomeActivity')

        ScanfuncSelect('main_page', 'photo_btn').select_func()
        close_private = base('authScanPath_page', 'close_private').getElement()
        close_private.click()

    # def access_Auth_Ultdata(self):
    #     access_Auth_btn = base('authScanPath_page', 'access_Auth_btn').getElement()
    #     access_Auth_btn.click()
    #     time.sleep(5)
    #     base('authScanPath_page', 'access_UltData_btn').getElement_by_elements()
    #     time.sleep(2)
    #     # 授权ultdata权限后返回
    #     back_dataAuth = base('authScanPath_page', 'back_dataAuth_btn').getElement()
    #     back_dataAuth.click()

    def access_Auth_Ultdata(self):
        access_Auth_btn = base('authScanPath_page', 'access_Auth_btn').getElement()
        access_Auth_btn.click()
        time.sleep(5)
        all_allow_btn = base('authScanPath_page', 'all_allow_btn').getElement()
        all_allow_btn.click()
        time.sleep(2)
        self.driver.keyevent(4)
        # back_dataAuth = base('authScanPath_page', 'back_dataAuth_btn').getElement()
        # back_dataAuth.click()
        # time.sleep(2)
        saf_Auth_btn = base('authScanPath_page', 'saf_Auth_btn').getElement()
        saf_Auth_btn.click()
        time.sleep(2)
        use_data_path = base('authScanPath_page', 'use_data_path').getElement()
        use_data_path.click()
        time.sleep(2)
        allow_data_btn = base('authScanPath_page', 'allow_data_btn').getElement()
        allow_data_btn.click()
        time.sleep(2)


if __name__ == "__main__":
    AuthUltdataScanpath = AuthUltdataScanpath()
    AuthUltdataScanpath.dis_access_Auth_Ultdata()
    AuthUltdataScanpath.access_Auth_Ultdata()
