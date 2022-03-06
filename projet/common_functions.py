import numpy as np
import pandas as pd
import random

def convert_attributes_into_pandas(filename):
    """
    Returns a pandas.array matrix containing names of attributes as top of the columns, and the ID and corresponding values in rows.

    Args :
        filename (str) : path to csv file

    Returns :
        df_attributes (pandas.array) :  matrix

    >>> convert_attributes_into_pandas(test_attributes)
    ?

    """
    return pd.read_csv(filename)

def matrix_reduction(df_attributes,fixed_attributes):
    """
    Reduces the matrix based on the traits specified by the witness and deletes all columns corresponding to the specified traits.

    Args :
        df_attributes (pandas.array) : attributes matrix to reduce
        fixed_attributes (dict) : attributes that have been selected by witness to reduce our matrixby columns

    Returns :
        reduced_matrix (pandas.array) :

    >>> matrix_reduction(*,*)
    ?

    """
    attributes = list(fixed_attributes.keys())
    values = list(fixed_attributes.values())
    for i in range(len(attributes)):
        df_attributes.drop(df_attributes.index[df_attributes[attributes[i]]!= values[i]],inplace=True)
    return df_attributes

def get_attributes_from_ID(df_attributes,photo_id):
    """
    Get the corresponding array with all the attributes from the specified string photo name.

    Args :
        df_attributes (panda.array) : attributes matrix with all photos
        photo_id (str) : XXXXXX.png name of the photo

    Returns :
        photo_attributes (pandas.array) :

    >>> get_attributes_from_ID(*,*)
    ?

    """
    return pd.DataFrame(df_attributes.loc[df_attributes['ID'] == photo_id])

def delete_photos(df_attributes,photos_ids):
    """
    Function that deletes photos from the database attribute matrix containing all the photos.

    Args :
        photo_ids list((str)) : list of photos names that look like XXXXXX.png
        df_attributes (panda.array) :

    Returns :
        reduced_df_attributes (panda.array) : same matrix as the arg one but without lines corresponding to photo_ids

    >>> delete_photos(*,*)
    ?

    """
    for i in range(len(photos_ids)):
        df_attributes.drop(df_attributes[df_attributes.ID == str(photos_ids[i])].index,inplace=True)
    return df_attributes
