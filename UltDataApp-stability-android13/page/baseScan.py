# encoding:utf-8
import time

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
        """授权许可协议->选择要扫描的功能"""
        self.ScanfuncSelect.select_func()


if __name__ == "__main__":
    BaseScan('main_page', 'photo_btn').scan_android_13_and_12()
