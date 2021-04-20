# section04-1
# Requests
# 모듈 사용법 (1) - Session

import requests

# 세션 활성화
s = requests.Session()
r = s.get('https://www.naver.com')

# 수신 데이터
# print(r.text)

# 수신 상태 코드
print('Status Code : {}'.format(r.status_code))
print('Ok? " {}'.format(r.ok))  # 조건문에서 사용하기 위한 기능 - True, False


# 세션 비활성화
s.close()



# ### 쿠키 Return 예제 ###

s = requests.Session()

# 쿠키 Return
r1 = s.get('https://httpbin.org/cookies', cookies={'name': 'y-hoon'})
print(r1.text)

# 쿠키 Set
r2 = s.get('https://httpbin.org/cookies/set', cookies={'name': 'y-hoon2'})
print(r2.text)

# User-Agent
url = 'https://httpbin.org'
headers = {'user-agent': 'chrome geko'}

# Header 정보 전송
r3 = s.get(url, headers=headers)
print(r3.text)

# 세션 비활성화
s.close()

# With문 사용(권장) -> 파일, DB, HTTP
with requests.Session() as s:
    r = s.get('https://daum.net')
    print(r.text)
    print(r.ok)
