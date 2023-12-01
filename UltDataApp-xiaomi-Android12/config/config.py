import os
import threading
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

print(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0])

from appium import webdriver

driver = webdriver.Remote('http://127.0.0.1:4777/wd/hub',
                          {
                              'platformName': 'Android',
                              'platformVersion': '12',
                              'deviceName': 'mi11',
                              'appPackage': 'com.android.settings',
                              'appActivity': '.Settings',
                              'automationName': 'UiAutomator2',
                              'noReset': True,
                              'unicodeKeyboard': True,
                              'resetKeyboard': True
                          })


def init_app():
    project_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 即handle_path的BASE_PATH
    if driver.is_app_installed('com.tenorshare.recovery') is True:
        driver.remove_app('com.tenorshare.recovery')
        os.system(f"adb install {project_path}\\resource\\ultdata.apk")

    else:
        os.system(f"adb install {project_path}\\resource\\ultdata.apk")


def click_agree_install():
    element = WebDriverWait(driver, timeout=60, poll_frequency=0.1).until(
        lambda x: x.find_element(By.ID, "android:id/button2"))
    time.sleep(2)
    element.click()


try:
    t1 = threading.Thread(target=init_app)
    t2 = threading.Thread(target=click_agree_install)
    t2.start()
    t1.start()
    t2.join()
except Exception as e:
    raise e
