# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：send_email.py
@Date      ：2023/7/21 11:49
@Author    ：ChenGH
"""
import smtplib
from email.mime.text import MIMEText
from email.header import Header

from common.logger import get_log

loggers = get_log()

# 第三方 SMTP 服务
# mail_host = "smtp.163.com"  # 设置服务器
# mail_sender = "zhanguang12@163.com"  # 用户名
# mail_pass = "OFQYZQXYXZMCRDSA"  # 口令
mail_host = "smtp.exmail.qq.com"  # 设置服务器
mail_sender = "chenguanghui@tenorshare.cn"  # 用户名
mail_pass = "Re12345"  # 口令


class EmailSender():
    def sendEmail(self, **kwargs):
        # receivers = ['zhanguang@tenorshare.cn']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        # PROJECT_NAME = "iCareFilesApiTest"
        # BUILD_NUMBER = 28
        # BUILD_URL = "http://jenkins-test.tenorshare.cn/me/my-views/view/all/job/iCareFilesApiTest/28/"
        receivers = kwargs.get("receivers")
        PROJECT_NAME = kwargs.get("projectName")
        BUILD_NUMBER = kwargs.get("buildNumber")
        BUILD_URL = kwargs.get("buildURL")
        loggers.info(f"receivers：{receivers}")
        loggers.info(f"PROJECT_NAME：{PROJECT_NAME}")
        loggers.info(f"BUILD_NUMBER：{BUILD_NUMBER}")
        loggers.info(f"BUILD_URL：{BUILD_URL}")
        REPORT_URL = f"http://jenkins-test.tenorshare.cn/job/{PROJECT_NAME}/{BUILD_NUMBER}/allure/"
        content = f'''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <title>{PROJECT_NAME}-第{BUILD_NUMBER}次构建日志</title>
        </head>
        <body leftmargin="8" marginwidth="0" topmargin="8" marginheight="4"
            offset="0">
            <table width="95%" cellpadding="0" cellspacing="0"
                style="font-size: 11pt; font-family: Tahoma, Arial, Helvetica, sans-serif">
                <tr>
                    <td><br />
                    <b><font color="#0B610B">构建信息</font></b>
                    <hr size="2" width="100%" align="center" /></td>
                </tr>
                <tr>
                    <td>
                        <ul>
                            <li>项目名称 ： {PROJECT_NAME}</li>
                            <li>构建编号 ： 第{BUILD_NUMBER}次构建</li>
                            <li>构建日志 ： <a href="{BUILD_URL}console">{BUILD_URL}console</a></li>
                            <li>测试报告 ： <a href="{REPORT_URL}">{REPORT_URL}</a></li>
                        </ul>
                    </td>
                </tr>

            </table>
        </body>
        </html>
        '''

        message = MIMEText(content, 'html', 'utf-8')
        message['From'] = Header("自动化测试", 'utf-8')
        # message['To'] = Header(f"iCareFiles项目组", 'utf-8')
        subject = f'{PROJECT_NAME}测试报告'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
            smtpObj.login(mail_sender, mail_pass)
            smtpObj.sendmail(mail_sender, receivers, message.as_string())
            loggers.info("邮件发送成功")
        except smtplib.SMTPException:
            loggers.info("Error: 无法发送邮件")