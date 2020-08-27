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
SHOW_ALL = False   # for showing all kind of messages
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

            if SHOW_ALL:
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

                if SHOW_ALL and INFO_INSIDE_FUNCTIONS:
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
                                #if element['content'] == 0:
                                if (element['content'] == 0) or (element['data']=='') or (element['data']==' '):
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
                                #if element['content'] == 0:
                                if (element['content'] == 0) or (element['data']=='') or (element['data']==' '):
                                    all_empty -= 1

                    if all_empty==0:
                        index = candidate_cols.index(col_index)
                        del candidate_cols[index]
             
            
                return [candidate_rows, candidate_cols]
            

            both = eliminate_empty_cols_rows(candidate_rows=candidate_rows, 
                                             candidate_cols=candidate_cols)
            

            empty_rows = list(
                set([x for x in range(number_rows)]) - set(both[0])
            )
            empty_cols = list(
                set([x for x in range(number_cols)]) - set(both[1])
            )

            if SHOW_ALL:
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

                if SHOW_ALL and INFO_INSIDE_FUNCTIONS:
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

            def cleaning_dataframe_rows(df):
                """
                :param df: 
                :return dfs:
                """
                dfs = [] # para guardar los dataframes una separado
                

                cleaned_df = df
                number_of_rows = cleaned_df.shape[0]
                number_of_columns = cleaned_df.shape[1]

                footpage_notes = []    # TODO: devolver esto

                # DIFFERENT GROUPS OF DATA
                try:
                    for row in range(1, number_of_rows-2):
                        total = 0
                        for element in cleaned_df.loc[row, :].values:
                            if (element=='') or (element==' '):
                                total+=1
                        if total==number_of_columns:
                            upper_df = cleaned_df.loc[:row, :]
                            lower_df = cleaned_df.loc[row:, :]
                            dfs.append({
                                'title': [],
                                'subtitle': [],
                                'footnotes': [],
                                'dataframe': upper_df,
                                })
                            dfs.append({
                                'title': [],
                                'subtitle': [],
                                'footnotes': [],
                                'dataframe': lower_df,
                                })

                except Exception as e:
                    print('Something has happend during cleaning the intermediate rows of the document. In this process we saparete between different datasets.')
                    print(e)
                    pass


                # TODO: REFACTORIZAR ESTA MIERDA ENORME!!!!
                # First row empty? -> Extraction of the title/titles and subtitles
                try:
                    # first empty row
                    for element in dfs:
                        
                        total_rows, total_columns = element['dataframe'].shape[0], element['dataframe'].shape[1]
                        first_row = element['dataframe'].iloc[0]

                        total = 0 
                        for single_element in first_row.values:
                            if (single_element=='') or (single_element==' '):
                                total+=1
                        if total==number_cols:
                            element['dataframe'] = element['dataframe'].iloc[1:]
                        
                    # TITLE and SUBTITLE
                    for element in dfs:
                        total_rows, total_columns = element['dataframe'].shape[0], element['dataframe'].shape[1]
                        # Used to contain the title
                        first_row = element['dataframe'].iloc[0]
                        # Used to coantain the subtitle

                        total_title=0 
                        total_subtitle=0

                        for single_element in first_row.values:
                            if (single_element=='') or (single_element==' '):
                                total_title+=1
                            else:
                                element['title'].append(single_element)
                        
                        # TODO: Localize and save the Subtitles, in case they exists.
                        '''
                        for single_element in second_row.values:
                            if (single_element=='') or (single_element==' '):
                                total_subtitle+=1
                            else:
                                element['subtitle'].append(single_element)


                        if (total_title==(number_cols-1)) and (total_subtitle==(number_cols-1)):
                            element['dataframe'] = element['dataframe'].iloc[2:]
                        '''

                        if (total_title==(number_cols-1)):
                            element['dataframe'] = element['dataframe'].iloc[2:]



                except Exception as e:
                    print('Something has happend during cleaning the first row of the document.')
                    print(e)
                    pass

                # TODO: Localize and save the Footnotes, in case they exists.
                '''
                # Last row? -> Extraction of the footnotes
                for element in dfs:
                    total_rows, total_columns = element['dataframe'].shape[0], element['dataframe'].shape[1]    
                    last_row = element['dataframe'].iloc[total_columns]

                    total_footnotes = 0
                    
                    if total_rows > 2:
                        for single_element in last_row.values:
                            if (single_element=='') or (single_element==' '):
                                total_footnotes+=1
                            else:
                                element['footnotes'].append(single_element)
                        if (total_footnotes==(total_columns-1)):
                            element['dataframe'] = element['dataframe'].iloc[:total_columns]
                '''
    
                # TODO: Look for empty rows in the midle of the dataframe and, if they corresponds
                # to different groups of data create two separate dataframes.
            
                if len(df) > 1:
                    return dfs 
                else:
                    return [{
                        'title': [],
                        'subtitle': [],
                        'footnotes': [],
                        'dataframe': cleaned_df,
                        }]
   

            def cleaning_dataframe_columns(df):
                """
                :param df:
                :return cleaned_df:
                """
                cleaned_df = df
                number_of_rows = cleaned_df.shape[0]
                number_of_columns = cleaned_df.shape[1]
                

                # Case 1: primera columna
                try:
                    total=0
                    for element in cleaned_df.loc[:, 0].values:
                        if (element == '') or (element == ' '):
                            total+=1
                    if total==number_of_rows:
                        cleaned_df = cleaned_df.loc[:, 1:]

                except Exception as e:
                    print('Something has happend during cleaning the first column of the dataframe.')
                    print(e)
                    pass 

                # Case 2: última columna 
                try:
                    total=0                    
                    for element in cleaned_df.loc[:, number_of_columns-1].values:
                        if (element=='') or (element==' '):
                            total+=1
                    if total==number_of_rows:
                        cleaned_df=cleaned_df.loc[:, :number_of_columns-2]
                     
                except Exception as e:
                    print('Something has happend during cleaning the last column of the dataframe.')
                    print(e)
                    pass

                # Case 3: clumnas en medio
                try:
                    for i in range(1, number_of_columns-2):
                        total=0
                        for element in cleaned_df.loc[:, i].values:
                            if (element=='') or (element==' '):
                                total+=1
                        if total==number_of_rows:
                            right_part = cleaned_df.loc[:, :i-1]
                            left_part = cleaned_df.loc[:, i+1:]
                            cleaned_df = pd.concat([right_part, left_part], axis=1, sort=False)

                except Exception as e:
                    print('Something has happend during cleaning the columns in the midle of the dataset.')
                    print(e)
                    pass

                return cleaned_df


            ###############################
            #### VISUALIZATION_PROCESS ####
            ###############################

            dfs=cleaning_dataframe_rows(df=df)    

            for element in dfs:
                print('Title: ', element['title'])
                print('Subtitle: ', element['subtitle'])
                df=cleaning_dataframe_columns(df=element['dataframe'])
                print(df)
                print('Footnotes: ', element['footnotes'])
                print('\n')


        