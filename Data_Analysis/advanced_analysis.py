"""
The GOAL is to perform a more advanced statistical analysis that the ones done until now.
"""

import os
import progressbar
import xlrd
import json
import numpy as np
import matplotlib.pyplot as plt

ROUTE_IMAGES = 'images/'

def advanced_analysis(list_data, NUMBER_DECIMAS=2):
    """
    More deep statistical analysis.
    :param list_dictionaries: list of Python dictionaries with the next key values:
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


    print('FUNCIONAN!!!!!MUHAHHAHA')