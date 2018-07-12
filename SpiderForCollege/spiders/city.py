# 获取省份及链接
import re
from multiprocessing.dummy import Pool

import requests
from bs4 import BeautifulSoup

from SpiderForCollege.db.DBUtil import DBUtil

pro_link = []
def get_provice(url):
    web_data = requests.get(url, headers=header)
    soup = BeautifulSoup(web_data.content, 'lxml')
    provice_link = soup.select('.area_box > a')
    for link in provice_link:
        href = link['href']
        provice = link.select('span')[0].text
        data = {
            'href': href,
            'provice': provice
        }
        #provice_href.insert_one(data)#存入数据库
        pro_link.append(href)
# 获取分数线
def get_score(url):

    web_data = requests.get(url, headers=header)
    soup = BeautifulSoup(web_data.content, 'lxml')
    # 获取省份信息
    provice = soup.select('.col-nav span')[0].text[0:-5]
    # 获取文理科
    categories = soup.select('h3.ft14')
    category_list = []
    for item in categories:
        category_list.append(item.text.strip().replace(' ', ''))#替换空格
    # 获取分数
    tables = soup.select('h3 ~ table')
    for index, table in enumerate(tables):
        tr = table.find_all('tr', attrs={'class': re.compile('^c_\S*')})#使用正则匹配
        for j in tr:
            td = j.select('td')
            score_list = []
            for k in td:
                # 获取每年的分数
                if 'class' not in k.attrs:
                    score = k.text.strip()
                    score_list.append(score)

                # 获取分数线类别
                elif 'class' in k.attrs:
                    score_line = k.text.strip()

                score_data = (
                     provice.strip(),#省份
                     category_list[index],#文理科分类
                     score_line,#分数线类别
                     str(score_list)#分数列表
                )
            sql = """INSERT INTO score(city, category,score_line, score_list)
                                                   VALUES (%s,%s,%s,%s)"""
            db = DBUtil()
            db.insert(sql, score_data)
            #score_detail.insert_one(score_data)#插入数据库
if __name__ == '__main__':

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
        'Connection': 'keep - alive'
        }
    url = 'http://www.gaokao.com/guangdong/fsx/'

    get_provice(url)
    pool = Pool()
    pool.map(get_score, [i for i in pro_link])  # 使用多线程