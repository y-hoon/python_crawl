# Section02 -3
# lxml
# pip install lxml, requests, cssselect

import requests
import lxml.html

file_path = 'd:/study_test/news.txt'


def main():
    """
    네이버 메인 뉴스 스탠드 스크래핑 메인함수
    """

    # 스크래핑 대상 URL
    response = requests.get("https://www.naver.com")

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)

    # 결과 출력
    for url in urls:
        print(url)

    #    with open(file_path, 'w') as c:
    #        c.write(url)


def scrape_news_list_page(response):
    # URL 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    # print(response.content)
    root = lxml.html.fromstring(response.content)
    # print('#########################')
    # print(root)

    for a in root.cssselect('.api_list .api_item a.api_link'):
        # 링크
        url = a.get('href')
        urls.append(url)

        return urls


# 스크랩핑 시작
if __name__ == "__main__":
    main()
