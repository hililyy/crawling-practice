import requests
from bs4 import BeautifulSoup

response = requests.get("https://m.search.naver.com/search.naver?where=m_news&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90&sm=tab_tmr&nso=so:r,p:all,a:all&sort=0")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") # 결과는 리스트로

for link in links:
    title = link.text # 태그 안에 텍스트요소를 가져옴
    url = link.attrs['href'] # href의 속성값을 가져옴
    print(title, url)