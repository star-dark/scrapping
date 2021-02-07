import requests
from bs4 import BeautifulSoup
LIMIT = 1
ranking = "rt" 
URL = f"https://www.menupan.com/restaurant/bestrest/bestrest.asp"


def extract_hotplace():
    hotp_result = requests.get(URL)
    hotp_soup = BeautifulSoup(hotp_result.text, "html.parser")

    paging = hotp_soup.find("div", class_="paging")
    first = paging.find("span", class_="pgClick").get_text()
    pagination = [first]
    pagination = []
    pages = paging.find_all("a")
    pages = pages[2:-2]
    for page in pages:
        pagination.append(page.string)
    max_page = pagination[-1]
    return max_page


def extract_hotp_lope(last_page):
    restaurant = []
    for page in range(last_page):
        call = requests.get(f"{URL}?page={LIMIT*page}&trec=9774&pt={ranking}")
        soup = BeautifulSoup(call.text, "html.parser")
        results = soup.find_all("li")
        for result in results:
            title = result.find("p", class_="listName").find(
                "span", class_="restName").find("a")
            food_type = result.find("p", class_="listType")
            area = result.find("p", class_="listArea")
            restaurant.append(title, food_type, area)
    return restaurant
