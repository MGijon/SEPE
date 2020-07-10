"""
Ya tengo los archivos descargados, ahora se trata de parsearlos como pueda.

SE TRATA SOLAMENTE DE SACAR LA INFORMACION DE UNA MANERA ESTRUCTURADA, DE ALMACENAR DE QUE YEAR Y MES SE TRATAE YA ME
ENCARGARE EN LA SIGUIENTE ITERACION.
"""

import os
import xlrd
import openpyxl
import pandas as pd

available_files = os.listdir('downloaded_files')
available_files = ['downloaded_files/' + file for file in available_files]

# now, let's take just the first one of the files
person_of_interest = available_files[0]



print('====')
print('Using the library XLRD:')
try:
    document = xlrd.open_workbook(person_of_interest)
    sheet_names = document.sheet_names()
    print('- File: '  + person_of_interest)
    print('   * This file has a total of ' + str(len(sheet_names)) + ' sheets.')
    print('   * Sheet by sheet: ')
    for i in range(len(sheet_names)):
        print('       (' + str(i) + ') > Sheet name: ' + sheet_names[i])
        current_sheet = document.sheet_by_index(i)
        print('            . Number of rows: ' + str(current_sheet.nrows))
        print('            . Number of columns: ' + str(current_sheet.ncols))

except Exception as e:
    print(e)
print('====')






"""
REFERENCES:
===========

(1) 

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



