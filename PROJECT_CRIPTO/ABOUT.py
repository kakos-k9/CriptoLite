# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ABOUT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(371, 186)
        Dialog.setWindowIcon(QtGui.QIcon("images/moed.png"))
        Dialog.setMinimumSize(QtCore.QSize(371, 186))
        Dialog.setMaximumSize(QtCore.QSize(371, 186))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(260, 10, 101, 91))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/QR_CODE.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 341, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 130, 191, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 160, 101, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 241, 51))
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 160, 91, 21))
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sobre Cripto Lite"))
        self.label_2.setText(_translate("Dialog", "Copyright © 2022 Kaique Afonso. Todos os Direitos Reservados."))
        self.label_3.setText(_translate("Dialog", "kaiqueafonsoferreira21@gmail.com"))
        self.label_4.setText(_translate("Dialog", "75981729111 - OI"))
        self.label_5.setText(_translate("Dialog", "\"A paz de consciência será conseguida pelo\n"
                                                  "cumprimento de deveres a que o homem se\n"
                                                  "obriga pela sua racionalidade e seu destino.\""))
        self.label_6.setText(_translate("Dialog", "Cripto Lite V1.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
