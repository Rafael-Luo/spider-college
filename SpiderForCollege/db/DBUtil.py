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
        self.db = "college"

    def connect(self,data):
        try:

            self.connect = pymysql.connect(host=self.host,
                                           port=self.port,
                                           user=self.user,
                                           passwd=self.password,
                                           db=self.db,
                                           charset='utf8')
            logging.info('成功连接！！！')
            self.cursor = self.connect.cursor()
            try:

                sql = """INSERT INTO college(name, icon,
                         city, department, type,levels, charact, url)
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""

                # 执行 sql 语句
                self.cursor.executemany(sql, data)
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





