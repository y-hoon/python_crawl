# Section05-1
# BeautifulSoup 사용 스크래핑
# 기본 사용법

from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <h1>this is h1 area</h1>
        <h2>this is h1 area</h2>
        <p class="title"><b>The Dormouse's story</b></p>
        <p class="story">Onceupon a time there were three little sisters.
            <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
            <a href="http://example.com/lacie" class="sister" id="link2">lacie</a>
            <a data-io="link3" href="http://example.com/little" class="brother" id="link3">Title</a>
        </p>
        <p class="story">
            story....
        </p>
    </body>
</html>
"""

# 예제1 (BeautifulSoup 기초) #

# bs4 초기화
soup = BeautifulSoup(html, 'html.parser')

# 타입 확인
print('soup : ', type(soup))
print('### prettify ###\n', soup.prettify())

# h1 태그 접근
h1 = soup.html.body.h1
print('h1 : {}'.format(h1))

# p 태그 접근, 태그가 여러개일때는 최초로 나오는 태그를 리턴함
p1 = soup.html.body.p
print('p1 : ', p1)

# 두번째 p 태그
p2 = p1.next_sibling.next_sibling
print('p2 : ', p2)

# 텍스트 출력1
print('h1 >> ', h1.string)

# 텍스트 출력2
print('p1 >> ', p1.string)

# 함수(사용가능) 확인
print(dir(p2))

# 다음 엘리먼트 확인
# print(list(p2.next_element))

# 반복 출력 확인
for v in p2.next_element:
    pass
    # print(v)

# 예제2(Find, Find_all)

# bs4 초기화
soup2 = BeautifulSoup(html, 'html.parser')

# a 태그 모두 선택
link1 = soup2.find_all('a')
print('links: ', link1)

# a태그 모두 선택해서 순서대로 2개만 가져옴(limit=2)
link1 = soup2.find_all('a', limit=2)

# 타입 확인
# print(type(link1))  # <class 'bs4.element.ResultSet'>

# 리스트 요소 확인
print('links: ', link1)

link2 = soup.find_all("a", class_='sister') # id="link2", string="title", string=["Elsie", "title"]
print("link2 : ", link2)

for t in link2:
    print(t)

link2_1 = soup.find_all("a", {'class': 'brother'})
print("link2_1 : ", link2_1)

# 처음 발견한 a 태그 선택
link3 = soup.find("a")
print()
print("first a tag : {}".format(link3))
print(link3.string)
print(link3.text)

# 다중 조건
link4 = soup.find("a", {"class": "brother", "data-io": "link3"})
print("link4 : {}".format(link4))
print(link4.string)
print(link4.text)

# css 선택자 : select, select_one 사용
# 태그로 접근 : find, find_all 사용
# 예제3 (select, select_one)
# 태그 + 클래스 + 자식선택자

# p 태그의 클래스 이름이 타이틀인 것의 하위에 b 태그를 가져온다.
link5 = soup.select_one('p.title > b')
print()
print("link5 : {}".format(link5))
print(link5.string)
print(link5.text)

# a태그에서 ID값이 Link1인 것
link6 = soup.select_one("a#link1")
print()
print("link6 : {}".format(link6))
print(link6.string)
print(link6.text)

# class나 id가 아닌 속성의 경우 대괄호 ( [ ] )로 처리함
# a 태그 안에 data-io라는 속성이 link3 인 것
link7 = soup.select_one("a[data-io='link3']")
print()
print("link7 : {}".format(link7))
print(link7.string)
print(link7.text)

# 선택자에 맞는 전체 선택
link8 = soup.select("p.story > a")
print()
print("link8 : {}".format(link8))

# p태그에서 class가 story인 것의 하위에 a 태그에서 2번째 것
link9 = soup.select('p.story > a:nth-of-type(2)')
print()
print("link9 : {}".format(link9))

# p 태그중에 class가 story인 것 전체
link10 = soup.select('p.story')
print()
print("link10 : {}".format(link10))

for t in link10:
    temp = t.find_all('a')
    print()
    print("link10 > a : {}".format(temp))

    if temp:    # list의 size가 1 이상일 때 true
        for v in temp:
            print('>>>>>', v)
            print('>>>>>', v.string)
    else:
        print('-----', t)
        print('-----', t.string)





