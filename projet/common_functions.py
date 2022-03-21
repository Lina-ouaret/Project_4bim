import numpy as np
import pandas as pd
import random
from itertools import combinations


def convert_attributes_into_pandas(filename):
    """
    Returns a pandas.array matrix containing names of attributes as top of the columns, and the ID and corresponding values in rows.

    Args :
        filename (str) : path to csv file

    Returns :
        df_attributes (pandas.array) :  matrix

    >>> type(convert_attributes_into_pandas("test_attributes.csv"))
    <class 'pandas.core.frame.DataFrame'>

    """
    return pd.read_csv(filename)

def matrix_reduction(df,fixed_att):
    """
    Reduces the matrix based on the traits specified by the witness and deletes all columns corresponding to the specified traits.

    Args :
        df (pandas.array) : attributes matrix to reduce
        fixed_att (dict) : attributes that have been selected by witness to reduce our matrixby columns

    Returns :
        reduced_matrix (pandas.array) :

    >>> df_test = convert_attributes_into_pandas("test_attributes.csv")
    >>> fixed_attributes_test = {"Pale_Skin":1}
    >>> df_test_list = matrix_reduction(df_test,fixed_attributes_test)
    >>> matrix_reduction(df_test,fixed_attributes_test)
    [18, 47, 88]
    """
    new_df = df
    attributes = list(fixed_att.keys())
    values = list(fixed_att.values())
    for i in range(len(attributes)):
        df.drop(df.index[df[attributes[i]]!= values[i]],inplace=True)
    return new_df.index.tolist()

def get_attributes_from_ID(df_attributes,photo_id):
    """
    Get the corresponding array with all the attributes from the specified string photo name.

    Args :
        df_attributes (panda.array) : attributes matrix with all photos
        photo_id (str) : XXXXXX.png name of the photo

    Returns :
        photo_attributes (pandas.array) :

    >>> df_test = convert_attributes_into_pandas("test_attributes.csv")
    >>> type(get_attributes_from_ID(df_test,'000018.jpg'))
    <class 'pandas.core.frame.DataFrame'>

    """
    return pd.DataFrame(df_attributes.loc[df_attributes['ID'] == photo_id])

def delete_photos(df,photos_ids_list):
    """
    Function that deletes photos from the database attribute matrix containing all the photos.

    Args :
        photo_ids list((str)) : list of photos names that look like XXXXXX.png
        df_attributes (panda.array) :

    Returns :
        reduced_df_attributes (panda.array) : same matrix as the arg one but without lines corresponding to photo_ids

    >>> df_test = convert_attributes_into_pandas("test_attributes.csv")
    >>> list_id = ['000018.jpg','000066.jpg']  
    >>> len(delete_photos(df_test,list_id))
    96
    
    # = len(df_test)-len(list_id)

    """
    new_df = df
    for i in range(len(photos_ids_list)):
        df.drop(df[df.ID == str(photos_ids_list[i])].index,inplace=True)
    return new_df

#################
#TESTS UNITAIRES#
#################

if __name__ == "__main__" :
    import doctest
    doctest.testmod(verbose = True)
