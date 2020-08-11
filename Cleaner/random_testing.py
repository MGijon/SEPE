"""
NOTES:
======
    - cell_type(row, col) == 0 ==>> the cell is empty.
    - cell_type(row, col) == 1 ==>> the cell contains text.
    - cell_type(row, col) == 2 ==>> the cell contains a number.
    - cell_type(row, col) == 3 ==>> the cell contains a date (does not considered now).
    - cell_type(row, col) == 4 ==>> the cell contains a boolean (does not considered now).
"""

import os            # TODO: clean dependencies
import progressbar
import xlrd
import pandas as pd



ROUTE_IN = '../Tests/downloaded_files/'
ROUTE_OUT = 'out_files/'
NUMBER_OF_DOCUMENTS = 2 # if < 0 -> take all documents


if __name__ == '__main__':

    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    if NUMBER_OF_DOCUMENTS < 0:
        sample = list_documents
    else:
        sample = list_documents[:NUMBER_OF_DOCUMENTS]

    for excel_file_route in sample:
        print(excel_file_route)

        document = xlrd.open_workbook(excel_file_route)
        
        # separate it in sheets
        sheet_names = document.sheet_names()

        for i in range(len(sheet_names)):
            
            sheet = document.sheet_by_index(i)
            number_rows = sheet.nrows
            number_cols = sheet.ncols


            print(' ----> ', sheet_names[i])

            # Read sheet
            posible_information = []
            map_posible_information = []

            for row in range(number_rows):
                datos_columna = []
                map_column = []
               
                for col in range(number_cols):    
                    datos_columna.append(sheet.cell_value(row, col))
                    map_column.append(sheet.cell_type(row, col))

                posible_information.append(datos_columna)
                map_posible_information.append(map_column)

            # Repasamos el mapeo buscando mierda varia, para empezar columnas vacías
            non_empty_columsn = []

            
            for line in posible_information:
                print(line)
            #print(pd.DataFrame(posible_information))
            #print('\n ............. \n')


        print('\n')