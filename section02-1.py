# Section02-1
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMTlfMjcz%2FMDAxNjEzNzMzODk4MTY2.ztqmHdAttpmObO-I7nyNU_7Za9mmO2WdePNkJVp6Cosg.iPljrLtASE_DggL86_2SviBLYS_Cab02giZYzO16_4cg.JPEG.hidawelgold5%2FKakaoTalk_20210219_200450710_02.jpg&type=a340'
html_url = 'https://www.google.co.kr/'

# 다운받을 경로 지정
save_img_path = 'd:/study_test/test1.jpg'
save_file_path = 'd:/study_test/index.html'

# 예외 처리
try:
    file1, header1 = req.urlretrieve(img_url, save_img_path)
    file2, header2 = req.urlretrieve(html_url, save_file_path)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Header 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    # 성공
    print('Download Succeed')

