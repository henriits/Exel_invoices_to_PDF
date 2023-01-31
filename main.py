import pandas as pd
import glob
# openepyxl package required


filepaths = glob.glob("invoices/*xlsx")
# print(filepaths)

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    print(df)
