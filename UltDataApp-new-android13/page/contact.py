# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataAppUITest
@FileName  ：contact.py
@Date      ：2023/4/10 17:50
@Author    ：ChenGH
"""
import time

from page.base import base
from page.baseRecovery import BaseRecovery

from page.scanfuncSelect import ScanfuncSelect


class contact(object):

    def auth_contact(self):
        # 关闭视频恢复完成弹框-》返回主界面-》扫描联系人
        BaseRecovery().back_recover_main_page()  # 返回主界面
        time.sleep(3)
        ScanfuncSelect("main_page", "contact_btn").select_func()  # 点击联系人
        base('auth_page', 'contact_allow').getElement().click()  # 授权联系人权限

    def scan_contact_success(self):
        # 等待扫描完成
        self.auth_contact()
        base('contact_page', 'scanComplete_btn').waitElement()

    def recover_contact_success(self):
        # 点击完成提示
        base('contact_page', 'scanComplete_btn').getElement().click()
        # 点击菜单按钮
        base('contact_page', 'menu_btn').getElement().click()
        # 点击全选按钮
        base('contact_page', 'select_all_btn').getElement().click()
        # 点击保存按钮
        base('contact_page', 'save_btn').getElement().click()
        # 选择恢复到通讯录app
        base('contact_page', 'save_contacts_btn').getElement().click()
        # 等待恢复完成
        base('contact_page', 'recover_success').waitElement()


if __name__ == '__main__':
    contact().auth_contact()
    contact().scan_contact_success()
    contact().recover_contact_success()
