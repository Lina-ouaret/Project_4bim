import algo_genetique as ag
import common_functions as cf
import neural_network_function as nn
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

if __name__ == "__main__" :

    # load model
    decoder_=keras.models.load_model('decoder.h5')

    # load encoded_imgs
    encoded_imgs = np.load('encoded_imgs.npy')
    decoded_imgs = np.load('decoded_imgs.npy')

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

    # Choix de l'utilisateur : PUJIAN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    new_index=random.sample(index, 4)
    encoded_choix=[None]*4
    for i in range(4):
        encoded_choix[i]=encoded_imgs[new_index[i]]

    # Algo genetique
    encoded_ag = ag.crossover_pixels(encoded_choix, 0.3)
    #print(len(encoded_ag))
    decoded_ag = decoder_.predict(encoded_ag)
    nn.save_reconstruction(8, decoded_ag)

    
