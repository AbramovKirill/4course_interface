import sys
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from sign_in_ui import Ui_sign_in
from sign_up_ui import Ui_sign_up
from program_ui import Ui_program

#Create application (инициализация приложения)
app = QtWidgets.QApplication(sys.argv)
#Create form and init UI (инициализирую нашу форму и интерфейс нашего приложения)
sign_in = QtWidgets.QMainWindow()
ui = Ui_sign_in()
ui.setupUi(sign_in)
sign_in.show()

#db







#Hook logic

# def bp():
# 	ui.lineEdit_1_login.setText("hello, world!")
# ui.pushButton_2_login.clicked.connect(bp)


def openRegWindow():
	global sign_up_ui
	sign_up_ui = QtWidgets.QDialog()
	ui = Ui_sign_up()
	ui.setupUi(sign_up_ui)
	sign_in.close()  # або можна використати authorization.hide()
	sign_up_ui.show()


ui.pushButton_2_login.clicked.connect(openRegWindow)




#Run main loop
sys.exit(app.exec_())