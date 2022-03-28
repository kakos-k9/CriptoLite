# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IMPORT_TXT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import MENSAGEM_CAIXA
import NOMES_SYSTEM
import sqlite3
import BANCO_TABLE
import os


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(548, 118)
        Dialog.setWindowIcon(QtGui.QIcon("images/moed.png"))
        Dialog.setMinimumSize(QtCore.QSize(548, 118))
        Dialog.setMaximumSize(QtCore.QSize(548, 118))
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 271, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 20, 531, 25))
        self.lineEdit.setStyleSheet("QLineEdit:focus {\n"
        "    border: 2px solid rgb(0, 85, 255);\n"
        "    background-color: rgb(255, 255, 231);\n"
        "}")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(8656)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_SALVAR = QtWidgets.QPushButton(Dialog)
        self.pushButton_SALVAR.setEnabled(False)
        self.pushButton_SALVAR.setGeometry(QtCore.QRect(510, 80, 31, 31))
        self.pushButton_SALVAR.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_SALVAR.setStyleSheet("QPushButton {\n"
        "    border: 1px solid rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 1px solid rgb(45, 204, 112);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border: 1px solid rgb(0, 255, 0);\n"
        "}")
        self.pushButton_SALVAR.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/sim.png"))
        self.pushButton_SALVAR.setIcon(icon)
        self.pushButton_SALVAR.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_SALVAR.setObjectName("pushButton_SALVAR")
        self.pushButton_CANCELA = QtWidgets.QPushButton(Dialog)
        self.pushButton_CANCELA.setGeometry(QtCore.QRect(470, 80, 31, 31))
        self.pushButton_CANCELA.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_CANCELA.setStyleSheet("QPushButton {\n"
        "    border: 1px solid rgb(240, 240, 240);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 1px solid rgb(186, 0, 0);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border: 1px solid rgb(255, 0, 0);\n"
        "}")
        self.pushButton_CANCELA.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/nao.png"))
        self.pushButton_CANCELA.setIcon(icon1)
        self.pushButton_CANCELA.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_CANCELA.setObjectName("pushButton_pesq_dol")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(518, 22, 20, 20))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton {\n"
        "    border: 1px solid rgb(255, 255, 255);\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border: 1px solid rgb(0, 0, 255);\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border: 1px solid rgb(255, 255, 0);\n"
        "}")
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/paste.png"))
        self.pushButton.setIcon(icon2)
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(10, 50, 531, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.pushButton_SALVAR)
        Dialog.setTabOrder(self.pushButton_SALVAR, self.pushButton_CANCELA)

        # CONEXÃO INSERE NOVO CAMINHO
        self.lineEdit.textEdited.connect(self.insere_novo_camin)

        # CONEXÃO ATIVAR BOTÃO
        self.lineEdit.textChanged[str].connect(self.ativar_btn)

        # CONEXÃO PESQUISAR ARQUIVO
        self.pushButton.clicked.connect(self.localizar_arq)

        # CONEXÃO SAIR
        self.pushButton_CANCELA.clicked.connect(Dialog.close)

        self.most_camin()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Importar TXT Cripto Moeda"))
        self.label.setText(_translate("Dialog", "Caminho Para Importar o Arquivo"))
        self.pushButton_SALVAR.setShortcut(_translate("Dialog", "Enter"))
        self.pushButton_CANCELA.setShortcut(_translate("Dialog", "Esc"))
        self.pushButton.setShortcut(_translate("Dialog", "F1"))

    def insere_novo_camin(self):
        caminho_novo = self.lineEdit.text()
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute(f"UPDATE config SET desc_config = '{caminho_novo}' WHERE cod = 3")
            conn.commit()
            conn.close()
        except Exception as ERROR:
            print(ERROR)

    def most_camin(self):
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("SELECT desc_config FROM config WHERE cod = 3")
            dados_lidos = c.fetchall()
            caminho = dados_lidos[0][0]
            self.lineEdit.setText(caminho)
        except Exception as ERROR:
            print(ERROR)

    def ativar_btn(self):
        if self.lineEdit.text():
            self.pushButton_SALVAR.setEnabled(True)
        else:
            self.pushButton_SALVAR.setEnabled(False)

    def localizar_arq(self):
        try:
            file_name = QtWidgets.QFileDialog.getOpenFileName(self, "Selecione o Arquivo a Importar", rf"{os.environ['USERPROFILE']}\\Desktop", "Text files (*.txt)")
            caminho = file_name[0]
            self.lineEdit.setText(caminho.replace("/", "\\"))
        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Não foi possível carregar o arquivo\n{ERROR}')


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
