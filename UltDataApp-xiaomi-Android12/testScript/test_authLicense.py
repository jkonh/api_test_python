# _*_ coding: utf-8 _*
import pytest

from testScript.AgentBaseTest import AgentBaseTest
import allure


@allure.story("测试授权license功能")
class Test_authLicense(AgentBaseTest):
    # @allure.title("不同意授权license")
    @pytest.mark.run(order=1)
    def test_AuthLicense_001(self):
        actualValue, expectValue = self.doTestSteps("test_AuthLicense_001")
        assert actualValue == expectValue

    # @allure.title("同意授权license")
    @pytest.mark.run(order=2)
    def test_AuthLicense_002(self):
        actualValue, expectValue = self.doTestSteps("test_AuthLicense_002")
        assert actualValue == expectValue


if __name__ == "__main__":
    tester = Test_authLicense()
    tester.test_AuthLicense_001()
    tester.test_AuthLicense_002()
