import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요 >>")

response = requests.get(f"https://m.search.naver.com/search.naver?where=m_news&query={keyword}")
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") # 결과는 리스트로

for link in links:
    title = link.text # 태그 안에 텍스트요소를 가져옴
    url = link.attrs['href'] # href의 속성값을 가져옴
    print(title, url)