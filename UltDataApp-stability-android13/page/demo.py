# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-stability-android13
@FileName  ：demo.py
@Date      ：2023/9/28 16:12
@Author    ：ChenGH
"""
import shutil
import time
import requests
import os

headers = {}
test_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
headers['user-agent'] = test_agent
urls = ["https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1094.exe",
        "https://download.ultfone.com/go/any-data-recovery_1097.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1289.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1290.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1291.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1292.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1293.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1294.exe",
        "https://download.tenorshare.com/go/tenorshare-4ddig-for-windows_1296.exe",
        "https://download.tenorshare.tw/go/tenorshare-4ddig-for-windows_1684.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_1686.exe",
        "https://download.tenorshare.com/go/tenorshare-4ddig-for-windows_2190.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_2355.exe",
        "https://download.tenorshare.net/go/tenorshare-4ddig-for-windows_2386.exe",
        "https://download.tenorshare.cn/go/tenorshare-4ddig-for-windows_2449.exe",
        "https://download.tenorshare.com/go/reiboot_1051.exe",
        "https://download.tenorshare.net/go/reiboot_1081.exe",
        "https://download.tenorshare.net/go/reiboot-bing_1342.exe",
        "https://download.tenorshare.net/go/reiboot_1304.exe",
        "https://download.tenorshare.net/go/reiboot_1302.exe",
        "https://download.tenorshare.com/go/4ddig-file-repair_5505.exe",
        "https://download.tenorshare.net/go/4ddig-file-repair_5511.exe",
        "https://download.tenorshare.net/go/4ukeyforandroid_1106.exe",
        "https://download.tenorshare.net/go/4ukeyforandroid-bing_1769.exe",
        "https://download.tenorshare.com/go/4ukey-for-android_1103.exe",
        "https://download.passfab.com/go/android-unlock_1941.exe",
        "https://download.passfab.net/go/android-unlock_2096.exe",
        "https://download.tenorshare.net/go/4ukeyforandroid_1517.exe",
        "https://download.tenorshare.net/go/4ukeyforandroid_1518.exe",
        "https://download.tenorshare.fr/go/4ukey-for-android_1442.exe",
        "https://download.tenorshare.de/go/4ukey-for-android_1629.exe",
        "https://download.tenorshare.kr/go/4ukey-for-android_2631.exe",
        "https://download.passfab.com/go/android-unlock_1943.exe",
        "https://download.passfab.com/go/android-unlock_2213.exe",
        "https://download.tenorshare.cn/go/4ukey-for-android_2409.exe",
        'https://download.tenorshare.net/go/4ukey_1016.exe',
        "https://download.tenorshare.net/go/4ukey-bing_1368.exe",
        "https://download.tenorshare.com/go/4ukey_1002.exe",
        "https://download.passfab.com/go/iphone-unlock_1752.exe",
        "https://download.passfab.net/go/iphone-unlock_2090.exe",
        "https://download.tenorshare.net/go/4ukey_1018.exe",
        'https://download.tenorshare.net/go/4ukey_1020.exe',
        "https://download.tenorshare.net/go/4ukey_1022.exe",
        "https://download.tenorshare.net/go/4ukey_1026.exe",
        "https://download.tenorshare.net/go/4ukey-bing_1373.exe",
        "https://download.tenorshare.jp/go/4ukey_1003.exe",
        "https://download.tenorshare.es/go/4ukey_1005.exe",
        "https://download.tenorshare.fr/go/4ukey_1006.exe",
        "https://download.passfab.com/go/iphone-unlock_1977.exe",
        "https://download.tenorshare.cn/go/4ukey_2405.exe",
        "https://download.tenorshare.com/go/icarefone_1101.exe",
        "https://download.tenorshare.net/go/icarefone_1104.exe",
        "https://download.tenorshare.net/go/icarefone_2929.exe",
        "https://download.tenorshare.com/go/whatsapp-transfer_2231.exe",
        "https://download.tenorshare.net/go/whatsapp-transfer_2232.exe",
        "https://download.tenorshare.com/go/ianygo_2573.exe",
        "https://download.tenorshare.net/go/ianygo_2576.exe",
        "https://download.tenorshare.net/go/ianygo_2576.exe",
        "https://download.tenorshare.net/go/ianygo_2576.exe",
        "https://download.tenorshare.net/go/ianygo_2576.exe",
        "https://download.ultfone.net/go/ultfone-toolkit_6073.exe",
        "https://download.ultfone.com/go/ios-location-changer_2733.exe",
        "https://download.ianygo.com/go/ianygo_6645.exe",
        "https://download.ultfone.com/go/ultfone-toolkit_6067.exe",
        "https://download.ultfone.net/go/ultfone-toolkit_6073.exe",
        "https://download.tenorshare.jp/go/ianygo_2551.exe",
        "https://download.tenorshare.tw/go/ianygo_2698.exe",
        "https://download.tenorshare.net/go/ianygo_2577.exe",
        "https://download.tenorshare.net/go/ianygo_2923.exe",
        "https://download.tenorshare.com/go/4ddig-partition-manager_5555.exe",
        "https://download.tenorshare.net/go/4ddig-partition-manager_5882.exe",
        "https://download.passfab.com/go/partition-manager_5560.exe",
        "https://download.passfab.net/go/partition-manager_5894.exe"
        ]

for url in urls:
    time.sleep(5)
    response = requests.get(url)
    # # 使用chardet自动检测编码方式
    # encoding = chardet.detect(response.content)['encoding']
    # # 设置响应对象的编码方式
    # response.encoding = encoding
    # 输出获取到的内容
    try:
        shutil.rmtree(f"{os.path.dirname(__file__)}//download_exe")
        print("删除成功")
        os.mkdir(f"{os.path.dirname(__file__)}//download_exe")
        print("新建成功")
    except:
        os.mkdir(f"{os.path.dirname(__file__)}//download_exe")
        print("新建成功")
        pass
    download_path = os.path.join(os.path.dirname(__file__), "download_exe")
    exe_name = os.path.split(url)[-1]
    file_name = os.path.join(download_path, exe_name)
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(f"{url}下载完成")
