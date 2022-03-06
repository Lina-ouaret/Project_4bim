import numpy as np
import pandas as pd
import random


def randomly_choose_photos(df_attributes,n):
    """
    Function that randomly chooses n photos from the current reduced matrix, in order to display them so one or two can be selected by the witness

    Args :
        number_photos (int) : number of photo to be selected
        df_attributes (pandas.array) : database from where the photo are selected
    Returns :
        photos_names (list(str)) :  list of photo names looking like XXXXXX.png

    >>> randomly_choose_photos(*)
    ?

    """
    list_ID = df_attributes.ID.tolist()
    return random.sample(list_ID,n)

def crossover(parent1,parent2,pc):
    """
    Function that crosses the attributes of the both parents to make an offspring.
    It takes a proportion pc of attributes from one parent and 1-pc from the other.

    Args :
        parent1 (pandas.array) : first parent (photo) from which we take the attributes
        parent2 (pandas.array) : second parent (photo) from which we take the attributes
        pc (int) : proportion of attributes taken from parent1 (1-pc being prop. of attributes taken from parent2)
    Returns :
        offspring (pandas.array) : offspring of 2 previous parents/photos

    >>> crossover(*,*,*)
    ?

    """
    list1 = parent1.columns.tolist()
    list1.remove('ID')
    #split of attributes list into two based on proportions
    k = int(len(list1)*pc)   #proportion pc from parent1
    l1 = random.sample(list1,k)
    l2 = []
    for attribute in list1 :
        if(attribute not in l1):
            l2.append(attribute)
    attributes = l1 + l2
    #getting each attribute respective value
    values = []
    for i in range(len(l1)):
        values.append(int(parent1.loc[:,l1[i]]))
    for j in range(len(l2)):
        values.append(int(parent1.loc[:,l2[j]]))

    #creating offspring as dataframe
    return pd.DataFrame(values,attributes).transpose()
