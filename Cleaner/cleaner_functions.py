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
import progressbar

# TODO: llevarme esta parte a la parte que tiene que ver cone el analisis de los datos,
# TODO: no es estadistico pero es analisis al fin y al cabo
import matplotlib.pyplot as plt
#import seaborn as sns


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

    posible_information = []   # es esto lo mas conveninte ???? NO CREO QUE LO SEA

    #p#rint(sheet_name.upper() + '\n')

    # CODIGO PARA IMPLEMNTAR LOS MAPAS DE CALOR !!!!   -> ES EL PUTO BUSCAMINAS!!!! 
    for row in range(number_rows):
        datos_columna = []
        for col in range(number_cols):
            datos_columna.append(sheet.cell_type(row, col))
        posible_information.append(datos_columna)


    plt.figure()
    H = np.asanyarray(posible_information)
    plt.imshow(H)
    #plt.savefig(ROUTE_HEATMAPS + sheet_name + '.png')
    plt.savefig(route_save_images + sheet_name + '.png')
    #plt.show()


    #print('===========================================')
    #######################################################




    # TODO: ARRELGAR ESTE DESTORZO COMPUTACIONAL!!!! -> SHITY CODE!!
    #for row in range(number_rows - 1):
    #    for col in range(number_cols):
    #
    #      try:
    #            if sheet.cell_type(row, col) == 1:
    #                if sheet.cell_type(row + 1, col) == 2:
    #                    #
    #                    #posible_information.append(sheet.)
    #                   print('Algo puede haber aquí muhahhahahahhaha')
    #
    #        except Exception as e:
    #            print('Something has happend muahhahahaha')
    #            print(e)


def main_cleaner(file, name):
    """
    :param file: excel file (route).
    :param name: excel file name.
    :return: None.
    """

    # open the document
    document = xlrd.open_workbook(file)
    # separate it in sheets
    sheet_names = document.sheet_names()

    # si no existe la carpeta con el nomrbe la creamos
    lista_carpetas = os.listdir('out_files/heatmaps/')
    if name + '/' not in lista_carpetas:
        os.mkdir('out_files/heatmaps/' + name)
    #print(lista_carpetas)



    # iterate over the sheets
    for i in range(len(sheet_names)):
        #
        current_sheet = document.sheet_by_index(i)
        #
        sheet_name = sheet_names[i]
        #
        looking_for_groups(sheet=current_sheet, sheet_name=sheet_name, excel_file_name = name)




'''
BAD_CODE:
=========


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

    if SHOW_DEBUGGING:
        print('\t\t\tEmpty cells: ' + str(empty_cells))
        print('\t\t\tText cells: ' + str(text_cells))
        print('\t\t\tNumber cells: ' + str(number_cells))
        print('\t\t\tDate cells: ' + str(date_cells))
        print('\t\t\tBoolen cells: ' + str(bool_cells))
        
#for element in posible_information:
     #   print(element)

    #
    #objeto_estudio = np.asanyarray([x for x in posible_information[0]])
    #print(objeto_estudio.shape)
    #

    #H = np.array(objeto_estudio)
    #plt.imshow(H)
    #plt.show()

    ##############
    #fig = plt.figure(figsize=(6, 3.2))

    #ax = fig.add_subplot(111)
    #ax.set_title('colorMap')
    #plt.imshow(posible_information[0])
    #ax.set_aspect('equal')

    #cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    #cax.get_xaxis().set_visible(False)
    #cax.get_yaxis().set_visible(False)
    #cax.patch.set_alpha(0)
    #cax.set_frame_on(False)
    #plt.colorbar(orientation='vertical')
    #plt.show()

'''