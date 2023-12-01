# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：handle_db.py
@Date      ：2023/11/23 15:01
@Author    ：ChenGH
"""
import pymysql

from common.handle_config import conf


class MySQLHandler(object):
    def __init__(self):
        self.con = pymysql.connect(host=conf.get("mysql", "host"),
                                   port=conf.getint("mysql", "port"),
                                   user=conf.get("mysql", "user"),
                                   password=conf.get("mysql", "password"),
                                   database=conf.get("mysql", "db"),
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
        # 创建一个游标对象
        self.cur = self.con.cursor()

    def find_one(self, sql):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def find_all(self, sql):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_count(self, sql):
        self.con.commit()
        res = self.cur.execute(sql)
        return res

    def update(self, sql):
        self.cur.execute(sql)
        self.con.commit()

    def close(self):
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    db = MySQLHandler()
    # sql = 'show tables'
    sql ='select * from member where mobile_phone=13374684413'
    # sql ='select member.leave_amount from member where id=168749'
    print(sql)
    res = db.find_all(sql)  # 看有几个phone的记录
    print(res)
    db.close()
