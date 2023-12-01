# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：photo.py
@Date      ：2023/7/21 17:14
@Author    ：ChenGH
"""
from page.base import base
from page.baseRecovery import BaseRecovery

from page.baseScan import BaseScan


class photo_scan_and_recovery(object):
    def __init__(self):
        self.BaseRecovery = BaseRecovery()

    def scan_photo(self):
        self.BaseRecovery.back_recover_main_page()  # 从音频恢复完成弹框，返回app主界面
        BaseScan('main_page', 'photo_btn').scan_android_13_and_12()

    def close_enhancer_export(self):
        # 关闭增强设置（避免出现导出后,显示的数量和导出路径数量不一致问题）：切换到所有图片，点击其中一张图片，进入预览界面，关闭增强说明弹框，点击右上角增强按钮，关闭导出增强，点击增强弹框关闭按钮，点击返回按钮
        self.BaseRecovery.useFilter('scan_photo_result_page', 'photo_source_btn')
        self.BaseRecovery.filterResult('scan_photo_result_page', 'photo_source_all')
        base('scan_photo_result_page', 'photo_filter_all_result').getElement().click()
        base('photo_view_page', 'guide_close_btn').getElement().click()
        base('photo_view_page', 'enhance_setting_btn').getElement().click()
        base('photo_view_page', 'setting_enhance').getElement().click()
        base('photo_view_page', 'close_btn').getElement().click()
        base('photo_view_page', 'back_btn').getElement().click()

    def recovery_same_step(self, page_name, filter_name):
        # 恢复功能的相同操作：清除缓存数据、点击过滤选项，选择过滤项、勾选数据，点击导出
        self.BaseRecovery.delCache('photo_path', 'cleanFile')
        self.BaseRecovery.useFilter('scan_photo_result_page', 'photo_source_btn')
        self.BaseRecovery.filterResult(page_name, filter_name)
        self.BaseRecovery.selectData('scan_photo_result_page', 'photo_select_all')
        self.BaseRecovery.recoveryData('scan_finish_page', 'export_photo_btn')

    def first_time_recovery_Photo(self, page_name, filter_name):
        base('scan_page', 'scan_finish_btn').getElement().click()  # 点击完成按钮
        self.close_enhancer_export()  # 关闭增强功能
        self.recovery_same_step(page_name, filter_name)

    # def second_time_recovery_Photo(self, page_name, filter_name):
    #     self.BaseRecovery.close_export_dialog()
    #     self.BaseRecovery.close_dialog()
    #     self.recovery_same_step(page_name, filter_name)

    def after_first_time_recovery_Photo(self, page_name, filter_name):
        self.BaseRecovery.close_export_dialog()
        self.recovery_same_step(page_name, filter_name)

    def recovery_photo_twitter(self):
        self.first_time_recovery_Photo('scan_photo_result_page', 'photo_source_twitter')

    def recovery_photo_album(self):
        self.after_first_time_recovery_Photo('scan_photo_result_page', 'photo_source_album')

    def recovery_photo_wab(self):
        self.after_first_time_recovery_Photo('scan_photo_result_page', 'photo_source_whatsapp_business')

    def recovery_photo_wechat(self):
        self.after_first_time_recovery_Photo('scan_photo_result_page', 'photo_source_wechat')

    def recovery_photo_line(self):
        self.after_first_time_recovery_Photo('scan_photo_result_page', 'photo_source_line')


if __name__ == '__main__':
    photo_scan_and_recovery().scan_photo()
    photo_scan_and_recovery().recovery_photo_twitter()
    photo_scan_and_recovery().recovery_photo_album()
