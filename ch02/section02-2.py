# Section02-2
# urlopen

import urllib.request as req
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명

path_list = ['d:/study_test/test1.jpg', 'd:/study_test/index.html']

# 다운로드 리소스 url
target_url = ['https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMTFfMzkg%2FMDAxNjEzMDE5MDc5NzQz.WypYPviQcPl1_OnAd3NIYH0Jxauj3fygvU3bL2jsMTEg.k0D4iuOrQ1onYZsd8DJDiVsKkYt6AsfvBIPrCf9q3iog.JPEG.nn830%2FIMG_8266.jpg&type=a340', 'http://google.co.kr']

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("=============")

        # 상태 정보 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))

        print("=============")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as  e:
        print("Download failed.")
        print("HTTPError Code: ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URL Error Reason : ", e.reason)
    # 성공
    else:
        print()
        print("Download SUcceed.")