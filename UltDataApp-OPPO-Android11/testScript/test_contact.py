# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataAppUITest
@FileName  ：test_contact.py
@Date      ：2023/4/18 14:18
@Author    ：ChenGH
"""
import allure
import pytest

from testScript.AgentBaseTest import AgentBaseTest


@allure.story("联系人扫描、恢复功能测试")
class Test_Contact(AgentBaseTest):

    @allure.title("测试正常扫描联系人完成")
    @pytest.mark.run(order=22)
    def test_Contact_001(self):
        actualValue, expectValue = self.doTestSteps("test_Contact_001")
        assert actualValue == expectValue

    @allure.title("测试正常导出联系人成功")
    @pytest.mark.run(order=23)
    def test_Contact_002(self):
        actualValue, expectValue = self.doTestSteps("test_Contact_002")
        assert actualValue == expectValue
