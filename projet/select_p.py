# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from shutil import copyfile
from shutil import rmtree
import os
import numpy as np
import background
import keras
import random

import sys

import algo_genetique as ag
import common_functions as cf
import neural_network_function as nn

import matplotlib.pyplot as plt  # plotting routines
from keras.models import Model  # Model type to be used
from keras.layers.core import Dense, Dropout, Activation  # Types of layers to be used in our model
from keras.utils import np_utils  # NumPy related tools
import tensorflow as tf
import pandas as pd

import os
import glob

choose = [0,0,0]

class Ui_MainWindow(object):
    switch_window = QtCore.pyqtSignal() #Convert to suspect selection page2 method

    def setupUi(self, MainWindow):
        """
        Label, button position, size setting

        Args :
            MainWindow : principal window displaying the program
        """
        global choose
        choose = [0,0,0]
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 600)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{background-image: url(:/background/background/grey.jpeg)}");
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(210, 40, 381, 41))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 70, 630, 350))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.skin_color = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.skin_color.setEnabled(False)
        self.skin_color.setMaximumSize(QtCore.QSize(16777215, 30))
        self.skin_color.setObjectName("skin_color")
        self.verticalLayout.addWidget(self.skin_color)
        self.Straight_Hair_T = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Straight_Hair_T.setObjectName("Straight_Hair_T")
        self.verticalLayout.addWidget(self.Straight_Hair_T)
        self.Straight_Hair_F = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Straight_Hair_F.setMaximumSize(QtCore.QSize(16777215, 32))
        self.Straight_Hair_F.setObjectName("Straight_Hair_F")
        self.verticalLayout.addWidget(self.Straight_Hair_F)
        self.Straight_Hair_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Straight_Hair_0.setMaximumSize(QtCore.QSize(16777215, 32))
        self.Straight_Hair_0.setObjectName("Straight_Hair_0")
        self.verticalLayout.addWidget(self.Straight_Hair_0)
        self.Ph_age = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ph_age.setEnabled(True)
        self.Ph_age.setMaximumSize(QtCore.QSize(16777215, 200))
        self.Ph_age.setText("")
        self.Ph_age.setPixmap(QtGui.QPixmap("selectionImage/hairstyle.png"))
        self.Ph_age.setObjectName("Ph_age")
        self.verticalLayout.addWidget(self.Ph_age)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.skin_color_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.skin_color_4.setEnabled(False)
        self.skin_color_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.skin_color_4.setObjectName("skin_color_4")
        self.verticalLayout_2.addWidget(self.skin_color_4)
        self.young_T = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.young_T.setMinimumSize(QtCore.QSize(0, 30))
        self.young_T.setObjectName("young_T")
        self.verticalLayout_2.addWidget(self.young_T)
        self.young_F = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.young_F.setMinimumSize(QtCore.QSize(0, 30))
        self.young_F.setObjectName("young_F")
        self.verticalLayout_2.addWidget(self.young_F)
        self.young_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.young_0.setMaximumSize(QtCore.QSize(16777215, 32))
        self.young_0.setObjectName("young_0")
        self.verticalLayout_2.addWidget(self.young_0)
        self.Ph_skin = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ph_skin.setText("")
        self.Ph_skin.setPixmap(QtGui.QPixmap("selectionImage/age.png"))
        self.Ph_skin.setObjectName("Ph_skin")
        self.verticalLayout_2.addWidget(self.Ph_skin)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gender = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.gender.setEnabled(False)
        self.gender.setMinimumSize(QtCore.QSize(0, 30))
        self.gender.setMaximumSize(QtCore.QSize(16777215, 30))
        self.gender.setObjectName("gender")
        self.verticalLayout_4.addWidget(self.gender)
        self.male_T = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.male_T.setObjectName("male_T")
        self.verticalLayout_4.addWidget(self.male_T)
        self.male_F = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.male_F.setObjectName("male_F")
        self.verticalLayout_4.addWidget(self.male_F)
        self.male_0 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.male_0.setMaximumSize(QtCore.QSize(16777215, 32))
        self.male_0.setObjectName("male_0")
        self.verticalLayout_4.addWidget(self.male_0)
        self.Ph_gender = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ph_gender.setText("")
        self.Ph_gender.setPixmap(QtGui.QPixmap("selectionImage/gender.png"))
        self.Ph_gender.setObjectName("Ph_gender")
        self.verticalLayout_4.addWidget(self.Ph_gender)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(500, 470, 129, 32))
        self.next.setMinimumSize(QtCore.QSize(0, 30))
        self.next.setObjectName("next")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        with open('select.txt', 'w') as file:
            file.write('{}')

        #Connect the buttons to the corresponding functions
        self.Straight_Hair_T.clicked.connect(self.press)
        self.Straight_Hair_F.clicked.connect(self.press)
        self.young_T.clicked.connect(self.press)
        self.young_F.clicked.connect(self.press)
        self.male_T.clicked.connect(self.press)
        self.male_F.clicked.connect(self.press)
        self.male_0.clicked.connect(self.press)
        self.young_0.clicked.connect(self.press)
        self.Straight_Hair_0.clicked.connect(self.press)
        self.next.clicked.connect(self.press3)

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
        self.label.setText(_translate("MainWindow", "Please select an initial set of physical traits for the search: \n"
                                                    ""))
        self.skin_color.setText(_translate("MainWindow", "hair style"))
        self.Straight_Hair_T.setText(_translate("MainWindow", "stright"))
        self.Straight_Hair_F.setText(_translate("MainWindow", "wavy"))
        self.Straight_Hair_0.setText(_translate("MainWindow", "no clue"))
        self.skin_color_4.setText(_translate("MainWindow", "age"))
        self.young_T.setText(_translate("MainWindow", "young"))
        self.young_F.setText(_translate("MainWindow", "old"))
        self.young_0.setText(_translate("MainWindow", "no clue"))
        self.gender.setText(_translate("MainWindow", "gender"))
        self.next.setText(_translate("MainWindow", "next"))
        self.gender.setText(_translate("MainWindow", "gender"))
        self.male_T.setText(_translate("MainWindow", "male"))
        self.male_F.setText(_translate("MainWindow", "female"))
        self.male_0.setText(_translate("MainWindow", "no clue"))

    def press(self):
        """
        Get the name of the button and write the corresponding function in select.txt
        """
        button_name = QtWidgets.QWidget().sender().objectName()
        l = len(button_name) - 2
        global choose
        with open('select.txt', 'r') as file:
            rd = file.read()
        dict1 = eval(rd)
        dict2 = {"Straight_Hair":0,"young":1,"male":2}
        if button_name[-1] == "T":
            dict1.update({button_name[:l]: 1})
            choose[dict2[button_name[:l]]]=1
        elif button_name[-1] == "F":
            dict1.update({button_name[:l]: -1})
            choose[dict2[button_name[:l]]]=1
        elif button_name[-1] == "0":
            choose[dict2[button_name[:l]]]=1
            if button_name[:l] in dict1:
                del dict1[button_name[:l]]

        with open('select.txt', 'w') as file:
            file.write(str(dict1))



    def press3(self):
        """
        Display the selection results and initialise the choice and jump to the suspect picture selection page1
        """
        global choose
        if not(choose==[1,1,1]):
            QtWidgets.QMessageBox.critical(self, "error", "you havn't choose all of 3 charateristics" )
            choose=[0,0,0]
        else:
            with open('select.txt', 'r') as file:
                rd = file.read()
            dict1 = eval(rd)
            lis = []
            for key in dict1.keys():
                if key == "Straight_Hair":
                    if dict1[key] == 1:
                        lis.append("stright hair ")
                    elif dict1[key] == -1:
                        lis.append("wavy hair ")
                elif key == "young":
                    if dict1[key] == 1:
                        lis.append("young ")
                    elif dict1[key] == -1:
                        lis.append("old ")
                elif key == "male":
                    if dict1[key] == 1:
                        lis.append("man.")
                    elif dict1[key] == -1:
                        lis.append("woman.")
            txt = "the suspspect is a "
            sex = ""
            for i in lis:
                if i == "man." or i == "woman.":
                    sex+= i
                else:
                    txt+=i
            txt += (sex)

            if ("man" in txt)==False:
                txt+="guy."
            else:




            QtWidgets.QMessageBox.critical(self, "your choice", txt)
            if os.path.exists('choice/'):
                rmtree('choice/')
                os.mkdir('choice/')
            #Clusters:
            att_cluster1 = {"male":-1,"Straight_Hair":-1,"young":-1}
            att_cluster2= {"male":-1,"Straight_Hair":-1,"young":1}
            att_cluster3 = {"male":-1,"Straight_Hair":1,"young":1}
            att_cluster4 = {"male":1,"Straight_Hair":1,"young":-1}
            att_cluster5 = {"male":1,"Straight_Hair":-1,"young":1}
            att_cluster6 = {"male":1,"Straight_Hair":-1,"young":-1}
            att_cluster7 = {"male":-1,"Straight_Hair":1,"young":-1}
            att_cluster8 = {"male":1,"Straight_Hair":1,"young":1}
            ## clusters with 1 nul attribut
            att_cluster9 = {"Straight_Hair":1,"young":1}
            att_cluster10 = {"Straight_Hair":-1,"young":-1}
            att_cluster11 = {"Straight_Hair":1,"young":-1}
            att_cluster12 = {"Straight_Hair":-1,"young":1}
            att_cluster13 = {"male":1,"young":1}
            att_cluster14 = {"male":-1,"young":-1}
            att_cluster15 = {"male":1,"young":-1}
            att_cluster16 = {"male":-1,"young":1}
            att_cluster17 = {"male":1,"Straight_Hair":1}
            att_cluster18 = {"male":-1,"Straight_Hair":-1}
            att_cluster19 = {"male":-1,"Straight_Hair":1}
            att_cluster20 = {"male":1,"Straight_Hair":-1}
            ## clusters with 2 nul attributs
            att_cluster21 = {"Straight_Hair":1}
            att_cluster22 = {"Straight_Hair":-1}
            att_cluster23 = {"young":-1}
            att_cluster24 = {"young":1}
            att_cluster25 = {"male":1}
            att_cluster26 = {"male":-1}
            ## clusters without attributs
            att_cluster27 = {}

            # Catch specific traits in a dictionnaire
            dict = eval(rd)

            # Proba to choose a cluster when 1 trait missing
            proba=np.random.random()

            # Proba to choose a cluster when 2 traits missing
            list_proba = list(range(0, 4, 1))
            proba_ = random.sample(list_proba, 1)[0]

            # Proba to choose a cluster when all traits missing
            list_proba_bis = list(range(1, 9, 1))
            proba_bis = random.sample(list_proba_bis, 1)[0]

            # cluster without attributs
            if dict == att_cluster27 :
                encoded_imgs = np.load('clusters/encoded_imgs'+str(proba_bis)+'.npy')
                decoder_ = keras.models.load_model('decoders/decoder'+str(proba_bis)+'.h5')

            ## dict
            if dict == att_cluster1 :
                encoded_imgs = np.load('clusters/encoded_imgs1.npy')
                decoder_ = keras.models.load_model('decoders/decoder1.h5')
            elif dict == att_cluster2 :
                encoded_imgs = np.load('clusters/encoded_imgs2.npy')
                decoder_ = keras.models.load_model('decoders/decoder2.h5')
            elif dict == att_cluster3 :
                encoded_imgs = np.load('clusters/encoded_imgs3.npy')
                decoder_ = keras.models.load_model('decoders/decoder3.h5')
            elif dict == att_cluster4 :
                encoded_imgs = np.load('clusters/encoded_imgs4.npy')
                decoder_ = keras.models.load_model('decoders/decoder4.h5')
            elif dict == att_cluster5 :
                encoded_imgs = np.load('clusters/encoded_imgs5.npy')
                decoder_ = keras.models.load_model('decoders/decoder5.h5')
            elif dict == att_cluster6 :
                encoded_imgs = np.load('clusters/encoded_imgs6.npy')
                decoder_ = keras.models.load_model('decoders/decoder6.h5')
            elif dict == att_cluster7 :
                encoded_imgs = np.load('clusters/encoded_imgs7.npy')
                decoder_ = keras.models.load_model('decoders/decoder7.h5')
            elif dict == att_cluster8 :
                encoded_imgs = np.load('clusters/encoded_imgs8.npy')
                decoder_ = keras.models.load_model('decoders/decoder8.h5')

            # cluster avec 2 attibuts nuls
            elif dict == att_cluster21 :
                if proba_ == 0 : dict.update(att_cluster9)
                elif proba_ == 1 : dict.update(att_cluster11)
                elif proba_ == 2 : dict.update(att_cluster17)
                elif proba_ == 3 : dict.update(att_cluster19)


            elif dict == att_cluster22 :
                if proba_ == 0 : dict.update(att_cluster10)
                elif proba_ == 1 : dict.update(att_cluster12)
                elif proba_ == 2 : dict.update(att_cluster18)
                elif proba_ == 3 : dict.update(att_cluster20)


            elif dict == att_cluster23 :
                if proba_ == 0 : dict.update(att_cluster10)
                elif proba_ == 1 : dict.update(att_cluster11)
                elif proba_ == 2 : dict.update(att_cluster14)
                elif proba_ == 3 : dict.update(att_cluster15)


            elif dict == att_cluster24 :
                if proba_ == 0 : dict.update(att_cluster9)
                elif proba_ == 1 : dict.update(att_cluster12)
                elif proba_ == 2 : dict.update(att_cluster13)
                elif proba_ == 3 : dict.update(att_cluster16)


            elif dict == att_cluster25 :
                if proba_ == 0 : dict.update(att_cluster13)
                elif proba_ == 1 : dict.update(att_cluster15)
                elif proba_ == 2 : dict.update(att_cluster17)
                elif proba_ == 3 : dict.update(att_cluster20)


            elif dict == att_cluster26 :
                if proba_ == 0 : dict.update(att_cluster14)
                elif proba_ == 1 : dict.update(att_cluster16)
                elif proba_ == 2 : dict.update(att_cluster18)
                elif proba_ == 3 : dict.update(att_cluster19)




            # cluster with nul attribut
            if dict == att_cluster9 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs8.npy')
                    decoder_ = keras.models.load_model('decoders/decoder8.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs3.npy')
                    decoder_ = keras.models.load_model('decoders/decoder3.h5')
            elif dict == att_cluster10 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs1.npy')
                    decoder_ = keras.models.load_model('decoders/decoder1.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs6.npy')
                    decoder_ = keras.models.load_model('decoders/decoder6.h5')
            elif dict == att_cluster11 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs4.npy')
                    decoder_ = keras.models.load_model('decoders/decoder4.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs7.npy')
                    decoder_ = keras.models.load_model('decoders/decoder7.h5')
            elif dict == att_cluster12 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs2.npy')
                    decoder_ = keras.models.load_model('decoders/decoder2.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs5.npy')
                    decoder_ = keras.models.load_model('decoders/decoder5.h5')
            elif dict == att_cluster13 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs5.npy')
                    decoder_ = keras.models.load_model('decoders/decoder5.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs8.npy')
                    decoder_ = keras.models.load_model('decoders/decoder8.h5')
            elif dict == att_cluster14 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs5.npy')
                    decoder_ = keras.models.load_model('decoders/decoder5.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs1.npy')
                    decoder_ = keras.models.load_model('decoders/decoder1.h5')
            elif dict == att_cluster15 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs4.npy')
                    decoder_ = keras.models.load_model('decoders/decoder4.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs7.npy')
                    decoder_ = keras.models.load_model('decoders/decoder7.h5')
            elif dict == att_cluster16 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs5.npy')
                    decoder_ = keras.models.load_model('decoders/decoder5.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs2.npy')
                    decoder_ = keras.models.load_model('decoders/decoder2.h5')
            elif dict == att_cluster17 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs4.npy')
                    decoder_ = keras.models.load_model('decoders/decoder4.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs8.npy')
                    decoder_ = keras.models.load_model('decoders/decoder8.h5')
            elif dict == att_cluster18 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs1.npy')
                    decoder_ = keras.models.load_model('decoders/decoder1.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs2.npy')
                    decoder_ = keras.models.load_model('decoders/decoder2.h5')
            elif dict == att_cluster19 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs7.npy')
                    decoder_ = keras.models.load_model('decoders/decoder7.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs3.npy')
                    decoder_ = keras.models.load_model('decoders/decoder3.h5')
            elif dict == att_cluster20 :
                if proba >= 0.5 :
                    encoded_imgs=np.load('clusters/encoded_imgs5.npy')
                    decoder_ = keras.models.load_model('decoders/decoder5.h5')
                else :
                    encoded_imgs=np.load('clusters/encoded_imgs6.npy')
                    decoder_ = keras.models.load_model('decoders/decoder6.h5')


            # Save model and cluster chosen
            np.save('clusters/encoded', encoded_imgs)
            decoder_.save('decoders/decoder.h5')

            # Random selection of first photo
            mylist = list(range(0, 700, 1))
            n = 9
            index = random.sample(mylist, n)

            # Pin up pictures
            decoded_imgs = decoder_.predict(encoded_imgs)
            decoded = [None] * n
            encoded = [None] * n
            for i in range(n):
                decoded[i] = decoded_imgs[index[i]]
                encoded[i] = encoded_imgs[index[i]]
            nn.save_reconstruction(n, decoded)  # in /son

            # Save first random pictures
            np.save('clusters/encoded_first', encoded)




            self.switch_window.emit()
