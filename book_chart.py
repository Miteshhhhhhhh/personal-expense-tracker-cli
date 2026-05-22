import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_excel(r"C:\Users\Owner\AppData\Roaming\JetBrains\PyCharmCE2025.1\scratches\sorted_books.xlsx")


cheap = len(df[df["CATEGORY"]== "cheap"] )
medium = len(df[df["CATEGORY"]== "medium"])
high = len(df[df["CATEGORY"]== "high"] )

categories = ["Cheap", "Medium", "High"]
counts = [3, 7, 10]

plt.bar(categories, counts, color=["green", "orange", "red"])
plt.title("Books by Price Category")
plt.xlabel("Category")
plt.ylabel("Number of Books")

plt.savefig("book_chart.png")
plt.show()