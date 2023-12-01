import os
import threading
import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.handle_path import RESOURCE_PATH

driver = webdriver.Remote('http://127.0.0.1:4777/wd/hub', {
    'platformName': 'Android',
    'platformVersion': '11',
    'deviceName': 'oppo reno',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True
})


def judge_app_install_status():
    try:
        os.system(f"adb install {RESOURCE_PATH}\\ultdata.apk")
        # driver.install_app(f"{RESOURCE_PATH}\\ultdata.apk") 这种方法会等待方法返回结果才能往下走，在安装界面要等待，不能实时点击
    except Exception:
        pass


def allow_install():
    allow_risk_element = WebDriverWait(driver, timeout=8000, poll_frequency=0.1).until(
        lambda x: x.find_element(By.ID, "com.oplus.appdetail:id/safe_guard_checkbox"))
    allow_risk_element.click()
    time.sleep(1)
    auth_btn_element = WebDriverWait(driver, timeout=8000, poll_frequency=0.1).until(
        lambda x: x.find_element(By.ID, "com.oplus.appdetail:id/view_bottom_guide_continue_install_btn"))
    auth_btn_element.click()


t1 = threading.Thread(target=judge_app_install_status)
t2 = threading.Thread(target=allow_install)


class Config(object):
    project_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 即handle_path的BASE_PATH
    driver = driver
    if driver.is_app_installed('com.tenorshare.recovery') is True:
        driver.remove_app('com.tenorshare.recovery')
        t2.start()
        t1.start()
        # t1.join()
        t2.join()
    else:
        t2.start()
        t1.start()
        # t1.join()
        t2.join()
    time.sleep(6)
    driver.start_activity('com.tenorshare.recovery', '.WelcomeActivity')
