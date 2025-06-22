# Text Files to Spreadsheet

import openpyxl

def text_to_spreadsheets(filenames):
    wb = openpyxl.Workbook()
    sheet = wb.active
    column = 0
    for file in filenames:
        row = 0
        column += 1
        with open(file, "r") as file:
            lines = file.readlines()
            for line in lines:
                row += 1
                sheet.cell(row=row, column=column, value=line) # type: ignore
    wb.save("text_to_spreadsheets.xlsx")

filenames = ["Text1.txt", "Text2.txt", "Text3.txt"]
text_to_spreadsheets(filenames)