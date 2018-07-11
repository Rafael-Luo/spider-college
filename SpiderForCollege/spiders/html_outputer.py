import MySQLdb

from SpiderForCollege.db.DBUtil import DBUtil


class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_mysql(self):
        db = DBUtil()
        db.connect(self.datas)

