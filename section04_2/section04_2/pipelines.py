# pipeline 실습
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, 메일 전송
from scrapy.exceptions import DropItem


class TestSpiderPipeline:

    # 최초 1회 호출됨
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started.')

    # prcess_item에 item이 건별로 입력됨
    def process_item(self, item, spider):
        # 여기서 데이터 처리 - 제거등
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            return item
        else:
            raise DropItem(f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막에서 1회 호출됨
    def close_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Closed.')
