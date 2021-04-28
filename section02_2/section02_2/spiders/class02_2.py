import scrapy


class Class022Spider(scrapy.Spider):
    name = 'test3'
    allowed_domains = ['www.zyte.com/blog']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        """
        :param => response
        :return => request
        """
        for url in response.css('div.oxy-post > div.oxy-post-wrap > div > a.oxy-post-title::attr("href")').getall():
            # print()
            # print("url : {}".format(url))

            # url 바로 사용보다 urljoin 사용함 (상대경로이면 도메인을 자동으로 붙여주고 절대경로이면 그대로 리턴함)
            # Filtered offsite request to 에 대한 해결 : dont_filter=True
            # print("urljoin : {}".format(response.urljoin(url)))
            yield scrapy.Request(response.urljoin(url), self.parse_title, dont_filter=True)

    def parse_title(self, response):
        """
        상세 페이지 -> 타이틀 추출
        :param => response
        :return text
        """
        # print()
        # print(response)

        # p태그 열개만 가져옴
        contents = response.css('div#blog-body > span > p::text').extract()[:10]
        # print()
        # print()
        # print(contents)

        # list의 text로 변형 => ''.join(contents)
        yield {'contents': ''.join(contents)}
