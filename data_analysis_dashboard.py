import pandas as pd
import re
df = pd.read_excel(r"C:\Users\Owner\AppData\Roaming\JetBrains\PyCharmCE2025.1\scratches\sorted_books.xlsx")

df["PRICE_NUM"] = df["PRICE"].apply(lambda x:float(re.sub(r'[^\d.]', "", str(x))))

print("Total books:", len(df))
print("Avg price:", round(df["PRICE_NUM"].mean(),2))
print("Most expensive:", df["PRICE_NUM"].max())
print("Cheapest:", df["PRICE_NUM"].min())
print("Cheap count:", len(df[df["CATEGORY"]== "cheap"]))
print("Medium count:", len(df[df["CATEGORY"]== "medium"]))
print("High count:", len(df[df["CATEGORY"]== "high"]))

summary = {
    "Metric": ["Total books", "Avg price", "Most expensive", "Cheapest", "Cheap count", "Medium count", "High count"],
    "Value": [len(df), round(df["PRICE_NUM"].mean(), 2), df["PRICE_NUM"].max(), df["PRICE_NUM"].min(),
              len(df[df["CATEGORY"]=="cheap"]), len(df[df["CATEGORY"]=="medium"]), len(df[df["CATEGORY"]=="high"])]
}

summary_df = pd.DataFrame(summary)
summary_df.to_excel("dashboard.xlsx", index=False)

import os
os.startfile("dashboard.xlsx")

