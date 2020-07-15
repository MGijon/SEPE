"""

"""

import pandas as pd


def cleaning_nas(data_frame):
    """

    :param data_frame:
    :return: a data frame without nan's and missing values.
    """

    #out_data = data_frame.dropna(axis = 'columns')
    return data_frame



def cleaning_pipeline(data_frame):
    """

    :param data_frame:
    :return: data_frame after applyed several transformations.
    """

    data_frame = cleaning_nas(data_frame)

    return data_frame



