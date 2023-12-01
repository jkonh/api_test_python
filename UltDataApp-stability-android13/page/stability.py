# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-new
@FileName  ：stability.py
@Date      ：2023/9/11 20:08
@Author    ：ChenGH
"""
import datetime
import os
import csv
import threading
import time
from matplotlib import pyplot as plt

from common.handle_path import CONFIG_PATH
from common.logger import get_log
from config import config
from config.config import driver
from page.base import base
from page.baseRecovery import BaseRecovery
from page.baseScan import BaseScan
from page.scanfuncSelect import ScanfuncSelect


# 前置步骤：安装->允许许可协议-》如有升级提示弹框：关闭升级提示弹框->选择图片功能->关闭隐私弹框->授权ultdata路径->
# 第二步：等待扫描完成->关闭完成提示->过滤扫描结果->勾选数据-》恢复-》关闭完成提示-》首次恢复完成关闭好评弹框-》过滤结果。恢复
# 第三步：返回主界面-》选择功能-》扫描-》第二步
def before_scan(page, element):
    config.Config()
    driver.start_activity('com.tenorshare.recovery', '.WelcomeActivity')
    time.sleep(2)
    base("authLicense_page", "license_agree").clickElement()
    try:
        time.sleep(2)
        base('main_page', 'version_dialog').getElement().click()
        # self.driver.find_element(By.ID, 'com.tenorshare.recovery:id/version_dialog_close').click()
        get_log().info("存在升级提示弹框，关闭成功")
    except Exception as e:
        get_log().info(f"升级提示弹框不存在，错误码为{e}")
        pass
    ScanfuncSelect(page, element).select_func()
    # close 隐私声明
    base('authScanPath_page', 'close_private').clickElement()
    # 点击去授权按钮
    base('authScanPath_page', 'access_Auth_btn').clickElement()
    time.sleep(3)
    # 开启ultdata app所有文件访问权限
    base('authScanPath_page', 'access_UltData_btn').getElement_by_elements()
    # 点击返回
    base('authScanPath_page', 'back_dataAuth_btn').clickElement()
    base("scan_page", "scan_finish_btn").waitElement()
    base(page_name="scan_page", element_name="scan_finish_btn").clickElement()


def choose_photo_recovery(page, element):
    BaseRecovery().delCache('photo_path', 'cleanFile')
    # 已进入扫描结果界面
    BaseRecovery().useFilter('scan_photo_result_page', 'photo_source_btn')
    BaseRecovery().filterResult(page, element)
    BaseRecovery().selectData('scan_photo_result_page', 'photo_select_all')
    BaseRecovery().recoveryData('scan_finish_page', 'export_photo_btn')
    # 等待导出完成
    base('recovery_page', 'recover_finish_btn').waitElement()
    # 点击恢复完成按钮
    base('recovery_page', 'recover_finish_btn').clickElement()


def scan_video():
    try:

        base('main_page', 'version_dialog').getElement().click()
        # self.driver.find_element(By.ID, 'com.tenorshare.recovery:id/version_dialog_close').click()
        get_log().info("存在升级提示弹框，关闭成功")
    except Exception as e:
        get_log().info(f"升级提示弹框不存在，错误码为{e}")
        pass
    BaseScan('main_page', 'video_btn').scan_android_13_and_12()
    base("scan_page", "scan_finish_btn").waitElement()
    base('scan_page', 'scan_finish_btn').getElement().click()


def choose_video_recovery(page, element):
    BaseRecovery().delCache('video_path', 'cleanFile')
    BaseRecovery().useFilter('scan_video_result_page', 'video_source_btn')
    BaseRecovery().filterResult(page, element)
    BaseRecovery().selectData('scan_video_result_page', 'video_select_all')
    BaseRecovery().recoveryData('scan_finish_page', 'export_video_btn')
    # 等待导出完成
    base('recovery_page', 'recover_finish_btn').waitElement()
    base('recovery_page', 'recover_finish_btn').clickElement()


def scan_audio():
    try:
        base('main_page', 'version_dialog').getElement().click()
        # self.driver.find_element(By.ID, 'com.tenorshare.recovery:id/version_dialog_close').click()
        get_log().info("存在升级提示弹框，关闭成功")
    except Exception as e:
        get_log().info(f"升级提示弹框不存在，错误码为{e}")
        pass
    BaseScan('main_page', 'audio_btn').scan_android_13_and_12()
    base('scan_page', 'scan_finish_btn').waitElement()
    base('scan_page', 'scan_finish_btn').clickElement()


def choose_audio_recovery(page, element):
    BaseRecovery().delCache(page_name='audio_path', del_path='cleanFile')
    BaseRecovery().useFilter('scan_audio_result_page', 'audio_source_btn')
    BaseRecovery().filterResult(page, element)
    BaseRecovery().selectData('scan_audio_result_page', 'audio_select_all')
    BaseRecovery().recoveryData('scan_finish_page', 'export_audio_btn')
    # 等待导出完成
    base('recovery_page', 'recover_finish_btn').waitElement()
    base('recovery_page', 'recover_finish_btn').clickElement()


def scan_document():
    try:

        base('main_page', 'version_dialog').getElement().click()
        # self.driver.find_element(By.ID, 'com.tenorshare.recovery:id/version_dialog_close').click()
        get_log().info("存在升级提示弹框，关闭成功")
    except Exception as e:
        get_log().info(f"升级提示弹框不存在，错误码为{e}")
        pass
    BaseScan('main_page', 'doc_btn').scan_android_13_and_12()
    base('scan_page', 'scan_finish_btn').waitElement()
    base('scan_page', 'scan_finish_btn').clickElement()


def choose_document_recovery(page, element):
    BaseRecovery().delCache(page_name='doc_path', del_path='cleanFile')
    BaseRecovery().useFilter('scan_doc_result_page', 'doc_source_btn')
    BaseRecovery().filterResult(page, element)
    BaseRecovery().selectData('scan_doc_result_page', 'doc_select_all')
    BaseRecovery().recoveryData('scan_finish_page', 'export_doc_btn')
    # 等待导出完成
    base('recovery_page', 'recover_finish_btn').waitElement()
    base('recovery_page', 'recover_finish_btn').clickElement()


def scan_whatsapp_attachment():
    try:
        base('main_page', 'version_dialog').getElement().click()
        # self.driver.find_element(By.ID, 'com.tenorshare.recovery:id/version_dialog_close').click()
        get_log().info("存在升级提示弹框，关闭成功")
    except Exception as e:
        get_log().info(f"升级提示弹框不存在，错误码为{e}")
        pass
    BaseScan('main_page', 'whatsapp_function_btn').scan_android_13_and_12()
    base('whatsapp_main_page', 'recovery_attach_btn').clickElement()
    base('whatsapp_main_page', 'whatsapp_scan_finish').waitElement()


def recover_whatsapp_attachment():
    # 恢复图片
    BaseRecovery().delCache('whatsapp_photo_path', 'cleanFile')
    base('whatsapp_main_page', 'whatsapp_photo_btn').clickElement()
    base('whatsapp_photo_page', 'photo_select_btn').clickElement()
    base('whatsapp_photo_page', 'photo_export_btn').clickElement()
    base('recovery_page', 'recover_finish_btn').waitElement()
    base('recovery_page', 'recover_finish_btn').getElement().click()
    driver.keyevent(4)
    # 恢复音频
    BaseRecovery().delCache('whatsapp_audio_path', 'cleanFile')
    base('whatsapp_main_page', 'whatsapp_audio_btn').clickElement()
    base('whatsapp_audio_page', 'audio_select_btn').clickElement()
    base('whatsapp_audio_page', 'audio_export_btn').clickElement()
    base('recovery_page', 'recover_finish_btn').waitElement()
    base('recovery_page', 'recover_finish_btn').getElement().click()
    driver.keyevent(4)
    # 恢复视频
    BaseRecovery().delCache('whatsapp_video_path', 'cleanFile')
    base('whatsapp_main_page', 'whatsapp_video_btn').clickElement()
    base('whatsapp_video_page', 'video_select_btn').clickElement()
    base('whatsapp_video_page', 'video_export_btn').clickElement()
    base('recovery_page', 'recover_finish_btn').waitElement()
    base('recovery_page', 'recover_finish_btn').getElement().click()
    driver.keyevent(4)
    # 恢复文档
    BaseRecovery().delCache('whatsapp_doc_path', 'cleanFile')
    base('whatsapp_main_page', 'whatsapp_doc_btn').clickElement()
    base('whatsapp_doc_page', 'doc_select_btn').clickElement()
    base('whatsapp_doc_page', 'doc_export_btn').clickElement()
    base('recovery_page', 'recover_finish_btn').waitElement()
    base('recovery_page', 'recover_finish_btn').getElement().click()
    driver.keyevent(4)
    driver.keyevent(4)
    base("scan_finish_page", "confirm_back_btn").clickElement()
    driver.keyevent(4)


def first_recover_contact():
    try:

        base('main_page', 'version_dialog').getElement().click()
        # self.driver.find_element(By.ID, 'com.tenorshare.recovery:id/version_dialog_close').click()
        get_log().info("存在升级提示弹框，关闭成功")
    except Exception as e:
        get_log().info(f"升级提示弹框不存在，错误码为{e}")
        pass
    ScanfuncSelect("main_page", "contact_btn").select_func()  # 点击联系人
    base('auth_page', 'contact_allow').getElement().click()  # 授权联系人权限
    base('contact_page', 'scanComplete_btn').waitElement()
    # 点击完成提示
    base('contact_page', 'scanComplete_btn').getElement().click()
    # 点击菜单按钮
    base('contact_page', 'menu_btn').getElement().click()
    # 点击全选按钮
    base('contact_page', 'select_all_btn').getElement().click()
    # 点击保存按钮
    base('contact_page', 'save_btn').getElement().click()
    # 选择恢复到通讯录app
    base('contact_page', 'save_contacts_btn').getElement().click()
    # 等待恢复完成
    base('contact_page', 'recover_success').waitElement()
    base('contact_page', 'recover_success').clickElement()
    driver.keyevent(4)
    driver.keyevent(4)
    base("scan_finish_page", "confirm_back_btn").clickElement()


def other_recover_contact():
    ScanfuncSelect("main_page", "contact_btn").select_func()  # 点击联系人
    # base('auth_page', 'contact_allow').getElement().click()  # 授权联系人权限
    base('contact_page', 'scanComplete_btn').waitElement()
    # 点击完成提示
    base('contact_page', 'scanComplete_btn').getElement().click()
    # 点击菜单按钮
    base('contact_page', 'menu_btn').getElement().click()
    # 点击全选按钮
    base('contact_page', 'select_all_btn').getElement().click()
    # 点击保存按钮
    base('contact_page', 'save_btn').getElement().click()
    # 选择恢复到通讯录app
    base('contact_page', 'save_contacts_btn').getElement().click()
    # 等待恢复完成
    base('contact_page', 'recover_success').waitElement()
    base('contact_page', 'recover_success').clickElement()
    driver.keyevent(4)
    driver.keyevent(4)
    base("scan_finish_page", "confirm_back_btn").clickElement()


times = int(input("请输入要运行的次数："))
run_time = 0


def test_ultdata():
    global run_time
    try:
        while True:
            if run_time == 0:
                print(f"需要运行的次数为{times},当前运行次数为{run_time + 1}")
                before_scan('main_page', 'photo_btn')
                choose_photo_recovery('scan_photo_result_page', 'photo_source_thumbnail')
                base('recovery_page', 'recover_close_dialog').getElement().click()
                # choose_photo_recovery('scan_photo_result_page', 'photo_source_album')
                choose_photo_recovery('scan_photo_result_page', 'photo_source_whatsapp_business')
                choose_photo_recovery('scan_photo_result_page', 'photo_source_wechat')
                # choose_photo_recovery('scan_photo_result_page', 'photo_source_line')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                scan_video()
                # choose_video_recovery('scan_video_result_page', 'video_source_album')
                # choose_video_recovery('scan_video_result_page', 'video_source_twitter')
                choose_video_recovery('scan_video_result_page', 'video_source_facebook')
                choose_video_recovery('scan_video_result_page', 'video_source_viber')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                scan_audio()
                choose_audio_recovery('scan_audio_result_page', 'audio_source_all')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                scan_document()
                choose_document_recovery('scan_doc_result_page', 'doc_format_doc')
                # choose_document_recovery('scan_doc_result_page', 'doc_format_ppt')
                # choose_document_recovery('scan_doc_result_page', 'doc_format_xls')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                # scan_whatsapp_attachment()
                # recover_whatsapp_attachment()

                first_recover_contact()
                run_time += 1

            elif run_time < times:
                print(f"需要运行的次数为{times},当前运行次数为{run_time + 1}")
                BaseScan('main_page', 'photo_btn').scan_android_13_and_12()
                base("scan_page", "scan_finish_btn").waitElement()
                base(page_name="scan_page", element_name="scan_finish_btn").clickElement()
                # choose_photo_recovery('scan_photo_result_page', 'photo_source_thumbnail')
                # choose_photo_recovery('scan_photo_result_page', 'photo_source_album')
                choose_photo_recovery('scan_photo_result_page', 'photo_source_whatsapp_business')
                # choose_photo_recovery('scan_photo_result_page', 'photo_source_wechat')
                choose_photo_recovery('scan_photo_result_page', 'photo_source_line')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                scan_video()
                choose_video_recovery('scan_video_result_page', 'video_source_album')
                # choose_video_recovery('scan_video_result_page', 'video_source_twitter')
                # choose_video_recovery('scan_video_result_page', 'video_source_facebook')
                # choose_video_recovery('scan_video_result_page', 'video_source_viber')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                scan_audio()
                choose_audio_recovery('scan_audio_result_page', 'audio_source_all')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                scan_document()
                choose_document_recovery('scan_doc_result_page', 'doc_format_doc')
                # choose_document_recovery('scan_doc_result_page', 'doc_format_ppt')
                choose_document_recovery('scan_doc_result_page', 'doc_format_xls')
                driver.keyevent(4)
                base("scan_finish_page", "confirm_back_btn").clickElement()

                scan_whatsapp_attachment()
                recover_whatsapp_attachment()

                other_recover_contact()

                run_time += 1

            else:
                print("运行完毕")
                break
    except Exception as E:
        print(E)
    finally:
        driver.quit()


# 监控变量
mem_dict = {}
time_list_mem = []
time_list_cpu = []
app_list = []
package_name = []
lines = []  # 行处理
cpu_list = []


# 读取进程名称（包名）
def get_applist():
    global package_name
    with open(f'{CONFIG_PATH}/director.txt', encoding='utf-8', mode='r') as f:
        lines_all = f.readlines()
        for appname in lines_all:
            package_name1 = appname
            appname_new = appname[0:15]
            package_name.append(package_name1)
            lines.append(appname_new)
        for line in lines:
            app_list.append(line.strip())


# 获取cpu信息
def get_cpu():
    global filename
    # adb = "adb shell top -n 1 > log_su/adb_cpuinfo.csv"  #获取cpu信息
    adb = "adb shell top -o ARGS -o %CPU -n 1 > log_su/adb_cpuinfo.csv"
    os.system(adb)
    filename = "log_su/adb_cpuinfo.csv"
    with open(filename, encoding="utf-8", mode="r") as f:
        lines = f.readlines()
        for appname in package_name:
            # appname_deletlelast = appname[:-1]
            for lis in lines:
                # 适配低版本手机
                if app_list[0] in lis and '%' in lis:
                    now = time.strftime("%H:%M:%S", time.localtime())
                    time_list_cpu.append(now)
                    cpu_1 = lis.split('%')[0]
                    cpu_2 = cpu_1.split(' ')
                    # print(cpu_2)
                    cpu = cpu_2[len(cpu_2) - 1]
                    print(f"{now}占用的cpu为：{cpu} ")
                    cpu_list.append(cpu)
                    break
                # 适配高版本手机
                elif appname in lis:
                    now = time.strftime("%H:%M:%S", time.localtime())
                    time_list_cpu.append(now)
                    cpu1 = lis.split(' ')
                    cpu2 = list(set(cpu1))
                    cpu2.sort(key=cpu1.index)
                    cpu_h = cpu2[-1].strip()
                    print(f"{now}占用的cpu为：{cpu_h} ")
                    cpu_list.append(cpu_h)
                    break
                else:
                    pass


# 获取内存信息
def get_mem():
    global filename
    adb = "adb shell dumpsys meminfo com.tenorshare.recovery > log_su/adb_meminfo.csv"
    os.system(adb)
    filename = "log_su/adb_meminfo.csv"
    with open(filename, encoding="utf-8", mode="r") as f:
        lines = f.readlines()
        # start_flag = False
        for appname in package_name:
            for line in lines:
                if "TOTAL PSS:" in line:
                    now_v = time.strftime("%H:%M:%S", time.localtime())
                    time_list_mem.append(now_v)
                    mem1 = line.split(' ')
                    mem2 = list(set(mem1))
                    mem2.sort(key=mem1.index)
                    mem_v = mem2[3]
                    mem_v = round(float(mem_v) / 1024, 2)
                    mem_dict[appname] = mem_v
                    print(f"{now_v}占用的内存为：{mem_v} ")
                    write_report_mem()
                    break
                elif "TOTAL:" in line:
                    now_v = time.strftime("%H:%M:%S", time.localtime())
                    time_list_mem.append(now_v)
                    mem1 = line.split(' ')
                    mem2 = list(set(mem1))
                    mem2.sort(key=mem1.index)
                    mem_v = mem2[2]
                    mem_v = round(float(mem_v) / 1024, 2)
                    mem_dict[appname] = mem_v
                    print(f"{now_v}占用的内存为：{mem_v} ")
                    write_report_mem()
                    break
                else:
                    pass


# csv头部
def write_head():
    headers = ['name:']
    headers.append(package_name[0])
    headers.append('init_mem')
    with open('log_su/meminfo.csv', 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
    headers = ['name:']
    headers.append(package_name[0])
    headers.append('init_cpu')
    with open('log_su/cpuinfo.csv', 'w+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()


# 将数值写入csv，用于绘图时读取
def write_report_cpu():
    # headers = ['name', 'aaa', 'init_cpu']
    with open('log_su/cpuinfo.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for key in cpu_list:
            writer.writerow([' ', ' ', key])


# 将数值写入csv，用于绘图时读取
def write_report_mem():
    headers = ['name', 'aaa', 'init_mem']
    with open('log_su/meminfo.csv', 'a+', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        for key in mem_dict:
            writer.writerow({'init_mem': mem_dict[key]})


# 绘制折线图，生成cpu测试报告
def mapping_cpu():
    filename = 'log_su/cpuinfo.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        highs = []
        for row in reader:
            high = row[2]
            highs.append(high)
        # print(highs)

    wights = time_list_cpu
    highs_float = list(map(float, highs))
    # print(f"****{highs}")
    print(f"CPU值：{highs_float}")
    # 输出平均值
    total = 0
    for value in highs_float:
        total += value
    if len(highs_float) == 0:
        print("未获取到cpu信息")
        return
    average = round(total / len(highs_float), 2)
    print(f"CPU平均值：{average}")

    # 输出最低值和最高值
    highs_hl = sorted(highs_float)
    print(f"CPU最低值：{highs_hl[0]}")
    print(f"CPU最高值：{highs_hl[len(highs_hl) - 1]}")

    # 根据数据绘制图形
    plt.figure(figsize=(11, 4), dpi=600)
    # 生成网格

    plt.grid(axis="y")
    # 折线图
    plt.plot(wights, highs_float, "c-", linewidth=1, label=package_name[0])

    plt.xlabel('time(H:Min:S)', fontsize=16)
    plt.ylabel("cpu_realtime(%)", fontsize=16)
    plt.title("cpu real time line chart", fontsize=24)
    plt.legend()

    # 横坐标显示间隔
    if len(wights) <= 15:
        pass
    else:
        t = int(len(wights) / 15)
        plt.xticks(range(0, len(wights), t))
    # 旋转日期
    plt.gcf().autofmt_xdate()
    plt.savefig("log_su/report_cpu.png")


# 绘制内存折线图
def mapping_mem():
    filename = 'log_su/meminfo.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        highs = []
        for row in reader:
            high = row[2]
            highs.append(high)

    wights = time_list_mem
    highs_float = list(map(float, highs))

    print(f"内存值：{highs_float}")

    # 输出平均值
    total = 0
    for value in highs_float:
        total += value
    if len(highs_float) == 0:
        print("未获取到内存信息")
        return
    average = round(total / len(highs_float), 2)
    print(f"内存平均值：{average}")

    # 输出最低值和最高值
    highs_hl = sorted(highs_float)
    print(f"内存最低值：{highs_hl[0]}")
    print(f"内存最高值：{highs_hl[len(highs_hl) - 1]}")

    # 根据数据绘制图形
    plt.figure(figsize=(11, 4), dpi=600)
    # 生成网格
    # plt.grid()
    plt.grid(axis="y")
    plt.plot(wights, highs_float, "c-", linewidth=1, label=package_name[0])
    plt.xlabel('time(H:Min:S)', fontsize=16)
    plt.ylabel("Number (Mb)", fontsize=16)
    plt.title("meminfo", fontsize=24)
    plt.legend()

    # 横坐标显示间隔
    if len(wights) <= 15:
        pass
    else:
        t = int(len(wights) / 15)
        plt.xticks(range(0, len(wights), t))
    # 旋转日期
    plt.gcf().autofmt_xdate()
    plt.savefig("log_su/report_memory.png")


def get_app_status():
    get_applist()
    write_head()
    while True:
        time.sleep(1)
        # 每间隔3秒检查一次运行状态
        # command = "adb shell dumpsys window | findstr mCurrentFocus"
        command = "adb shell pidof com.tenorshare.recovery"
        result = os.popen(command).read()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        get_cpu()
        get_mem()
        if run_time == times:
            write_report_cpu()
            mapping_cpu()
            mapping_mem()
            print(f"{current_time}主线程已结束，监控线程结束")
            break
        else:
            if result:

                print(f"{current_time}正常运行")
            else:
                print(f"{current_time}崩溃")
                write_report_cpu()
                mapping_cpu()
                mapping_mem()
                break


if __name__ == '__main__':
    # 开启图片扫描恢复线程
    task1 = threading.Thread(target=test_ultdata)
    # 开启监控app运行状态进程
    task2 = threading.Thread(target=get_app_status)
    task1.start()
    task2.start()
    task1.join()
    task2.join()
