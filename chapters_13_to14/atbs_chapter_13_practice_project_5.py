# Spreadsheets to Text Files

import openpyxl


def text_to_spreadsheets(filename):
    wb = openpyxl.load_workbook(filename)
    sheet = wb.active
    excel_data = []

    for row in sheet.iter_rows(values_only=True):  # type:ignore
        excel_data.append(list(row))
    transposed_data = list(zip(*excel_data))

    for i, row in enumerate(transposed_data, start=1):
        with open(f"spreadsheet{i}.txt", "w") as file:
            for j, value in enumerate(row, start=1):
                file.write(str(value) + "\n")


text_to_spreadsheets("text_to_spreadsheets.xlsx")
