# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：document.py
@Date      ：2023/7/24 17:27
@Author    ：ChenGH
"""
import time

from page.base import base
from page.baseRecovery import BaseRecovery
from page.baseScan import BaseScan


class document_scan_and_recovery(object):
    def __init__(self):
        self.BaseRecovery = BaseRecovery()

    def scan_document(self):
        BaseRecovery().back_recover_main_page()
        BaseScan('main_page', 'doc_btn').scan_android_13_and_12()

    def recovery_same_step(self, page, element):
        self.BaseRecovery.delCache(page_name='doc_path', del_path='cleanFile')
        self.BaseRecovery.useFilter('scan_doc_result_page', 'doc_source_btn')
        self.BaseRecovery.filterResult(page, element)
        self.BaseRecovery.selectData('scan_doc_result_page', 'doc_select_all')
        # time.sleep(2)
        # base('scan_doc_result_page', 'dallselect_click_btn').click_location()
        # time.sleep(1)
        self.BaseRecovery.recoveryData('scan_finish_page', 'export_doc_btn')

    def first_time_recovery_Doc(self, page_name, filter_name):
        base('scan_page', 'scan_finish_btn').getElement().click()
        self.recovery_same_step(page_name, filter_name)

    # def second_time_recovery_Doc(self, page_name, filter_name):
    #     self.BaseRecovery.close_export_dialog()
    #     self.BaseRecovery.close_dialog()
    #     self.recovery_same_step(page_name, filter_name)

    def after_first_time_recovery_Doc(self, page_name, filter_name):
        self.BaseRecovery.close_export_dialog()
        self.recovery_same_step(page_name, filter_name)

    def recovery_Doc_doc(self):
        self.first_time_recovery_Doc('scan_doc_result_page', 'doc_format_doc')

    def recovery_Doc_ppt(self):
        self.after_first_time_recovery_Doc('scan_doc_result_page', 'doc_format_ppt')

    def recovery_Doc_xls(self):
        self.after_first_time_recovery_Doc('scan_doc_result_page', 'doc_format_xls')

    def recovery_Doc_zip(self):
        self.after_first_time_recovery_Doc('scan_doc_result_page', 'doc_format_zip')

    def recovery_Doc_rar(self):
        self.after_first_time_recovery_Doc('scan_doc_result_page', 'doc_format_rar')

    def recovery_Doc_apk(self):
        self.after_first_time_recovery_Doc('scan_doc_result_page', 'doc_format_apk')

    def recovery_Doc_txt(self):
        self.after_first_time_recovery_Doc('scan_doc_result_page', 'doc_format_txt')
