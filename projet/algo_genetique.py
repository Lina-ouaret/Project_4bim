import numpy as np
import pandas as pd
import random
from itertools import combinations

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
    list_ID = df_attributes.index.tolist()
    return random.sample(list_ID,n)

def crossover_pixels(parents,pc):
    """
    Function that crosses the reduced pixel matrix (encoded by neural network) of the both parents to make an offspring.
    It takes a proportion pc of attributes from one parent and 1-pc from the other.

    Args :
        parents (list(pandas.array)) : list of arrays representing the reduced pixel matrix of the parents we will use for the

        pc (int) : proportion of attributes taken from parent1 (1-pc being prop. of attributes taken from parent2)
    Returns :
        offspring (pandas.array) : offspring of 2 previous parents/photos

    >>> crossover(*,*,*)
    ?

    """
    index_parents = list(range(0,len(parents)))
    p_combinations = list(combinations(index_parents,2))
    offsprings = []
    for i in range(len(p_combinations)):
        parent_1 = (parents[p_combinations[i][0]]).tolist()
        parent_2 = (parents[p_combinations[i][1]]).tolist()
        k = int(parents[0].size*pc)  #proportion pc from parent1
        offsprings.append(random.sample(parent_1,k)+ random.sample(parent_2,parents[0].size-k))
    return offsprings

def crossover_attributes(parent1,parent2,pc):
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

def mutation_pixels(parents,pm):
    """
    Function that crosses the reduced pixel matrix (encoded by neural network) of the both parents to make an offspring.
    It takes a proportion pc of attributes from one parent and 1-pc from the other.

    Args :
        parents (list(pandas.array)) : list of arrays representing the reduced pixel matrix of the parents we will use for the

        pc (int) : proportion of attributes taken from parent1 (1-pc being prop. of attributes taken from parent2)
    Returns :
        offspring (pandas.array) : offspring of 2 previous parents/photos

    >>> mutation_pixels(*,*,*)
    ?

    """
    muted_parents = parents
    for j in range(len(parents)):
        for i in range(parents[0].size) :
            r = random.random()
            if r < pm :
                muted_parents[j][i] = random.randint(0, 255)
    return muted_parents

def mutation_attributes(offspring,pm):
    """
    Function that mutates a population of parents and creates a certain number of offsprings by mutating each pixel with a certain probability pm

    Args :
        offspring (pandas.array) : offspring getting the mutation
        pm (int) : proportion of attributes that will be mutated (multiply by -1 to get the opposite)
    Returns :
        offspring (pandas.array) : offspring of 2 previous parents/photos

    >>> crossover(*,*,*)
    ?

    """
    muted_offspring = offspring
    for i in range(offspring.shape[1]) :
        r = random.random()
        if r < pm :
            muted_offspring.iloc[0,i] = offspring.iloc[0,i] * (-1)
    return muted_offspring

#################
#TESTS UNITAIRES#
#################

if __name__ == "__main__" :
    import doctest
    doctest.testmod(verbose = True)