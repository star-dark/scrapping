import requests
from bs4 import BeautifulSoup
LIMIT = 1
URL =   f"https://www.menupan.com/restaurant/bestrest/bestrest"
def extract_hotplace():
  hotp_result = requests.get(URL)
  hotp_soup = BeautifulSoup(hotp_result.text, "html.parser")

  paging = hotp_soup.find("div", class_="paging")
  first = paging.find("span",class_="pgClick").get_text()
  pagination = [first]
  pages = paging.find_all("a") 
  pages = pages[2:-2]
  for page in pages:
    pagination.append(page.string)
  max_page = pagination[-1]
  return max_page

def extract_hotp_lope(last_page):
  for page in range(last_page):
    result = requests.get(f"{URL}.asp?page={LIMIT*page}&trec=9817&pt=rt")
    print(result.status_code)