import scrapy


class NewsSpider(scrapy.Spider):
    name = 'test11'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    def parse(self, response):
        print(response)

