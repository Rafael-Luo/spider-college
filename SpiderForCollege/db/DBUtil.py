# mysql驱动连接
import logging

import pymysql

from SpiderForCollege.logs.Logging import load_my_logging_cfg


class DBUtil(object):
    load_my_logging_cfg()
    def __init__(self):

        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.password = '123456'
        self.db = "learner"

    def connect(self):
        try:
            self.connect = pymysql.connect(host=self.host,
                                           port=self.port,
                                           user=self.user,
                                           passwd=self.password,
                                           db=self.db,
                                           charset='utf8')


            logging.info('成功连接！！！')
            logging.error('测试error')
            # self.cursor = self.connect.cursor()  # 获取游标
        except:
            print('error in connect to mysql')


if __name__ == '__main__':
    dbUtil = DBUtil()
    dbUtil.connect()
