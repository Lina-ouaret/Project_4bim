import numpy as np
import pandas as pd
import random
import common_functions as cf
from itertools import permutations

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
        pc (int) : proportion of attributes taken from parent1 (1-pc being prop. of attributes taken from parent2)
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
    p_combinations = list(permutations(index_parents,2))
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
        parents(list(list)) : list of arrays representing the reduced pixel matrix of the parents we will use for the

        pc (int) : proportion of attributes taken from parent1 (1-pc being prop. of attributes taken from parent2)
    Returns :
        offspring(list(list)) : offspring of 2 previous parents/photos

    >>> encoded_imgs_test = np.load('encoded_imgs_test.npy')
    >>> random.seed(4)
    >>> new_parents = mutation_pixels(encoded_imgs_test,0.5)
    >>> print(new_parents[0][:10])
    [ 52.   0.  46. 205.   0.  30. 184.  88.   0.  13.]

    >>> encoded_imgs_test.shape == new_parents.shape
    True

    """
    muted_parents = parents
    for j in range(len(parents)):
        for i in range(len(parents[0])) :
            r = random.random()
            if r < pm :
                muted_parents[j][i] = round(random.uniform(0, 7),2)
    return muted_parents

def mutation_attributes(offspring,pm):
    """
    Function that mutates a population of parents and creates a certain number of offsprings by mutating each pixel with a certain probability pm

    Args :
        offspring (pandas.array) : offspring getting the mutation
        pm (int) : proportion of attributes that will be mutated (multiply by -1 to get the opposite)
    Returns :
        offspring (pandas.array) : offspring of 2 previous parents/photos


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
