# encoding:utf-8
import time

from page.authLicense import AuthLicense
from page.base import base
from page.scanfuncSelect import ScanfuncSelect
from config.config import driver


class BaseScan(object):
    def __init__(self, page_name, element_name):
        self.ScanfuncSelect = ScanfuncSelect(page_name, element_name)

    def back_scan_main_page(self):
        # 图片、视频、音频、文档：点击完成按钮-》点击返回-》点击确认返回
        # 该方法仅用于授权data路径之后扫描完成界面返回主界面
        base(page_name="scan_page", element_name="scan_finish_btn").clickElement()
        time.sleep(2)
        driver.keyevent(4)
        base("scan_finish_page", "confirm_back_btn").clickElement()

    def scan_android_13_and_12(self):
        "授权许可协议->选择要扫描的功能"
        # AuthLicense().agreeLicense() 紧接着授权后的用例执行，不需要该步骤，若单独执行，需要该步骤
        # self.back_main_page()
        self.ScanfuncSelect.select_func()
        # ScanfuncSelect().select_func('main_page', 'photo_btn')
        # # 关闭隐私说明弹框
        # close_private = base('authScanPath_page', 'close_private').getElement()
        # close_private.click()
        # access_Auth_btn = base('authScanPath_page', 'access_Auth_btn').getElement()
        # access_Auth_btn.click()
        # time.sleep(5)
        # base('authScanPath_page', 'access_UltData_btn').getElement_by_elements()
        # time.sleep(2)
        # # 授权ultdata权限后返回，返回即进入扫描界面
        # back_dataAuth = base('authScanPath_page', 'back_dataAuth_btn').getElement()
        # back_dataAuth.click()


"""
以下代码是安卓11及以下的设备需要的
    def access_data_path_after_ultdata(self):
        # 授权ultdata后立马授权data路径
        saf_Auth_btn = base('authScanPath_page', 'saf_Auth_btn').getElement()
        saf_Auth_btn.click()
        use_data_path = base('authScanPath_page', 'use_data_path').getElement()
        use_data_path.click()
        allow_data_btn = base('authScanPath_page', 'allow_data_btn').getElement()
        allow_data_btn.click()
        scan_finish = base('scan_page', 'scan_finish_btn').waitElement()
        scan_finish.click()

    def scan_part(self):
        self.access_Ultdata_path()
        base('authScanPath_page', 'scan_first_btn').getElement().click()
        base('scan_page', 'scan_finish_btn').waitElement()

    def scan_all(self):
        # 接着部分扫描的进行全部扫描，不需要选择功能
        scan_part_finish = base('scan_page', 'scan_finish_btn').waitElement()
        scan_part_finish.click()
        # 扫描完成界面返回并确认返回
        config.Config.driver.keyevent(4)
        base('scan_finish_page', 'confirm_back_btn').getElement().click()
        # 选择主界面功能，和scan_part中一致
        # base().getElement(page_name, element_name).click()
        saf_Auth_btn = base('authScanPath_page', 'saf_Auth_btn').getElement()
        saf_Auth_btn.click()
        use_data_path = base('authScanPath_page', 'use_data_path').getElement()
        use_data_path.click()
        allow_data_btn = base('authScanPath_page', 'allow_data_btn').getElement()
        allow_data_btn.click()
        base('scan_page', 'scan_finish_btn').waitElement()
"""

if __name__ == "__main__":
    BaseScan('main_page', 'photo_btn').scan_android_13_and_12()
