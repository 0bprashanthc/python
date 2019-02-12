from datetime import date, datetime, timedelta
import openpyxl
import glob
import csv
import os

def convertCSVToExcel(csv_files, date):
    wb = openpyxl.Workbook()
    for each_file in csv_files:
        print each_file.split('.')[0]
        sheet_title = (each_file.split('.')[0]).split('/')[-1]
        ws = wb.create_sheet(index=0, title=sheet_title)
        with open(each_file) as f:
            reader = csv.reader(f,delimiter=',')
            for row in reader:
                ws.append(row)
    wb.save('StarOSDailyReport_'+date+'.xlsx')

def getDate():
    yesterday = date.today() - timedelta(1)
    yesterday = str(yesterday.strftime('%m-%d-%y'))
    month,day,year = yesterday.split('-')
    year = str(datetime.now().year)
    return year+'-'+month+'-'+day

if __name__ == "__main__":
    #calculate the current date
    date = getDate()
    print("Lookup Date is : "+date)

    #collect all zip files for input date
    print("Lookup files are *"+date+"*")
    zip_files = glob.glob("*"+date+".csv.zip")

    #unzip all collected zip files
    for each_file in zip_files:
        os.system("unzip "+each_file)

    #collect all csv files
    files = glob.glob("exportdaily/*"+date+".csv")
    convertCSVToExcel(files, date)
