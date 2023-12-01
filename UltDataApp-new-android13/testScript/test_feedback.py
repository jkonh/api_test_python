# encoding:utf-8
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("测试反馈功能")
class Test_Feedback(AgentBaseTest):

    @allure.title('输入错误邮箱提交反馈失败')
    @pytest.mark.run(order=37)
    def test_feedback_001(self):
        actualValue, expectValue = self.doTestSteps("test_feedback_001")
        assert actualValue == expectValue

    @allure.title('不输入反馈内容提交反馈失败')
    @pytest.mark.run(order=38)
    def test_feedback_002(self):
        actualValue, expectValue = self.doTestSteps("test_feedback_002")
        assert actualValue == expectValue

    @allure.title('输入正确的邮箱及反馈内容提交反馈成功')
    @pytest.mark.run(order=39)
    def test_feedback_003(self):
        actualValue, expectValue = self.doTestSteps("test_feedback_003")
        assert actualValue == expectValue


if __name__ == "__main__":
    tester = Test_Feedback()
    tester.test_feedback_001()
    tester.test_feedback_002()
    tester.test_feedback_003()
