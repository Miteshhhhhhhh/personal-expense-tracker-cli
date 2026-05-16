import pandas as pd
import os

if os.path.exists("personal_expenses.xlsx"):
    df = pd.read_excel("personal_expenses.xlsx")
else:
    df = pd.DataFrame(columns=["Category", "Amount"])

def add_expense():
    category = input("Category:")
    amount = float(input("Amount: "))

    global df
    new_row = pd.DataFrame([{"Category": category, "Amount": amount}])
    df = pd.concat([df, new_row], ignore_index=True)
    print("Expense added")

def view_expenses():
    if df.empty:
        print("No expense yet")
    else:
        print(df)

def show_total():
    print("Total spent:", df["Amount"].sum())

def filter_by_category():
    cat = input("Enter category:")
    filtered = df[df["Category"].str.contains(cat, case=False, na=False)]
    print(filtered)

def export_t_excel():
    df.to_excel("personal_expenses.xlsx", index=False)
    os.startfile("personal_expenses.xlsx")
    print("Exported")

while True:
    print("\n1. Add expense\n2. View all\n3. Show total\n4. Filter by category\n5. Export\n6.Exit")
    choice = input("Choose:")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        filter_by_category()
    elif choice == "5":
        export_t_excel()
    elif choice == "6":
        break