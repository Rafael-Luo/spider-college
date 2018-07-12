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
        self.db = "faker"


    def insert(self, sql, data):
        try:

            self.connect = pymysql.connect(host=self.host,
                                           port=self.port,
                                           user=self.user,
                                           passwd=self.password,
                                           db=self.db,
                                           charset='utf8')
            #logging.info('成功连接！！！')
            self.cursor = self.connect.cursor()
            try:



                # 执行 sql 语句
                self.cursor.execute(sql, data)
                # 提交到数据库执行
                self.cursor.close()
                self.connect.commit()
                print('提交完毕')
            except:
                # 如果发生错误则进行回滚
                self.connect.rollback()
                print('\n Some Error happend ! \n')
            # 关闭数据库连接
            self.connect.close()

        except:
            logging.error('连接失败！！！')
    def select(self,name):
        try:

            self.connect = pymysql.connect(host=self.host,
                                           port=self.port,
                                           user=self.user,
                                           passwd=self.password,
                                           db=self.db,
                                           charset='utf8')
            #logging.info('成功连接！！！')
            self.cursor = self.connect.cursor()
            try:


                # 执行 sql 语句
                collegeId =self.cursor.execute('SELECT * FROM college WHERE name ="'+name+'"')
                # 提交到数据库执行
                self.cursor.close()
                self.connect.commit()
                return collegeId
            except:
                # 如果发生错误则进行回滚
                self.connect.rollback()
                print('\n Some Error happend ! \n')
            # 关闭数据库连接
            self.connect.close()

        except:
            logging.error('连接失败！！！')


if __name__ == '__main__':
    db = DBUtil()
    if db.select('111')>0:
        print('存在相同的值')
    else:
        print('不存在')


