
from bs4 import BeautifulSoup

from SpiderForCollege.bean.College import College
from SpiderForCollege.db.DBUtil import DBUtil
from SpiderForCollege.logs.Logging import load_my_logging_cfg


class HtmlParser(object):
    load_my_logging_cfg()
    def split(self, text):
        result = text.split('：')
        return result[1]

    def _get_new_urls(self, page_url):
        # http://college.gaokao.com/schlist/p1/
        url = page_url.split('/')
        num = url[4].split('p')
        newNum = int(num[1])+1
        if newNum > 107:
            return None
        else:
            new_urls = ' http://college.gaokao.com/schlist/p'+str(newNum)+'/'
            return new_urls
    def _get_new_data(self, soup):
        res_data = []
        college =College()
        # find_all 查到所有dl列表
        for dl in soup.find_all('dl', ):

            imglist = dl.find_all('img')
            try:
                college.name = imglist[0].attrs['alt']
                college.icon = imglist[0].attrs['src']
            except IndexError as e:
                pass

            li = dl.find_all('li')
            try:

                college.city = self.split(li[0].text.strip())
                college.charact = self.split(li[1].text.strip())
                college.type = self.split(li[2].text.strip())
                college.department = self.split(li[3].text.strip())
                college.levels = self.split(li[4].text.strip())
                college.url = self.split(li[5].text.strip())
                collegeOne = (college.name, college.icon, college.city, college.department, college.type, college.levels, college.charact, college.url)
                # print(collegeOne)
                # res_data.append(collegeOne)
                #print("学校名称:"+college.name+" 图标:"+college.icon+" 所在地:"+college.city+
                #      " 性质:"+college.levels+" 特色:"+college.character+" 类型:"+college.type+" 网址:"+college.url)
                sql = """INSERT INTO college(name, icon,
                                        city, department, type,levels, charact, url)
                                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
                db = DBUtil()
                db.insert(sql, collegeOne)
            except IndexError as e:
                pass

        return res_data

    def parse(self, page_url, html_result):
        if page_url is None or html_result is None:
            return
        soup = BeautifulSoup(html_result, 'html.parser')

        new_urls = self._get_new_urls(page_url)
        new_data = self._get_new_data(soup)
        return new_urls, new_data

