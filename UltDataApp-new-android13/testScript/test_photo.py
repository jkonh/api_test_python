# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：test_photo.py
@Date      ：2023/7/21 17:18
@Author    ：ChenGH
"""
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("测试图片扫描和恢复")
class Test_photo(AgentBaseTest):
    @allure.title("安卓13成功扫描图片")
    @pytest.mark.run(order=10)
    def test_PhotoScan_001(self):
        actualValue, expectValue = self.doTestSteps("test_PhotoScan_001")
        assert actualValue == expectValue

    @allure.title("安卓13成功恢复twitter图片")
    @pytest.mark.run(order=11)
    def test_PhotoRecovery_001(self):
        actualValue, expectValue = self.doTestSteps("test_PhotoRecovery_001")
        assert actualValue == expectValue

    @allure.title("安卓13成功恢复相册图片")
    @pytest.mark.run(order=12)
    def test_PhotoRecovery_002(self):
        actualValue, expectValue = self.doTestSteps("test_PhotoRecovery_002")
        assert actualValue == expectValue

    @allure.title("恢复WhatsAppBusiness图片")
    @pytest.mark.run(order=13)
    def test_PhotoRecovery_003(self):
        actualValue, expectValue = self.doTestSteps("test_PhotoRecovery_003")
        assert actualValue == expectValue

    @allure.title("恢复微信图片")
    @pytest.mark.run(order=14)
    def test_PhotoRecovery_004(self):
        actualValue, expectValue = self.doTestSteps("test_PhotoRecovery_004")
        assert actualValue == expectValue

    @allure.title("恢复line图片")
    @pytest.mark.run(order=15)
    def test_PhotoRecovery_005(self):
        actualValue, expectValue = self.doTestSteps("test_PhotoRecovery_005")
        assert actualValue == expectValue


if __name__ == "__main__":
    tester = Test_photo()
    tester.test_PhotoScan_001()
    tester.test_PhotoRecovery_001()
    tester.test_PhotoRecovery_002()
    tester.test_PhotoRecovery_003()
    tester.test_PhotoRecovery_004()
    tester.test_PhotoRecovery_005()
