import gzip
import urllib.request

import requests


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
            'Connection': 'keep - alive'
        }
        web_data = requests.get(url, headers=header)
        result = web_data.content
        # response = urllib.request.urlopen(url)
        #
        #
        # if response.getcode() != 200:
        #     return None
        # else:
        #
        #     result = response.read()

            #print(result)
            # # 内容有压缩过，直接decode不行，需要用gzip来解压。然后再decode。
            # html = gzip.decompress(result)
            # html = html.decode('gbk')
        return result
