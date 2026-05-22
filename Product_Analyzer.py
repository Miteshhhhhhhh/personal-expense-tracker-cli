import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
import re

wb = Workbook()
ws = wb.active
ws.append(["TITLE", "PRICE", "RATING"])

url = "https://books.toscrape.com/"
result = requests.get(url)
result.encoding = "utf-8"
soup = BeautifulSoup(result.text, "html.parser")

books = soup.find_all("h3")
prices = soup.find_all("p", class_="price_color")
ratings = soup.find_all("p", class_="star-rating")
rating_map = {"One": 1, "Two":2, "Three":3,"Four":4,"Five":5}

minimum_rating = int(input("Enter minimum rating(1-5):"))
maximum_price = float(input("Enter maximum price:"))

for book,price,rating in zip(books, prices, ratings):
    price_clean = re.sub(r'[^\d.]', "", price.text)
    price_value = float(price_clean)
    rating_num = rating_map[rating["class"][1]]

    if rating_num >= minimum_rating and price_value <= maximum_price:
        ws.append([book.text, price.text, rating_num])

wb.save("Product_Analyzer.xlsx")
import os
os.startfile("Product_Analyzer.xlsx")


import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel("Product_Analyzer.xlsx")
df["PRICE_NUM"] = df["PRICE"].apply(lambda x:float(re.sub(r'[^\d.]', "", str(x))))

plt.figure(figsize=(10, 6))
plt.bar(df["TITLE"], df["PRICE_NUM"], color="blue")
plt.title("Filtered Books by Price")
plt.xlabel("Book Title")
plt.ylabel("Prices")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("Product_chart.png")
plt.show()



