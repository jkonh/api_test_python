# _*_ coding:utf-8 _*_
"""
@Software  ：duplicate project
@FileName  ：main.py
@Date      ：2023/2/20 9:27
@Author    ：ChenGH
"""

import pytest
import os
import subprocess
import sys

from common.send_email import EmailSender
from common.handle_path import TEST_SCRIPT_PATH, BASE_PATH
from common.logger import get_log
from config.config import driver

loggers = get_log()


def runCmd(cmd):
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as p1:
        data = p1.stdout.read().decode('gbk', 'ignore').splitlines()
        for d in data:
            if d and len(d) > 0:
                print(d)
        errdata = p1.stderr.read().decode('gbk', 'ignore').splitlines()
        for err in errdata:
            if err and len(err) > 0:
                print(err)
        return data, errdata


def get_all_testScript_filenames():
    testScript_dir = TEST_SCRIPT_PATH
    testScript_filenames = []
    for root, dirs, filenames in os.walk(testScript_dir):
        for filename in filenames:
            if filename.endswith(".py") and filename != "AgentBaseTest.py":
                testScript_filenames.append(filename)
    return testScript_filenames


if __name__ == "__main__":
    # 本地运行所有用例
    paramList = list()
    paramList.append("-v")
    # 运行单个用例
    scriptFile = "test_authLicense.py"
    paramList.append("testScript/" + scriptFile)
    # 运行所有用例
    # for scriptFile in get_all_testScript_filenames():
    #     paramList.append(os.path.join(TEST_SCRIPT_PATH, scriptFile))
    projectPath = os.path.dirname(os.path.abspath(__file__))
    # 确定当前系统用户密码
    password = "*****"
    # 确定allure测试结果生成路径
    resultPath = os.path.join(projectPath, "allure-results")
    # 本地运行allure
    paramList.append("--alluredir=" + resultPath)
    pytest.main(paramList)
    report_path = os.path.join(resultPath, 'report')
    # 本地运行生成allure报告
    genargs = ["cmd", "/c", "call", "allure", "generate", resultPath, "--clean", "-o", report_path]
    showargs = ["cmd", "/c", "call", "allure", "open", report_path, "-p", "34567"]
    runCmd(genargs)
    runCmd(showargs)
"""
    # jenkins构建 运行所有用例
    pytest.main(["-vs"])
    projectName = sys.argv[1]
    buildNumber = sys.argv[2]
    buildURL = sys.argv[3]
    emailReceivers = sys.argv[4]
    loggers.info(f"emailReceivers：{emailReceivers}")
    paramList = list()
    paramList.append("-v")
    # 运行单个用例
    # scriptFile = "test_extractPDF.py"
    # paramList.append("testScript/" + scriptFile)
    # 运行所有用例
    for scriptFile in get_all_testScript_filenames():
        paramList.append(os.path.join(BASE_PATH, "testScript/" + scriptFile))
    # 运行标记teskMark的测试用例
    # paramList.append("-m")
    # paramList.append("testMark")
    # 获取当前项目路径r'D:\\Users\\Desktop\\现行项目\\ultdata Android\\UltDataAppUITest'
    projectPath = os.path.dirname(os.path.abspath(__file__))
    # 确定当前系统用户密码
    password = "666666"
    # 确定allure测试结果生成路径
    resultPath = os.path.join(projectPath, "allure-results")
    # Jenkins运行allure
    resultPath_build = os.path.join(resultPath, buildNumber)
    paramList.append("--alluredir=" + resultPath_build)
    # 本地运行allure
    # paramList.append("--alluredir=" + resultPath)
    pytest.main(paramList)
    jenkinsWorkspace = rf"/var/lib/jenkins/workspace/{projectName}"
    cmd_uploadReport = fr"pscp -pw {password} -r -batch -hostkey SHA256:xPaEbA+66bmpNfDEvn7kYPkGRqcl//YXTPiumvJ7nss {resultPath} root@192.168.1.48:{jenkinsWorkspace}"
    data, errdata = runCmd(cmd_uploadReport)
    loggers.info(f"data：{data}")
    loggers.info(f"errdata：{errdata}")
    receivers = emailReceivers.split(";")
    emailSender = EmailSender()
    emailSender.sendEmail(receivers=receivers, projectName=projectName, buildNumber=buildNumber, buildURL=buildURL)
    report_path = os.path.join(resultPath, 'report')
"""
