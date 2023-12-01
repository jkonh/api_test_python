# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：WhatsApp.py
@Date      ：2023/7/24 19:30
@Author    ：ChenGH
"""
import time

from config import config
from page.base import base
from page.baseRecovery import BaseRecovery
from page.baseScan import BaseScan


class whatsapp_san_and_recovery(object):
    def __init__(self):
        self.BaseRecovery = BaseRecovery()

    def Whatsapp_attachment_Scan(self):
        self.BaseRecovery.back_recover_main_page()  # 返回主界面
        BaseScan('main_page', 'whatsapp_function_btn').scan_android_13_and_12()
        base('whatsapp_main_page', 'recovery_attach_btn').clickElement()
        base('whatsapp_main_page', 'whatsapp_scan_state').waitElement()

    def recovery_whatsapp_photo(self):
        """扫描whatsapp-->清除以前的数据-->点击恢复的模块-->全选数据-->恢复-->点击完成-->点击好评"""
        self.BaseRecovery.delCache('whatsapp_photo_path', 'cleanFile')
        base('whatsapp_main_page', 'whatsapp_photo_btn').clickElement()
        # time.sleep(2)
        # base('whatsapp_main_page', 'whatsapp_photos_btn').click_location()
        # time.sleep(1)
        base('whatsapp_photo_page', 'photo_select_btn').clickElement()
        # time.sleep(2)
        # base('whatsapp_photo_page', 'pallselect_click_btn').click_location()
        # time.sleep(1)
        base('whatsapp_photo_page', 'photo_export_btn').clickElement()
        base('recovery_page', 'recover_finish_btn').waitElement()

    def recovery_whatsapp_video(self):
        self.BaseRecovery.close_export_dialog()
        self.BaseRecovery.delCache('whatsapp_video_path', 'cleanFile')
        # self.BaseRecovery.close_dialog()
        config.Config.driver.keyevent(4)
        base('whatsapp_main_page', 'whatsapp_video_btn').clickElement()
        base('whatsapp_video_page', 'video_select_btn').clickElement()
        # time.sleep(2)
        # base('whatsapp_video_page', 'vallselect_click_btn').click_location()
        # time.sleep(1)
        base('whatsapp_video_page', 'video_export_btn').clickElement()
        base('recovery_page', 'recover_finish_btn').waitElement()

    def recovery_whatsapp_audio(self):
        self.BaseRecovery.close_export_dialog()
        self.BaseRecovery.delCache('whatsapp_audio_path', 'cleanFile')
        config.Config.driver.keyevent(4)
        base('whatsapp_main_page', 'whatsapp_audio_btn').clickElement()
        base('whatsapp_audio_page', 'audio_select_btn').clickElement()
        # time.sleep(2)
        # base('whatsapp_video_page', 'aallselect_click_btn').click_location()
        # time.sleep(1)
        base('whatsapp_audio_page', 'audio_export_btn').clickElement()
        base('recovery_page', 'recover_finish_btn').waitElement()

    def recovery_whatsapp_doc(self):
        self.BaseRecovery.close_export_dialog()
        self.BaseRecovery.delCache('whatsapp_doc_path', 'cleanFile')
        config.Config.driver.keyevent(4)
        base('whatsapp_main_page', 'whatsapp_doc_btn').clickElement()
        base('whatsapp_doc_page', 'doc_select_btn').clickElement()
        # time.sleep(2)
        # base('whatsapp_doc_page', 'dallselect_click_btn').click_location()
        # time.sleep(1)
        base('whatsapp_doc_page', 'doc_export_btn').clickElement()
        base('recovery_page', 'recover_finish_btn').waitElement()
