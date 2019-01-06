import pandas as pd
import xlsxwriter
import glob
import os

writer = pd.ExcelWriter('multi_sheet.xlsx', engine='xlsxwriter')
folders = next(os.walk('.'))[1]

for host in folders:
    Path = os.path.join(os.getcwd(), host)
    for f in glob.glob(os.path.join(Path, "*.csv")):
        print(f)
        df = pd.read_csv(f)
        df.to_excel(writer, sheet_name=os.path.basename(f)[:31])
writer.save()
