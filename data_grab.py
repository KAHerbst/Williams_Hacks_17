#need to install two modules xlrd xlwt uisng pip install
#import xlrd
#open spreadsheet file
#Select sheet
#Extract

from xlrd import open_workbook
import csv
wb = xlrd.open_workbook('my_file_name.xls')
with open(wb, "w") as fin:
    writer = csv.writer(fin, delimiter = ",")
    header = [cell.value for cell in sheet.row(0)]
    writer.writerow(header)
    for row_idx in range(1, sheet.nrows):
        row = [int(cell.value) if isinstance(cell.value, float) else cell.value
               for cell in sheet.row(row_idx)]
        writer.writerow(row)


if __name__ == '__main__':
    name = sys.argv[1]
