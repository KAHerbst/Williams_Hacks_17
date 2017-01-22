#need to install two modules xlrd xlwt uisng pip install
#import xlrd
#open spreadsheet file
#Select sheet
#Extract

from xlrd import open_workbook
import csv
wb = open_workbook('el_Names.xls')
for i in range(wb.nsheets):
    sheet = wb.sheet_by_index(i)
    with open("data/%s.csv" %(sheet.name.replace(" ","")), "w") as file:
        writer = csv.writer(file, delimiter = ",")
        header = [cell.value for cell in sheet.row(0)]
        writer.writerow(header)
        for row_idx in range(1, sheet.nrows):
            row = [int(cell.value) if isinstance(cell.value, float) else cell.value
                   for cell in sheet.row(row_idx)]
            writer.writerow(row)
