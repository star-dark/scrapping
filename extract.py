import requests, re
from bs4 import BeautifulSoup
LIMIT = 1
ranking = "rt" 
URL = f"https://www.menupan.com/restaurant/bestrest/bestrest.asp"


def extract_page():
    menupan_result = requests.get(URL)
    menupan_soup = BeautifulSoup(menupan_result.text, "html.parser")
    paging = menupan_soup.find("div", class_="paging")
    first = paging.find("span", class_="pgClick").get_text()
    pagination = [first]
    pagination = []
    pages = paging.find_all("a")
    pages = pages[2:-2]
    for page in pages:
        pagination.append(page.string)
    max_page = pagination[-1]
    return max_page
def extract_rest(html):
  rest_list = html.find_all("li")
  for i in rest_list:
    if "cid_tab_list_li" in i:
      title = html.find("span", class_= "restName").text
      food_type = html.find("p", class_="listType").text
      area = html.find("p", class_="listArea").text
      return {'title' : title, 'type' : food_type, 'area' : area}
    else : continue 
def extract_hotp_lope(last_page):
    restaurant = []
    for page in range(last_page):
        call = requests.get(f"{URL}?page={LIMIT*page}&trec=9774&pt={ranking}")
        soup = BeautifulSoup(call.text, "html.parser")
        results = soup.find_all("li")
        print(results)
        for result in results:
          rest = extract_rest(result)
          restaurant.append(rest)
    return restaurant
