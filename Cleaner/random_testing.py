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

            information = []

            for row in range(number_rows):
                for col in range(number_cols):
                    data = sheet.cell_value(row, col)
                    content = sheet.cell_type(row, col)
                    information.append({
                        'row': row,
                        'col': col,
                        'data': data,
                        'content': content,
                    })

            # ROWS
            # ahora limpiamos todo lo que podamos la información eliminando filas enteras si hace falta
            candidate_rows = []
            #candidate_cols = []
            for element in information:
                if element['content'] == 0:
                    candidate_rows.append(element['row'])
                    #candidate_cols.append(element['col'])

            candidate_rows = list(set(candidate_rows))
            #candidate_cols = list(set(candidate_cols))
            
            to_erase_rows = []

            for row in candidate_rows:
                all_columns = 0
                for element in information:
                    for j in range(number_cols):
                        if (element['row'] == row) and (element['col'] == j) and (element['content'] == 0):
                            all_columns += 1
                if all_columns == number_cols:
                    #print('Eliminar fila ', str(row))
                    to_erase_rows.append(row)

            for element in information:
                for row in to_erase_rows:
                    if element['row'] == row:
                        index = information.index(element)
                        del information[index]


            # COLS 
            candidate_cols = []
            for element in information:
                if element['content'] == 0:
                    candidate_rows.append(element['col'])
#
            candidate_cols = list(set(candidate_cols))
            to_erase_cols = []

            for col in candidate_cols:
                all_rows = 0
                for element in information:
                    for j in range(number_cols):
                        if (element['col'] == col) and (element['row'] == j) and (element['content'] == 0):
                            all_rows +=1
                if all_rows == number_cols:
                    to_erase_cols.append(col) 

            
            for element in information:
                for col in to_erase_cols:
                    if element['col'] == col:
                        index = information.index(element)
                        del information[index]


            ## VAMOS A VISUALIZAR EL RESULTADO, 
            #datos_array = [[] for x in len(information)]
            #for element in information:
            
            new_max_rows = number_rows
            new_max_cols = number_cols
            
            new_indexes_rows = []
            new_indexes_cols = []

            for element in information:
                new_indexes_rows.append(element['row'])
                new_indexes_cols.append(element['col'])

            new_indexes_rows = list(set(new_indexes_rows))
            new_indexes_cols = list(set(new_indexes_cols))
            
            new_number_rows = len(new_indexes_rows)
            new_number_cols = len(new_indexes_cols)

            print(min(new_indexes_rows), ' - ', max(new_indexes_rows))
            print(min(new_indexes_cols), ' - ', max(new_indexes_cols))

            print('Old number of rows ' + str(number_rows) + ' - New number of rows ' + str(new_number_rows))
            print('Old number of rows ' + str(number_cols) + ' - New number of cols ' + str(new_number_cols))

            '''
            if element['row'] = row: # nos quedamos en la fila candidata, se trata ahora de comprobar si todas las columnas están vacías
                for col in range(number_cols):
                    for element2 in information:
                        if element[]
            '''
            '''
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

            for row in map_posible_information:
                if sum(row) != 0:
                    non_empty_columsn.append(row)
            
            for line in posible_information:
                print(line)
            print('NON EMPTY COLUMNS: ', non_empty_columsn)
            '''





            #print(pd.DataFrame(posible_information))
            #print('\n ............. \n')


        print('\n')