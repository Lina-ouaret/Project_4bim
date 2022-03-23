import algo_genetique as ag
import common_functions as cf
import neural_network_function as nn
import

import numpy as np
import random
import matplotlib.pyplot as plt      # plotting routines
import keras
from keras.models import Model       # Model type to be used
from keras.layers.core import Dense, Dropout, Activation # Types of layers to be used in our model
from keras.utils import np_utils                         # NumPy related tools
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from PIL.Image import *
import os
import glob

if __name__ == "__main__" :

    # load model
    decoder_=keras.models.load_model('decoder.h5')
    #decoder_ = keras.Sequential()

    # load encoded_imgs
    encoded_imgs = np.load('encoded_imgs.npy')
    decoded_imgs = np.load('decoded_imgs.npy')
    #encoded_imgs.tolist()

    # Upload photos
    from sklearn.datasets import fetch_olivetti_faces # Olivetti faces dataset
    dataset = fetch_olivetti_faces()
    df = dataset["data"]
    attribut = dataset["target"]

    # Reduction matrice
    # pas besoin pour olivetti*
    #cf.matrix_reduction(df, attributs)

    # Choix aléatoire des premières photos
    mylist = list(range(0,80,1))
    n=8
    index = random.sample(mylist, n)
    #ag.randomly_choose_photos(index,n)

    # Afficher images
    # decoded_imgs = decoder_.predict(encoded_imgs)
    decoded=[None]*n
    for i in range(n):
        decoded[i]=decoded_imgs[index[i]]

    nn.save_reconstruction(n, decoded) # dans pictures_showed






    # Suppression images dans répertoires pictures_showed
    py_files = glob.glob("show/img*.png")
    for py_file in py_files:
        os.remove(py_file)

    # Choix de l'utilisateur :
    files = os.listdir("choice/")  # 读入文件夹
    num_png = len(files)  # 统计文件夹中的文件个数
    num_p =[]
    for i in files:
        num_p.append(i[7]-1)

    # new_index=random.sample(index, n)
    # encoded_choix=[None]*n
    for i in range(n):
        encoded_choix[i]=encoded_imgs[num_p[i]]

    # Algo genetique1 : crossover
    print(type(encoded_choix))
    print(type(encoded_choix[0]))
    #np.save('encoded_choix', encoded_choix)
    encoded_ag = ag.crossover_pixels(encoded_choix, 0.3)
    decoded_ag = decoder_.predict(encoded_ag)
    nn.save_reconstruction(12, decoded_ag)

    # Choix de l'utilisateur2 : PUJIAN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    mylist = list(range(0,12,1))
    index = random.sample(mylist, 4)
    new_index=random.sample(index, 4)
    encoded_choix=[None]*4
    for i in range(4):
        encoded_choix[i]=np.array(encoded_ag[new_index[i]])

    # Algo genetique2 : crossover
    print(type(encoded_choix))
    print(type(encoded_choix[0]))
    encoded_ag = ag.crossover_pixels(encoded_choix, 0.3)
    print(type(encoded_ag[0]))
    decoded_ag = decoder_.predict(encoded_ag)
    #nn.save_reconstruction(12, decoded_ag)


    # Choix de l'utilisateur2 : PUJIAN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    new_index=random.sample(index, 4)
    encoded_choix=[None]*4
    for i in range(4):
        encoded_choix[i]=encoded_ag[new_index[i]]

    # Algo genetique : mutation
    encoded_ag = ag.mutation_pixels(encoded_choix, 0.3)

    print(type(encoded_ag[0]))
    decoded_ag = decoder_.predict(encoded_ag)
    #nn.save_reconstruction(4, decoded_ag)
