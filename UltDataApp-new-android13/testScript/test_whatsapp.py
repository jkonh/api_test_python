# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：test_whatsapp.py
@Date      ：2023/7/24 20:01
@Author    ：ChenGH
"""
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("测试安卓13扫描、恢复WhatsApp附件数据")
class Test_whatsapp(AgentBaseTest):
    @allure.title("测试扫描安卓13设备WhatsApp附件")
    @pytest.mark.run(order=32)
    def test_whatsappScan_001(self):
        actualValue, expectValue = self.doTestSteps("test_whatsappScan_001")
        assert actualValue == expectValue

    @allure.title("安卓13恢复WhatsApp图片")
    @pytest.mark.run(order=33)
    def test_WhatsappRecovery_001(self):
        actualValue, expectValue = self.doTestSteps("test_WhatsappRecovery_001")
        assert actualValue == expectValue

    @allure.title("安卓13恢复WhatsApp视频")
    @pytest.mark.run(order=34)
    def test_WhatsappRecovery_002(self):
        actualValue, expectValue = self.doTestSteps("test_WhatsappRecovery_002")
        assert actualValue == expectValue

    @allure.title("安卓13恢复WhatsApp音频")
    @pytest.mark.run(order=35)
    def test_WhatsappRecovery_003(self):
        actualValue, expectValue = self.doTestSteps("test_WhatsappRecovery_003")
        assert actualValue == expectValue

    @allure.title("安卓13恢复WhatsApp文档")
    @pytest.mark.run(order=36)
    def test_WhatsappRecovery_004(self):
        actualValue, expectValue = self.doTestSteps("test_WhatsappRecovery_004")
        assert actualValue == expectValue


if __name__ == '__main__':
    tester = Test_whatsapp()
    tester.test_whatsappScan_001()
    tester.test_WhatsappRecovery_001()
    tester.test_WhatsappRecovery_002()
    tester.test_WhatsappRecovery_003()
    tester.test_WhatsappRecovery_004()
