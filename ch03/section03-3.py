# section03-3
# 기본 스크래핑
# 다음 주식정보

import json
import urllib.request as req
from fake_useragent import UserAgent

# Fake Useragent 사용
ua = UserAgent()
print("ua.ie : {}".format(ua.ie))
print("ua.msie : {}".format(ua.msie))
print("ua.chrome : {}".format(ua.chrome))
print("ua.safari : {}".format(ua.safari))
print("ua.random : {}".format(ua.random))

# 헤더 정보
headers = {
    'User-agent': ua.ie,
    'referer': 'https://finance.daum.net/'
}

# 저장할 파일명
FILE_NAME = 'd:/study_test/finance.txt'

# 다음 주식 요청 URL
URL = "https://finance.daum.net/api/search/ranks?limit=10"

# 요청
response = req.urlopen(req.Request(URL, headers=headers)).read().decode('UTF-8')

# 응답 데이터 확인(Json Data)
print("response : {}".format(response))

# 응답 데이터 str -> json 변환 및 data 값 출력
rank_json = json.loads(response)['data']
print("rank_json : {}".format(rank_json))

with open(FILE_NAME, "a") as c:

    c.write("#### 상위 10위 주식정보 ####\n\n")

    for elm in rank_json:
        print(type(elm))
        print(elm)
        print(elm['rank'])
        print(elm['name'])
        print("순위 : {}, 금액 : {}, 회사명 : {}".format(elm['rank'], elm['tradePrice'], elm['name']) )
        print("순위 : {}, 금액 : {}, 회사명 : {}".format(elm.get('rank'), elm.get('tradePrice'), elm.get('name')) )
        c.write("순위 : {}, 금액 : {}, 회사명 : {} \n".format(elm['rank'], elm['tradePrice'], elm['name']))


