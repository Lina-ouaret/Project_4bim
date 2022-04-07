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

class Ui_MainWindow(object):
    switch_window = QtCore.pyqtSignal() #Convert to suspect selection page2 method

    def setupUi(self, MainWindow):
        """
        Label, button position, size setting

        Args :
            MainWindow : principal window displaying the program
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(704, 600)
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#MainWindow{background-image: url(:/background/background/Blue-Gradient-Blur-Background-For-Free.jpeg)}");
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
        self.hair_nc = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.hair_nc.setMaximumSize(QtCore.QSize(16777215, 32))
        self.hair_nc.setObjectName("hair_nc")
        self.verticalLayout.addWidget(self.hair_nc)
        self.Ph_age = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ph_age.setEnabled(True)
        self.Ph_age.setMaximumSize(QtCore.QSize(16777215, 200))
        self.Ph_age.setText("")
        self.Ph_age.setPixmap(QtGui.QPixmap("hairstyle.png"))
        self.Ph_age.setObjectName("Ph_age")
        self.verticalLayout.addWidget(self.Ph_age)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(3, 0, 0, 0)
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
        self.Ph_skin.setPixmap(QtGui.QPixmap("age.png"))
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
        self.Ph_gender.setPixmap(QtGui.QPixmap("gender.png"))
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

        #Connect the buttons to the corresponding functions
        self.Straight_Hair_T.clicked.connect(self.press)
        self.Straight_Hair_F.clicked.connect(self.press)
        self.young_T.clicked.connect(self.press)
        self.young_F.clicked.connect(self.press)
        self.male_T.clicked.connect(self.press)
        self.male_F.clicked.connect(self.press)
        self.male_0.clicked.connect(self.press)
        self.young_0.clicked.connect(self.press)
        self.hair_nc.clicked.connect(self.press2)
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
        self.hair_nc.setText(_translate("MainWindow", "no clue"))
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
        with open('select.txt', 'r') as file:
            rd = file.read()
        dict1 = eval(rd)
        if button_name[-1] == "T":
            dict1.update({button_name[:l]: 1})
        elif button_name[-1] == "F":
            dict1.update({button_name[:l]: -1})
        elif button_name[-1] == "0":
            del dict1[button_name[:l]]
        with open('select.txt', 'w') as file:
            file.write(str(dict1))

    def press2(self):
        """
        Delete button corresponding to the hair style option
        """
        with open('select.txt', 'r') as file:
            rd = file.read()
        dict1 = eval(rd)
        del dict1["Wavy_Hair"]
        del dict1["Straight_Hair"]
        with open('select.txt', 'w') as file:
            file.write(str(dict1))

    def press3(self):
        """
        Display the selection results and initialise the choice and jump to the suspect picture selection page1
        """
        with open('select.txt', 'r') as file:
            rd = file.read()
        QtWidgets.QMessageBox.critical(self, "error", rd)
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
        ## clusters avec un attribut nul
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



        dict = eval(rd)
        print(dict)

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
<<<<<<< HEAD
            decoder_ = keras.models.load_model('decoders/decoder8.h5')
        elif dict == att_cluster9 :
=======
        elif dic == att_cluster9 :
>>>>>>> 7200456819518709844cf7d2a383d1ac1ac41508
            encoded1=np.load('clusters/encoded_imgs8.npy')
            encoded2=np.load('clusters/encoded_imgs3.npy')
            encoded_imgs = encoded1[0]+encoded2[0]
        elif dic == att_cluster10 :
            encoded3=np.load('clusters/encoded_imgs1.npy')
            encoded4=np.load('clusters/encoded_imgs6.npy')
            encoded_imgs = encoded3[0]+encoded4[0]
        elif dic == att_cluster11 :
            encoded5=np.load('clusters/encoded_imgs4.npy')
            encoded6=np.load('clusters/encoded_imgs7.npy')
            encoded_imgs = encoded5[0]+encoded6[0]
        elif dic == att_cluster12 :
            encoded7=np.load('clusters/encoded_imgs2.npy')
            encoded8=np.load('clusters/encoded_imgs5.npy')
            encoded_imgs = encoded7[0]+encoded8[0]
        elif dic == att_cluster13 :
            encoded9=np.load('clusters/encoded_imgs5.npy')
            encoded10=np.load('clusters/encoded_imgs8.npy')
            encoded_imgs = encoded9[0]+encoded10[0]
        elif dic == att_cluster14 :
            encoded11=np.load('clusters/encoded_imgs5.npy')
            encoded12=np.load('clusters/encoded_imgs1.npy')
            encoded_imgs = encoded11[0]+encoded12[0]
        elif dic == att_cluster15 :
            encoded13=np.load('clusters/encoded_imgs4.npy')
            encoded14=np.load('clusters/encoded_imgs7.npy')
            encoded_imgs = encoded13[0]+encoded14[0]
        elif dic == att_cluster16 :
            encoded15=np.load('clusters/encoded_imgs5.npy')
            encoded16=np.load('clusters/encoded_imgs2.npy')
            encoded_imgs = encoded15[0]+encoded16[0]
        elif dic == att_cluster17 :
            encoded17=np.load('clusters/encoded_imgs4.npy')
            encoded18=np.load('clusters/encoded_imgs8.npy')
            encoded_imgs = encoded17[0]+encoded18[0]
        elif dic == att_cluster18 :
            encoded19=np.load('clusters/encoded_imgs1.npy')
            encoded20=np.load('clusters/encoded_imgs2.npy')
            encoded_imgs = encoded19[0]+encoded20[0]
        elif dic == att_cluster19 :
            encoded21=np.load('clusters/encoded_imgs7.npy')
            encoded22=np.load('clusters/encoded_imgs3.npy')
            encoded_imgs = encoded21[0]+encoded22[0]
        elif dic == att_cluster20 :
            encoded23=np.load('clusters/encoded_imgs5.npy')
            encoded24=np.load('clusters/encoded_imgs6.npy')
            encoded_imgs = encoded23[0]+encoded24[0]
<<<<<<< HEAD
        elif dict == att_clusters21 :
            encoded25=np.load('clusters/encoded_imgs1.npy')
            encoded26=np.load('clusters/encoded-imgs8.npy')
            encoded_imgs = encoded25[0]+encoded26[0]
        #np.save('encoded', encoded_imgs)
        decoder_.save('decoders/decoder.h5')
        # load model

        # decoder_ = keras.Sequential()

        # load encoded_imgs
        #encoded_imgs = np.load('encoded.npy')

        # Choix aléatoire des premières photos
        mylist = list(range(0, 500, 1))
        n = 9
        index = random.sample(mylist, n)
        # ag.randomly_choose_photos(index,n)
=======
>>>>>>> 7200456819518709844cf7d2a383d1ac1ac41508

        np.save('encoded', encoded_imgs)


        self.switch_window.emit()
