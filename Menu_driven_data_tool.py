import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

base_url = "https://books.toscrape.com/"

names = []
prices = []
ratings = []

def scrape_books():  # this was get_data()
    global names, prices, ratings
    names, prices, ratings = [], [], []  # reset

    result = requests.get(base_url)
    soup = BeautifulSoup(result.text, "html.parser")
    book = soup.find_all("h3")
    price = soup.find_all("p", class_="price_color")
    rating = soup.find_all("p", class_="star-rating")

    for b, p, r in zip(book, price, rating):
        names.append(b.a["title"])
        prices.append(float(re.sub(r'[^\d.]', "", p.text)))
        ratings.append(r["class"][1])
    print(f"Scraped {len(names)} books")

    df = pd.DataFrame({"NAME": names, "PRICE": prices, "RATING": ratings})
    df.to_excel("all_books.xlsx", index=False)
    print(f"Scraped {len(names)} books")
    print("Raw data saved to all_books.xlsx")
    import os
    os.startfile("all_books.xlsx")

def analyze_books():  # this was clean_data()
    if not names:
        print("No data. Run option 1 first")
        return
    import pandas as pd
    df = pd.DataFrame({"NAME": names, "PRICE": prices, "RATING": ratings})
    minimum_price = float(input("Enter minimum price: "))
    df_filtered = df[df["PRICE"] >= minimum_price]
    print(df_filtered.sort_values("PRICE"))


def top_rated():
    if not names:
        print("No data. Run option 1 first")
        return
    import pandas as pd
    df = pd.DataFrame({"NAME": names, "PRICE": prices, "RATING": ratings})
    five_star = (df[df["RATING"] == "Five"])  # just 5-star books
    print(five_star)
    five_star.to_excel("top_rated_books.xlsx", index=False)
    import os
    os.startfile("top_rated_books.xlsx")
    print("Top rated books exported to excel")


def export_summary():
    if not names :
        print("No data. Run 'Scrape Books' first")
        return
    df = pd.DataFrame({
        "NAME" : names,
        "PRICE" : prices,
        "RATING" : ratings
    })

    total_books = len(df)
    avg_price = round(df["PRICE"].mean(), 2)
    min_price = df["PRICE"].min()
    max_price = df["PRICE"].max()

    summary_df = pd.DataFrame({
        'Metric': ["Total Books", "Avg Price", "Min Price", "Max Price"],
        'Value': [total_books, avg_price, min_price, max_price]
    })
    summary_df.to_excel("book_summary.xlsx", index=False)
    import os
    os.startfile("book_summary.xlsx")
    print("Summary exported and opened: book_summary.xlsx")

# Menu - same as guide
while True:
    print("\n1. Scrape Books")
    print("2. Analyze Books")
    print("3. Top Rated Books")
    print("4. Export Summary")
    print("5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        scrape_books()
    elif choice == '2':
        analyze_books()
    elif choice == '3':
        top_rated()
    elif choice == '4':
        export_summary()
    elif choice == '5':
        break