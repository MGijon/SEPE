"""
Functions that clean the files.
"""

import os
import pandas as pd
import xlrd
import progressbar



SHOW_DEBUGGING = True

def main_cleaner(file, name):
    """
    :param file: excel file (route).
    :param name: excel file name.
    """

    # open the document
    document = xlrd.open_workbook(file)
    # separate it in sheets
    sheet_names = document.sheet_names()

    for i in range(len(sheet_names)):
        current_sheet = document.sheet_by_index(i)
        name = sheet_names[i]

        number_rows = current_sheet.nrows
        number_cols = current_sheet.ncols

        empty_cells = 0
        text_cells = 0
        number_cells = 0
        date_cells = 0
        bool_cells = 0

        for row in range(number_rows):
            for col in range(number_cols):

                if current_sheet.cell_type(row, col) == 0:
                    empty_cells += 1
                elif current_sheet.cell_type(row, col) == 1:
                    text_cells += 1
                elif current_sheet.cell_type(row, col) == 2:
                    number_cells += 1
                elif current_sheet.cell_type(row, col) == 3:
                    date_cells += 1
                else:
                    # sheet.cell_type(row, col) == 4
                    bool_cells += 1

        if SHOW_DEBUGGING:
            print('\t\t\tEmpty cells: ' + str(empty_cells))
            print('\t\t\tText cells: ' + str(text_cells))
            print('\t\t\tNumber cells: ' + str(number_cells))
            print('\t\t\tDate cells: ' + str(date_cells))
            print('\t\t\tBoolen cells: ' + str(bool_cells))


