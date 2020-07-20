"""
The GOAL is to analyze the data in order to decide a strategy for extracting the information.
"""


# TODO: clean the dependencies!!!!
import os
import progressbar
import xlrd
import json
import numpy as np
import matplotlib.pyplot as plt

# Data extraction functions
from data_extraction import extract_information
# Data analysis functions
from basic_analysis import basic_analysis
from advanced_analysis import advanced_analysis

ROUTE_IN = '../Tests/downloaded_files/'
NUMBER_OF_DOCUMENTS = -150   # if <0 analyze all documents


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

if __name__ == "__main__":

   
    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    if NUMBER_OF_DOCUMENTS < 0:
        sample = list_documents
    else:
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

    print('# ========================== #')
    print('# SUBPART (a) BASIC ANALYSIS #')
    print('# ========================== #')

    basic_analysis(list_data=information_collection)

    print('# ============================= #')
    print('# SUBPART (b) ADVANCED ANALYSIS #')
    print('# ============================= #')

    advanced_analysis(list_data=information_collection)