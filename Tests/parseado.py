"""
Ya tengo los archivos descargados, ahora se trata de parsearlos como pueda.

SE TRATA SOLAMENTE DE SACAR LA INFORMACION DE UNA MANERA ESTRUCTURADA, DE ALMACENAR DE QUE YEAR Y MES SE TRATAE YA ME
ENCARGARE EN LA SIGUIENTE ITERACION.
"""

import os
import time
import progressbar
import xlrd
import pandas as pd


from auxiliar_parser_functions import *

available_files = os.listdir('downloaded_files')
#available_files = ['downloaded_files/' + file for file in available_files]    # uncomment to eat files directly as they are in the server
available_files = ['intermediate_steps/' + file for file in available_files]


def all_at_once_reading(show_selected_function_title=False):
    """
    Dummy reading code.
    :return:
    """

    try:
        if show_selected_function_title:
            print('\t# ------------------------ #')
            print('\t# Dummy reading function 1 #')
            print('\t# ------------------------ #')

        #dummy_reading(file=person_of_interest, name=person_of_interest[17:])

        if show_selected_function_title:
            print('\n')
            print('\t# ------------------------ #')
            print('\t# Dummy reading function 2 #')
            print('\t# ------------------------ #')

        dummy_reading_2(file=person_of_interest, name=person_of_interest[17:])

    except Exception as e:
        print(e)


def shet_by_shet_reading():
    """
    Sheet by sheet reading.
    :return:
    """

    try:
        document = xlrd.open_workbook(person_of_interest)
        sheet_names = document.sheet_names()
        print('- File: ' + person_of_interest)
        print('\t* This file has a total of ' + str(len(sheet_names)) + ' sheets.')
        print('\t* Sheet by sheet: ')
        for i in range(len(sheet_names)):
            print('\t(' + str(i) + ') > Sheet name: ' + sheet_names[i])
            current_sheet = document.sheet_by_index(i)
            print('\t\t. Number of rows: ' + str(current_sheet.nrows))
            print('\t\t. Number of columns: ' + str(current_sheet.ncols))

            # show_info_sheet(sheet= current_sheet, show_info=True)
            # parse_sheet(file_name=person_of_interest[17:], sheet=current_sheet)

        print('\n')
    except Exception as e:
        print(e)



if __name__ == "__main__":

    # now, let's take just the first one of the files
    sample = available_files

    # ============= #
    # DUMMY_READING #
    # ============= #
    print('==== Starting with Dummy Reading ====\n')

    with progressbar.ProgressBar(max_value=len(sample)) as bar:

        counter = 0
        # person_of_interest -> single file
        for person_of_interest in sample:

            all_at_once_reading(show_selected_function_title=False)

            bar.update(counter)
            counter +=1


    print('==== Ended with Dummy Reading ====')

    # ====================== #
    # SHEET_BY_SHEET_READING #
    # ====================== #
    #print('==== Sheet by Sheet reading ====')
    #for person_of_interest in sample:

        #shet_by_shet_reading()

    #print('==== Ended Sheet by Sheet reading ====')





"""
REFERENCES:
===========

(1) https://www.sitepoint.com/using-python-parse-spreadsheet-data/
(2) http://www.python-excel.org/
(3) https://openpyxl.readthedocs.io/en/stable/tutorial.html#playing-with-data
(4) https://xlrd.readthedocs.io/en/latest/formatting.html#formatting-features-not-included-in-xlrd
(5) https://programacion.net/articulo/como_trabajar_con_archivos_excel_utilizando_python_1419
(6) https://blogs.harvard.edu/rprasad/2014/06/16/reading-excel-with-python-xlrd/
(7) https://robologs.net/2019/03/09/como-leer-ficheros-excel-con-python-y-xlrd/
(8) https://pypi.org/project/xlwt/
(9) https://www.sqlshack.com/python-scripts-to-format-data-in-microsoft-excel/
(10) https://pypi.org/project/progressbar2/

"""




"""
BAD_CODE:
=========

print('====')
print('OPENPXL')
try:
    document = openpyxl.load_workbook(person_of_interest)
except Exception as e:
    print(e)
print('====\n')



"""



