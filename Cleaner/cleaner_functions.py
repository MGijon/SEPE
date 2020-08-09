"""
CONTENT: Functions that clean the files.
========
NOTES:
======
    - For previous studies -> there is not date type cells.
     -> We don't take them.
    - For previous studies -> there is just a few booleans.
     -> We don't consider this.
"""


# TODO: LIMPIAR DEPENDENCIAS
import os
import numpy as np
import pandas as pd
import xlrd
#import progressbar

# TODO: llevarme esta parte a la parte que tiene que ver cone el analisis de los datos,
# TODO: no es estadistico pero es analisis al fin y al cabo
import matplotlib.pyplot as plt


SHOW_DEBUGGING = False #
ROUTE_HEATMAPS = 'out_files/heatmaps/'

def looking_for_groups(sheet, sheet_name, excel_file_name, route_save_images=ROUTE_HEATMAPS):
    """
    TODO: PRECISE THIS PROCESS
    :param sheet: excel sheet.
    :param sheet_name: name of the sheet.
    :param excel_file_name: name of the excel file.
    :return: None.

    NOTES:
    ======
        - cell_type(row, col) == 0 ==>> the cell is empty.
        - cell_type(row, col) == 1 ==>> the cell contains text.
        - cell_type(row, col) == 2 ==>> the cell contains a number.
        - cell_type(row, col) == 3 ==>> the cell contains a date (does not considered now).
        - cell_type(row, col) == 4 ==>> the cell contains a boolean (does not considered now).

    """

    excel_file_name = excel_file_name.replace('.csv', '').replace('.xlsx', '').replace('.xls', '')
    route_save_images = route_save_images + excel_file_name + '/'

    number_rows = sheet.nrows
    number_cols = sheet.ncols

    posible_information = []

    for row in range(number_rows):
        datos_columna = []
        for col in range(number_cols):
            datos_columna.append(sheet.cell_type(row, col))
        posible_information.append(datos_columna)


    plt.figure()
    H = np.asanyarray(posible_information)
    plt.imshow(H)
    plt.savefig(route_save_images + sheet_name + '.png')


def erasing_empty_columns_rows(sheet, sheet_name, excel_file_name):
    """
    TODO: description.
    :param sheet: excell sheet.
    :param sheet_name: name of the sheet.
    :param excel_file_name: name of the excel file.
    :return: None.

    NOTES:
    ======
        - cell_type(row, col) == 0 ==>> the cell is empty.
        - cell_type(row, col) == 1 ==>> the cell contains text.
        - cell_type(row, col) == 2 ==>> the cell contains a number.
        - cell_type(row, col) == 3 ==>> the cell contains a date (does not considered now).
        - cell_type(row, col) == 4 ==>> the cell contains a boolean (does not considered now).

    """




    return 0




def main_cleaner(file, name, heatmaps=False):
    """
    :param file: excel file (route).
    :param name: excel file name.
    :return: None.
    """

    # open the document
    document = xlrd.open_workbook(file)
    # separate it in sheets
    sheet_names = document.sheet_names()

    # Create heatmaps based on the content in the sheets
    if heatmaps:
        # si no existe la carpeta con el nomrbe la creamos
        lista_carpetas = os.listdir('out_files/heatmaps/')
        if name + '/' not in lista_carpetas:
            os.mkdir('out_files/heatmaps/' + name)

        # iterate over the sheets
        for i in range(len(sheet_names)):
            #
            current_sheet = document.sheet_by_index(i)
            #
            sheet_name = sheet_names[i]
            #
            looking_for_groups(sheet=current_sheet, sheet_name=sheet_name, excel_file_name = name)

