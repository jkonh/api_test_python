# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：AgentBaseTest.py
@Date      ：2023/7/21 14:35
@Author    ：ChenGH
"""
import importlib
import inspect
import os
import time
import yaml
from common.handle_path import PAGE_PATH, TEST_DATA_PATH
from page.base import base


class AgentBaseTest(object):
    """
    获取page目录下所有python文件中的class对象，存放在classList中
    """

    def getClassList(self):
        onlyfiles = []

        for dirPath, subDir, filenames in os.walk(PAGE_PATH):
            for filename in filenames:
                if filename.endswith(".py"):
                    module_name = filename.split(".py")[0]
                    # onlyfiles = ["controller.FileManagement", "controller.UserManagement"]
                    onlyfiles.append(f"page.{module_name}")
        classList = []
        for x in onlyfiles:
            module = importlib.import_module(x)
            for name, obj in inspect.getmembers(module, inspect.isclass):
                classList.append(obj)
        return classList

    """
    读取测试数据
    读取testData目录下的所有yml文件，将数据存入data_all字典
    """

    def getTestData(self):
        test_data_path = TEST_DATA_PATH
        yml_lst = [f"{test_data_path}/{item}"
                   for item in os.listdir(f'{test_data_path}')
                   if item.endswith(".yml") or item.endswith(".yaml")]
        data_all = {}
        for test_yml in yml_lst:
            with open(test_yml, "r", encoding="utf-8") as file:
                data = yaml.load(file, Loader=yaml.FullLoader)
                data_all.update(data)
        return data_all

    '''
    提取测试数据里面的操作步骤数据
    '''

    def getTestSteps(self, testCaseName):
        data = self.getTestData()
        testSteps = data[testCaseName]["test_step"]
        return testSteps

    '''
    执行测试步骤，输出执行结果，及预期结果
    '''

    def doTestSteps(self, testCaseName):
        testSteps = self.getTestSteps(testCaseName)
        '''
        遍历并执行当前用例的所有测试步骤
        '''
        for testStep in testSteps:
            for funcName, params in testStep.items():
                '''
                遍历controller目录文件，从所有封装的class对象里，找到当前测试步骤对应的函数
                注意：封装测试函数的时候，不要封装同名函数，不然这里可能会出错
                '''
                for mClass in self.getClassList():
                    if hasattr(mClass, funcName):
                        func = getattr(mClass(), funcName)
                        break
                    # else:
                    #      print(f"未找到{funcName}")
                if "test_assert" not in params:
                    print(f"{funcName}缺少断言")
                else:
                    assertData = params.pop("test_assert")
                    func(**params)
                    assertType = assertData.pop("type")
                    time_sleep = assertData.pop("sleep")

                    # self.driver.implicitly_wait(time_sleep)
                    time.sleep(time_sleep)
                    expectValue = True
                    '''
                    判断控件是否存在，如果有其他判断需求，可以在UIElement中增加对应的判断函数封装
                    '''
                    if assertType == "assertExist":
                        element = assertData.pop("element")
                        # element = assertData.pop("element")
                        for key, value in element.items():
                            actualValue = True if base(key, value).isExist() else False
                            break
                    elif assertType == 'assertNotExist':
                        element = assertData.pop("element")
                        """判断控件是否不存在"""
                        # element = assertData.pop("element")
                        for key, value in element.items():
                            actualValue = True if base(key, value).isnotExist() else False
                            break
                    elif assertType == 'assertActivityExist':
                        element = assertData.pop("element")
                        """判断元素是否不存在"""
                        # element = assertData.pop("element")
                        for key, value in element.items():
                            actualValue = True if base(key, value).isAcitivityExist() else False
                            break
                    elif assertType == 'assertCount':

                        """获取数量"""
                        count = assertData.pop('path_name')
                        for key, value in count.items():
                            expectValue = base('recovery_page', 'recover_count').getElement().get_attribute(
                                'text').strip()
                            actualValue = base('recovery_page', 'recover_count').getFileCount(value).strip()

                    else:
                        try:
                            element = assertData.pop("element")
                            for key, value in element.items():
                                actualValue = getattr(base(key, value), assertType)(**assertData)
                        except Exception:
                            print(f"未找到断言方法{assertType}")
                    return actualValue, expectValue


if __name__ == "__main__":
    agentBaseTest = AgentBaseTest()
    print(agentBaseTest.getClassList())
