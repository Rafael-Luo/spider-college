import logging

from SpiderForCollege.logs.Logging import load_my_logging_cfg
from SpiderForCollege.spiders \
    import url_manager, \
    html_downloader, \
    html_parser, html_outputer


class SpiderMain(object):
    load_my_logging_cfg()
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                logging.info('craw %d: %s' % (count, new_url))
                html_result = self.downloader.download(new_url)
                # print(html_result)
                new_urls, new_data = self.parser.parse(new_url, html_result)
                # print(new_urls)
                self.urls.add_new_url(new_urls)
                self.outputer.collect_data(new_data)

                if count == 1000:
                    break
                count = count + 1
            except:
                logging.error('craw failed')
        self.outputer.output_mysql()
if __name__ == "__main__":
    root_url = "http://college.gaokao.com/schlist/p1/"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
