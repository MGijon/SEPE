"""
NOTES:
======
    - cell_type(row, col) == 0 ==>> the cell is empty.
    - cell_type(row, col) == 1 ==>> the cell contains text.
    - cell_type(row, col) == 2 ==>> the cell contains a number.
    - cell_type(row, col) == 3 ==>> the cell contains a date (does not considered now).
    - cell_type(row, col) == 4 ==>> the cell contains a boolean (does not considered now).
"""

import os            
import xlrd
import pandas as pd



ROUTE_IN = '../Tests/downloaded_files/'
ROUTE_OUT = 'out_files/'
NUMBER_OF_DOCUMENTS = 2 # if < 0 -> take all documents
SHOW_ALL_SHIT = False   # for showing all kind of messages

if __name__ == '__main__':

    ######################
    #### DATA_READING ####
    ######################

    list_documents = os.listdir(ROUTE_IN)
    list_documents = [ROUTE_IN + file for file in list_documents]

    if NUMBER_OF_DOCUMENTS < 0:
        sample = list_documents
    else:
        sample = list_documents[:NUMBER_OF_DOCUMENTS]

    for excel_file_route in sample:

        print(excel_file_route)

        document = xlrd.open_workbook(excel_file_route)
        sheet_names = document.sheet_names()

        # TODO : eliminar indice
        for i in range(len(sheet_names))[:3]:   
            
            print(' ----> ', sheet_names[i])

            sheet = document.sheet_by_index(i)
            
            number_rows = sheet.nrows
            number_cols = sheet.ncols

            if SHOW_ALL_SHIT:
                print('Original number of rows: ', number_rows)
                print('Original number of cols: ', number_cols)

            information = []

            for row in range(number_rows):
                for col in range(number_cols):
                    data = sheet.cell_value(row, col)
                    content = sheet.cell_type(row, col)
                    information.append({
                        'row': row,
                        'col': col,
                        'data': data,
                        'content': content,
                    })

            
            ##########################
            #### CLEANING_PROCESS ####
            ##########################
            
            '''
            # (1) Detecting titles: TODO AÑADIR DENTRO DE UNO DE LOS OTROS BUCLES POR COSTO COMPUTACIONAL
            # ===
            sheet_title, sheet_title_row, sheet_title_col = [], [], []

            for row_index in candidate_rows:
                if number_cols==1:
                    # in this case the title is all
                    pass
                else:
                    filled_cells = number_cols 
                    for col_index in candidate_rows:
                        for element in information:
                            if (element['row']==row_index) and (element['col']==col_index):
                                # We are in the correct place
                                if element['content'] == 0:
                                    filled_cells-=1
                                else:
                                    sheet_title.append(element['data'])
                                    sheet_title_row.append(row_index)
                                    sheet_title_col.append(col_index)
                    #if filled_cells==1:
                        # that means this row contains only the title
                       # index=candidate_cols.index(row_index)
                        #del candidate_rows[index]
            
                print(sheet_title)
                print('****')
               ''' 
            
            candidate_rows = [x for x in range(number_rows)]
            candidate_cols = [c for c in range(number_cols)]

            def part_1(candidate_rows, candidate_cols):
                """
                :param candidate_rows:
                :param candidate_cols:
                """
                for row_index in candidate_rows:
                    all_empty = number_cols
                    for col_index in candidate_cols:
                        for element in information:
                            if (element['row']==row_index) and (element['col']==col_index):
                                # we are in the correct place
                                if element['content'] == 0:
                                    all_empty -= 1
                    if all_empty==0:
                        index = candidate_rows.index(row_index)
                        del candidate_rows[index]
                
                if SHOW_ALL_SHIT:
                    print('Total rows after cleaning: ', len(candidate_rows))

                for col_index in candidate_rows:
                    all_empty = number_rows
                    for row_index in candidate_rows:
                        for element in information:
                            if (element['row']==row_index) and (element['col']==col_index):
                                # We are in the correct place
                                if element['content'] == 0:
                                    all_empty -= 1
                    if all_empty==0:
                        index = candidate_cols.index(col_index)
                        del candidate_cols[index]
                
                if SHOW_ALL_SHIT:
                    print('Total cols after cleaning: ', len(candidate_cols))
                return [candidate_rows, candidate_rows]
            
            both = part_1(candidate_rows=candidate_rows, 
                          candidate_cols=candidate_cols)
            
            if SHOW_ALL_SHIT:
                print(set(both[1]) - set([x for x in range(number_cols)]))
                print(set(both[0]) - set([x for x in range(number_rows)]))

                print('Number of non-empty rows: ', len(candidate_rows))
                print('Number of non-empty columns: ', len(candidate_cols))

    

            def matrix_to_dataframe(candidate_rows, candidate_cols):
                """
                :param candidate_rows:
                :param candidate_cols:
                :return df: 
                """
                structured_information = []

                for row_index in candidate_rows:
                    auxiliar_vector_content = []
                    auxiliar_vector_data = []
                    for element in information:
                        if (element['row']==row_index):
                            auxiliar_vector_content.append(element['content'])
                            auxiliar_vector_data.append(element['data'])


                    structured_information.append(auxiliar_vector_data)
            
                return pd.DataFrame(structured_information)

            df = matrix_to_dataframe(candidate_rows=both[0],
                                     candidate_cols=both[1])


            

            def dataframe_to_dataframes(df):
                """
                :param df: 
                :return dfs:
                """
                dfs = [] # para guardar los dataframes una separado

                for row in df.rows:
                    for col in df.cols:
                        pass
            

            ###############################
            #### VISUALIZATION_PROCESS ####
            ###############################

            print(df)

        print('\n')