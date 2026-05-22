import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

base_url = "https://webscraper.io/test-sites/e-commerce/static"

def get_data(url):
    import time
    time.sleep(2)
    names = []
    prices = []

    result = requests.get(url)
    result.encoding = "utf-8"
    soup = BeautifulSoup(result.text, "html.parser")

    name = soup.find_all("a", class_="title")
    price = soup.find_all("h4", class_="price")

    for n, p in zip(name, price):
        names.append(n.text.strip())
        price_clean = re.sub(r'[^\d.]', '', p.text)
        prices.append(float(price_clean))
    return names, prices

def clean_data(names, prices):
    import pandas as pd
    df = pd.DataFrame({"NAME": names, "PRICE": prices})
    minimum_price = float(input("Enter minimum price: "))
    df_filtered = df[df["PRICE"] >= minimum_price]
    df_sorted = df_filtered.sort_values("PRICE")
    return df_sorted

def save_excel(df):
    df.to_excel("dynamic_category.xlsx", index=False)
    import os
    os.startfile("dynamic_category.xlsx")

def create_chart(df):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.bar(df["NAME"], df["PRICE"], color="purple")
    plt.title("Products Above Minimum Price")
    plt.xlabel("Product Name")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("dynamic_category_chart.png")
    plt.show()

while True:
    print("1. Laptop")
    print("2. Tablets")
    print("3. Phones")
    print("4. Exit")

    choice = input("Enter choice:").strip()
    print(repr(choice))

    if choice == "1":
        url = base_url + "/computers/laptops"
    elif choice == "2":
        url = base_url + "/computers/tablets"
    elif choice == "3":
        url = base_url + "/phones"
    elif choice == "4":
        break
    else:
        print("Invalid choice")
        continue
    # Call all functions
    names, prices = get_data(url)
    cleaned = clean_data(names, prices)
    save_excel(cleaned)
    create_chart(cleaned)

