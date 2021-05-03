import scrapy

# scrapy 환경설정
# 실행방법
# 1. 커맨드라인 실행 -> scrapy crawl 크롤러명 -s(--set) <NAME>=<VALUE>
# 2. Spider 실행시 직접 지정 -> custom_settings
# 3. Settings.py에 지정 -> 추천하는 방법
# 4. 서브 명령어 (사용하지 말 것)
# 5. 글로벌 설정 : scrapy.settings.default_settings
# 추천하는방법 : 커맨드라인 실행으로 테스트하면서 개발하고 개발완료되면 setting.py에 설정을 저장함

class TestSpider(scrapy.Spider):
    name = 'test8'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']

    def parse(self, response):
        # xpath + css 혼합
        for i, v in enumerate(response.xpath('//div[@class="post-summary-content"]').css('div.post-excerpt-container > h3 > a::text').extract(), 1):
            # 인덱스 번호, 헤드라인
            yield dict(num=i, headline=v)

