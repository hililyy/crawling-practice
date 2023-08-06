import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com/")

# naver 에서 html을 줌
html = response.text

# html 번역선생님으로 수프 만듦
soup = BeautifulSoup(html, 'html.parser')

# id 값이 NM_set_home_btn인 것 찾아냄
word = soup.select_one('#NM_set_home_btn')

# 텍스트 요소만 출력
print(word.text)