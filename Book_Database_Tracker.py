import os
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

DB_FILE = "books_database.xlsx"
BASE_URL = "https://books.toscrape.com/"


def add_new_books():
    print("Scraping books.toscrape.com...")
    result = requests.get(BASE_URL)
    soup = BeautifulSoup(result.text, "html.parser")

    book = soup.find_all("h3")
    price = soup.find_all("p", class_="price_color")
    rating = soup.find_all("p", class_="star-rating")

    names, prices, ratings = [], [], []

    for b, p, r in zip(book, price, rating):
        names.append(b.a["title"])
        prices.append(float(re.sub(r'[^\d.]', '', p.text)))
        ratings.append(r["class"][1])

    new_df = pd.DataFrame({"Name": names, "Price": prices, "Rating": ratings})

    if os.path.exists(DB_FILE):
        old_df = pd.read_excel(DB_FILE)
        combined_df = pd.concat([old_df, new_df], ignore_index=True)
        print(f"Added {len(new_df)} new books. Database now has {len(combined_df)} books.")
    else:
        combined_df = new_df
        print(f"First scrape! Added {len(new_df)} books to new database.")

    combined_df.to_excel(DB_FILE, index=False)


def view_all_books():
    if not os.path.exists(DB_FILE):
        print("No books saved yet. Run option 1 first.")
        return

    df = pd.read_excel(DB_FILE)
    print("\n--- ALL SAVED BOOKS ---")
    print(df)
    print(f"\nTotal books in database: {len(df)}")


def search_by_title():
    if not os.path.exists(DB_FILE):
        print("No books saved yet. Run option 1 first.")
        return

    search_term = input("Enter book title to search: ")
    df = pd.read_excel(DB_FILE)

    # case=False means "harry" matches "Harry"
    results = df[df['Name'].str.contains(search_term, case=False, na=False)]

    if results.empty:
        print(f"No books found with '{search_term}' in title.")
    else:
        print(f"\n--- SEARCH RESULTS FOR '{search_term}' ---")
        print(results)


def filter_by_rating():
    if not os.path.exists(DB_FILE):
        print("No books saved yet. Run option 1 first.")
        return

    rating = input("Enter rating to filter (One/Two/Three/Four/Five): ").capitalize()
    df = pd.read_excel(DB_FILE)

    results = df[df['Rating'] == rating]

    if results.empty:
        print(f"No books found with rating '{rating}'.")
    else:
        print(f"\n--- {rating.upper()} STAR BOOKS ---")
        print(results)


def show_cheapest():
    if not os.path.exists(DB_FILE):
        print("No books saved yet. Run option 1 first.")
        return

    df = pd.read_excel(DB_FILE)
    cheapest = df.loc[df['Price'].idxmin()]  # finds row with min price

    print("\n--- CHEAPEST BOOK IN DATABASE ---")
    print(f"Name: {cheapest['Name']}")
    print(f"Price: £{cheapest['Price']}")
    print(f"Rating: {cheapest['Rating']}")


# MENU LOOP - this runs the whole program
while True:
    print("\n" + "=" * 30)
    print("BOOK DATABASE TRACKER")
    print("=" * 30)
    print("1. Add new scraped books")
    print("2. View all saved books")
    print("3. Search books by title")
    print("4. Filter by rating")
    print("5. Show cheapest book")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == '1':
        add_new_books()
    elif choice == '2':
        view_all_books()
    elif choice == '3':
        search_by_title()
    elif choice == '4':
        filter_by_rating()
    elif choice == '5':
        show_cheapest()
    elif choice == '6':
        print("Exiting. Your data is saved in books_database.xlsx")
        break
    else:
        print("Invalid choice. Enter 1-6.")