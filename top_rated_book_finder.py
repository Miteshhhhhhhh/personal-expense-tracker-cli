import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
titles = []
prices = []
ratings = []

for page in range(1,6):
    url = f"https://books.toscrape.com/catalogue/page-{page}.html"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    books = soup.find_all("h3")
    prices_raw = soup.find_all("p", class_="price_color")
    ratings_raw = soup.find_all("p", class_="star-rating")
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

for book, price, rating in zip(books, prices_raw, ratings_raw):
    price_clean = re.sub(r'[^\d.]', '', price.text)
    price_value = float(price_clean)
    rating_num = rating_map[rating["class"][1]]
    titles.append(book.text)
    prices.append(price_value)
    ratings.append(rating_num)
df = pd.DataFrame({
    "TITLE" : titles,
    "PRICE" : prices,
    "RATING" : ratings
})
df_filtered = df[(df["RATING"]>4) & (df["PRICE"]<=50)]
df_sorted = df_filtered.sort_values("PRICE")
df_sorted.to_excel("top_rated.xlsx", index=False)

import os
os.startfile("top_rated.xlsx")

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(df_sorted["TITLE"], df_sorted["PRICE"], color="green")
plt.title("Top Rated Books by Price")
plt.xlabel("Book Title")
plt.ylabel("Price (£)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("top_rated_chart.png")
plt.show()