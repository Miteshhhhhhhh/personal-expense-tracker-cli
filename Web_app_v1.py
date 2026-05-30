from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "expenses.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, category TEXT, amount REAL)')
    conn.commit()
    conn.close()


init_db()


# PAGE 1: ADD EXPENSE
@app.route("/", methods=['GET', 'POST'])
def add_expense():
    if request.method == "POST":
        category = request.form.get('category')
        amount = float(request.form.get('amount'))

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (category, amount) VALUES(?,?)", (category, amount))
        conn.commit()
        conn.close()
        return 'Expense added! <a href="/">Add more</a> | <a href="/expenses">View All</a>'

    return '''
    <h2>Add Expense</h2>
    <form method="POST">
        Category: <input type="text" name="category" required><br><br>
        Amount: <input type="number" name="amount" required><br><br>
        <input type="submit" value="Add Expense">
    </form>
    <br>
    <a href="/expenses">View All Expenses</a>
    '''


# PAGE 2: VIEW EXPENSES
@app.route("/expenses")
def view_expenses():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT category, amount FROM expenses")
    all_expenses = cursor.fetchall()
    conn.close()

    # Plain text me dikha rahe - no table, no CSS
    output = "<h2>All Expenses</h2>"
    output += "<pre>"  # <pre> tag se plain text jaisa dikhega
    for category, amount in all_expenses:
        output += f"{category}    {amount}\n"
    output += "</pre>"
    output += '<br><a href="/">Add More</a>'

    return output


if __name__ == "__main__":
    app.run(debug=True, port=5001)