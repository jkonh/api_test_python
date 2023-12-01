# _*_ coding: utf-8 _*
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("测试ultdata APP扫描权限授权")
class Test_AuthUltdataScanpath(AgentBaseTest):
    @allure.title("不授权ultdata APP")
    @pytest.mark.run(order=3)
    def test_AuthUltdataScanpath_001(self):
        actualValue, expectValue = self.doTestSteps("test_AuthUltdataScanpath_001")
        assert actualValue == expectValue

    @pytest.mark.run(order=4)
    @allure.title("成功授权ultdata APP")
    def test_AuthUltdataScanpath_002(self):
        actualValue, expectValue = self.doTestSteps("test_AuthUltdataScanpath_002")
        assert actualValue == expectValue


if __name__ == "__main__":
    tester = Test_AuthUltdataScanpath()
    tester.test_AuthUltdataScanpath_001()
    tester.test_AuthUltdataScanpath_002()
