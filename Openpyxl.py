from openpyxl import Workbook , load_workbook

wb = Workbook()
ws = wb.active
ws.title = "grades"

ws.append(["name", "marks", "grades"])
ws.append(["mitesh", 90, "A"])
ws.append(["jhony", 70 , "B"])

wb.save("NewGrades.xlsx")

import os
os.startfile("NewGrades.xlsx")