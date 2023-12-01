# encoding:utf-8
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("测试小米安卓12音频扫描及恢复")
class Test_Audio(AgentBaseTest):
    @allure.title("小米安卓12扫描音频")
    @pytest.mark.run(order=5)
    def test_AudioScan_001(self):
        actualValue, expectValue = self.doTestSteps("test_AudioScan_001")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12所有音频")
    @pytest.mark.run(order=6)
    def test_AudioRecovery_001(self):
        actualValue, expectValue = self.doTestSteps("test_AudioRecovery_001")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12QQ音频")
    @pytest.mark.run(order=7)
    def test_AudioRecovery_002(self):
        actualValue, expectValue = self.doTestSteps("test_AudioRecovery_002")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12line音频")
    @pytest.mark.run(order=8)
    def test_AudioRecovery_003(self):
        actualValue, expectValue = self.doTestSteps("test_AudioRecovery_003")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12Viber音频")
    @pytest.mark.run(order=9)
    def test_AudioRecovery_004(self):
        actualValue, expectValue = self.doTestSteps("test_AudioRecovery_004")
        assert actualValue == expectValue


if __name__ == "__main__":
    tester = Test_Audio()
    tester.test_AudioScan_001()
    tester.test_AudioRecovery_001()
    tester.test_AudioRecovery_002()
    tester.test_AudioRecovery_003()
    tester.test_AudioRecovery_004()
