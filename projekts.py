                                                                        
# 241RDB167 Nils Elans Logins 
# 241RDB148 Ilvars Arājs

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://www.ss.lv/lv/transport/cars/"

response = requests.get(BASE_URL)
response.raise_for_status()

main_soup = BeautifulSoup(response.text, "html.parser")
category_tags = main_soup.find_all(class_="a_category")
category_hrefs = [tag["href"] for tag in category_tags if tag.get("href")]

for href in category_hrefs[:42]:
    full_url = urljoin(BASE_URL, href)
    page = requests.get(full_url)
    page.raise_for_status()
    soup = BeautifulSoup(page.text, "html.parser")
    listings = soup.find_all(class_="msg2")

    
    results = {}

    for listing in listings:
        link = listing.find("a", href=True)
        if not link:
            continue

        detail_url = urljoin(BASE_URL, link["href"])
        detail_resp = requests.get(detail_url)
        if detail_resp.status_code != 200:
            continue
        detail_soup = BeautifulSoup(detail_resp.text, "html.parser")

        price_tag = detail_soup.find(class_="ads_price")
        date_tag  = detail_soup.find(id="tdo_18")
        if not price_tag or not date_tag:
            continue

    
        price_digits = re.sub(r"\D", "", price_tag.get_text(strip=True))
        date_digits  = re.sub(r"\D", "", date_tag.get_text(strip=True))
        try:
            price = int(price_digits)
            year  = int(date_digits)
        except ValueError:
            continue

        score = year / price

       
        results[detail_url] = {
            "price": price,
            "year":  year,
            "score": score
        }

    top5 = sorted(
        results.items(),
        key=lambda item: item[1]["score"],
        reverse=True
    )[:5]

    print(f"\n=== Category: {href} (top 5 by year/price) ===")
    for rank, (url, info) in enumerate(top5, start=1):
        print(f"{rank}. {url}")
        print(f"     Year: {info['year']}, Price: €{info['price']}, Score: {info['score']:.5f}")
