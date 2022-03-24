# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suspect2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from shutil import copyfile
from shutil import rmtree
import os
from PyQt5 import QtWidgets,QtCore
import sys
from shutil import copyfile

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
import glob


class Ui_MainWindow(object):
    switch_window = QtCore.pyqtSignal()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(280, 0, 411, 41))
        self.label1.setObjectName("label1")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(300, 50, 330, 439))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.photo_8 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_8.setText("")
        self.photo_8.setObjectName("photo_8")
        self.gridLayout_4.addWidget(self.photo_8, 4, 1, 1, 1)
        self.photo_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_2.setText("")
        self.photo_2.setObjectName("photo_2")
        self.gridLayout_4.addWidget(self.photo_2, 0, 1, 1, 1)
        self.suspect5 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect5.setObjectName("suspect5")
        self.gridLayout_4.addWidget(self.suspect5, 3, 1, 1, 1)
        self.suspect6 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect6.setObjectName("suspect6")
        self.gridLayout_4.addWidget(self.suspect6, 3, 2, 1, 1)
        self.photo_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_3.setText("")
        self.photo_3.setObjectName("photo_3")
        self.gridLayout_4.addWidget(self.photo_3, 0, 2, 1, 1)
        self.photo_4 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_4.setText("")
        self.photo_4.setObjectName("photo_4")
        self.gridLayout_4.addWidget(self.photo_4, 2, 0, 1, 1)
        self.suspect2 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect2.setObjectName("suspect2")
        self.gridLayout_4.addWidget(self.suspect2, 1, 1, 1, 1)
        self.suspect3 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect3.setObjectName("suspect3")
        self.gridLayout_4.addWidget(self.suspect3, 1, 2, 1, 1)
        self.photo_6 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_6.setText("")
        self.photo_6.setObjectName("photo_6")
        self.gridLayout_4.addWidget(self.photo_6, 2, 2, 1, 1)
        self.photo_5 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_5.setText("")
        self.photo_5.setObjectName("photo_5")
        self.gridLayout_4.addWidget(self.photo_5, 2, 1, 1, 1)
        self.suspect4 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect4.setObjectName("suspect4")
        self.gridLayout_4.addWidget(self.suspect4, 3, 0, 1, 1)
        self.photo_9 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_9.setText("")
        self.photo_9.setObjectName("photo_9")
        self.gridLayout_4.addWidget(self.photo_9, 4, 2, 1, 1)
        self.photo_1 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_1.setText("")
        self.photo_1.setObjectName("photo_1")
        self.gridLayout_4.addWidget(self.photo_1, 0, 0, 1, 1)
        self.photo_7 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.photo_7.setText("")
        self.photo_7.setObjectName("photo_7")
        self.gridLayout_4.addWidget(self.photo_7, 4, 0, 1, 1)
        self.suspect1 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect1.setObjectName("suspect1")
        self.gridLayout_4.addWidget(self.suspect1, 1, 0, 1, 1)
        self.suspect7 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect7.setObjectName("suspect7")
        self.gridLayout_4.addWidget(self.suspect7, 5, 0, 1, 1)
        self.suspect8 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect8.setObjectName("suspect8")
        self.gridLayout_4.addWidget(self.suspect8, 5, 1, 1, 1)
        self.suspect9 = QtWidgets.QPushButton(self.gridLayoutWidget_3)
        self.suspect9.setObjectName("suspect9")
        self.gridLayout_4.addWidget(self.suspect9, 5, 2, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 10, 218, 293))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.suspect3_f = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.suspect3_f.setObjectName("suspect3_f")
        self.gridLayout_2.addWidget(self.suspect3_f, 5, 0, 1, 1)
        self.suspect1_f = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.suspect1_f.setObjectName("suspect1_f")
        self.gridLayout_2.addWidget(self.suspect1_f, 3, 0, 1, 1)
        self.suspect4_f = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.suspect4_f.setObjectName("suspect4_f")
        self.gridLayout_2.addWidget(self.suspect4_f, 5, 1, 1, 1)
        self.photo_f3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_f3.setText("")
        self.photo_f3.setObjectName("photo_f3")
        self.gridLayout_2.addWidget(self.photo_f3, 4, 0, 1, 1)
        self.photo_f1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_f1.setText("")
        self.photo_f1.setObjectName("photo_f1")
        self.gridLayout_2.addWidget(self.photo_f1, 2, 0, 1, 1)
        self.photo_f4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_f4.setText("")
        self.photo_f4.setObjectName("photo_f4")
        self.gridLayout_2.addWidget(self.photo_f4, 4, 1, 1, 1)
        self.suspect2_f = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.suspect2_f.setObjectName("suspect2_f")
        self.gridLayout_2.addWidget(self.suspect2_f, 3, 1, 1, 1)
        self.photo_f2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.photo_f2.setText("")
        self.photo_f2.setObjectName("photo_f2")
        self.gridLayout_2.addWidget(self.photo_f2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, -10, 48, 16))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(300, 490, 331, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stop = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.stop.setObjectName("stop")
        self.horizontalLayout.addWidget(self.stop)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.next = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.next.setObjectName("next")
        self.horizontalLayout.addWidget(self.next)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(50, 330, 191, 251))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.photo_c2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.photo_c2.setText("")
        self.photo_c2.setObjectName("photo_c2")
        self.gridLayout_3.addWidget(self.photo_c2, 2, 1, 1, 1)
        self.photo_c3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.photo_c3.setText("")
        self.photo_c3.setObjectName("photo_c3")
        self.gridLayout_3.addWidget(self.photo_c3, 3, 0, 1, 1)
        self.photo_c1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.photo_c1.setText("")
        self.photo_c1.setObjectName("photo_c1")
        self.gridLayout_3.addWidget(self.photo_c1, 2, 0, 1, 1)
        self.photo_c4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.photo_c4.setText("")
        self.photo_c4.setObjectName("photo_c4")
        self.gridLayout_3.addWidget(self.photo_c4, 3, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 300, 91, 20))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.photo_1.setPixmap(QtGui.QPixmap("son/1.png"))
        self.photo_2.setPixmap(QtGui.QPixmap("son/2.png"))
        self.photo_3.setPixmap(QtGui.QPixmap("son/3.png"))
        self.photo_4.setPixmap(QtGui.QPixmap("son/4.png"))
        self.photo_5.setPixmap(QtGui.QPixmap("son/5.png"))
        self.photo_6.setPixmap(QtGui.QPixmap("son/6.png"))
        self.photo_7.setPixmap(QtGui.QPixmap("son/7.png"))
        self.photo_8.setPixmap(QtGui.QPixmap("son/8.png"))
        self.photo_9.setPixmap(QtGui.QPixmap("son/9.png"))
        files = os.listdir("choice/")  # 读入文件夹
        names = []
        for i in files:
            names.append("choice/"+i)
        #print(names)
        self.suspect1.clicked.connect(self.saveChoice)
        self.suspect2.clicked.connect(self.saveChoice)
        self.suspect3.clicked.connect(self.saveChoice)
        self.suspect4.clicked.connect(self.saveChoice)
        self.suspect5.clicked.connect(self.saveChoice)
        self.suspect6.clicked.connect(self.saveChoice)
        self.suspect7.clicked.connect(self.saveChoice)
        self.suspect8.clicked.connect(self.saveChoice)
        self.suspect9.clicked.connect(self.saveChoice)
        self.suspect1_f.clicked.connect(self.saveChoice_f)
        self.suspect2_f.clicked.connect(self.saveChoice_f)
        self.suspect3_f.clicked.connect(self.saveChoice_f)
        self.suspect4_f.clicked.connect(self.saveChoice_f)
        self.next.clicked.connect(self.nextf)
        self.stop.clicked.connect(self.saveChoice)




        self.photo_f1.setPixmap(QtGui.QPixmap(names[0]))
        self.photo_f2.setPixmap(QtGui.QPixmap(names[1]))
        self.photo_f3.setPixmap(QtGui.QPixmap(names[2]))
        self.photo_f4.setPixmap(QtGui.QPixmap(names[3]))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "chose four image that look like the suspect, untill you found suspect"))
        self.suspect5.setText(_translate("MainWindow", "suspect5"))
        self.suspect6.setText(_translate("MainWindow", "suspect6"))
        self.suspect2.setText(_translate("MainWindow", "suspect2"))
        self.suspect3.setText(_translate("MainWindow", "suspect3"))
        self.suspect4.setText(_translate("MainWindow", "suspect4"))
        self.suspect1.setText(_translate("MainWindow", "suspect1"))
        self.suspect7.setText(_translate("MainWindow", "suspect7"))
        self.suspect8.setText(_translate("MainWindow", "suspect8"))
        self.suspect9.setText(_translate("MainWindow", "suspect9"))
        self.suspect3_f.setText(_translate("MainWindow", "suspect3_f"))
        self.suspect1_f.setText(_translate("MainWindow", "suspect1_f"))
        self.suspect4_f.setText(_translate("MainWindow", "suspect4_f"))
        self.suspect2_f.setText(_translate("MainWindow", "suspect2_f"))
        self.label.setText(_translate("MainWindow", "last one"))
        self.stop.setText(_translate("MainWindow", "i found suspect"))
        self.next.setText(_translate("MainWindow", "next"))
        self.label_3.setText(_translate("MainWindow", "your choice"))


    def saveChoice_f(self):
        button_name = QtWidgets.QWidget().sender().objectName()
        source = "father/" + str(int(button_name[-3])) + ".png"
        destination = "choice/" + str(int(button_name[-3])) + "f.png"
        copyfile(source, destination)

        files = os.listdir("choice/")  # 读入文件夹
        num_png = len(files)  # 统计文件夹中的文件个数
        if num_png ==1:
            QtWidgets.QApplication.processEvents()
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))
        elif num_png ==2:
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
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))

        if num_png ==1:
            QtWidgets.QApplication.processEvents()
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))
        elif num_png ==2:
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
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))
    def saveChoice(self):
        button_name = QtWidgets.QWidget().sender().objectName()
        source = "son/" + button_name[-1] + ".png"
        destination = "choice/" + button_name[-1] + ".png"
        copyfile(source, destination)
        files = os.listdir("choice/")  # 读入文件夹
        num_png = len(files)  # 统计文件夹中的文件个数
        if num_png ==1:
            QtWidgets.QApplication.processEvents()
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))
        elif num_png ==2:
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
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))

        if num_png ==1:
            QtWidgets.QApplication.processEvents()
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))
        elif num_png ==2:
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
            self.photo_c1.setPixmap(QtGui.QPixmap(destination))
    def nextf(self):
        files = os.listdir("choice/")  # 读入文件夹
        num_png = len(files)  # 统计文件夹中的文件个数
        # load model
        decoder_=keras.models.load_model('decoder.h5')
        encoded_son = np.load('encoded_ag.npy')
        encoded_choice = np.load('encoded_choix.npy')
        if num_png == 4:

            # Choix de l'utilisateur :
            files = os.listdir("choice/")
            num_png = len(files)
            num_p =[]
            for i in files:
                num_p.append(int(i[0])-1)

            n=4
            encoded_father=[None]*n
            encoded_ag=[]
            encoded_cross=[]
            encoded_mut=[]
            for i in range(n):
                if files[i][1]=='f':
                    encoded_father[i]=encoded_choice[num_p[i]]
                    for m in range(3):
                        encoded_mut.append(ag.mutation_pixels(encoded_father[i],0.3))
                else:
                    encoded_father[i]=encoded_son[num_p[i]]
                    encoded_cross.append(encoded_father[i])
            encoded_cross2=ag.crossover_pixels(encoded_cross, 0.3)
            for k in range(len(encoded_mut)):
                encoded_ag.append(encoded_mut[k].tolist())
            for j in range(len(encoded_cross2)):
                res=encoded_cross2[j]
                encoded_ag.append(res)


            # Algo genetique1 : crossover
            #np.save('encoded_choix', encoded_choix)
            # encoded_ag = ag.crossover_pixels(encoded_father, 0.3)
            print(len(encoded_ag))
            print(len(encoded_ag[0]))
            print(type(encoded_ag))
            print(type(encoded_ag[0]))
            decoded_ag = decoder_.predict(encoded_ag)
            nn.save_reconstruction(9, decoded_ag)
            np.save('encoded_choix', encoded_father)
            np.save('encoded_ag', encoded_ag)
            files = os.listdir("choice/")
            rmtree('father/')
            os.mkdir('father/')
            for i in files:
                fil = os.listdir("father/")

                source = "choice/" + i
                destination = "father/" + str(len(fil)+1)+".png"
                copyfile(source, destination)
            QtWidgets.QApplication.processEvents()
            self.photo_c1.setPixmap(QtGui.QPixmap())
            self.photo_c2.setPixmap(QtGui.QPixmap())
            self.photo_c3.setPixmap(QtGui.QPixmap())
            self.photo_c4.setPixmap(QtGui.QPixmap())
            self.photo_1.setPixmap(QtGui.QPixmap())
            self.photo_2.setPixmap(QtGui.QPixmap())
            self.photo_3.setPixmap(QtGui.QPixmap())
            self.photo_4.setPixmap(QtGui.QPixmap())
            self.photo_5.setPixmap(QtGui.QPixmap())
            self.photo_6.setPixmap(QtGui.QPixmap())
            self.photo_7.setPixmap(QtGui.QPixmap())
            self.photo_8.setPixmap(QtGui.QPixmap())
            self.photo_9.setPixmap(QtGui.QPixmap())
            names = []
            for i in files:
                names.append("choice/"+i)
            self.photo_1.setPixmap(QtGui.QPixmap("son/1.png"))
            self.photo_2.setPixmap(QtGui.QPixmap("son/2.png"))
            self.photo_3.setPixmap(QtGui.QPixmap("son/3.png"))
            self.photo_4.setPixmap(QtGui.QPixmap("son/4.png"))
            self.photo_5.setPixmap(QtGui.QPixmap("son/5.png"))
            self.photo_6.setPixmap(QtGui.QPixmap("son/6.png"))
            self.photo_7.setPixmap(QtGui.QPixmap("son/7.png"))
            self.photo_8.setPixmap(QtGui.QPixmap("son/8.png"))
            self.photo_9.setPixmap(QtGui.QPixmap("son/9.png"))
            self.photo_f1.setPixmap(QtGui.QPixmap(names[0]))
            self.photo_f2.setPixmap(QtGui.QPixmap(names[1]))
            self.photo_f3.setPixmap(QtGui.QPixmap(names[2]))
            self.photo_f4.setPixmap(QtGui.QPixmap(names[3]))
            rmtree('choice/')
            os.mkdir('choice/')
            self.switch_window.emit()
