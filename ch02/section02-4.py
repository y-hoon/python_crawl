# Section02 -4
# lxml
# xpath 이용

import requests
from lxml.html import fromstring, tostring

file_path_name = 'd:/study_test/news.txt'

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

    # 파일에 쓰기
    with open(file_path_name, 'a') as c:
        for k in urls.keys():
            l = urls.get(k)
            news = k + " : " + l + "\n"
            c.write(news)



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
    # cont = root.xpath('//div[@id="NM_NEWSSTAND_VIEW_CONTAINER"]/div[@id="NM_NEWSSTAND_DEFAULT_THUMB"]/div[@class="_NM_UI_PAGE_CONTAINER"]')
    # cont = root.xpath('//div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]')
    # print("##########")
    # print(cont)
    # print("##########")
    # for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
    for a in root.xpath('//div[@class="thumb_box _NM_NEWSSTAND_THUMB _NM_NEWSSTAND_THUMB_press_valid"]'):
        # print(tostring(a, pretty_print=True))

        # a 구조 확인
        # print(a)

        # dom에서 뉴스매체 이름, url을 가져옴
        name, url = extract_contents(a)

        # 딕셔너리 삽입
        urls[name] = url

    return urls


def extract_contents(dom):
    name = dom.xpath('./a[@class="thumb"]/img')[0].get('alt')
    # a_link = a.xpath('./div[@class="popup_wrap"]/a[@class="btn_popup"]')  btn_popup이 3개임
    a_link = dom.xpath('./div[@class="popup_wrap"]/a[@data-clk="logo"]')[0]
    url = a_link.get("href")

    # for b in a_link:
    #     print(tostring(b, pretty_print=True))

    # print("##########")
    # print(a_link)
    # print(tostring(a_link, pretty_print=True))
    # print("##########")
    # print(url)
    # print("##########")
    # print(tostring(a_link, pretty_print=True))
    # url = a_link.get("href")

    # print(url)

    return name, url



# 스크랩핑 시작
if __name__ == "__main__":
    main()
