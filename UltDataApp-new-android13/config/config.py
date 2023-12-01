import os

from appium import webdriver

driver = webdriver.Remote('http://127.0.0.1:4777/wd/hub', {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'Galaxy S22',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True
})


class Config(object):
    project_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 即handle_path的BASE_PATH
    driver = driver
    if driver.is_app_installed('com.tenorshare.recovery') is True:
        driver.remove_app('com.tenorshare.recovery')
        driver.install_app(f"{project_path}\\resource\\ultdata.apk")
    else:
        driver.install_app(f"{project_path}\\resource\\ultdata.apk")


"""def reset_app(self):
    if self.driver.is_app_installed('com.tenorshare.recovery') is True:
        self.driver.remove_app('com.tenorshare.recovery')
        self.driver.install_app(f"{self.project_path}\\resource\\ultdata.apk")
    else:
        self.driver.install_app(f"{self.project_path}\\resource\\ultdata.apk")
    # return self.driver.start_activity('com.tenorshare.recovery', '.WelcomeActivity')
"""

"""
# 安卓11以下设备,由于未授权权限时，启动APP，APP的activity会变为安卓系统的activity，
直接以APP授权界面启动会报错，所以在设备设置中授权APP存储权限，以vivo Y3作为测试机，执行之前需要重装APP
driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', {
    'platformName': 'Android',
    'platformVersion': '9',
    'deviceName': 'Galaxy S22',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'automationName': 'UiAutomator2',
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
})


def click_element_by_elements_by_id(attributes, text):
    elements = driver.find_elements(By.ID, attributes)
    for element in elements:
        if element.get_attribute('text') == text:
            element.click()
            break


def click_element_by_elements_by_class(attributes, text):
    elements = driver.find_elements(By.CLASS_NAME, attributes)
    for element in elements:
        if element.get_attribute('text') == text:
            element.click()
            break

def reset_app():
    if driver.is_app_installed('com.tenorshare.recovery'):
        driver.remove_app('com.tenorshare.recovery')
        driver.install_app(f"{self.project_path}\\resource\\ultdata.apk")
    else:
        driver.install_app(f"{self.project_path}\\resource\\ultdata.apk")
reset_app()
driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
# 进入设置--》‘应用管理’--》点击ultdata APP
driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys('应用管理')
time.sleep(2)
click_element_by_elements_by_id('com.android.settings:id/breadcrumb', '更多设置')
time.sleep(6)
driver.tap([(700, 1172), (701, 1172)], 100)
time.sleep(2)
click_element_by_elements_by_id('android:id/title', 'UltData')
time.sleep(2)
click_element_by_elements_by_class('android.widget.TextView', '权限')
WebDriverWait(driver, timeout=10, poll_frequency=0.1).until(
    lambda x: x.find_element(By.ID, 'com.android.packageinstaller:id/preferenceLayout'))
driver.find_elements(By.ID, 'com.android.packageinstaller:id/preferenceLayout')[0].click()
print('打开ultdata APP存储权限成功')
driver.start_activity('com.tenorshare.recovery', '.WelcomeActivity')
"""
