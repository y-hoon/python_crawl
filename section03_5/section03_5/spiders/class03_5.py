import scrapy
from ..items import ItArticle

# scrapy Feed Export 실습
# 출력 형식

# JSON, JSON Lines
# CSV
# XML, Pickle, Marshal

# 저장 위치
# Local File System - My Pc
# FTP - (Server)
# S3 - (AWS) Amazon
# 기본 콘솔

# 방법 2가지
# 1.커맨드 이용
# (--output, -o) , (--output-format, -t)
# 옵션 설정 예) --set=FEED_EXPORT_INDENT = 2

# 2. Setttings.py 이용
# 자동으로 저장(파일명, 형식, 위치)

class TestSpider(scrapy.Spider):
    name = 'test7'
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