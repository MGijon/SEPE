"""
"""
# Python
import os            # TODO: clean dependencies
import progressbar
import xlrd
import pandas as pd
# Functions to Inspect the Sheets
from inspection_functions import main_inspector

ROUTE_IN = '../Tests/downloaded_files/'
ROUTE_OUT = 'out_files/'
NUMBER_OF_DOCUMENTS = 2 # if (NUMBER_OF_DOCUMENTS <= 0) then take all documents


if __name__ == '__main__':

    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    # selecting samples
    if NUMBER_OF_DOCUMENTS <= 0:
        sample = list_documents
    else:
        sample = list_documents[:NUMBER_OF_DOCUMENTS]

    try: 
        with progressbar.ProgressBar(max_value=len(sample)) as bar:

            counter = 1
            for excel_file in sample:
                excel_name = excel_file.replace(ROUTE_IN, '')
                excel_name = excel_name.replace('.csv', '').replace('.xls', '').replace('.xlsx', '')

                try:
                    main_inspector(file=excel_file, name=excel_name)
                    bar.update(counter)

                except Exception as e:
                    print('Something has happend during processing the file... sorry bro! :(')
                    print(e)
                    bar.update(counter)

                counter += 1
    
    except:
        pass 



"""
REFERENCES:
===========

(1) https://xlrd.readthedocs.io/en/latest/vulnerabilities.html
(2) https://pypi.org/project/XlsxWriter/
(3) https://xlsxwriter.readthedocs.io/
"""
