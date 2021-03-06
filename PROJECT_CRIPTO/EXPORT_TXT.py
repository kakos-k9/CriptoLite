# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FORM_CAMIN_TXT.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import MENSAGEM_CAIXA
import NOMES_SYSTEM
import sqlite3
import BANCO_TABLE


class Ui_Dialog(QtWidgets.QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowIcon(QtGui.QIcon("images/moed.png"))
        Dialog.resize(548, 95)
        Dialog.setMinimumSize(QtCore.QSize(548, 95))
        Dialog.setMaximumSize(QtCore.QSize(548, 95))
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
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_SALVAR = QtWidgets.QPushButton(Dialog)
        self.pushButton_SALVAR.setEnabled(False)
        self.pushButton_SALVAR.setGeometry(QtCore.QRect(510, 60, 31, 31))
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
        self.pushButton_CANCELA.setGeometry(QtCore.QRect(470, 60, 31, 31))
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
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(100, 50, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.data = ""
        self.hora = ""
        self.cot_dolar = ""

        # CONEX??O INSERE NOVO CAMINHO
        self.lineEdit.textEdited.connect(self.insere_novo_camin)

        # CONEX??O PESQUISAR CAMINHO
        self.pushButton.clicked.connect(self.localizar_ende)

        # CONEX??O GERAR TXT
        self.pushButton_SALVAR.clicked.connect(self.gerar_txt)

        # CONEX??O ATIVAR BTN
        self.lineEdit.textChanged[str].connect(self.ativar_btn)

        # CONEX??O SAIR
        self.pushButton_CANCELA.clicked.connect(Dialog.close)

        # MOSTRA CAMINHO PADR??O
        self.most_camin()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEdit, self.pushButton_SALVAR)
        Dialog.setTabOrder(self.pushButton_SALVAR, self.pushButton_CANCELA)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Exportar TXT Cripto Moeda"))
        self.label.setText(_translate("Dialog", "Caminho Para Salvar o Arquivo"))
        #self.lineEdit.setText(_translate("Dialog", f"{os.environ['USERPROFILE']}\\Desktop"))
        self.pushButton_SALVAR.setShortcut(_translate("Dialog", "Enter"))
        self.pushButton_CANCELA.setShortcut(_translate("Dialog", "Esc"))
        self.pushButton.setShortcut(_translate("Dialog", "F1"))
        self.label_2.setText(_translate("Dialog", "Nome do Arquivo:"))
        self.label_3.setText(_translate("Dialog", "CRIPTO.TXT"))

    def insere_novo_camin(self):
        caminho_novo = self.lineEdit.text()
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute(f"UPDATE config SET desc_config = '{caminho_novo}' WHERE cod = 2")
            conn.commit()
            conn.close()
        except Exception as ERROR:
            print(ERROR)

    def most_camin(self):
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("SELECT desc_config FROM config WHERE cod = 2")
            dados_lidos = c.fetchall()
            caminho = dados_lidos[0][0]
            self.lineEdit.setText(caminho)
        except Exception as ERROR:
            print(ERROR)

    def gerar_txt(self):
        try:
            caminho = fr"{self.lineEdit.text()}\{self.label_3.text()}"

            if os.path.isfile(caminho) == True:
                os.remove(caminho)
            else:
                pass
            if os.path.isdir(self.lineEdit.text()) == True:
                pass
            else:
                os.makedirs(self.lineEdit.text())

            arquivo = open(caminho, 'w+')
            arquivo.write("*|POWERED BY K&A SOFTWARE|\n")
            arquivo.write("*|DATA/ATUAL|HORATUAL|MOEDA/US$ | VALOR/COTACAO|\n")
            arquivo.write(f"1|{self.data[0:2]}/{self.data[3:5]}/{self.data[6:10]}|{self.hora[0:2]}:{self.hora[3:5]}:{self.hora[6:8]}|US$       |{self.cot_dolar.rjust(14, ' ')}|\n")
            arquivo.write("*|NOME/MOEDA|--------------------VALOR/US|------------------VALOR/REAL|ID-------|NOME/CRIPTO-------------------|FORNECIMENTO/CIRCULANTE----------|RANKTOP|DTCRIACAO-|HCRIACAO|A|F|ULTATUALIZ|HRUATUAL|SUPRIMENTO/MAXIMO----------------|NUM/PAR|VALOR/MERCADO/TOT/DILUIDO--------|DTULTCOTAC|HRULTCOT|VALOR/MERCADO--------------------|DOMINANCIA/CAP/MERCADO-----------|PERC/MUDANCA/1H--------|PERC/MUDANCA/24H-------|PERC/MUDANCA/30D-------|PERC/MUDANCA/60D-------|PERC/MUDANCA/7D--------|PERC/MUDANCA/90D-------|PRECO----------------------------|VOLUME/24H-----------------------|VOLUME/ALTERACAO/24H-------------|FORNECIMENTO/TOTAL---------------|QUANTIDADE/DE/COMPRA-------------|PRECO/DE/COMPRA------------------|DATACOMPRA|HORACOMP|COTACAO/COMPRA-------------------|\n")
            try:
                conn = sqlite3.connect(BANCO_TABLE.banco)
                c = conn.cursor()
                c.execute("SELECT nome, valor_us, valor_rs, id_crypto, slug, circulating_supply, cmc_rank, date_added, is_active, is_fiat, last_update, max_supply, num_market_pairs, fully_diluted_market_cap, quote_last_updated,"
                          "market_cap, market_cap_dominance, percent_change_1h, percent_change_24h, percent_change_30d, percent_change_60d, percent_change_7d, percent_change_90d, price, volume_24h, volume_change_24h, total_supply, quant_compra, preco_compra, data_hora_compra, cotacao_compra FROM cripto_moed")
                dados_lidos = c.fetchall()
                for a in dados_lidos:
                    nome = str(a[0])
                    val_us = str(a[1])
                    val_rs = str(a[2])
                    id_crypto = str(a[3])
                    nome_crypto = str(a[4])
                    circulating_supply = str(a[5])
                    cmc_rank = str(a[6])

                    date_added = str(a[7])
                    dia_date_added = date_added[8:10]
                    mes_date_added = date_added[5:7]
                    ano_date_added = date_added[0:4]
                    horas_date_added = date_added[11:13]
                    minuto_date_added = date_added[14:16]
                    segundo_date_added = date_added[17:19]

                    is_active = str(a[8])
                    is_fiat = str(a[9])

                    last_update = str(a[10])
                    dia_last_update = last_update[8:10]
                    mes_last_update = last_update[5:7]
                    ano_last_update = last_update[0:4]
                    horas_last_update = last_update[11:13]
                    minuto_last_update = last_update[14:16]
                    segundo_last_update = last_update[17:19]

                    max_supply = str(a[11])
                    num_market_pairs = str(a[12])
                    fully_diluted_market_cap = str(a[13])

                    quote_last_update = str(a[14])
                    dia_quote_last_update = quote_last_update[8:10]
                    mes_quote_last_update = quote_last_update[5:7]
                    ano_quote_last_update = quote_last_update[0:4]
                    horas_quote_last_update = quote_last_update[11:13]
                    minuto_quote_last_update = quote_last_update[14:16]
                    segundo_quote_last_update = quote_last_update[17:19]

                    market_cap = str(a[15])
                    market_cap_dominance = str(a[16])
                    percent_change_1h = str(a[17])
                    percent_change_24h = str(a[18])
                    percent_change_30d = str(a[19])
                    percent_change_60d = str(a[20])
                    percent_change_7d = str(a[21])
                    percent_change_90d = str(a[22])
                    price = str(a[23])
                    volume_24h = str(a[24])
                    volume_change_24h = str(a[25])
                    total_supply = str(a[26])
                    quant_compra = str(a[27])
                    preco_compra = str(a[28])
                    data_hora_compra = str(a[29])

                    dia_data_compra = data_hora_compra[8:10]
                    mes_data_compra = data_hora_compra[5:7]
                    ano_data_compra = data_hora_compra[0:4]
                    horas_data_compra = data_hora_compra[11:13]
                    minuto_data_compra = data_hora_compra[14:16]
                    segundo_data_compra = data_hora_compra[17:19]

                    cotacao_compra = str(a[30])

                    arquivo.write(f"2|{nome.ljust(10)}|{val_us.rjust(28)}|{val_rs.rjust(28)}|{id_crypto.rjust(9)}|{nome_crypto.ljust(30)}|{circulating_supply.rjust(33)}|"
                                  f"{cmc_rank.rjust(7)}|{dia_date_added}/{mes_date_added}/{ano_date_added}|{horas_date_added}:{minuto_date_added}:{segundo_date_added}|"
                                  f"{is_active}|{is_fiat}|{dia_last_update}/{mes_last_update}/{ano_last_update}|{horas_last_update}:{minuto_last_update}:{segundo_last_update}|"
                                  f"{max_supply.rjust(33)}|{num_market_pairs.rjust(7)}|{fully_diluted_market_cap.rjust(33)}|{dia_quote_last_update}/{mes_quote_last_update}/{ano_quote_last_update}|"
                                  f"{horas_quote_last_update}:{minuto_quote_last_update}:{segundo_quote_last_update}|{market_cap.rjust(33)}|{market_cap_dominance.rjust(33)}|{percent_change_1h.rjust(23)}|"
                                  f"{percent_change_24h.rjust(23)}|{percent_change_30d.rjust(23)}|{percent_change_60d.rjust(23)}|{percent_change_7d.rjust(23)}|{percent_change_90d.rjust(23)}|{price.rjust(33)}|"
                                  f"{volume_24h.rjust(33)}|{volume_change_24h.rjust(33)}|{total_supply.rjust(33)}|{quant_compra.rjust(33)}|{preco_compra.rjust(33)}|{dia_data_compra}/{mes_data_compra}/{ano_data_compra}|"
                                  f"{horas_data_compra}:{minuto_data_compra}:{segundo_data_compra}|{cotacao_compra.rjust(33)}|\n")
                conn.close()
            except Exception as ERROR:
                print(ERROR)
            arquivo.close()
            MENSAGEM_CAIXA.TimerMessageBox().func(f'{NOMES_SYSTEM.aviso_info}', 'Arquivo Gerado Com Sucesso!', 1)
            self.pushButton_CANCELA.click()

        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'N??o Foi Poss??vel Gerar o txt\n{ERROR}')


    def localizar_ende(self):
        try:
            file_name = QtWidgets.QFileDialog.getExistingDirectory(self, "Selecione o Local/Pasta Para Salvar o Arquivo", rf"{os.environ['USERPROFILE']}\\Desktop")
            self.lineEdit.setText(file_name.replace("/", "\\"))

        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'N??o foi poss??vel carregar o caminho\n{ERROR}')

    def ativar_btn(self):
        if self.lineEdit.text():
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
