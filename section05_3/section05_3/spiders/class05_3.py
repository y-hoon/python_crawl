import scrapy
# 페이지를 이동하면서 크롤링을 실행(Link)
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItems


# LinkExtractor 를 사용하려면 crawlSpider를 사용해야 함
# class NewsSpider(scrapy.Spider):
# class NewsSpider(CrawlSpider):
# 미들웨어 설치 : pip install scrapy_fake_useragent
class NewsSpider(CrawlSpider):
    name = 'test13'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규표현식 사용추천)
    # '/breakingnews/digital\?page=\d$' => 숫자 1자리
    # '/breakingnews/digital\?page=\d+' => 숫자 여러자리, follow=True로 줘야 함 (마지막 페이지까지 확인함)
    # Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d+'), callback='parse_headline', follow=True),
    rules = [
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'), callback='parse_parent'),
    ]

    def parse_parent(self, response):
        # 부모 URL 로깅
        self.logger.info('Parent Respnose URL : %s' % response.url)

        for url in response.css('ul.list_news2.list_allnews > li > div'):
            # URL 신문 기사 URL
            article_url = url.css('strong > a::attr(href)').extract_first().strip()
            self.logger.info('article_url : %s' % article_url)
            # 요청, 중복요청의 경우 함수호출이 안되면 dont_filter=True 가 필요함
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url}, dont_filter=True)

    def parse_child(self, response):

        # 부모, 자식 수신 정보 로깅
        self.logger.info('====================================')
        self.logger.info('Response From Parent URL : %s' % response.meta['parent_url'])
        self.logger.info('Child Response URL : %s' % response.url)
        self.logger.info('Child Response Status : %s' % response.status)
        self.logger.info('====================================')

        # 헤드라인
        headline = response.css('h3.tit_view::text').extract_first().strip()

        # 본문
        c_list = response.css('div.article_view p::text').extract()
        contents = ''.join(c_list).strip()

        yield ArticleItems(headline=headline, contents=contents, parent_link=response.meta['parent_url'],
                           article_link=response.url)
