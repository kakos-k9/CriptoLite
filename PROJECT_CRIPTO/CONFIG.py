# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'CAD_KEY_API.ui'

from PyQt5 import QtCore, QtGui, QtWidgets
import BANCO_TABLE
import MENSAGEM_CAIXA
import NOMES_SYSTEM
import NOME_DB
import sqlite3
import os


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(616, 231)
        Dialog.setWindowIcon(QtGui.QIcon("images/moed.png"))
        Dialog.setMinimumSize(QtCore.QSize(616, 231))
        Dialog.setMaximumSize(QtCore.QSize(616, 231))
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        Dialog.setModal(True)
        self.pushButton_SALVAR = QtWidgets.QPushButton(Dialog)
        self.pushButton_SALVAR.setEnabled(False)
        self.pushButton_SALVAR.setGeometry(QtCore.QRect(580, 190, 31, 31))
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
        self.pushButton_CANCELA.setGeometry(QtCore.QRect(540, 190, 31, 31))
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
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 601, 81))
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 40, 581, 25))
        self.lineEdit_4.setFocus()
        self.lineEdit_4.setStyleSheet("QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(0, 85, 255);\n"
                                      "    background-color: rgb(255, 255, 231);\n"
                                      "}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 21))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 100, 601, 81))
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 40, 581, 25))
        self.lineEdit_5.setStyleSheet("QLineEdit:focus {\n"
                                      "    border: 2px solid rgb(0, 85, 255);\n"
                                      "    background-color: rgb(255, 255, 231);\n"
                                      "}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(570, 42, 20, 20))
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
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 281, 21))
        self.label_2.setObjectName("label_2")

        # ATIVAR BOTÃO
        self.lineEdit_4.textChanged[str].connect(self.ativar_btn)
        self.lineEdit_5.textChanged[str].connect(self.ativar_btn)

        # CONEXÃO SAIR
        self.pushButton_CANCELA.clicked.connect(Dialog.close)

        # CONEXÃO SALVAR/ALTERAR DADOS
        self.pushButton_SALVAR.clicked.connect(self.function_btn)

        # CONEXÃO PREENCHER CAMINHO
        self.pushButton.clicked.connect(self.localizar_ende)

        self.most_chave()
        self.most_camin_bd()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        Dialog.setTabOrder(self.pushButton_SALVAR, self.pushButton_CANCELA)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Configurações"))
        self.pushButton_SALVAR.setShortcut(_translate("Dialog", "Enter"))
        self.pushButton_CANCELA.setShortcut(_translate("Dialog", "Esc"))
        self.groupBox.setTitle(_translate("Dialog", "Chave API"))
        self.label.setText(_translate("Dialog", "Chave da API (CoinMarketCap)"))
        self.groupBox_2.setTitle(_translate("Dialog", "Banco de Dados"))
        self.pushButton.setShortcut(_translate("Dialog", "F1"))
        self.label_2.setText(_translate("Dialog", "Caminho do Arquivo de Banco de Dados"))

    def function_btn(self):
        self.cad_alte_chave()
        self.grava_txt()
        MENSAGEM_CAIXA.MessageBoxs.about(f'{NOMES_SYSTEM.aviso_info}', 'Configurações Atualizadas Com Sucesso, Se o Caminho do Banco Foi Alterado Recomenda-se Reiniciar o Sistema')

    def grava_txt(self):
        texto = self.lineEdit_5.text().replace(f"\\{NOME_DB.nome_bd}", "")
        try:
            arquivo = open("CONFIG_BANC.txt", 'w')
            arquivo.write(f"{texto}\\{NOME_DB.nome_bd}")
            if os.path.isdir(self.lineEdit_5.text()) == True:
                pass
            else:
                os.makedirs(self.lineEdit_5.text().replace(f"\\{NOME_DB.nome_bd}", ""))
            arquivo.close()

        except FileExistsError:
            pass

        except Exception as ERROR:
            print(ERROR)

    def cad_alte_chave(self):
        chave_key = self.lineEdit_4.text()
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("SELECT count(*) FROM config WHERE cod = 1")
            dados_count = c.fetchall()
            if dados_count[0][0] == 0:
                c.execute("INSERT INTO config (cod, desc_config) VALUES (?,?)", ('1', chave_key))
                conn.commit()
                self.pushButton_CANCELA.click()
            else:
                c.execute(f"UPDATE config SET desc_config = '{chave_key}' WHERE cod = 1")
                conn.commit()
                self.pushButton_CANCELA.click()
            conn.close()
        except Exception as ERROR:
            print(ERROR)

    def most_chave(self):
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("SELECT desc_config FROM config WHERE cod = 1")
            dados_lidos = c.fetchall()
            chave = dados_lidos[0][0]
            self.lineEdit_4.setText(chave)
        except Exception as ERROR:
            print(ERROR)

    def most_camin_bd(self):
        self.lineEdit_5.setText(NOME_DB.most_camin_bd())


    def localizar_ende(self):
        try:
            file_name = QtWidgets.QFileDialog.getExistingDirectory(self, "Selecione o Local/Pasta Para Salvar o Arquivo", rf"{os.environ['USERPROFILE']}\\Desktop")
            self.lineEdit_5.setText(file_name.replace("/", "\\"))

        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Não foi possível carregar o caminho\n{ERROR}')

    def ativar_btn(self):
        if self.lineEdit_4.text() and self.lineEdit_5:
            self.pushButton_SALVAR.setEnabled(True)
        else:
            self.pushButton_SALVAR.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
