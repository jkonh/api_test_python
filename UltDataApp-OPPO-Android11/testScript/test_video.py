# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：test_video.py
@Date      ：2023/7/24 9:42
@Author    ：ChenGH
"""
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("测试oppo_reno安卓11视频扫描和恢复")
class Test_video(AgentBaseTest):
    @allure.title("oppo_reno安卓11成功扫描视频")
    @pytest.mark.run(order=16)
    def test_VideoScan_001(self):
        actualValue, expectedValue = self.doTestSteps("test_VideoScan_001")
        assert actualValue == expectedValue

    @allure.title("恢复相册视频")
    @pytest.mark.run(order=17)
    def test_VideoRecovery_001(self):
        actualValue, expectValue = self.doTestSteps("test_VideoRecovery_001")
        assert actualValue == expectValue

    @allure.title("恢复Twitter视频")
    @pytest.mark.run(order=18)
    def test_VideoRecovery_002(self):
        actualValue, expectValue = self.doTestSteps("test_VideoRecovery_002")
        assert actualValue == expectValue

    @allure.title("恢复Facebook视频")
    @pytest.mark.run(order=19)
    def test_VideoRecovery_003(self):
        actualValue, expectValue = self.doTestSteps("test_VideoRecovery_003")
        assert actualValue == expectValue

    @allure.title("恢复QQ视频")
    @pytest.mark.run(order=20)
    def test_VideoRecovery_004(self):
        actualValue, expectValue = self.doTestSteps("test_VideoRecovery_004")
        assert actualValue == expectValue

    @allure.title("恢复Viber视频")
    @pytest.mark.run(order=21)
    def test_VideoRecovery_005(self):
        actualValue, expectValue = self.doTestSteps("test_VideoRecovery_005")
        assert actualValue == expectValue


if __name__ == "__main__":
    tester = Test_video()
    tester.test_VideoScan_001()
    tester.test_VideoRecovery_001()
    tester.test_VideoRecovery_002()
    tester.test_VideoRecovery_003()
    tester.test_VideoRecovery_004()
    tester.test_VideoRecovery_005()
