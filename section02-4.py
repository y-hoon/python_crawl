# Section02 -4
# lxml
# xpath 이용

import requests
from lxml.html import fromstring, tostring

def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 메인함수
    """

    # 세션사용
    session = requests.Session()

    # 스크래핑 대상 URL
    response = session.get("https://www.naver.com")

    # 신문사 링크 딕셔너리 획득
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)


    # 결과 출력
    for name, url in urls.items():
        # url 출력
        print(name)


def scrape_news_list_page(response):
    # URL 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    # print(response.content)
    root = fromstring(response.content)
    # print('#########################')
    # print(root)

    # xpath 사용법
    # // 전체문서
    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):

        # a 구조 확인
        # print(a)

        # a 문자열 출력
        # print(tostring(a, pretty_print=True))

        name, url = extract_contents(a)
        # 딕셔너리 삽입
        urls[name] = url

        return urls

def extract_contents(dom):
    # 링크 주소
    link = dom.get("href")

    # 신문사 명
    name = dom.xpath('./img')[0].get('alt')
    # print(name)

    return name, link



# 스크랩핑 시작
if __name__ == "__main__":
    main()
