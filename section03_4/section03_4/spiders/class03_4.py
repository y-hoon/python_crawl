import scrapy
from ..items import ItArticle

class TestSpider(scrapy.Spider):
    name = 'test6'
    allowed_domains = ['www.computerworld.com']
    start_urls = ['https://www.computerworld.com/news/']

    def parse(self, response):
        """
        :param : response
        :return : request
        """

        for url in response.css('div.main-col div.post-cont > h3 > a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        """
        :param : response
        :return : Items
        """

        item = ItArticle()
        item['title'] = response.xpath('//h1[@itemprop="headline"]/text()').get()
        item['img_url'] = response.xpath('//img[@itemprop="contentUrl"]/@data-original').get()
        item['contents'] = ''.join(response.xpath('//div[@itemprop="articleBody"]/p/text()').getall())

        print(dict(item))
        print(dir(dict(item)))

        yield item

# dictionary 그대로 출력
# scrapy crawl test6 -o test6.jl

# 데이터를 json format으로 출력
# scrapy crawl test6 -o test6.json -t json