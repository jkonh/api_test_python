# _*_ coding:utf-8 _*_
"""
@Software  ：api_learning
@FileName  ：handle_logging.py
@Date      ：2023/11/23 18:02
@Author    ：ChenGH
"""
import logging
import os
import time

from common.handle_config import conf
from common.handle_path import LOG_DIR, CONF_FILE
from logging.handlers import TimedRotatingFileHandler


class HandleLogger(object):
    def __init__(self):
        filename = time.strftime('%Y-%m-%d.log')
        self.log_path = os.path.join(LOG_DIR, filename)

    def log(self):
        logger = logging.getLogger('mylogger')
        logger.setLevel(conf['log']['level'])
        if not logger.handlers:
            formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-%(message)s')
            file_handle = TimedRotatingFileHandler(filename=self.log_path, when='D', interval=1, backupCount=3)
            file_handle.setFormatter(formatter)
            logger.addHandler(file_handle)
            # 设置控制台输出
            sh_handle = logging.StreamHandler()
            sh_handle.setFormatter(formatter)
            logger.addHandler(sh_handle)
        return logger

    def debug(self, msg):
        self.log().debug(msg)

    def info(self, msg):
        self.log().info(msg)

    def warning(self, msg):
        self.log().warning(msg)

    def error(self, msg):
        self.log().error(msg)

    def critical(self, msg):
        self.log().critical(msg)


log = HandleLogger()
if __name__ == '__main__':
    log = HandleLogger()
    log.info("this is info log....")
    log.warning("this is warning log....")
    log.error("this is error log....")
    log.critical("this is critical log....")
