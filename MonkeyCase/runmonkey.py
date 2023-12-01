import os
import subprocess
import zipfile

import openpyxl
import zmail


# 执行monkey用例
def runmonkey(excelpath, monkeyClickCount):
    device1 = os.popen('adb devices').readlines()
    device2 = str(device1).split(' ')
    for i in device2:
        if r'\tdevice' in i:
            # 获取连接成功设备序列号
            devicename = i.split(r'\t')[0][1:]

            # 执行monkey测试用例循环次数
            for i in range(int(monkeyClickCount)):

                # 打开用例excel表格
                excel = openpyxl.load_workbook(filename=excelpath)
                # 获取对应的表名
                sheet = excel['monkey']
                for values in sheet.values:
                    if type(values[0]) is int:
                        # 当前所执行命令
                        print(f'*******************************正在执行：{values[1]}********************************')
                        str_temp = values[2].split(',')
                        cmd = ''.join(str_temp)
                        path = os.path.dirname(os.path.abspath(__file__))
                        save_path = os.path.join(path, f'log\log{i + 1}')
                        if os.path.exists(save_path):
                            print(f'文件夹{save_path}已存在！')
                        else:
                            os.makedirs(save_path)

                        logpath = os.path.join(save_path, f'log{values[0]}.txt')
                        monkeycmd = f'adb -s {devicename} shell ' + cmd + logpath

                        # 执行表里的全部用例
                        p2 = subprocess.Popen(monkeycmd, shell=True, stdout=subprocess.PIPE).stdout
                        print(p2.read().decode('gbk'))

            print(f'*******************************正在执行：打印崩溃日志********************************')
            crash1 = 'dumpsys dropbox | findstr data_app_crash'
            order1 = f'adb -s {devicename} shell ' + crash1

            p3 = subprocess.Popen(order1, shell=True, stdout=subprocess.PIPE).stdout
            print(p3.read().decode('gbk'))

            print(f'*******************************正在执行：打印具体时间的崩溃日志********************************')
            path = os.path.dirname(os.path.abspath(__file__))
            crashpath = os.path.join(path, r'log\crash_log.txt')
            # crash = f'adb -s {devicename} shell ' + 'dumpsys dropbox --print 11:03:27>' + crashpath
            crash_log_order = f'adb -s {devicename} shell ' + 'dumpsys dropbox --print >' + crashpath
            p4 = subprocess.Popen(crash_log_order, shell=True, stdout=subprocess.PIPE).stdout
            print(p4.read().decode('gbk'))


def zipDir(dirpath, outFullName):
    """压缩指定文件夹：
    dirpath：目标文件夹路径
    outFullName：压缩文件保存路径+XXX.zip
    """
    # 遍历目录和处理文件
    zip = zipfile.ZipFile(outFullName, 'w', zipfile.ZIP_DEFLATED)
    for path, dirname, filenames in os.walk(dirpath):
        # 去掉目标根路径，只对目标文件夹下边的文件及文件夹进行压缩(包括父文件夹本身)
        this_path = os.path.abspath('.')  # 获取当前脚本的绝对路径
        fpath = path.replace(this_path, '')
        for filename in filenames:
            # 遍历文件夹中所有的文件并写入压缩文件中
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()


def sendEmail():
    # 邮件内容
    mail_content = {
        'subject': 'ultdata monkey测试日志',
        'Content_text': '所有日志发送',
        'Attachments': './log/ultdata_log.zip'
    }
    # 发送人yzhoroizvvelbfjj
    sender = {'username': '641238672@qq.com', 'password': 'yzhoroizvvelbfjj'}
    # 接收者
    receivers = ['hedongxia@tenorshare.cn', '641238672@qq.com']
    # 登录邮箱
    server = zmail.server(sender['username'], sender['password'])
    # 发送邮件
    try:
        server.send_mail(receivers, mail_content)
        print('邮件发送成功')
    except Exception as e:
        print('邮件发送失败' % e)


if __name__ == '__main__':

    num = input("请输入monkey测试循环次数：")
    path1 = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(path1, r'data\monkeyTestcase.xlsx')
    # runmonkey('D:\Python\monkeyCase\data\monkeyTestcase.xlsx', 1)
    # 执行monkey
    monkey = runmonkey(path, num)

    with open(os.path.join(path1, 'log\crash_log.txt'), encoding="utf-8") as f:
        file = f.read()
        crash_log_info = file.split('========================================')

    for i in crash_log_info:
        if 'Exception' in i or 'Error' in i or 'ANR IN' in i or "Crashed" in i:
            # print(i)

            # 目标文件夹路径
            dirpath = os.path.join(path1, 'log')
            # 压缩文件保存路径
            outFullName = os.path.join(dirpath, 'ultdata_log.zip')
            # outFullName = input("请输入压缩后崩溃日志文件保存路径：")
            zipDir(dirpath, outFullName)

            print('文件压缩成功')
            sendEmail()
            print('邮件发送成功')

    print("**********************本次monkey测试无崩溃*****************************”")
