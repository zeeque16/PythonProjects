import csv
import openpyxl

data = open('D:\\Project\\XflowInternship\\CSV2Excel\\SampleSheet.csv')

csvData = csv.reader(data)
rowsData = list(csvData)

wb = openpyxl.Workbook()
sheet = wb.active

for row in rowsData:
    sheet.append(row)

wb.save("D:\\Project\\XflowInternship\\CSV2Excel\\ConvertedFile.xlsx")