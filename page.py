import requests
from bs4 import BeautifulSoup
hotp_result = requests.get(
    "http://www.menupan.com/restaurant/search/search_main.asp")

hotp_soup = BeautifulSoup(hotp_result.text, "html.parser")

paging = hotp_soup.find("div", class_="paging")
pages = paging.find_all('a')
pages = pages[1:-2]
print(pages)