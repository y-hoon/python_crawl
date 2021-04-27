# Section03-1
# rss feed
# Get 방식 데이터 통신 (2)

import urllib.request
import urllib.parse

# 행정 안전부 : https://www.mois.go.kr/
# 행정 안전부 RSS API URL
API = "https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"

params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# params 확인
# print(params)

# 연속해서 4회 요청
for c in params:
    # 파라미터 출력
    # print(c)
    # URL 인코딩
    param = urllib.parse.urlencode(c)

    # URL 완성
    url = API + "?" + param
    # URL 출력
    print("url : ", url)
    # print("url : {}".format(url))

    # 요청
    res_data = urllib.request.urlopen(url).read()
    #디코딩후 출력
    decode_data = res_data.decode('utf-8')
    print("#" * 100)
    print("decdoe_data : {}".format(decode_data))
