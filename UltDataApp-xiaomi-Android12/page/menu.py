import time

from config import config
from page.authLicense import AuthLicense
from page.base import base


class Menu(object):
    def __init__(self):
        self.AuthLicense = AuthLicense()
        self.driver = config.driver

    def about_visit(self):
        self.AuthLicense.agreeLicense()
        base('main_page', 'menu_btn').getElement().click()
        base('menu_page', 'menu_about_btn').getElement().click()
        time.sleep(2)
        base('about_page', 'visit_website_btn').getElement().click()
        time.sleep(6)
        self.driver.switch_to.context('WEBVIEW_chrome')
    #     需要提前将设备默认浏览器设置为chrome，并且电脑安装的浏览器版本要和设备的保持一致
    #     参考https://blog.csdn.net/qq_27061049/article/details/126711410配置浏览器
    #     chrome://inspect/#devices 点击Open dedicated DevTools for Node定位设备浏览器的元素

    def about_policy(self):
        self.driver.keyevent(4)
        self.driver.switch_to.context('NATIVE_APP')
        base('about_page', 'policy_btn').getElement().click()
        if self.driver.query_app_state('com.sec.android.app.sbrowser') == 3:
            time.sleep(4)
            self.driver.switch_to.context('WEBVIEW_chrome')

    def about_license(self):
        self.driver.keyevent(4)
        self.driver.switch_to.context('NATIVE_APP')
        base('about_page', 'license_btn').getElement().click()
        time.sleep(4)
        self.driver.switch_to.context('WEBVIEW_chrome')

    def about_support(self):
        self.driver.keyevent(4)
        self.driver.switch_to.context('NATIVE_APP')
        self.driver.keyevent(4)
        base('main_page', 'menu_btn').getElement().click()
        time.sleep(2)
        base('menu_page', 'menu_support_btn').getElement().click()
        time.sleep(6)
        self.driver.switch_to.context('WEBVIEW_chrome')


if __name__ == "__main__":
    Menu = Menu()
    Menu.about_visit()
    Menu.about_policy()
    Menu.about_license()
    Menu.about_support()
