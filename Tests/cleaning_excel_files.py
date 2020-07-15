"""
The GOAL is to clean as much as posible the excel files.
"""

import os
import progressbar
import xlrd
import json

ROUTE_IN = 'downloaded_files/'
ROUTE_OUT = 'intermediate_steps/'


def show_stats(document, name):
    """
    Show statistics about the document.
    :param document: route to an Excel file.
    :param name: name of the document.
    :return: None.
    """
    # separamos el documento por sheets
    sheet_names = document.sheet_names()

    ALL_DATA = {
        'name': name,
    }

    number_of_sheets = len(sheet_names)
    print(name)





if __name__ == "__main__":

    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    sample = list_documents[:2]

    for excel_file in sample:

        excel_name = excel_file.replace(ROUTE_IN, '')
        excel_name = excel_name.replace('.csv', '').replace('.xls', '').replace('.xlsx', '')

        try:

            document = xlrd.open_workbook(excel_file)

            show_stats(document=document, name=excel_name)

        except Exception as e:

            print('Something has happend during cleaning the Excel file')
            print(e)

