# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：Synergy.py
@Date      ：2023/11/27 9:26
@Author    ：ChenGH
"""
import time


def task_1():
    while True:
        print("---1----")
        time.sleep(0.1)
        yield
        print('3')



def task_2():
    while True:
        print("---2----")
        time.sleep(0.1)
        yield
        print('4')
        break



def main():
    t1 = task_1()
    t2 = task_2()
    # 先让t1运行一会，当t1中遇到yield的时候，再返回到24行，然后
    # 执行t2，当它遇到yield的时候，再次切换到t1中
    # 这样t1/t2/t1/t2的交替运行，最终实现了多任务....协程
    while True:
        try:
            next(t1)
            next(t2)
        except StopIteration:
            break


if __name__ == "__main__":
    main()
