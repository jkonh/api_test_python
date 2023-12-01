# _*_ coding:utf-8 _*_
"""
@Software  ：UltDataApp-2
@FileName  ：logger.py
@Date      ：2023/7/21 11:49
@Author    ：ChenGH
"""
import datetime
import logging
import os.path
from logging.handlers import TimedRotatingFileHandler

from common.handle_path import LOG_PATH


class get_log(object):
    def __init__(self):
        # 设置日志文件名格式
        self.filename = datetime.datetime.now().strftime('%Y-%m-%d.log')
        # 设置日志文件保存位置
        self.log_file = os.path.join(LOG_PATH, self.filename)
        self.logger = logging.getLogger(self.log_file)
        # 设置日志收集级别
        self.logger.setLevel(logging.INFO)
        # 设置日志收集的格式
        formatter = logging.Formatter("%(asctime)s - [%(filename)s -line:%(lineno)d]- %(levelname)s -%(message)s")
        # 设置日志按天轮转
        file_handle = TimedRotatingFileHandler(filename=self.log_file, when='D', interval=1, backupCount=0)
        # 设置轮转的格式
        file_handle.setFormatter(formatter)
        # 添加日志handle
        self.logger.addHandler(file_handle)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == "__main__":
    log = get_log()
    log.debug('--debug---')
    log.info('---info--')
    log.warning('---warning---')
    log.error('--error--')
    log.critical('--critical--')
