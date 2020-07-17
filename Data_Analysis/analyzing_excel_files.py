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
        single_file_struct['empty_cells'].append(empty)

        if single_file_struct['total_number_of_cells'][-1] != 0:
            single_file_struct['percent_empty_cells'].append(np.round((empty / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        else: 
            single_file_struct['percent_empty_cells'].append(0)

        single_file_struct['text_cells'].append(text)
        single_file_struct['percent_text_cells'].append(np.round((text / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        single_file_struct['number_cells'].append(number)
        single_file_struct['percent_number_cells'].append(np.round((number / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        single_file_struct['date_cells'].append(date)
        single_file_struct['percent_date_cells'].append(np.round((date / single_file_struct['total_number_of_cells'][-1]) * 100, 2))
        single_file_struct['bool_cells'].append(boolean)
        single_file_struct['percent_bool_cells'].append(np.round((boolean / single_file_struct['total_number_of_cells'][-1]) * 100, 2))


    return single_file_struct

def analyce_information(list_data):
    """

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
            
        for single_file_data in list_data:
            # TOTAL_NUMBER_OF_SHEETS
            all_number_of_sheets.append(single_file_data['total_number_of_sheets'])

            # NUMBER_OF_ROWS

            # NUMBER_OF_COLS

            # TOTAL_NUMBER_OF_CELLS

            # EMPTY_CELLS

            # TEXT_CELLS

            # MUMBER_CELLS

            # DATE_CELLS

            # BOOLS_CELLS

            bar.update(counter)
            counter += 1

    # (2) OBTAINING INSIGHTS
    # ===

    print('Mean: ' + str(np.mean(all_number_of_sheets)))
    print('Std: ' + str(np.std(all_number_of_sheets)))

if __name__ == "__main__":

    NUMBER_OF_DOCUMENTS = 5   # TODO: borrar cuando haya acabado el debugging.

    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    sample = list_documents[:NUMBER_OF_DOCUMENTS]

    print('PROCESS PART 1: OBTAINING THE DATA FROM THE FILES')
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

    print('PROCESS PART 2: EXTRACTING INSIGTHS FROM THE DATA')
    analyce_information(list_data=information_collection)

    