# pipeline 실습
# 예) 잘못된 데이터 제거, DB 저장, SNS 전송, 메일 전송
from scrapy.exceptions import DropItem
import csv
import xlsxwriter

class TestSpiderPipeline:

    # 초기화
    def __init__(self):
        # 엑셀 처리 선언
        self.workbook = xlsxwriter.Workbook("D:/study_test/result_excel.xlsx")
        # csv 처리 선언 (a - 추가, w - 쓰기)
        self.file_opener = open("D:/study_test/result_csv.csv", "w")
        self.csv_writer = csv.DictWriter(self.file_opener, fieldnames=['rank_num', 'site_name', 'daily_time_site',
                                                                       'daily_page_view', 'is_pass'])
        
        # 삽입 수
        self.rowcount = 1
        
        # 워크시트
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.write('A%s' % self.rowcount, '랭킹')
        self.worksheet.write('B%s' % self.rowcount, '사이트이름')
        self.worksheet.write('C%s' % self.rowcount, '체류시간')
        self.worksheet.write('D%s' % self.rowcount, '방문수')
        self.worksheet.write('E%s' % self.rowcount, '수집대상')
        self.rowcount += 1
        

    # 최초 1회 호출됨
    def open_spider(self, spider):
        spider.logger.info('TestSpider Pipeline Started.')

    # prcess_item에 item이 건별로 입력됨
    def process_item(self, item, spider):
        # 여기서 데이터 처리 - 제거등
        if int(item.get('rank_num')) < 41:
            item['is_pass'] = True
            # 엑셀 저장
            # item['rank_num'] : 데이터가 없으면 에러 발생, item.get('rank_num'): 데이터가 없으면 None
            self.worksheet.write('A%s' % self.rowcount, item.get('rank_num'))
            self.worksheet.write('B%s' % self.rowcount, item.get('site_name'))
            self.worksheet.write('C%s' % self.rowcount, item.get('daily_time_site'))
            self.worksheet.write('D%s' % self.rowcount, item.get('daily_page_view'))
            self.worksheet.write('E%s' % self.rowcount, item.get('is_pass'))
            self.rowcount += 1

            # csv 저장
            self.csv_writer.writerow(item)


            return item
        else:
            raise DropItem(f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막에서 1회 호출됨
    def close_spider(self, spider):

        # 엑셀 파일 닫기
        self.workbook.close()
        # csv 파일 닫기
        self.file_opener.close()

        spider.logger.info('TestSpider Pipeline Closed.')
