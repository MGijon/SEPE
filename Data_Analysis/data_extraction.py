"""
The GOAL is to extract the important data from the files.
"""

# TODO: clean the dependencies!!!!
import os
import progressbar
import xlrd
import json
import numpy as np
import matplotlib.pyplot as plt


def extract_information(document, name, route_in):
    """
    Show statistics about the document.
    :param document: route to an Excel file.
    :param name: name of the document.
    :param route_in: route where the document is saved.
    :return: information in a dictionary format about the file.
    """
    # separamos el documento por sheets
    sheet_names = document.sheet_names()

    single_file_struct = {
        'route_in': route_in,
        'name': name,
        'total_number_of_sheets': len(sheet_names),
        'sheets_names': sheet_names,
        'number_of_rows': [],
        'number_of_cols': [],
        'total_number_of_cells': [],
        'empty_cells': [],
        'text_cells': [],
        'number_cells': [],
        'date_cells': [],
        'bool_cells': [],
        'percent_empty_cells': [],
        'percent_text_cells': [],
        'percent_number_cells': [],
        'percent_date_cells': [],
        'percent_bool_cells': [],
    }

    # information extraction process for every sheet
    for i in range(len(sheet_names)):
        current_sheet = document.sheet_by_index(i)
        # number of rows
        number_rows = current_sheet.nrows
        single_file_struct['number_of_rows'].append(number_rows)
        # number of columns
        number_columns = current_sheet.ncols
        single_file_struct['number_of_cols'].append(number_columns)
        # total number of cells
        single_file_struct['total_number_of_cells'].append(number_rows * number_rows)
        # kind of data
        empty = 0
        text = 0
        number = 0
        date = 0
        boolean = 0
        for row in range(number_rows):
            for col in range(number_columns):
                # empty cells
                if current_sheet.cell_type(row, col) == 0:
                    empty += 1
                # text cells
                elif current_sheet.cell_type(row, col) == 1:
                    text += 1
                # number cells
                elif current_sheet.cell_type(row, col) == 2:
                    number += 1
                # date cells
                elif current_sheet.cell_type(row, col) == 3:
                    date += 1
                # boolean cells
                else:
                    boolean += 1
        # empty
        single_file_struct['empty_cells'].append(empty)
        if single_file_struct['total_number_of_cells'][-1] != 0:
            single_file_struct['percent_empty_cells'].append(np.round((empty / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        else: 
            single_file_struct['percent_empty_cells'].append(0)
        # text
        single_file_struct['text_cells'].append(text)
        if single_file_struct['total_number_of_cells'][-1] != 0:
            single_file_struct['percent_text_cells'].append(np.round((text / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        else:
            single_file_struct['percent_text_cells'].append(0)
        # number
        single_file_struct['number_cells'].append(number)
        if single_file_struct['total_number_of_cells'][-1] != 0:
            single_file_struct['percent_number_cells'].append(np.round((number / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        else:
            single_file_struct['percent_number_cells'].append(0)
        # date
        single_file_struct['date_cells'].append(date)
        if single_file_struct['total_number_of_cells'][-1] != 0:
            single_file_struct['percent_date_cells'].append(np.round((date / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        else:
            single_file_struct['percent_date_cells'].append(0)
        # boolean
        single_file_struct['bool_cells'].append(boolean)
        if single_file_struct['total_number_of_cells'][-1] != 0:
            single_file_struct['percent_bool_cells'].append(np.round((boolean / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        else:
            single_file_struct['percent_bool_cells'].append(0)


    return single_file_struct