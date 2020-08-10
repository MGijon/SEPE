"""
GOAL: centralize ejecution of the cleaning process.
"""
# Python
import os            # TODO: clean dependencies
import progressbar
import xlrd
import pandas as pd
# cleaner_functions
from cleaner_functions import main_cleaner


ROUTE_IN = '../Tests/downloaded_files/'
ROUTE_OUT = 'out_files/'


if __name__ == '__main__':

    NUMBER_OF_DOCUMENTS = -1 # if < 0 -> take all documents

    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    # selecting samples
    if NUMBER_OF_DOCUMENTS < 0:
        sample = list_documents
    else:
        sample = list_documents[:NUMBER_OF_DOCUMENTS]

    print('# ============== #')
    print('# PROCESS PART 1 #')
    print('# ============== #')

    '''
    # NO PROGRESSBAR version
    for excel_file in sample:
        try:
            excel_name = excel_file.replace('ROUTE_IN', '')
            excel_name = excel_name.replace('.csv', '').replace('.xls', '').replace('.xlsx', '')

            # wont add another try/except becouse until this point there is no reason to fail
            main_cleaner(file=excel_file, 
                         name=excel_name)

        except Exception as e:
            print(e)
            pass 

    '''
    try: 
        with progressbar.ProgressBar(max_value=len(sample)) as bar:

            counter = 1
            for excel_file in sample:
                excel_name = excel_file.replace(ROUTE_IN, '')
                excel_name = excel_name.replace('.csv', '').replace('.xls', '').replace('.xlsx', '')

                try:

                    main_cleaner(file=excel_file, name=excel_name)
                    bar.update(counter)


                except Exception as e:
                    print('Something has happend during processing the file... sorry bro! :(')
                    print(e)
                    bar.update(counter)


                counter += 1
    
    except:
        pass 
    
    print('# ============== #')
    print('# PROCESS PART 2 #')
    print('# ============== #')


"""
REFERENCES:
===========

(1) https://xlrd.readthedocs.io/en/latest/vulnerabilities.html
(2) https://pypi.org/project/XlsxWriter/
(3) https://xlsxwriter.readthedocs.io/
"""
