import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # allowed_domains = ['www.xx.com']

    start_urls = ['https://www.baidu.com/', 'https://www.sogou.com/']

    def parse(self, response):
        print(response)
