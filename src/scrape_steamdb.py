import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = "https://steamdb.info/sales/"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the sales table
table = soup.find("table", {"class": "table-sales"})

rows = []
for row in table.find_all("tr")[1:]:  # skip header
    cols = row.find_all("td")
    if len(cols) < 5:
        continue
    game = cols[0].text.strip()
    price = cols[3].text.strip()
    discount = cols[2].text.strip()
    rating = cols[5].text.strip() if len(cols) > 5 else ""
    rows.append({
        "game": game,
        "price": price,
        "discount": discount,
        "rating": rating,
        "scraped_at": pd.Timestamp.now()
    })
    time.sleep(0.1)  # be polite to SteamDB

df = pd.DataFrame(rows)
df.to_csv("data/live_steam_sales.csv", index=False)
print("Live scraped data saved.")
