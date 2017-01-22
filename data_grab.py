#need to install two modules xlrd xlwt uisng pip install
#import xlrd
#open spreadsheet file
#Select sheet
#Extract

from xlrd import open_workbook
import csv
wb = open_workbook('Williams_Major_Reqs.xlsx')
for i in range(wb.nsheets):
    sheet = wb.sheet_by_index(i)
    with open("data.csv", "w") as file:
        writer = csv.writer(file, delimiter = ",")
        for row_idx in range(1, sheet.nrows):
            if "Major" not in str(sheet.row(row_idx)[1]):
                continue
            row = [int(cell.value) if isinstance(cell.value, float) else cell.value
               for cell in sheet.row(row_idx)]
            writer.writerow(row)
