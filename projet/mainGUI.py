from PyQt5 import QtWidgets, QtCore
import sys
from shutil import copyfile

from select_p import Ui_MainWindow as Ui1
from suspect_p1 import Ui_MainWindow as Ui2
from suspect_p2 import Ui_MainWindow as Ui3
from lastphoto import Ui_MainWindow as Ui4

import algo_genetique as ag
import common_functions as cf
import neural_network_function as nn

import numpy as np
import random
import matplotlib.pyplot as plt  # plotting routines
import keras
from keras.models import Model  # Model type to be used
from keras.layers.core import Dense, Dropout, Activation  # Types of layers to be used in our model
from keras.utils import np_utils  # NumPy related tools
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import pandas as pd
from PIL.Image import *
import os
import glob

#Suspect screening page initialisation
class mywindow(QtWidgets.QMainWindow, Ui1):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

#Suspect picture selection page 1 initialisation
class mywindow2(QtWidgets.QMainWindow, Ui2):
    def __init__(self):
        super(mywindow2, self).__init__()
        self.setupUi2(self)

#Suspect picture selection page 2 initialisation
class mywindow3(QtWidgets.QMainWindow, Ui3):
    def __init__(self):
        super(mywindow3, self).__init__()
        self.setupUi(self)

#Return suspect photo page initialization
class mywindow4(QtWidgets.QMainWindow, Ui4):
    def __init__(self):
        super(mywindow4, self).__init__()
        self.setupUi(self)

#Multi-page dedicated page system

class Controller():
    def __init__(self):
        pass

    def show_select(self):
        self.login = mywindow()
        self.login.switch_window.connect(self.show_main)
        # self.window_three = mywindow4()
        if cycle >=1:
            self.window_three.close()
        self.login.show()

    def show_main(self):
        self.window = mywindow2()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self):
        self.window_two = mywindow3()
        self.window.close()
        if cycle >=1:
            self.window_three.close()
        self.window.switch_window.connect(self.show_window_two)
        self.window_two.switch_window2.connect(self.show_window_lastphoto)
        self.window_two.show()

    def show_window_lastphoto(self):
        self.window_three = mywindow4()
        self.window_two.close()
        self.window_three.switch_window.connect(self.show_select)
        self.window_three.switch_window2.connect(self.show_window_two)
        global cycle
        cycle +=1
        print('cycle = '+str(cycle))
        self.window_three.show()


if __name__ == "__main__":

    # load model
    decoder_ = keras.models.load_model('decoders/decoder1.h5')
    # decoder_ = keras.Sequential()

    # load encoded_imgs
    encoded_imgs = np.load('clusters/encoded_imgs1.npy')
    #decoded_imgs = np.load('clusters/decoded_imgs1.npy')
    # encoded_imgs.tolist()

    # # Upload photos
    # from sklearn.datasets import fetch_olivetti_faces  # Olivetti faces dataset
    #
    # dataset = fetch_olivetti_faces()
    # df = dataset["data"]
    # attribut = dataset["target"]

    # Reduction matrice
    # pas besoin pour olivetti*
    # cf.matrix_reduction(df, attributs)

    # Choix aléatoire des premières photos
    mylist = list(range(0, 500, 1))
    n = 9
    index = random.sample(mylist, n)
    # ag.randomly_choose_photos(index,n)

    # Afficher images
    decoded_imgs = decoder_.predict(encoded_imgs)
    decoded = [None] * n
    for i in range(n):
        decoded[i] = decoded_imgs[index[i]]
    nn.save_reconstruction(n, decoded)  # dans pictures_showed

    #Page initialisation
    cycle = 0
    app = QtWidgets.QApplication(sys.argv)
    main = QtWidgets.QWidget()
    latout = QtWidgets.QHBoxLayout()
    main.setLayout(latout)

    #Generate a multi-page selection system, initialise it and show it
    cycle = 0
    controller = Controller()
    controller.show_select()
    sys.exit(app.exec_())
