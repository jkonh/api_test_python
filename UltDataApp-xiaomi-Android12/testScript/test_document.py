# _*_ coding: utf-8 _*
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("小米安卓12文档扫描及恢复功能")
class Test_Doc(AgentBaseTest):
    @allure.title("扫描小米安卓12文档")
    @pytest.mark.run(order=24)
    def test_DocumentScan_001(self):
        actualValue, expectValue = self.doTestSteps("test_DocumentScan_001")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12 doc文档")
    @pytest.mark.run(order=25)
    def test_DocRecovery_001(self):
        actualValue, expectValue = self.doTestSteps("test_DocRecovery_001")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12 PPT文档")
    @pytest.mark.run(order=26)
    def test_DocRecovery_002(self):
        actualValue, expectValue = self.doTestSteps("test_DocRecovery_002")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12 xls文档")
    @pytest.mark.run(order=27)
    def test_DocRecovery_003(self):
        actualValue, expectValue = self.doTestSteps("test_DocRecovery_003")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12 zip文档")
    @pytest.mark.run(order=28)
    def test_DocRecovery_004(self):
        actualValue, expectValue = self.doTestSteps("test_DocRecovery_004")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12 rar文档")
    @pytest.mark.run(order=29)
    def test_DocRecovery_005(self):
        actualValue, expectValue = self.doTestSteps("test_DocRecovery_005")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12 apk文档")
    @pytest.mark.run(order=30)
    def test_DocRecovery_006(self):
        actualValue, expectValue = self.doTestSteps("test_DocRecovery_006")
        assert actualValue == expectValue

    @allure.title("恢复小米安卓12 txt文档")
    @pytest.mark.run(order=31)
    def test_DocRecovery_007(self):
        actualValue, expectValue = self.doTestSteps("test_DocRecovery_007")
        assert actualValue == expectValue


if __name__ == "__main__":
    tester = Test_Doc()
    tester.test_DocumentScan_001()
    tester.test_DocRecovery_001()
    tester.test_DocRecovery_002()
    tester.test_DocRecovery_003()
    tester.test_DocRecovery_004()
    tester.test_DocRecovery_005()
    tester.test_DocRecovery_006()
    tester.test_DocRecovery_007()
