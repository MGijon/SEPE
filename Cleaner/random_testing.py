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
SHOW_ALL_SHIT = True   # for showing all kind of messages
INFO_INSIDE_FUNCTIONS = False

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
            print('\n')
            print(' ----> ', sheet_names[i])
            print('\n')

            sheet = document.sheet_by_index(i)
            
            number_rows = sheet.nrows
            number_cols = sheet.ncols

            if SHOW_ALL_SHIT:
                print('===============================')
                print('Original number of rows: ', number_rows)
                print('Original number of cols: ', number_cols)
                print('===============================')

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
            
            
            candidate_rows = [x for x in range(number_rows)]
            candidate_cols = [c for c in range(number_cols)]

            def eliminate_empty_cols_rows(candidate_rows, candidate_cols):
                """
                :param candidate_rows:
                :param candidate_cols:
                :return [candidate_rows, candidate_cols]
                """

                if SHOW_ALL_SHIT and INFO_INSIDE_FUNCTIONS:
                    print('===============================')
                    print('--------')
                    print('Function: eliminate_empty_cols_rows')
                    print('--------')
                    print(':param candidate_rows:')
                    print(':param candidate_cols:')
                    print(':return [candidate_rows, candidate_cols]:')
                    print('===============================')

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
             
            
                return [candidate_rows, candidate_cols]
            

            both = eliminate_empty_cols_rows(candidate_rows=candidate_rows, 
                                             candidate_cols=candidate_cols)
            
            ###############################################################
            ###############################################################
            def looking_for_the_title(cand_rows, cand_cols):
                """
                TODO: Descurpcuión pormenorizada de esta cosa
                :param cand_rows:
                :param cand_cols:
                :return:
                """ 



                if SHOW_ALL_SHIT and INFO_INSIDE_FUNCTIONS:
                    print('===============================')
                    print('--------')
                    print('Function: looking_for_the_title')
                    print('--------')
                    print(':param cand_rows:')
                    print(':param cand_cols:')
                    print(':return:')
                    print('===============================')
                

                

                '''
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
                '''         
                return True

            ################################################################
            ###############################################################


            empty_rows = list(
                set([x for x in range(number_rows)]) - set(both[0])
            )
            empty_cols = list(
                set([x for x in range(number_cols)]) - set(both[1])
            )
            if SHOW_ALL_SHIT:

                print('Rows eliminated: ', empty_rows)
                print('Columns eliminated: ', empty_cols)

                print('Number of non-empty rows: ', len(candidate_rows))
                print('Number of non-empty columns: ', len(candidate_cols))
                print('===============================')
              

    

            def matrix_to_dataframe(cand_rows, cand_cols):
                """
                :param cand_rows:
                :param cand_cols:
                :return df: 
                """

                if SHOW_ALL_SHIT and INFO_INSIDE_FUNCTIONS:
                    print('===============================')
                    print('--------')
                    print('Function: matrix_to_dataframe')
                    print('--------')
                    print(':param cand_rows:')
                    print(':param cand_cols:')
                    print(':return df:')
                    print('===============================\n')

                structured_information = []

                for row_index in cand_rows:
                    auxiliar_vector_content = []
                    auxiliar_vector_data = []
                    for element in information:
                        if (element['row']==row_index):
                            auxiliar_vector_content.append(element['content'])
                            auxiliar_vector_data.append(element['data'])


                    structured_information.append(auxiliar_vector_data)
            
                return pd.DataFrame(structured_information)

            df = matrix_to_dataframe(cand_rows=both[0],
                                     cand_cols=both[1])



            def dataframe_to_dataframes(df):
                """
                :param df: 
                :return dfs:
                """
                dfs = [] # para guardar los dataframes una separado
                

                ## CLEANING FIRST ROW AND EXTRACTING TITLE IF THERE IS ONE
                first_row = df.loc[0, :]

                container = []
                
                for element in first_row.values:
                    if element == '':
                        pass
                    elif element == ' ':
                        pass
                    else:
                        container.append(element)

                if len(container) == 0:
                    df = df.loc[1:, :]
                elif len(container) == 1:
                    title = container[0]
                    df = df.loc[1:, :]
                else:
                    df = df # nothing happends


                #### HASTA AQÍ ESTÁ FUNCIONAND, A PARTIR DE AQUÍ SOLO EL INFINITO NOS ESPERA

                number_rows_df, number_columns_df = df.shape[0], df.shape[1]
                print(number_rows_df)
                print(number_columns_df)
                

                ## De momeonto lo haré por separado, primero eliminaré columnas vacías y luego filas
                '''
                for col in range(1, number_columns_df+1):
                    contador = 0
                    for row in range(1, number_columns_df+1):
                        element = df.loc[1, 1]
                        if (element == '') or (element== ' '):
                            contador+=1
                    print(contador)
                '''
                '''
                for row_index in range(number_rows_df):
                    counter = 0
                    for col_index in range(number_columns_df):
                        element = df.loc[row_index, col_index]
                        if (element == '') or (element==' '):
                            counter += 1
                        if counter==number_columns_df:
                            # esto significa que la columna está vacía de acuerdo a LA CASUÍSTICA ESTUDIADA
                            # TODO: LLEVARSE EL TRIGER A UNA FUNCIÓN APARTE
                            print('Detectada FILA VACÍA')
                '''


                #print(container)
                #print(type(first_row))

                #df = df.dropna()               
                return df
            

            ###############################
            #### VISUALIZATION_PROCESS ####
            ###############################

            procesed_df=dataframe_to_dataframes(df=df)
            print(procesed_df)

        print('\n')


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