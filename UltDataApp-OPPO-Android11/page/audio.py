# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：audio.py
@Date      ：2023/7/24 17:10
@Author    ：ChenGH
"""
import time

from selenium.webdriver.common.by import By

from config.config import driver
from page.authLicense import AuthLicense
from page.base import base
from page.baseRecovery import BaseRecovery
from page.baseScan import BaseScan




class audio_scan_and_recovery(object):
    def __init__(self):
        self.BaseRecovery = BaseRecovery()

    def scan_audio(self):
        # 返回主界面-》扫描音频
        BaseScan('main_page', 'audio_btn').back_scan_main_page()  # 返回主界面
        BaseScan('main_page', 'audio_btn').scan_android_13_and_12()  # 扫描音频

    def recovery_same_step(self, page, element):
        self.BaseRecovery.delCache(page_name='audio_path', del_path='cleanFile')
        self.BaseRecovery.useFilter('scan_audio_result_page', 'audio_source_btn')
        self.BaseRecovery.filterResult(page, element)
        # time.sleep(2)
        self.BaseRecovery.selectData('scan_audio_result_page', 'audio_select_all')
        # base('authScanPath_page', 'allselect_click_btn').click_location()

        # driver.tap([(24, 434), (84, 494)], 500)
        # driver.tap([(978, 2263)])
        # time.sleep(1)
        self.BaseRecovery.recoveryData('scan_finish_page', 'export_audio_btn')

    def first_time_recovery_Audio(self, page_name, filter_name):
        base('scan_page', 'scan_finish_btn').getElement().click()
        self.recovery_same_step(page_name, filter_name)

    def second_time_recovery_Audio(self, page_name, filter_name):
        self.BaseRecovery.close_export_dialog()
        self.BaseRecovery.close_dialog()
        self.recovery_same_step(page_name, filter_name)

    def after_second_time_recovery_Audio(self, page_name, filter_name):
        self.BaseRecovery.close_export_dialog()
        self.recovery_same_step(page_name, filter_name)

    def recovery_audio_all(self):
        self.first_time_recovery_Audio('scan_audio_result_page', 'audio_source_all')

    def recovery_audio_qq(self):
        self.second_time_recovery_Audio('scan_audio_result_page', 'audio_source_qq')

    def recovery_audio_line(self):
        self.after_second_time_recovery_Audio('scan_audio_result_page', 'audio_source_line')

    def recovery_audio_viber(self):
        self.after_second_time_recovery_Audio('scan_audio_result_page', 'audio_source_viber')


