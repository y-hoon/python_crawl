# section04-3
# Requests 스크래핑
# Rest API

import requests

# 세션 활성화
s = requests.Session()

# 예제1
r = s.get('https://api.github.com/events')

# 수신상태 체크
r.raise_for_status()

# 출력
print(r.text)

# 예제2
# 쿠키설정
jar = requests.cookies.RequestsCookieJar()
jar.set('name', 'y-hoon', domain="httpbin.org", path="/cookies")

# 요청
r = s.get('http://httpbin.org/cookies', cookies=jar)

# 출력
print(r.text)

# 예제3
r = s.get('https://github.com', timeout=5)

# 출력
print(r.text)

# 예제4
r = s.post('https://httpbin.org/post', data={'id':'y-hoon', 'pw':'1234'}, cookies=jar)

# 출력
print(r.text)
print(r.headers)

# 예제5
payload1 = {'id':'y-hoon', 'pw':'1234'}
payload2 = (('id', 'y-hoon1'), ('pw', '12341'))

r = s.post('http://httpbin.org/post', data=payload1)

# 출력
print(r.text)

# 예제6(PUT)

r = s.put('http://httpbin.org/put', data=payload2)
print(r.text)

# 예제7(DELETE)

r = s.delete('http://httpbin.org/delete', data={'id': 1})
print(r.text)

r = s.delete('http://jsonplaceholder.typicode.com/posts/1')
print(r.ok)
print(r.text)
print(r.headers)

s.close()
