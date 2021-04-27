# section04-2
# Requests
# Requests 사용 스크래핑 - JSON

import json
import requests

s = requests.Session()

# 100개 JSON 데이터 요청
r = s.get('https://httpbin.org/stream/100', stream=True)

# 수신 확인
print(r.text)

# Encoding 확인
print("Encoding: {}".format(r.encoding))

# Encoding 지정
if r.encoding is None:
    r.encoding = 'UTF-8'

# Encoding 재확인
print("After Encoding: {}".format(r.encoding))

for line in r.iter_lines(decode_unicode=True):
    # 라인 출력 후 타입 확인
    # print(line)
    # print(type(line))

    # JSON(Dict) 변환 후 타입 확인
    b = json.loads(line)    # str -> dict 로 변환
    # print(b)
    # print(type(b))

    for k, v in b.items():
        print("Key : {}, Value : {}".format(k, v))

    print()
    print()

s.close()

r = s.get('https://jsonplaceholder.typicode.com/todos/1')

# Header 정보
print(r.headers)

# 본문 정보
print(r.text)

# json 변환
b = json.loads(r.text)
print(b)
print(type(b))

for k, v in b.items():
    print("Key : {}, Value : {}".format(k, v))

# json 변환, 단일일때
c = r.json()
print("=====")
print("=====")
print(c)
print(type(c))

# key 반환
print(r.json().keys())

# value 반환
print(r.json().values())

# 인코딩 반환
print(r.encoding)

# 바이너리 정보
print(r.content)

s.close()

