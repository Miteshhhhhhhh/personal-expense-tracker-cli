import sqlite3
import os
import pandas as pd
from datetime import datetime

conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

cursor.execute("""
      CREATE TABLE IF NOT EXISTS expenses (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       category TEXT,
       amount REAL,
       date TEXT
)
""")

conn.commit()

def add_expense():
    category = input("Category: ")
    amount = float(input("Amount: "))
    date = datetime.today().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO expenses (category,amount,date) VALUES(?,?,?)",
                   (category, amount, date))
    conn.commit()
    print("Expense added.")

def view_expenses():
   cursor.execute("SELECT * FROM expenses")
   rows = cursor.fetchall()
   if not rows :
       print("No expenses")
   else:
       print("expense found")
       for row in rows:
           print(f"ID:{row[0]}| Category: {row[1]}| Amount: {row[2]}| Date: {row[3]}")

def show_total():
    cursor.execute("SELECT SUM(amount) FROM expenses")
    row = cursor.fetchone()
    total = row[0] if row[0] else 0
    print(f"Total : {total}")

def search_category():
    search_term = input("Enter category: ")
    cursor.execute("SELECT * FROM expenses WHERE category = ?", (search_term,))
    rows = cursor.fetchall()
    if not rows:
        print("No expense found")
    else:
        print("Found expenses")
        for row in rows:
            print(f"ID:{row[0]}| Category: {row[1]}| Amount: {row[2]}| Date: {row[3]}")

def show_highest_expense():
    cursor.execute("SELECT * FROM expenses ORDER BY amount DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        print(f"HIGHEST EXPENSE -> ID: {row[0]}|{row[1]}|{row[2]}|{row[3]}")
    else:
        print("NO EXPENSES ADDED YET")

def delete_expense():
    view_expenses()
    expense_id = input("Delete which ID?")

    cursor.execute("DELETE FROM expenses WHERE id= ?", (expense_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("ID not Found.")
    else:
        print("Deleted.")

def update_expense():
    view_expenses()
    expense_id = input("Enter ID to update :")
    new_amount = input("Enter new amount: ")

    cursor.execute("UPDATE expenses SET amount = ? WHERE ID = ?", (new_amount, expense_id))
    conn.commit()
    if cursor.rowcount == 0:
        print("ID not found")
    else:
        print("Updated.")

def category_summary():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()

    if not rows:
        print("No expenses yet.")
    else:
        print("--- Category Summary ---")
        for category, total in rows:
            print(f"{category}: {total}")
        print("-------------------------")

def export_to_excel():
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    column_names = [description[0] for description in cursor.description]

    df = pd.DataFrame(rows, columns=column_names)
    file_name = "expenses.xlsx"
    df.to_excel(file_name, index=False)

    print(f"Exported! Opening{file_name}....")
    os.startfile(file_name)

while True:
    print("1. Add expense")
    print("2. View all expense")
    print("3. Show total")
    print("4. Search category")
    print("5. Show highest expenses")
    print("6. Delete expense")
    print("7. Update expense")
    print("8. Category summary")
    print("9. Export to excel")
    print("10. Exit")
    choice = input("Choice 1-10:")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        show_total()
    elif choice == "4":
        search_category()
    elif choice == "5":
        show_highest_expense()
    elif choice == "6":
        delete_expense()
    elif choice == "7":
        update_expense()
    elif choice == "8":
        category_summary()
    elif choice == "9":
        export_to_excel()
    elif choice == "10":
        break
    else:
        print("Invalid choice")

conn.close()
print("Bye! Database closed.")




