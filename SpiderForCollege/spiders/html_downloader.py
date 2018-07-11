import gzip
import urllib.request


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        response = urllib.request.urlopen(url)


        if response.getcode() != 200:
            return None
        else:
            try:
                result = response.read()
            # print(result)
            # # 内容有压缩过，直接decode不行，需要用gzip来解压。然后再decode。
            # html = gzip.decompress(result)
            # html = html.decode('gbk')
                return result
            except Warning:
                html = gzip.decompress(result)
                html = html.decode('gbk')
                return html
