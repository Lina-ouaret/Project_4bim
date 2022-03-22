from PyQt5 import QtWidgets,QtCore
import sys
from shutil import copyfile

from select2 import Ui_MainWindow as Ui1
from suspect3 import Ui_MainWindow as Ui2
from suspect2_2 import Ui_MainWindow as Ui3


class mywindow(QtWidgets.QMainWindow,Ui1):
    def __init__(self):
        super(mywindow,self).__init__()
        self.setupUi(self)


class mywindow2(QtWidgets.QMainWindow,Ui2):
    def __init__(self):
        super(mywindow2,self).__init__()
        self.setupUi2(self)
class mywindow3(QtWidgets.QMainWindow,Ui3):
    def __init__(self):
        super(mywindow3,self).__init__()
        self.setupUi(self)
class Controller:

    def __init__(self):
        pass

    def show_select(self):
        self.login = mywindow()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = mywindow2()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self):
        self.window_two = mywindow3()
        self.window.close()
        self.window_two.show()



app = QtWidgets.QApplication(sys.argv)
#MainWindow = QMainWindow()
main=QtWidgets.QWidget()
latout = QtWidgets.QHBoxLayout()
main.setLayout(latout)



controller = Controller()
controller.show_select()
sys.exit(app.exec_())