# Blank Row Inserter
#! python3

import openpyxl


def insert_blanks(n, m, filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    sheet.insert_rows(n, m)  # type:ignore
    wb.save(f"updated_{filename}")


insert_blanks(2, 3, "Fruits.xlsx")