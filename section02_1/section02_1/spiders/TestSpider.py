import scrapy


class TestSpider(scrapy.Spider):
    name = 'test2'
    # allowed_domains = ['blog.scrapinghub.com']
    # start_urls = ['https://blog.scrapinghub.com/']
    allowed_domains = ['www.zyte.com/blog']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        """
        :param => response
        :return => Title Text
        """

        # 2가지 (CSS Selector, XPath)
        # get() <-> getAll(), extract_first() <-> extract()

        # 예제1 (CSS selector)
        # css
        # a::text => scrapy에서 지원. a태그의 text만 가져옴
        # for text in response.css('div.post-header h2 a::text').getall():
        # 출력 옵션
        # -o 파일명.확장자, -t 파일 타입(json, jsonlines, jl, csv, xml, marshal, pickle)
        for text in response.css('div.oxy-post div.oxy-post-wrap a.oxy-post-title::text').getall():
        #     # return type : Request, BaseItem, Dictionary, None
        #     print("text: {}".format(text))
        #
             yield {'text': text}

        # 예제2(xpath)
        # for i, text in enumerate(response.xpath(
        #         '//div[@class="oxy-post"]/div[@class="oxy-post-wrap"]/div/a/text()').getall()):
        #     print("i: {}".format(i))
        #     print("text: {}".format(text))
        #
        #     yield {
        #         'number': i,
        #         'text': text
        #     }
