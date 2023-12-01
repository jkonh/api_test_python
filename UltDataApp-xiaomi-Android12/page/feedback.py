from page.authLicense import AuthLicense
from page.base import base
from config.config import driver

class Feedback(object):
    # def __init__(self):
    #     self.AuthLicense = AuthLicense()

    def feedback_email_error(self):
        # self.AuthLicense.agreeLicense()
        base("recovery_page", "recover_finish_btn").clickElement()
        driver.keyevent(4)
        base("whatsapp_scan_result_page","back_whatsapp_main_btn").clickElement()
        # 点击确认返回
        base("scan_finish_page", "confirm_back_btn").clickElement()
        # 返回主界面
        base("whatsapp_main_page","back_main_btn").clickElement()
        base('main_page', 'feedback_btn').clickElement()
        base('feedback_page', 'feedback_submit').clickElement()

    def feedback_contain_null(self):
        base('feedback_page', 'feedback_email').getElement().send_keys('chenguanghui@tenorshare.cn')
        base('feedback_page', 'feedback_submit').clickElement()

    def feedback_success(self):
        base('feedback_page', 'feedback_email').getElement().send_keys('chenguanghui@tenorshare.cn')
        base('feedback_page', 'feedback_content').getElement().send_keys('test ultdata feedback')
        base('feedback_page', 'feedback_submit').clickElement()


if __name__ == "__main__":
    Feedback = Feedback()
    Feedback.feedback_email_error()
    Feedback.feedback_contain_null()
    Feedback.feedback_success()
