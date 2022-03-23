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

class Ui_MainWindow(object):

    switch_window = QtCore.pyqtSignal()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 647)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 321, 41))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 110, 630, 316))
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
        self.Pale_Skin_T = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Pale_Skin_T.setObjectName("Pale_Skin_T")
        self.verticalLayout.addWidget(self.Pale_Skin_T)
        self.Pale_Skin_F = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Pale_Skin_F.setMaximumSize(QtCore.QSize(16777215, 32))
        self.Pale_Skin_F.setObjectName("Pale_Skin_F")
        self.verticalLayout.addWidget(self.Pale_Skin_F)
        self.Ph_skin = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ph_skin.setText("")
        self.Ph_skin.setPixmap(QtGui.QPixmap("noun-sudden-paleness-186406.png"))
        self.Ph_skin.setObjectName("Ph_skin")
        self.verticalLayout.addWidget(self.Ph_skin)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(3, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.age = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.age.setEnabled(False)
        self.age.setMinimumSize(QtCore.QSize(0, 30))
        self.age.setMaximumSize(QtCore.QSize(16777215, 30))
        self.age.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.age.setObjectName("age")
        self.verticalLayout_2.addWidget(self.age)
        self.young_T = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.young_T.setMinimumSize(QtCore.QSize(0, 30))
        self.young_T.setObjectName("young_T")
        self.verticalLayout_2.addWidget(self.young_T)
        self.young_F = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.young_F.setMinimumSize(QtCore.QSize(0, 30))
        self.young_F.setObjectName("young_F")
        self.verticalLayout_2.addWidget(self.young_F)
        self.Ph_age = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ph_age.setEnabled(True)
        self.Ph_age.setMaximumSize(QtCore.QSize(16777215, 200))
        self.Ph_age.setText("")
        self.Ph_age.setPixmap(QtGui.QPixmap("noun-aged-2452301.png"))
        self.Ph_age.setObjectName("Ph_age")
        self.verticalLayout_2.addWidget(self.Ph_age)
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
        self.Ph_gender = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Ph_gender.setText("")
        self.Ph_gender.setPixmap(QtGui.QPixmap("noun-gender-2184468.png"))
        self.Ph_gender.setObjectName("Ph_gender")
        self.verticalLayout_4.addWidget(self.Ph_gender)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(360, 470, 129, 32))
        self.next.setMinimumSize(QtCore.QSize(0, 30))
        self.next.setObjectName("next")
        self.print = QtWidgets.QPushButton(self.centralwidget)
        self.print.setGeometry(QtCore.QRect(230, 470, 100, 32))
        self.print.setObjectName("print")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.print.clicked.connect(self.press2)
        self.Pale_Skin_T.clicked.connect(self.press)
        self.Pale_Skin_F.clicked.connect(self.press)
        self.young_T.clicked.connect(self.press)
        self.young_F.clicked.connect(self.press)
        self.male_T.clicked.connect(self.press)
        self.male_F.clicked.connect(self.press)
        self.next.clicked.connect(self.press3)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "please entre the intentification of the criminal"))
        self.skin_color.setText(_translate("MainWindow", "skin color"))
        self.Pale_Skin_T.setText(_translate("MainWindow", "pale"))
        self.Pale_Skin_F.setText(_translate("MainWindow", "dark"))
        self.age.setText(_translate("MainWindow", "age"))
        self.young_T.setText(_translate("MainWindow", "young"))
        self.young_F.setText(_translate("MainWindow", "old"))
        self.gender.setText(_translate("MainWindow", "gender"))
        self.male_T.setText(_translate("MainWindow", "male"))
        self.male_F.setText(_translate("MainWindow", "female"))
        self.next.setText(_translate("MainWindow", "next"))
        self.print.setText(_translate("MainWindow", "print"))

    def press(self):
        button_name = QtWidgets.QWidget().sender().objectName()
        l = len(button_name) - 2
        with open('select.txt', 'r') as file:
            rd = file.read()
        dict1 = eval(rd)
        if button_name[-1] == "T":
            dict1.update({button_name[:l]: 1})
        elif button_name[-1] == "F":
            dict1.update({button_name[:l]: -1})
        with open('select.txt', 'w') as file:
            file.write(str(dict1))

    def press2(self):
        with open('select.txt', 'r') as file:
            rd = file.read()
        print(rd)

    def press3(self):
        if os.path.exists('choice/'):
            rmtree('choice/')
        os.mkdir('choice/')
        self.switch_window.emit()
