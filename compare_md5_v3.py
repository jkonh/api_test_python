# -*- encoding: utf8 -*-
import glob
import hashlib
import os

import ftplib
import shutil
import string

md5_list = []
txt_content = []
filename_md5 = {}


# md5_list存储计算出的exe或者dmg安装包的MD5值，txt_content存储读取到的MD5.txt文档中的md5数据，filename_md5存储安装包和MD5对应的关系


class FTPSync(object):
    def __init__(self):
        self.handle_path = self.create_download_path()
        self.conn = ftplib.FTP('192.168.1.4', 'fileshare', 'tenorshare@123')
        # path = input('请输入.4服务器上路径：')
        # # 截掉输入的路径前面的//192.168.1.4/字符串
        # remotepath = path[14:].replace('\\', '/')
        while True:
            path = input(r'请输入.4服务器上带版本号的路径：(例如：\\192.168.1.4\产品库\6.发布版本_new\2023\数据线Other\Computer Management\1.0.7):')
            remotepath = path[14:].replace('\\', '/')
            if remotepath.count('/') != 0:
                try:
                    # if remotepath.count('.') == 3:
                    self.conn.cwd(remotepath)
                    break
                # print('成功获取到路径')
                # else:
                #     print('路径错误,请重新输入路径')

                except Exception as e:
                    print(e)
                    print('路径错误,请重新输入路径')
            else:
                try:
                    self.conn.cwd(remotepath)
                except Exception as e:
                    print(e)
                    print('路径错误,请重新输入路径')
        # self.conn.cwd(remotepath)
        # 取出产品名称
        # a = remotepath.rsplit('/', 3)
        product_name = remotepath.split('/', 3)

        # 将.4服务器的文件或者文件夹保存到最大盘的download\Tenorshare目录下
        self.localpath = self.handle_path + '\\Tenorshare\\' + product_name[3]
        self.localpath = self.localpath.replace("/", '\\')

        print('保存的本地路径{}'.format(self.localpath))

        if os.path.exists(self.localpath):
            try:
                shutil.rmtree(self.localpath)

            except PermissionError:
                print(f"检测到路径被占用，请关闭{self.localpath}")

            os.makedirs(self.localpath)  # 新建本地目录
            os.chdir(self.localpath)  # 切换到本地下载目录
            os.startfile(self.localpath)

        else:
            os.makedirs(self.localpath)
            os.chdir(self.localpath)
            os.startfile(self.localpath)

    def get_exe_dmg_file_md5(self, file):
        # 计算exe、dmg、zip文件的MD5值
        myHash = hashlib.md5()
        if file.endswith(".exe") or file.endswith(".dmg") or file.endswith(".zip")or file.endswith(".iso"):
            print(f"正在计算{file}文件MD5值")
            with open(file, 'rb') as f:
                while True:
                    b = f.read(4096)
                    if not b:
                        break
                    myHash.update(b)
                # print("------")
                # print(f"{file}文件MD5为{myHash.hexdigest()}")
                # print("------")
                md5_list.append(myHash.hexdigest())
                filename_md5[file] = myHash.hexdigest()
        else:
            print(f"{file}不是exe/dmg/zip/iso文件，不需计算MD5值")
        return md5_list

    def get_file_md5(self):
        # 获取文件MD5

        path1 = self.localpath + '\\*'

        print('正在计算MD5值，请稍后...')
        for file in glob.glob(path1):
            # 判断文件夹里面的内容如果是文件，则调用计算MD5的方法
            if os.path.isfile(file):
                self.get_exe_dmg_file_md5(file)

            else:
                # 如果不是文件,则进入下一层
                file = file + '\\*'

                for f1 in glob.glob(file):
                    if os.path.isfile(f1):
                        self.get_exe_dmg_file_md5(f1)

        print(f"MD5计算完毕，总MD5值如列表{md5_list}")
        return md5_list

    def traverse1(self, f):
        """
        作用：列出文件夹下的所有子文件目录，寻找想要的txt文件
        """
        # md5_file_content = []
        # path = r"E:\download\Tenorshare\4uKey for iOS\win\3.2.0"
        listFiles = os.listdir(f)
        print(listFiles)
        for file in listFiles:
            # 判断MD5.txt文件是否存在,存在则读取里面的数据
            # 用正则表达式匹配MD5.txt文件是否存在
            print(file)
            md5_txt = f + "\\" + file + '\\' + "MD5.txt"
            print(md5_txt)
            md5_value1 = []
            with open(md5_txt, 'r') as f:
                md5_value = f.read()
                md5_value = md5_value.replace('\n', '').replace(' ', '')  # 去掉md5.txt中的换行符和空格
                md5_value1.append(md5_value.split(','))
                for value in md5_value1:
                    txt_content.append(value)

        return txt_content

    def traverse(self, f):
        fs = os.listdir(f)
        # print(f"fs is {fs}")

        for f1 in fs:
            # files = []
            tmp_path = os.path.join(f, f1)

            if not os.path.isdir(tmp_path):
                if tmp_path[-14:] == '\md5_total.txt' or tmp_path[-8:] == '\md5.txt' or tmp_path[-8:] == '\MD5.txt':
                    # print(f'记录总MD5文件路径为{file}')
                    temp_md5 = []
                    with open(tmp_path, 'r') as f:
                        md5_value = f.read()
                        md5_value = md5_value.replace('\n', '').replace(' ', '')
                        temp_md5.append(md5_value.split(','))
                        # print(f'txt记录的MD5数据为{txt_content[0]}')
                        for md5 in temp_md5[0]:
                            txt_content.append(md5)
                        # print(txt_content)
                        return txt_content
                # print("file: %s" % tmp_path)
                # files.append(tmp_path)
            elif os.path.isdir(tmp_path):
                self.traverse(tmp_path)
            else:
                # self.traverse(tmp_path)
                if tmp_path[-14:] == '\md5_total.txt' or tmp_path[-8:] == '\md5.txt' or tmp_path[-8:] == '\MD5.txt':
                    # print(f'记录总MD5文件路径为{file}')
                    temp_md5 = []
                    with open(tmp_path, 'r') as f:
                        md5_value = f.read()
                        md5_value = md5_value.replace('\n', '').replace(' ', '')
                        temp_md5.append(md5_value.split(','))
                        for md5 in temp_md5[0]:
                            txt_content.append(md5)
                        return txt_content
        else:
            return False

    def compare_md5(self):
        try:
            for md5 in md5_list:

                if md5 not in txt_content:
                    file_name = list(filename_md5.keys())[list(filename_md5.values()).index(md5)]
                    print(f'******校验结果******\n'
                          f'{file_name}校验失败，请在.4服务器上重新上传对应站点的安装包并检查MD5.txt中是否存在该包的md5值')
                else:
                    print(f'******校验结果******\n'
                          f'{list(filename_md5.keys())[list(filename_md5.values()).index(md5)]}校验md5通过'
                          )
        except IndexError:

            print('记录总MD5的md5.txt文件不存在，无法校验')

    def create_download_path(self):
        self.disklist = {}
        for C in string.ascii_uppercase:
            """从ascii编码的大写字母中匹配读取到的磁盘名称，并加上冒号"""
            self.disk = C + ':'
            self.gb = 1024 ** 3
            if os.path.isdir(self.disk):
                total_d, used_d, free_d = shutil.disk_usage(self.disk)
                free_space = free_d / self.gb
                self.disklist[self.disk] = free_space

        self.max_dickSpace = max(self.disklist.values())
        """使用max函数找出最大剩余空间"""
        for i, j in enumerate(self.disklist.items()):
            """找出字典disklist对应的磁盘名称和大小，并将最大剩余空间的磁盘名称找出来"""
            # print(i, j)
            """查看i和j的数据类型，发现j是列表类型，通过遍历j，查找最大盘名称，找到后返回最大盘名称"""

            if self.max_dickSpace in list(j):
                self.max_diskname = list(j)[0]
                print(f"最大盘为{self.max_diskname},将在该盘下保存下载的文件")
                break
        """
        在最大盘下创建下载目录，存在该目录，则提示存在，不存在则创建
        """
        try:
            if os.path.exists("{}\download".format(self.max_diskname)):
                """
                判断路径是否存在os.path.exists()
                """
                print(f"{self.max_diskname}\download 路径已存在,即将下载文件")
                # os.startfile("{}\download".format(self.max_diskname))


            else:
                os.mkdir("{}\download".format(self.max_diskname))
                print(f"{self.max_diskname}\download 路径不存在，新建成功")
                # os.startfile("{}\download".format(self.max_diskname))

            self.save_path = "{}\download".format(self.max_diskname)
            # print(f"保存到本地的路径为{self.save_path}")
            # os.startfile("{}\Download".format(self.max_diskname))
            """在文件资源管理器中打开对应的路径"""

        except Exception as e:
            print(e)
        return self.save_path

    def get_dirs_files(self):
        ''' 得到当前目录和文件, 放入dir_res列表 '''
        dir_res = []
        files = []
        # self.conn = ftplib.FTP('192.168.1.4', 'fileshare', 'tenorshare@123')
        self.conn.dir('.', dir_res.append)
        for f in dir_res:
            if f.endswith('.exe') or f.endswith('.dmg') or f.endswith('.txt') or f.endswith(".zip")or f.endswith(".iso"):
                file = f.split(None, 8)[-1]
                files.append(file)

        # files = [f.split(None, 8)[-1] for f in dir_res if f.endswith('-')]

        dirs = [f.split(None, 8)[-1] for f in dir_res if f.startswith('d')]
        return (files, dirs)

    def walk(self, next_dir):
        # print('Walking to', next_dir)
        self.conn.cwd(next_dir)
        try:
            os.mkdir(next_dir)
        except OSError:
            pass
        os.chdir(next_dir)
        ftp_curr_dir = self.conn.pwd()
        local_curr_dir = os.getcwd()
        files, dirs = self.get_dirs_files()
        # print("FILES: ", files)
        # print("DIRS: ", dirs)
        for f in files:
            print("正在下载", ':', f)
            outf = open(f, 'wb')
            try:
                self.conn.retrbinary('RETR %s' % f, outf.write)
            except Exception as e:
                print(f"下载失败，错误码为{e}")
            finally:
                outf.close()
        for d in dirs:
            os.chdir(local_curr_dir)
            self.conn.cwd(ftp_curr_dir)
            self.walk(d)

    def run(self):
        self.walk('.')


def main():
    f = FTPSync()
    f.run()
    f.get_file_md5()
    f.traverse(f.localpath)
    print(f"MD5文档记录的数据为{txt_content}")
    f.compare_md5()


# \\192.168.1.4\产品库\6.发布版本_new\2023\Ultdata\ultdata for android\win\6.8.2 部分通过，部分失败
# \\192.168.1.4\产品库\6.发布版本_new\2023\Ultdata\test\4uKey for Android\2.6.6.9 校验通过
# \\192.168.1.4\产品库\6.发布版本_new\2023\4uKey for iOS\mac\3.1.0 校验通过
# \\192.168.1.4\产品库\6.发布版本_new\2023\4uKey for iOS\win\3.1.1无MD5.txt文件，无法校验
# \\192.168.1.4\产品库\6.发布版本_new\2023\4uKey for iOS\win\3.2.0 存在两个文件夹，每个文件夹下各存在一个MD5.txt
# \\192.168.1.4\产品库\6.发布版本_new\2023\Ultdata\ultdata for android\win\test

# 以下两个存在问题
# \\192.168.1.4\产品库\6.发布版本_new\2023\4uKey iTunes Backup\mac\2.1.16
# \\192.168.1.4\产品库\6.发布版本_new\2023\iCareFone\iCareFone for LINE\Win\3.1.0

if __name__ == '__main__':
    print('******正在进行MD5校验******')
    main()
    input('请按enter键退出·····')
