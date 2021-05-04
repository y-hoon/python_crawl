import scrapy
# 페이지를 이동하면서 크롤링을 실행(Link)
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# LinkExtractor 를 사용하려면 crawlSpider를 사용해야 함
# class NewsSpider(scrapy.Spider):
# class NewsSpider(CrawlSpider):
class NewsSpider(CrawlSpider):
    name = 'test11'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용추천)
    # '/breakingnews/digital\?page=\d$' => 숫자 1자리
    # '/breakingnews/digital\?page=\d+' => 숫자 여러자리, follow=True로 줘야 함 (마지막 페이지까지 확인함)
    # Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d+'), callback='parse_headline', follow=True),
    rules = [
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_headline'),
    ]

    def parse_headline(self, response):
        # URL 로깅
        self.logger.info('Respnose URL : %s' % response.url)

        for m in response.css('ul.list_news2.list_allnews > li > div'):
            # 헤드라인
            headline = m.css('strong > a::text').extract_first().strip()
            # 본문 20글자
            contents = m.css('div > span::text').extract_first().strip()

            yield {'headline': headline, 'contents': contents}


