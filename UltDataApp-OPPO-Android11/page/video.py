# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：video.py
@Date      ：2023/7/24 15:42
@Author    ：ChenGH
"""
import time

from page.base import base
from page.baseRecovery import BaseRecovery
from page.baseScan import BaseScan


class video_scan_and_recovery(object):
    def __init__(self):
        self.BaseRecovery = BaseRecovery()

    def scan_video(self):
        BaseRecovery().back_recover_main_page()
        BaseScan('main_page', 'video_btn').scan_android_13_and_12()

    def recovery_same_step(self, page_name, filter_name):
        self.BaseRecovery.delCache('video_path', 'cleanFile')
        self.BaseRecovery.useFilter('scan_video_result_page', 'video_source_btn')
        self.BaseRecovery.filterResult(page_name, filter_name)
        self.BaseRecovery.selectData('scan_video_result_page', 'video_select_all')
        # time.sleep(2)
        # base('scan_video_result_page', 'viallselect_click_btn').click_location()
        # # base('authScanPath_page', 'allselect_click_btn').click_location()
        # time.sleep(1)
        self.BaseRecovery.recoveryData('scan_finish_page', 'export_video_btn')

    def first_time_recovery_Video(self, page_name, filter_name):
        base('scan_page', 'scan_finish_btn').getElement().click()
        self.recovery_same_step(page_name, filter_name)

    # def second_time_recovery_Video(self, page_name, filter_name):
    #     self.BaseRecovery.close_export_dialog()
    #     self.BaseRecovery.close_dialog()
    #     self.recovery_same_step(page_name, filter_name)

    def after_first_time_recovery_Video(self, page_name, filter_name):
        self.BaseRecovery.close_export_dialog()
        self.recovery_same_step(page_name, filter_name)

    def recovery_video_album(self):
        self.first_time_recovery_Video('scan_video_result_page', 'video_source_album')

    def recovery_video_twitter(self):
        self.after_first_time_recovery_Video('scan_video_result_page', 'video_source_twitter')

    def recovery_video_facebook(self):
        self.after_first_time_recovery_Video('scan_video_result_page', 'video_source_facebook')

    def recovery_video_qq(self):
        self.after_first_time_recovery_Video('scan_video_result_page', 'video_source_qq')

    def recovery_video_viber(self):
        self.after_first_time_recovery_Video('scan_video_result_page', 'video_source_viber')
