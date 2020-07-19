"""
The GOAL is to clean as much as posible the excel files.

"""

import os
import progressbar
import xlrd
import json
import numpy as np
import matplotlib.pyplot as plt

ROUTE_IN = '../Tests/downloaded_files/'

def show_dictionary_nicely(list_dictionaries):
    """
    Just print nicelly the information contained in a dictionary.
    :param dictionary: dictionary.
    :return: None.
    """

    for element in list_dictionaries:
        # cada elemento es un diccionario
        for key in element:
            print('----------------')
            print(key)
            print('----------------')
            print(element[key])

        print('================================================================\n')

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

def analyce_information(list_data, NUMBER_DECIMALS=2):
    """
    Short statistical analysis.
    :param list_data: list of Python dictionaries with the next key values:
        - 'route_in': No useful now.
        - 'name': No useful now.
        - 'total_number_of_sheets': number of sheets per document.
        - 'sheets_names': No useful now.
        - 'number_of_rows': number of rows per sheet.
        - 'number_of_cols': number of columns per sheet.
        - 'total_number_of_cells': total number of cells in the sheet.
        - 'empty_cells': total number of empty cells.
        - 'text_cells': total number of cells that contains text.
        - 'number_cells': total number of cells that contains numbers.
        - 'date_cells': total numbers of cell that contains dates.
        - 'bool_cells': total number of cells thtat contains booleans.
        - 'percent_empty_cells': No useful now (because depends on some of the other ones).
        - 'percent_text_cells': No useful now (because depends on some of the other ones).
        - 'percent_number_cells': No useful now (because depends on some of the other ones).
        - 'percent_date_cells': No useful now (because depends on some of the other ones).
        - 'percent_bool_cells': No useful now (because depends on some of the other ones).

    :return: 1 (to pass to the progressbar).
    """
    
    # (1) EXTRACTING THE DATA 
    # ===
    with progressbar.ProgressBar(max_value=len(list_data)) as bar:
        counter = 1

        all_number_of_sheets = []
        
        bolquete_rows = []
        collection_means_all_sheets = []    # ? TODO: decidir como analizar esto?!?!
        collection_stds_all_sheets = []     # ? TODO: decidir como analizar esto?!?!

        bolquete_cols = []
        collection_means_all_sheets = []  # ? TODO: decidir como analizar esto?!?!
        collection_stds_all_sheets = []   # ? TODO: decidir como analizar esto?!?!
 
        bolquete_cells = []

        bolquete_empty = []
        bolquete_text = []
        bolquete_number = [] 
        bolquete_date = []
        bolquete_bools = []
            
        for single_file_data in list_data:
            # TOTAL_NUMBER_OF_SHEETS
            all_number_of_sheets.append(single_file_data['total_number_of_sheets'])

            # NUMBER_OF_ROWS
            rows_single_file = 0
            for rows_in_sheet in single_file_data['number_of_rows']:
                bolquete_rows.append(rows_in_sheet)
                rows_single_file += rows_in_sheet
           
            # NUMBER_OF_COLS   TODO: decidir como analizar esto?!?!
            cols_single_file = 0 # ??? TODO: LO ESTOY USANDO??? 
            for cols_in_sheet in single_file_data['number_of_cols']:
                bolquete_cols.append(cols_in_sheet)
                cols_single_file += cols_in_sheet

            # TOTAL_NUMBER_OF_CELLS  TODO: decidir como analizar esto?!?!
            for cells_in_sheet in single_file_data['total_number_of_cells']:
                bolquete_cells.append(cells_in_sheet)

            # EMPTY_CELLS  TODO: decidir como analizar esto?!?!
            for empty_in_sheet in single_file_data['empty_cells']:
                bolquete_empty.append(empty_in_sheet)

            # TEXT_CELLS  TODO: decidir como analizar esto?!?!
            for text_in_sheet in single_file_data['text_cells']:
                bolquete_text.append(text_in_sheet)

            # MUMBER_CELLS  TODO: decidir como analizar esto?!?!
            for number_in_sheet in single_file_data['number_cells']:
                bolquete_number.append(number_in_sheet)

            # DATE_CELLS  TODO: decidir como analizar esto?!?!
            for date_in_sheet in single_file_data['date_cells']:
                bolquete_date.append(date_in_sheet)

            # BOOLS_CELLS  TODO: decidir como analizar esto?!?!
            for bool_in_sheet in single_file_data['bool_cells']:
                bolquete_bools.append(bool_in_sheet)

            bar.update(counter)
            counter += 1

    # (2) OBTAINING INSIGHTS: BASIC ANALYSIS
    # ===

    print('\n#### #### #### ####\n')
    # (2.0)
    print('\n· We have analyzed a total of ' + str(len(list_data)) + ' documents.')
    
    # (2.1) Total_number_of_sheets
    print('· Number of seets:')
    print('\t· Max number of sheets: ' + str(max(all_number_of_sheets)))
    print('\t· Min number of sheets: ' + str(min(all_number_of_sheets)))
    auxiliar_0 = np.mean(all_number_of_sheets)
    print('\t· Mean: ' + str(np.round(auxiliar_0, NUMBER_DECIMALS)))
    auxiliar_1 = np.std(all_number_of_sheets)
    print('\t· Std: ' + str(np.round(auxiliar_1, NUMBER_DECIMALS)))
    
    # (2.2) Number_of_rows
    print('· About the number of rows: ')
    print('\t· Total number of rows in all documents: ' + str(sum(bolquete_rows)))
    auxiliar_2 = np.mean(single_file_data['number_of_rows'])
    print('\t· The mean is: ' + str(np.round(auxiliar_2, NUMBER_DECIMALS)))
    auxiliar_3 = np.std(single_file_data['number_of_cols'])
    print('\t· The std is: ' + str(np.round(auxiliar_3, NUMBER_DECIMALS)))

    # (2.3) Number_of_columns
    print('· About the number of columns: ')
    print('\t· Total number of columns in all documents: ' + str(sum(bolquete_rows)))
    auxiliar_4 = np.mean(single_file_data['number_of_cols'])
    print('\t· The mean is: ' + str(np.round(auxiliar_4, NUMBER_DECIMALS)))
    auxiliar_5 = np.std(single_file_data['number_of_cols'])
    print('\t· The std is: ' + str(np.round(auxiliar_5, NUMBER_DECIMALS)))

    # (2.4) Total_number_of_cells
    print('· About the total number of cells: ')
    print('\t· Total number of cells in all documents: ' + str(sum(bolquete_cells)))
    auxiliar_6 = np.mean(single_file_data['total_number_of_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_6, NUMBER_DECIMALS)))
    auxiliar_7 = np.std(single_file_data['total_number_of_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_7, NUMBER_DECIMALS)))

    # (2.5) Number_of_empty_cells
    print('· About the cells that are empty: ')
    print('\t· Total number of empty cells: ' + str(sum(bolquete_empty)))
    auxiliar_8 = np.mean(single_file_data['empty_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_8, NUMBER_DECIMALS)))
    auxiliar_9 = np.std(single_file_data['empty_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_9, NUMBER_DECIMALS)))

    # (2.6) Number_of_text_cells
    print('· About the cells that contains text: ')
    print('\t· Total number of text cells: ' + str(sum(bolquete_text)))
    auxiliar_10 = np.mean(single_file_data['text_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_10, NUMBER_DECIMALS)))
    auxiliar_11 = np.std(single_file_data['text_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_11, NUMBER_DECIMALS)))

    # (2.7) Number_of_number_cells
    print('· About the cells that contains numbers: ')
    print('\t· Total number of number cells: ' + str(sum(bolquete_number)))
    auxiliar_12 = np.mean(single_file_data['number_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_12, NUMBER_DECIMALS)))
    auxiliar_13 = np.std(single_file_data['number_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_13, NUMBER_DECIMALS)))

    # (2.8) Number_of_date_cells
    print('· About the cells that contains dates: ')
    print('\t· Total number of date cells: ' + str(sum(bolquete_date)))
    auxiliar_14 = np.mean(single_file_data['date_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_14, NUMBER_DECIMALS)))
    auxiliar_15 = np.std(single_file_data['date_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_15, NUMBER_DECIMALS)))

    # (2.9) Number_of_bools_cells
    print('· About the cells that contains boolean data: ')
    print('\t· Total number of boolean cells: ' + str(sum(bolquete_bools)))
    auxiliar_16 = np.mean(single_file_data['bool_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_16, NUMBER_DECIMALS)))
    auxiliar_17 = np.std(single_file_data['bool_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_17, NUMBER_DECIMALS)))

    print('#### #### #### ####\n')

if __name__ == "__main__":

    NUMBER_OF_DOCUMENTS = 100   # TODO: borrar cuando haya acabado el debugging.

    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    sample = list_documents[:NUMBER_OF_DOCUMENTS]

    print('\n# ================================================= #')
    print('# PROCESS PART 1: OBTAINING THE DATA FROM THE FILES #')
    print('# ================================================= #\n')
    # Here we save the information extracted from the excel files :)
    information_collection = []
    with progressbar.ProgressBar(max_value=len(sample)) as bar:

        counter = 1
        for excel_file in sample:
            excel_name = excel_file.replace(ROUTE_IN, '')
            excel_name = excel_name.replace('.csv', '').replace('.xls', '').replace('.xlsx', '')
            try:

                document = xlrd.open_workbook(excel_file)
                information_collection.append(extract_information(document=document, name=excel_name, route_in=excel_file))
                #show_dictionary_nicely(list_dictionaries=information_collection)
            except Exception as e:

                print('Something has happend during extractign information from the Excel files')
                print(e)

            bar.update(counter)
            counter += 1

    print('\n# ================================================= #')
    print('# PROCESS PART 2: EXTRACTING INSIGTHS FROM THE DATA #')
    print('# ================================================= #\n')
    analyce_information(list_data=information_collection)

    
