"""Auxiliar functions for the parsing process."""

import os
import pandas as pd
import numpy as np
import xlrd

def show_info_sheet(sheet, show_info):
    """
	TODO: ahora mismo solo muestra info si show_info está activada, no tiene sentido que si esto es false se ejecute nada de esto, debo de arreglarlo para que tenga coherencia intera que le falta y mucho ahora mismo 
    :param sheet:
    :param show_info:
    :return:
    """
    number_rows = sheet.nrows
    number_cols = sheet.ncols

    empty_cells = 0
    text_cells = 0
    number_cells = 0
    date_cells = 0
    bool_cells = 0

    for row in range(number_rows):
        for col in range(number_cols):

            if sheet.cell_type(row, col) == 0:
                empty_cells += 1
            elif sheet.cell_type(row, col) == 1:
                text_cells += 1
            elif sheet.cell_type(row, col) == 2:
                number_cells += 1
            elif sheet.cell_type(row, col) == 3:
                date_cells += 1
            else:
                # sheet.cell_type(row, col) == 4
                bool_cells += 1

    if show_info:
        print('\t\t\tEmpty cells: ' + str(empty_cells))
        print('\t\t\tText cells: ' + str(text_cells))
        print('\t\t\tNumber cells: ' + str(number_cells))
        print('\t\t\tDate cells: ' + str(date_cells))
        print('\t\t\tBoolen cells: ' + str(bool_cells))

def dummy_reading(file, name):
    """
	Just trying to read the file all at once and saving the resoult as a csv using pandas.
	:param file: Excel file.
	:param name: name of the temporal file.
	:return: None.
	"""
    ROOT_DUMMY = 'dummy/'
    print(name)
    df = pd.read_excel(file)
    print(df.head())
    df.to_csv(ROOT_DUMMY + name + '.csv')

def parse_sheet(file_name, sheet):
    """
    :param sheet:
    :param shoe_info:
    :return:
    """
    ROOT_INTERMEDIATE = 'intermediate_steps/'
    print(os.listdir(ROOT_INTERMEDIATE))
    return 0


