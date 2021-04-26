# Section06-3
# Selenium 자동으로 다음 페이지 데이터 수집

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정 (Chrome, Firefox 등) - headless 모드
browser = webdriver.Chrome('./../webdriver/chrome/chromedriver.exe', options=chrome_options)

# webdriver 설정 (Chrome, Firefox 등) - 일반 모드
# browser = webdriver.Chrome('./../webdriver/chrome/chromedriver.exe')

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)

# 브라우저 사이즈
browser.set_window_size(1920, 1280) # maximize_window(), minimize_window()

# 페이지 이동
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# 1차 페이지 내용
# print('Before Page Contents : {}'.format(browser.page_source))

# 제조사별 더 보기 클릭 1
# Explicitly wait
# 3초동안 기다리는데( WebDriverWait(browser, 3) ) XPATH로 표현된 모든 요소가 다 보여질때까지
# 3초안에 해당 요소(XPAH)가 보여지지 않으면 error를 내보내고 프로그램이 멈춤
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# 제조사별 더 보기 클릭 2
# Implicitly wait
# time.sleep(3)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# 원하는 모델 카테고리 클릭
WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[15]/label'))).click()

# 2차 페이지 내용
# print('After Page Contents : {}'.format(browser.page_source))

# 사람이 하는 것처럼 delay 처리
time.sleep(2)

# 현재 페이지
cur_page = 1

# 크롤링 페이지 수
target_crawl_num = 5

while cur_page <= target_crawl_num:



    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 소스코드 정리
    # print(soup.prettify())

    # 메인 상품 리스트 선택
    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li.prod_item.prod_layer')

    # 상품 리스트 확인
    # print(pro_list)

    # 페이지 번호 출력
    print('****** Current Page : {}'.format(cur_page), '*****')
    print()

    # 필요 정보 추출
    for v in pro_list:
        # 임시 출력
        # print("=================================")
        # print(v)
        if not v.find('div', class_="ad_header"):

        #상품명, 이미지, 가격
            try :
                print(v.select('p.prod_name > a[name="productName"]')[0].text.strip())
                print(v.select('a.thumb_link > img')[0]['data-original'])
                print(v.select('p.price_sect > a')[0].text.strip())

                # 이 부분에서 엑셀 저장(파일, DB등)

            except IndexError as e:
                print("=== error ")
                print(e)
                print("=== error ")
            except KeyError as ke:
                print("=== error ")
                print(ke)
                print("=== error ")

        print()
        print()
    print()

    # 페이지별 스크린 샷 저장
    browser.save_screenshot('D:/study_test/target_page{}.png'.format(cur_page))

    # 페이지 증가
    cur_page += 1

    if cur_page > target_crawl_num:
        print('Crawling Succeed.')
        break

    # 페이지 이동 클릭 element의 하위 :: nth-child
    WebDriverWait(browser, 3).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    # BeautifulSoup 인스턴스 삭제
    del soup

    # 3초간 대기
    time.sleep(3)




# 브라우저 종료
# browser.close()
browser.quit()