"""
CONTENT: Functions that show the distribution of the data types in each sheet.
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

def looking_for_groups(sheet, sheet_name, excel_file_name, plot_heatmap=False, save=False, route_save_images=ROUTE_HEATMAPS):
    """
    We look for data groups in the specified sheet creating heatmaps and returning a 2-Dimensional array with the infarmation 
    of what kinf of info is in every sheet.
    :param sheet: excel sheet.
    :param sheet_name: name of the sheet.
    :param excel_file_name: name of the excel file.
    :param plot_heatmap: if True show the heatmaps.
    :param save: if True save the images in the precised route.
    :param route_save_images: route where the images are gonna be saved.
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
    if save:
        plt.savefig(route_save_images + sheet_name + '.png')

    return posible_information



def main_inspector(file, name, heatmaps=False):
    """
    :param file: excel file (route).
    :param name: excel file name.
    :return: None.
    """

    # open the document
    document = xlrd.open_workbook(file)
    # separate it in sheets
    sheet_names = document.sheet_names()

    # Create heatmaps based on the content in the sheets: TODO ELIMINAR LOS BUCLES IF/ELSE, NO HACE FALTA YA QUE SE PASA POR PARÁMETRO!!
    if heatmaps:
        # si no existe la carpeta con el nomrbe la creamos
        lista_carpetas = os.listdir('out_files/heatmaps/')
        if name + '/' not in lista_carpetas:
            os.mkdir('out_files/heatmaps/' + name)

        # iterate over the sheets
        for i in range(len(sheet_names)):
            
            current_sheet = document.sheet_by_index(i)
            sheet_name = sheet_names[i]
            looking_for_groups(sheet=current_sheet, 
                               sheet_name=sheet_name, 
                               excel_file_name = name,
                               plot_heatmap=True,
                               save=True)
    else:
        
        for i in range(len(sheet_names)):
            current_sheet = document.sheet_by_index(i)
            sheet_name = sheet_names[i]

            information = looking_for_groups(sheet=current_sheet,
                                            sheet_name=sheet_name, 
                                            excel_file_name=name, 
                                            plot_heatmap=False, 
                                            save=False)

        for line in information:
            print(line)