import sys
import foxhome
from PyQt5.QtWidgets import QApplication, QMainWindow


app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = foxhome.Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

############################################################
# import sys
# from foxhome import Ui_MainWindow
# from PyQt5 import QtWidgets
#
#
# class mywindow(QtWidgets.QWidget, Ui_MainWindow):
#     def __init__(self):
#         super(mywindow, self).__init__()
#         self.setupUi(self)
#
#
# def www():
#     app=QtWidgets.QApplication(sys.argv)
#     myshow=mywindow()
#     myshow.show()
#     sys.exit(app.exec_())
#
# www()