# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suspect1.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from shutil import copyfile
from shutil import rmtree
import os
from PyQt5 import QtWidgets, QtCore
import sys
from shutil import copyfile

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


class Ui_MainWindow(object):
    switch_window = QtCore.pyqtSignal()  # Convert to suspect selection page2 method

    def setupUi2(self, MainWindow):
        """
        Label, button position, size setting， show photos

        Args :
            MainWindow : principal window displaying the program
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(370, 10, 321, 41))
        self.label1.setObjectName("label1")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setEnabled(True)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(360, 60, 414, 523))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.suspect6 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect6.setEnabled(True)
        self.suspect6.setObjectName("suspect6")
        self.gridLayout_4.addWidget(self.suspect6, 3, 2, 1, 1)
        self.suspect7 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect7.setEnabled(True)
        self.suspect7.setObjectName("suspect7")
        self.gridLayout_4.addWidget(self.suspect7, 5, 0, 1, 1)
        self.suspect4 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect4.setEnabled(True)
        self.suspect4.setObjectName("suspect4")
        self.gridLayout_4.addWidget(self.suspect4, 3, 0, 1, 1)
        self.photo_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_5.setEnabled(True)
        self.photo_5.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_5.setText("")
        self.photo_5.setObjectName("photo_5")
        self.gridLayout_4.addWidget(self.photo_5, 2, 1, 1, 1)
        self.suspect8 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect8.setEnabled(True)
        self.suspect8.setObjectName("suspect8")
        self.gridLayout_4.addWidget(self.suspect8, 5, 1, 1, 1)
        self.photo_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_6.setEnabled(True)
        self.photo_6.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_6.setText("")
        self.photo_6.setObjectName("photo_6")
        self.gridLayout_4.addWidget(self.photo_6, 2, 2, 1, 1)
        self.photo_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_4.setEnabled(True)
        self.photo_4.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_4.setText("")
        self.photo_4.setObjectName("photo_4")
        self.gridLayout_4.addWidget(self.photo_4, 2, 0, 1, 1)
        self.suspect3 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect3.setEnabled(True)
        self.suspect3.setObjectName("suspect3")
        self.gridLayout_4.addWidget(self.suspect3, 1, 2, 1, 1)
        self.suspect9 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect9.setEnabled(True)
        self.suspect9.setObjectName("suspect9")
        self.gridLayout_4.addWidget(self.suspect9, 5, 2, 1, 1)
        self.suspect5 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect5.setEnabled(True)
        self.suspect5.setObjectName("suspect5")
        self.gridLayout_4.addWidget(self.suspect5, 3, 1, 1, 1)
        self.suspect2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect2.setEnabled(True)
        self.suspect2.setObjectName("suspect2")
        self.gridLayout_4.addWidget(self.suspect2, 1, 1, 1, 1)
        self.suspect1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect1.setEnabled(True)
        self.suspect1.setObjectName("suspect1")
        self.gridLayout_4.addWidget(self.suspect1, 1, 0, 1, 1)
        self.photo_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_7.setEnabled(True)
        self.photo_7.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_7.setText("")
        self.photo_7.setObjectName("photo_7")
        self.gridLayout_4.addWidget(self.photo_7, 4, 0, 1, 1)
        self.photo_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_8.setEnabled(True)
        self.photo_8.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_8.setText("")
        self.photo_8.setObjectName("photo_8")
        self.gridLayout_4.addWidget(self.photo_8, 4, 1, 1, 1)
        self.photo_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_9.setEnabled(True)
        self.photo_9.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_9.setText("")
        self.photo_9.setObjectName("photo_9")
        self.gridLayout_4.addWidget(self.photo_9, 4, 2, 1, 1)
        self.photo_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_1.setEnabled(True)
        self.photo_1.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_1.setText("")
        self.photo_1.setObjectName("photo_1")
        self.gridLayout_4.addWidget(self.photo_1, 0, 0, 1, 1)
        self.photo_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_2.setEnabled(True)
        self.photo_2.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_2.setText("")
        self.photo_2.setObjectName("photo_2")
        self.gridLayout_4.addWidget(self.photo_2, 0, 1, 1, 1)
        self.photo_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_3.setEnabled(True)
        self.photo_3.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_3.setText("")
        self.photo_3.setObjectName("photo_3")
        self.gridLayout_4.addWidget(self.photo_3, 0, 2, 1, 1)
        self.suspect1_3 = QtWidgets.QPushButton(self.centralwidget)
        self.suspect1_3.setGeometry(QtCore.QRect(520, 600, 100, 32))
        self.suspect1_3.setObjectName("suspect1_3")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 50, 268, 268))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.photo_c2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_c2.setEnabled(True)
        self.photo_c2.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_c2.setText("")
        self.photo_c2.setObjectName("photo_c2")
        self.gridLayout_2.addWidget(self.photo_c2, 0, 1, 1, 1)
        self.photo_c1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_c1.setEnabled(True)
        self.photo_c1.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_c1.setText("")
        self.photo_c1.setObjectName("photo_c1")
        self.gridLayout_2.addWidget(self.photo_c1, 0, 0, 1, 1)
        self.photo_c3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_c3.setEnabled(True)
        self.photo_c3.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_c3.setText("")
        self.photo_c3.setObjectName("photo_c3")
        self.gridLayout_2.addWidget(self.photo_c3, 1, 0, 1, 1)
        self.photo_c4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_c4.setEnabled(True)
        self.photo_c4.setMaximumSize(QtCore.QSize(128, 128))
        self.photo_c4.setText("")
        self.photo_c4.setObjectName("photo_c4")
        self.gridLayout_2.addWidget(self.photo_c4, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 10, 91, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # son frame photo display
        self.photo_1.setPixmap(QtGui.QPixmap("son/1.png"))
        self.photo_2.setPixmap(QtGui.QPixmap("son/2.png"))
        self.photo_3.setPixmap(QtGui.QPixmap("son/3.png"))
        self.photo_4.setPixmap(QtGui.QPixmap("son/4.png"))
        self.photo_5.setPixmap(QtGui.QPixmap("son/5.png"))
        self.photo_6.setPixmap(QtGui.QPixmap("son/6.png"))
        self.photo_7.setPixmap(QtGui.QPixmap("son/7.png"))
        self.photo_8.setPixmap(QtGui.QPixmap("son/8.png"))
        self.photo_9.setPixmap(QtGui.QPixmap("son/9.png"))
        #MainWindow : principal window displaying the program
        # Connect the buttons to the corresponding functions
        self.suspect1.clicked.connect(self.saveChoice)
        self.suspect2.clicked.connect(self.saveChoice)
        self.suspect3.clicked.connect(self.saveChoice)
        self.suspect4.clicked.connect(self.saveChoice)
        self.suspect5.clicked.connect(self.saveChoice)
        self.suspect6.clicked.connect(self.saveChoice)
        self.suspect7.clicked.connect(self.saveChoice)
        self.suspect8.clicked.connect(self.saveChoice)
        self.suspect9.clicked.connect(self.saveChoice)
        self.suspect1_3.clicked.connect(self.swich)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        """
        Text display on buttons and labels

        Args :
            MainWindow : principal window displaying the program
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "Please select 4 images that look most like the criminal'"))
        self.suspect5.setText(_translate("MainWindow", "suspect5"))
        self.suspect6.setText(_translate("MainWindow", "suspect6"))
        self.suspect9.setText(_translate("MainWindow", "suspect9"))
        self.suspect7.setText(_translate("MainWindow", "suspect7"))
        self.suspect3.setText(_translate("MainWindow", "suspect3"))
        self.suspect2.setText(_translate("MainWindow", "suspect2"))
        self.suspect4.setText(_translate("MainWindow", "suspect4"))
        self.suspect8.setText(_translate("MainWindow", "suspect8"))
        self.suspect1.setText(_translate("MainWindow", "suspect1"))
        self.suspect1_3.setText(_translate("MainWindow", "next"))
        self.label.setText(_translate("MainWindow", "your choice"))

    def saveChoice(self):
        """
        Put the selected photos into the choices folder and show in the choices box that the selection cannot be greater
        than 4, clear the selection if it is greater.
        """
        button_name = QtWidgets.QWidget().sender().objectName()
        source = "son/" + button_name[-1] + ".png"
        destination = "choice/" + button_name[-1] + ".png"
        copyfile(source, destination)
        files = os.listdir("choice/")
        num_png = len(files)
        if num_png == 1:
            QtWidgets.QApplication.processEvents()
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))
        elif num_png == 2:
            QtWidgets.QApplication.processEvents()
            self.photo_c2.setPixmap(QtGui.QPixmap(destination))
        elif num_png == 3:
            QtWidgets.QApplication.processEvents()
            self.photo_c3.setPixmap(QtGui.QPixmap(destination))
        elif num_png == 4:
            QtWidgets.QApplication.processEvents()
            self.photo_c4.setPixmap(QtGui.QPixmap(destination))
        elif num_png >= 5:
            QtWidgets.QApplication.processEvents()
            rmtree('choice/')
            os.mkdir('choice/')
            self.photo_c2.setPixmap(QtGui.QPixmap())
            self.photo_c3.setPixmap(QtGui.QPixmap())
            self.photo_c4.setPixmap(QtGui.QPixmap())
            self.photo_c1.setPixmap(QtGui.QPixmap())
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))

    def swich(self):
        """
        If the selection is 4, skip to the next page and generate the offspring photo by AI
        """
        files = os.listdir("choice/")
        print(files)
        num_png = len(files)
        # load model
        decoder_ = keras.models.load_model('decoders/decoder.h5')
        encoded_img = np.load('clusters/encoded_first.npy')
        if num_png == 4:
            # Choix de l'utilisateur :
            files = os.listdir("choice/")
            num_png = len(files)
            num_p = []
            for i in files:
                print(i[0])
                num_p.append(int(i[0]) - 1)
            print(num_p)

            # new_index=random.sample(index, n)
            n = 4
            encoded_choix = [None] * n
            for i in range(n):
                encoded_choix[i] = encoded_img[num_p[i]]

            # Algo genetique1 : crossover
            # print(type(encoded_choix))
            # print(type(encoded_choix[0]))
            np.save('encoded_choix', encoded_choix)
            encoded_ag = ag.crossover_pixels(encoded_choix, 1)
            decoded_ag = decoder_.predict(encoded_ag)
            nn.save_reconstruction(12, decoded_ag)
            np.save('encoded_choix', encoded_choix)
            np.save('encoded_ag', encoded_ag)
            files = os.listdir("choice/")

            rmtree('father/')
            os.mkdir('father/')
            for i in files:
                fil = os.listdir("father/")
                source = "choice/" + i
                destination = "father/" + str(len(fil) + 1) + ".png"
                copyfile(source, destination)
            self.switch_window.emit()

        #when selected photos is not 4, Report an error
        else:
            QtWidgets.QMessageBox.critical(self, "error", "please select 4 photos")
            rmtree('choice/')
            os.mkdir('choice/')
            QtWidgets.QApplication.processEvents()
            self.photo_c1.setPixmap(QtGui.QPixmap())
            self.photo_c2.setPixmap(QtGui.QPixmap())
            self.photo_c3.setPixmap(QtGui.QPixmap())
            self.photo_c4.setPixmap(QtGui.QPixmap())
