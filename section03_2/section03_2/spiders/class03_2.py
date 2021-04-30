import scrapy
#scrapy 내부 logger가 아닌 logger 사용
import logging

logger = logging.getLogger('pythonLogger')


# 스파이더 종류 : CrawlSpider, XMLFeedSpider, CSVFeedSpider, SitemapSpider
class TestSpider(scrapy.Spider):
    name = 'test4'
    allowed_domains = ['www.zyte.com/blog', 'naver.com', 'daum.net']

    # 실행 방법 1
    # 멀티 도메인 크롤링
    start_urls = ['https://www.zyte.com/blog/', 'https://www.naver.com', 'https://www.daum.net']

    # 사용자 시스템 설정
    # settings.py의 설정을 변경. 변수명은 custom_settings여야 함
    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'COOKIES_ENABLED': True
    }

    def parse(self, response):
        # 위에서 import한 logger
        logger.info('Response URL : %s' % response.url)
        logger.info('Response Status : %s' % response.status)
        # scrapy 기본 logger
        self.logger.info('Response URL : %s' % response.url)
        self.logger.info('Response Status : %s' % response.status)

        if response.url.find('www.zyte.com'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        elif response.url.find('naver'):
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }
        else:
            yield {
                'sitemap': response.url,
                'contents': response.text[:100]
            }

    # 실행 방법 2
    # 멀티 도메인 크롤링 (이미 선언되어 있는 start_requests 함수를 재정의하여 사용함
    # Request 각각 지정
    # 장점 : 도메인별로 처리 함수를 지정할 수 있다.
    # def start_requests(self):
    #     yield scrapy.Request('https://www.zyte.com/blog/', self.parse1)
    #     yield scrapy.Request('https://naver.com', self.parse2)
    #     yield scrapy.Request('https://daum.net', self.parse3)
    #
    # def parse1(self, response):
    #     pass
    #
    # def parse2(self, response):
    #     pass
    #
    # def parse3(self, response):
    #     pass

