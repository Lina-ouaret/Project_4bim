import numpy as np
import pandas as pd
import random
import common_functions as cf
from itertools import permutations
from itertools import combinations

def randomly_choose_photos(df,n):
    """
    Function that randomly chooses n photos from the current reduced matrix, in order to display them so one or two can be selected by the witness

    Args :
        number_photos (int) : number of photo to be selected
        df (pandas.array) : database from where the photo are selected
    Returns :
        photos_names (list(str)) :  list of photo names looking like XXXXXX.png

    >>> df_test = cf.convert_attributes_into_pandas("test_attributes.csv")
    >>> fixed_attributes_test = {"Male":1,"Young":-1}
    >>> df_test_list = cf.matrix_reduction(df_test,fixed_attributes_test)
    >>> random.seed(2)
    >>> randomly_choose_photos(df_test_list,6)
    [78, 14, 20, 68, 50, 29]

    >>> random.seed(3)
    >>> len(randomly_choose_photos(df_test_list,10))
    10

    """
    return random.sample(df,n)

def crossover_pixels(parents,pc):
    """
    Function that crosses the vectors of pixels from n parents to make an offspring.
    For all possible combinations of two parents, it creates an offspring taking a proportion pc of the pixels from one parent and 1-pc from the other
    and another one taking the inverse proportions.

    Args :
        parents (list(list)) : list of lists representing the reduced pixel matrix of the parents we will use for the crossover
        pc (float) : proportion of attributes taken from parent1 (1-pc being prop. of attributes taken from parent2)
    Returns :
        offsprings (list(lists)) : offspring of 2 previous parents/photos

    >>> encoded_imgs_test = np.load('encoded_imgs_test.npy')
    >>> random.seed(1)
    >>> offsprings = crossover_pixels(encoded_imgs_test,0.3)
    >>> offsprings[0][:10]
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.843132019042969, 2.2844715118408203]

    >>> random.seed(5)
    >>> offsprings2 = crossover_pixels(encoded_imgs_test,0.5)
    >>> offsprings2[0][:10]
    [0.358284056186676, 0.0, 2.050474166870117, 0.0, 0.0, 0.5806276202201843, 0.0, 0.23518957197666168, 0.0, 0.0]

    """
    index_parents = list(range(0,len(parents)))
    p_combinations = list(combinations(index_parents,2))
    offsprings = []
    print("début",len(parents[0]))
    for i in range(len(p_combinations)):
        parent_1 = (parents[p_combinations[i][0]]).tolist()
        parent_2 = (parents[p_combinations[i][1]]).tolist()
        offsprings_temp=[]
        for j in range(len(parent_1)) :
            offsprings_temp.append((parent_1[j]+parent_2[j])/2)
        offsprings.append(offsprings_temp)
        print("taille enfant :",len(offsprings_temp))
    while(len(offsprings))<13:
        offsprings.append(offsprings[2])
    return offsprings

def mutation_pixels(parent,pm):
    """
    Function that mutates one parent by adding a fixed value to randoms elements of the list
    representing the encoded photo.

    Args :
        parent (np.array) : array representing the encoded photo, has to mutate
        pm (float) : chances that one element of the np array (parent) gets the mutation
    Returns :
        muted_parent (np.array) : same array but with mutation, ready to be decoded and displayed

    >>> encoded_imgs_test = np.load('encoded_imgs_test.npy')
    >>> random.seed(4)
    >>> new_parents = mutation_pixels(encoded_imgs_test,0.5)
    >>> print(new_parents[0][:10])
    [ 52.   0.  46. 205.   0.  30. 184.  88.   0.  13.]

    >>> encoded_imgs_test.shape == new_parents.shape
    True

    """
    muted_parent = parent
    for i in range(len(parent)):
        r = random.random()
        if r < pm :
            #print(muted_parent)
            muted_parent[i] = muted_parent[i]+ 2.5
    return muted_parent

#################
#TESTS UNITAIRES#
#################

if __name__ == "__main__" :
    import doctest
    doctest.testmod(verbose = True)
