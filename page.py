import requests
from bs4 import BeautifulSoup
indeed_result = requests.get("https://kr.indeed.com/jobs?q=%EC%99%B8%EA%B5%AD%EA%B3%84%EA%B8%B0%EC%97%85")

indeed_soup = BeautifulSoup(indeed_result.text,"html.parser")
pagination = indeed_soup.find("div",{"class":"pagination"})
pages = pagination.soup('a')
print(pages)