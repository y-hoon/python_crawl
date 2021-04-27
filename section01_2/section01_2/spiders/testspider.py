import scrapy


class TestSpider(scrapy.Spider):
    name = 'test1'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        print('[dir]\n', dir(response))

        print('[status]\n', response.status)

        print('[text]\n', response.body)
