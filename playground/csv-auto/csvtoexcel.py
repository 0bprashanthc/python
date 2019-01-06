import openpyxl
import glob
import csv

files = glob.glob("*.csv")
wb = openpyxl.Workbook()
for each_file in files:
    print each_file.split('.')[0]
    ws = wb.create_sheet(index=0, title=each_file.split('.')[0])
    with open(each_file) as f:
        reader = csv.reader(f,delimiter=',')
        for row in reader:
            ws.append(row)
wb.save('StarOSreport.xlsx')
