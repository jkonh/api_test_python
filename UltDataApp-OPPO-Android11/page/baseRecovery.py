# encoding:utf-8
import time

from config import config
from page.base import base, deCache
from config.config import driver


class BaseRecovery(object):
    def back_recover_main_page(self):
        # 点击确认按钮->点击返回-》确认返回
        base("recovery_page", "recover_finish_btn").clickElement()
        driver.keyevent(4)
        base("scan_finish_page", "confirm_back_btn").clickElement()

    # 前置条件：先扫描完成，并关闭了扫描完成提示弹框
    def useFilter(self, page_name, filter_element):
        """
        扫描结果展开过滤选项
        :param page_name: 页面name，一般为扫描结果界面的name
        :param filter_element: 要展开的下拉选项
        :return:
        """

        # base('scan_page', 'scan_finish_btn').getElement().click()  # 先关闭扫描完成提示弹框
        time.sleep(1)
        base(page_name, filter_element).getElement().click()

    def filterResult(self, page_name, element_name):
        """
        扫描结果过滤功能
        :param page_name: 页面name，一般为扫描结果界面的name
        :param element_name: 展开的过滤选项菜单中的元素，如相册
        :return:
        """
        base(page_name, element_name).getElement().click()
        config.Config.driver.keyevent(4)

    def selectData(self, page_name, element_name):
        """
        勾选过滤结果并清空缓存文件
        :param page_name: 过滤结果界面名/扫描结果界面名
        :param element_name:全选按钮的元素名
        :param del_path:要清空的路径名称,参考cmdCommand.yml文件中封装的名称
        :return:
        """
        base(page_name, element_name).getElement().click()
        time.sleep(2)

    # 清理缓存文件
    def delCache(self, page_name, del_path):
        deCache(page_name, del_path)

    def recoveryData(self, page_name, element_name):
        # 点击恢复按钮
        base(page_name, element_name).getElement().click()
        # 等待恢复成功
        base('recovery_page', 'recover_finish_btn').waitElement()

    def close_export_dialog(self):
        # 关闭恢复完成弹框
        base('recovery_page', 'recover_finish_btn').getElement().click()

    def close_dialog(self):
        # 首次恢复完成后关闭好评弹框
        base('recovery_page', 'recover_close_dialog').getElement().click()


if __name__ == '__main__':
    br = BaseRecovery()
    br.useFilter('scan_video_result_page', 'video_source_btn')
    br.delCache('video_path', 'cleanFile')
    br.filterResult('scan_video_result_page', 'video_source_album')
    br.selectData('scan_video_result_page', 'video_select_all')
    br.recoveryData('scan_finish_page', 'export_video_btn')
