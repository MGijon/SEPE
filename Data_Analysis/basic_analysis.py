"""
The GOAL is to analyze the data that comes from the files.
"""

# TODO: clean the dependencies!!!!
import os
import progressbar
import xlrd
import json
import numpy as np
import matplotlib.pyplot as plt

ROUTE_IMAGES = 'images/'

def basic_analysis(list_data, NUMBER_DECIMALS=2):
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
    # =====
    print('\n· We have analyzed a total of ' + str(len(list_data)) + ' documents.')
    
    # (2.1) Total_number_of_sheets
    # =====
    print('· Number of seets:')
    print('\t· Max number of sheets: ' + str(max(all_number_of_sheets)))
    print('\t· Min number of sheets: ' + str(min(all_number_of_sheets)))
    auxiliar_0 = np.mean(all_number_of_sheets)
    print('\t· Mean: ' + str(np.round(auxiliar_0, NUMBER_DECIMALS)))
    auxiliar_1 = np.std(all_number_of_sheets)
    print('\t· Std: ' + str(np.round(auxiliar_1, NUMBER_DECIMALS)))
    
    # (2.2) Number_of_rows
    # =====
    print('· About the number of rows: ')
    print('\t· Total number of rows in all documents: ' + str(sum(bolquete_rows)))
    auxiliar_2 = np.mean(single_file_data['number_of_rows'])
    print('\t· The mean is: ' + str(np.round(auxiliar_2, NUMBER_DECIMALS)))
    auxiliar_3 = np.std(single_file_data['number_of_cols'])
    print('\t· The std is: ' + str(np.round(auxiliar_3, NUMBER_DECIMALS)))

    # (2.3) Number_of_columns
    # =====
    print('· About the number of columns: ')
    print('\t· Total number of columns in all documents: ' + str(sum(bolquete_rows)))
    auxiliar_4 = np.mean(single_file_data['number_of_cols'])
    print('\t· The mean is: ' + str(np.round(auxiliar_4, NUMBER_DECIMALS)))
    auxiliar_5 = np.std(single_file_data['number_of_cols'])
    print('\t· The std is: ' + str(np.round(auxiliar_5, NUMBER_DECIMALS)))

    # (2.4) Total_number_of_cells
    # =====
    print('· About the total number of cells: ')
    print('\t· Total number of cells in all documents: ' + str(sum(bolquete_cells)))
    auxiliar_6 = np.mean(single_file_data['total_number_of_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_6, NUMBER_DECIMALS)))
    auxiliar_7 = np.std(single_file_data['total_number_of_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_7, NUMBER_DECIMALS)))

    # (2.5) Number_of_empty_cells
    # =====
    print('· About the cells that are empty: ')
    print('\t· Total number of empty cells: ' + str(sum(bolquete_empty)))
    auxiliar_8 = np.mean(single_file_data['empty_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_8, NUMBER_DECIMALS)))
    auxiliar_9 = np.std(single_file_data['empty_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_9, NUMBER_DECIMALS)))

    # (2.6) Number_of_text_cells
    # =====
    print('· About the cells that contains text: ')
    print('\t· Total number of text cells: ' + str(sum(bolquete_text)))
    auxiliar_10 = np.mean(single_file_data['text_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_10, NUMBER_DECIMALS)))
    auxiliar_11 = np.std(single_file_data['text_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_11, NUMBER_DECIMALS)))

    # (2.7) Number_of_number_cells
    # =====
    print('· About the cells that contains numbers: ')
    print('\t· Total number of number cells: ' + str(sum(bolquete_number)))
    auxiliar_12 = np.mean(single_file_data['number_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_12, NUMBER_DECIMALS)))
    auxiliar_13 = np.std(single_file_data['number_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_13, NUMBER_DECIMALS)))

    # (2.8) Number_of_date_cells
    # =====
    print('· About the cells that contains dates: ')
    print('\t· Total number of date cells: ' + str(sum(bolquete_date)))
    auxiliar_14 = np.mean(single_file_data['date_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_14, NUMBER_DECIMALS)))
    auxiliar_15 = np.std(single_file_data['date_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_15, NUMBER_DECIMALS)))

    # (2.9) Number_of_bools_cells
    # =====
    print('· About the cells that contains boolean data: ')
    print('\t· Total number of boolean cells: ' + str(sum(bolquete_bools)))
    auxiliar_16 = np.mean(single_file_data['bool_cells'])
    print('\t· The mean is: ' + str(np.round(auxiliar_16, NUMBER_DECIMALS)))
    auxiliar_17 = np.std(single_file_data['bool_cells'])
    print('\t· The std is: ' + str(np.round(auxiliar_17, NUMBER_DECIMALS)))

    print('\n#### #### #### ####\n')



    # (3) OBTAINING INSIGHTS: GENERATING GRAPHICS
    # ===

    NUMBER_BINS = 50 
    # (3.1) Total_number_of_sheets
    # =====
    plt.figure()
    plt.title('Number of sheets per document (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(all_number_of_sheets, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(all_number_of_sheets)) + ' - STD: ' + str(np.std(all_number_of_sheets)))
    plt.savefig(ROUTE_IMAGES + 'number_of_sheets_per_document.png')

    
    # (2.2) Number_of_rows
    # =====
    plt.figure()
    plt.title('Number of rows (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_rows, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_rows)) + ' - STD: ' + str(np.std(bolquete_rows)))
    plt.savefig(ROUTE_IMAGES + 'number_of_rows_per_document_(all_sheets_at_once).png')

    # (2.3) Number_of_columns
    # =====
    plt.figure()
    plt.title('Number of columns  (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_cols, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_cols)) + ' - STD: ' + str(np.std(bolquete_cols)))
    plt.savefig(ROUTE_IMAGES + 'number_of_cols_per_document_(all_sheets_at_once).png')

    # (2.4) Total_number_of_cells
    # =====
    plt.figure()
    plt.title('Number of cells  (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_cells, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_cells)) + ' - STD: ' + str(np.std(bolquete_cells)))
    plt.savefig(ROUTE_IMAGES + 'number_of_cells_per_document_(all_sheets_at_once).png')

    # (2.5) Number_of_empty_cells
    # =====
    plt.figure()
    plt.title('Number of empty cells (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_empty, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_empty)) + ' - STD: ' + str(np.std(bolquete_empty)))
    plt.savefig(ROUTE_IMAGES + 'number_of_empty_cells_per_document_(all_sheets_at_once).png')

    # (2.6) Number_of_text_cells
    # =====
    plt.figure()
    plt.title('Cells that contains text  (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_text, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_text)) + ' - STD: ' + str(np.std(bolquete_cells)))
    plt.savefig(ROUTE_IMAGES + 'number_of_text_cells_per_document_(all_sheets_at_once).png')

    # (2.7) Number_of_number_cells
    # =====
    plt.figure()
    plt.title('Cells that contains numbers  (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_number, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_number)) + ' - STD: ' + str(np.std(bolquete_number)))
    plt.savefig(ROUTE_IMAGES + 'number_of_number_cells_per_document_(all_sheets_at_once).png')

    # (2.8) Number_of_date_cells
    # =====
    plt.figure()
    plt.title('Cells that contains dates  (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_date, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_date)) + ' - STD: ' + str(np.std(bolquete_date)))
    plt.savefig(ROUTE_IMAGES + 'number_of_date_cells_per_document_(all_sheets_at_once).png')

    # (2.9) Number_of_bools_cells
    # =====
    plt.figure()
    plt.title('Cells that contains booleans  (total of ' + str(len(list_data)) + ' documents analyzed)')
    plt.hist(bolquete_bools, bins=NUMBER_BINS)
    plt.xlabel('MEAN: ' + str(np.mean(bolquete_bools)) + ' - STD: ' + str(np.std(bolquete_bools)))
    plt.savefig(ROUTE_IMAGES + 'number_of_bools_cells_per_document_(all_sheets_at_once).png')