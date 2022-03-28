# -*- coding: utf-8 -*-
#
# Form implementation generated from reading ui file 'MAIN.ui'
#
# Develper: Kaique Afonso Ferreira do Rosário
#
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from RECONNECT import reconnect
import MENSAGEM_CAIXA
import NOMES_SYSTEM
import CONSULT_API
import BANCO_TABLE
import IMPORT_TXT
import EXPORT_TXT
import HISTORICO
import cot_dolar
import CAD_CP_M
import requests
import sqlite3
import CONFIG
import ABOUT
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(661, 587)
        MainWindow.setWindowIcon(QtGui.QIcon("images/moed.png"))
        MainWindow.setMinimumSize(QtCore.QSize(661, 587))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_data = QtWidgets.QLabel(self.centralwidget)
        self.label_data.setEnabled(False)
        self.label_data.setObjectName("label_data")
        self.gridLayout.addWidget(self.label_data, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("QLineEdit:focus {\n"
                                    "    border: 2px solid rgb(0, 85, 255);\n"
                                    "    background-color: rgb(255, 255, 231);\n"
                                    "}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.pushButton_pesq_dol = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pesq_dol.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_pesq_dol.setStyleSheet("QPushButton {\n"
                                              "    border: 1px solid rgb(180, 180, 180);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover {\n"
                                              "    border: 1px solid rgb(0, 0, 186);\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:pressed {\n"
                                              "    border: 1px solid rgb(0, 0, 186);\n"
                                              "}")
        self.pushButton_pesq_dol.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/calc_dol.png"))
        self.pushButton_pesq_dol.setIcon(icon)
        self.pushButton_pesq_dol.setIconSize(QtCore.QSize(25, 25))
        self.pushButton_pesq_dol.setObjectName("pushButton_pesq_dol")
        self.gridLayout.addWidget(self.pushButton_pesq_dol, 1, 3, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 641, 391))
        self.tableWidget.setFocus()
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(34)
        self.tableWidget.setStyleSheet("selection-color: rgb(255, 255, 255); selection-background-color: rgb(0, 0, 255);")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setHorizontalHeaderLabels(("Id_Crypto", "Símbolo Moeda", "Slug", "Valor US$", "Valor R$", "Fornecimento Circulante", "Ranking Top", "Data de Criação",
                                                    "Está Ativo?", "É Fiduciário?", "Última Atualização", "Suprimento Máximo", "Número de Pares de Mercado", "Valor de Mercado Totalmente Diluído",
                                                    "Última Cotação Atualização", "Valor de Mercado", "Dominância de Capitalização de Mercado", "Percentual de Mudança em 1H", "Percentual de Mudança em 24H",
                                                    "Percentual de Mudança em 30 Dias", "Percentual de Mudança em 60 Dias", "Percentual de Mudança em 7 Dias", "Percentual de Mudanças em 90 Dias", "Preço", "Volume 24h", "Volume de Alteração em 24H",
                                                    "Nome Completo", "Símbolo", "Fornecimento Total", "Quantidade de Compra", "Preço de Compra", "Data de Compra", "Cotação da Compra", "Seq"))
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(55, 49))
        self.toolBar.setFloatable(True)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 661, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuDiversos = QtWidgets.QMenu(self.menuBar)
        self.menuDiversos.setObjectName("menuDiversos")
        self.menuConfigura_es = QtWidgets.QMenu(self.menuBar)
        self.menuConfigura_es.setObjectName("menuConfigura_es")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toolBar_2.setMovable(False)
        self.toolBar_2.setIconSize(QtCore.QSize(59, 49))
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.actionIncluir_Insert = QtWidgets.QAction(MainWindow)
        self.actionIncluir_Insert.setEnabled(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/adicionar.png"))
        self.actionIncluir_Insert.setIcon(icon1)
        self.actionIncluir_Insert.setObjectName("actionIncluir_Insert")
        self.actionAlterar_Enter = QtWidgets.QAction(MainWindow)
        self.actionAlterar_Enter.setEnabled(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/alterar.png"))
        self.actionAlterar_Enter.setIcon(icon2)
        self.actionAlterar_Enter.setObjectName("actionAlterar_Enter")
        self.actionExcluir = QtWidgets.QAction(MainWindow)
        self.actionExcluir.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/excluir.png"))
        self.actionExcluir.setIcon(icon3)
        self.actionExcluir.setObjectName("actionExcluir")
        self.actionZerar_Valor = QtWidgets.QAction(MainWindow)
        self.actionZerar_Valor.setEnabled(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/zer_val.png"))
        self.actionZerar_Valor.setIcon(icon4)
        self.actionZerar_Valor.setObjectName("actionZerar_Valor")
        self.actionExportar_Arquivo_TXT = QtWidgets.QAction(MainWindow)
        self.actionExportar_Arquivo_TXT.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/exportar_txt.png"))
        self.actionExportar_Arquivo_TXT.setIcon(icon5)
        self.actionExportar_Arquivo_TXT.setObjectName("actionExportar_Arquivo_TXT")
        self.actionSobre = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/develper.png"))
        self.actionSobre.setIcon(icon6)
        self.actionSobre.setObjectName("actionSobre")
        self.actionEncerrar_Sitema_Esc = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/sair.png"))
        self.actionEncerrar_Sitema_Esc.setIcon(icon7)
        self.actionEncerrar_Sitema_Esc.setVisible(True)
        self.actionEncerrar_Sitema_Esc.setMenuRole(QtWidgets.QAction.NoRole)
        self.actionEncerrar_Sitema_Esc.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionEncerrar_Sitema_Esc.setObjectName("actionEncerrar_Sitema_Esc")
        self.actionConfig = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/config.png"))
        self.actionConfig.setIcon(icon8)
        self.actionConfig.setObjectName("actionConfig")
        self.actionAtualizar_Valores_F11 = QtWidgets.QAction(MainWindow)
        self.actionAtualizar_Valores_F11.setCheckable(False)
        self.actionAtualizar_Valores_F11.setEnabled(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/atua_moeds.png"))
        self.actionAtualizar_Valores_F11.setIcon(icon9)
        self.actionAtualizar_Valores_F11.setObjectName("actionAtualizar_Valores_F11")
        self.actionImportar_Arquivo_TXT = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/importar_txt.png"))
        self.actionImportar_Arquivo_TXT.setIcon(icon10)
        self.actionImportar_Arquivo_TXT.setObjectName("actionImportar_Arquivo_TXT")
        self.actionHist_rico = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/historic.png"))
        self.actionHist_rico.setIcon(icon11)
        self.actionHist_rico.setObjectName("actionHist_rico")
        self.toolBar.addAction(self.actionIncluir_Insert)
        self.toolBar.addAction(self.actionAlterar_Enter)
        self.toolBar.addAction(self.actionExcluir)
        self.toolBar.addAction(self.actionZerar_Valor)
        self.toolBar.addAction(self.actionImportar_Arquivo_TXT)
        self.toolBar.addAction(self.actionExportar_Arquivo_TXT)
        self.toolBar.addAction(self.actionAtualizar_Valores_F11)
        self.toolBar.addAction(self.actionHist_rico)
        self.toolBar.addSeparator()
        self.menuDiversos.addAction(self.actionSobre)
        self.menuConfigura_es.addAction(self.actionConfig)
        self.menuBar.addAction(self.menuConfigura_es.menuAction())
        self.menuBar.addAction(self.menuDiversos.menuAction())
        self.toolBar_2.addAction(self.actionEncerrar_Sitema_Esc)
        self.data = QtCore.QDate.currentDate()
        self.hora = QtCore.QTime.currentTime()

        # CRIAÇÃO DE TABELAS
        BANCO_TABLE.Cria_Tabelas.table_cripto(self)
        BANCO_TABLE.Cria_Tabelas.table_historic(self)
        BANCO_TABLE.Cria_Tabelas.table_cot_dola(self)
        BANCO_TABLE.Cria_Tabelas.table_config(self)

        # INSERÇÕES DE CONFIGURAÇÃO
        BANCO_TABLE.Cria_Tabelas.insere_caminho_export_txt(self)
        BANCO_TABLE.Cria_Tabelas.insere_caminho_import_txt(self)

        # CONEXÃO INSERIR COTAÇÃO DOLAR
        #self.lineEdit.editingFinished.connect(self.insere_cot_dolar)

        # CONEXÃO MOSTRA COTAÇÃO DOLAR
        self.mostrar_cot_dolar()

        # CONEXÃO MOSTRA COTAÇÃO DOLAR (TEMPO REAL)
        self.pushButton_pesq_dol.clicked.connect(self.atualizar_dolar)

        # CONEXÃO REFRESH
        self.actua()

        # CHAMA TELA CONFIGURAÇÃO DE CHAVE API
        self.actionConfig.triggered.connect(self.chama_tela_config)

        # CHAMA TELA SOBRE
        self.actionSobre.triggered.connect(self.chama_tela_sobre)

        # VALIDATOR ACEITAR NÚMEROS DOUBLE
        self.lineEdit.setValidator(QtGui.QDoubleValidator())

        # CONEXÃO FORMATAR VALOR COTAÇÃO
        self.lineEdit.editingFinished.connect(self.formatar_line_cot_dolar)

        # CONEXÃO CADASTRAR CRIPTO MOEDA
        self.actionIncluir_Insert.triggered.connect(self.chama_cad_cp)

        # CONEXÃO EDITAR CRIPTO MOEDA
        self.tableWidget.doubleClicked.connect(self.editar_cptm)
        self.actionAlterar_Enter.triggered.connect(self.editar_cptm)

        # CONEXÃO DELETAR CRIPTO MOEDAS
        self.actionExcluir.triggered.connect(self.excluir_cpt)

        # CONEXÃO ZERAR VALORES
        self.actionZerar_Valor.triggered.connect(self.zerar_valores)

        # CONEXÃO CHAMA IMPORTAR TXT
        self.actionImportar_Arquivo_TXT.triggered.connect(self.chama_tela_importar_txt)

        # CONEXÃO EXPORTAR GERA TXT
        self.actionExportar_Arquivo_TXT.triggered.connect(self.chama_gera_txt)

        # CONEXÃO HISTÓRICO
        self.actionHist_rico.triggered.connect(self.chama_historico)

        # CONEXÃO ATUALIZAR VALORES
        self.actionAtualizar_Valores_F11.triggered.connect(self.question_actua)

        # CONEXÃO SAIR DO SISTEMA
        self.actionEncerrar_Sitema_Esc.triggered.connect(lambda: self.encerrar_system(MainWindow))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.data_hora)
        self.timer.start(1000)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.tableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cripto Lite"))
        self.label.setText(_translate("MainWindow", "Data Atual"))
        self.label_2.setText(_translate("MainWindow", "Valor da Cotação (US$)"))
        self.label_data.setText(_translate("MainWindow", "00/00/0000  00:00:00"))
        self.pushButton_pesq_dol.setShortcut(_translate("MainWindow", "F1"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuDiversos.setTitle(_translate("MainWindow", "Diversos"))
        self.menuConfigura_es.setTitle(_translate("MainWindow", "Configurações"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.actionIncluir_Insert.setText(_translate("MainWindow", "Incluir [Ins]"))
        self.actionIncluir_Insert.setStatusTip(_translate("MainWindow", "Incluir Cripto Moeda"))
        self.actionIncluir_Insert.setShortcut(_translate("MainWindow", "Ins"))
        self.actionAlterar_Enter.setText(_translate("MainWindow", "Alterar [Enter]"))
        self.actionAlterar_Enter.setStatusTip(_translate("MainWindow", "Alterar Cripto Moeda"))
        self.actionAlterar_Enter.setShortcut(_translate("MainWindow", "Enter"))
        self.actionExcluir.setText(_translate("MainWindow", "Excluir [Del]"))
        self.actionExcluir.setStatusTip(_translate("MainWindow", "Excluir Cripto Moeda"))
        self.actionExcluir.setShortcut(_translate("MainWindow", "Del"))
        self.actionZerar_Valor.setText(_translate("MainWindow", "Zerar Valor [Z]"))
        self.actionZerar_Valor.setStatusTip(_translate("MainWindow", "Zerar Valores da(s) Cripto Moeda(s)"))
        self.actionZerar_Valor.setShortcut(_translate("MainWindow", "Z"))
        self.actionImportar_Arquivo_TXT.setText(_translate("MainWindow", "Importar Arquivo TXT [F9]"))
        self.actionImportar_Arquivo_TXT.setStatusTip(_translate("MainWindow", "Importar TXT das Cripto Moedas"))
        self.actionImportar_Arquivo_TXT.setShortcut(_translate("MainWindow", "F9"))
        self.actionExportar_Arquivo_TXT.setText(_translate("MainWindow", "Eportar Arquivo TXT [F10]"))
        self.actionExportar_Arquivo_TXT.setStatusTip(_translate("MainWindow", "Exportar Arquivo TXT das Cripto Moedas"))
        self.actionExportar_Arquivo_TXT.setShortcut(_translate("MainWindow", "F10"))
        self.actionSobre.setText(_translate("MainWindow", "Sobre"))
        self.actionEncerrar_Sitema_Esc.setText(_translate("MainWindow", "Encerrar Sitema [Esc]"))
        self.actionEncerrar_Sitema_Esc.setStatusTip(_translate("MainWindow", "Encerrar Sistema"))
        self.actionEncerrar_Sitema_Esc.setShortcut(_translate("MainWindow", "Esc"))
        self.actionConfig.setText(_translate("MainWindow", "Configurações"))
        self.actionAtualizar_Valores_F11.setText(_translate("MainWindow", "Atualizar Valores [F11]"))
        self.actionAtualizar_Valores_F11.setStatusTip(_translate("MainWindow", "Atualizar Valores da(s) Cripto Moeda(s)"))
        self.actionAtualizar_Valores_F11.setShortcut(_translate("MainWindow", "F11"))
        self.actionHist_rico.setText(_translate("MainWindow", "Histórico de Cripto Moedas [F12]"))
        self.actionHist_rico.setStatusTip(_translate("MainWindow", "Histórico de Cripto Moedas"))
        self.actionHist_rico.setShortcut(_translate("MainWindow", "F12"))

    def data_hora(self):
        current_time = QtCore.QDateTime.currentDateTime()
        timer = current_time.toString("dd/MM/yyyy  HH:mm:ss")
        self.label_data.setText(timer)

    def chama_historico(self):
        self.janela = QtWidgets.QMainWindow()
        self.tela_hist = HISTORICO.Ui_MainWindow()
        self.tela_hist.setupUi(self.janela)
        self.janela.show()

    def atualizar_dolar(self):
        try:
            requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
            requisicao_dic = requisicao.json()
            cot_dolar = requisicao_dic['USDBRL']['bid']
            try: self.lineEdit.setText("{:.4f}".format(float(cot_dolar)))
            except Exception as ERROR: MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Erro ao Consultar a Cotação do Dolar, Verifique Sua Conexão Com a WEB\n{ERROR}')
        except Exception as ERROR:
            pass

    def chama_tela_sobre(self):
        self.janela = QtWidgets.QDialog()
        self.tela_sobre = ABOUT.Ui_Dialog()
        self.tela_sobre.setupUi(self.janela)
        self.janela.show()

    def chama_tela_config(self):
        self.janela = QtWidgets.QDialog()
        self.tela_config = CONFIG.Ui_Dialog()
        self.tela_config.setupUi(self.janela)
        self.janela.show()

    def chama_tela_importar_txt(self):
        self.janela = QtWidgets.QDialog()
        self.tela_import = IMPORT_TXT.Ui_Dialog()
        self.tela_import.setupUi(self.janela)
        self.janela.show()

        def importar_dados():
            try:
                valor = 0
                texto = self.tela_import.lineEdit.text()

                arquivo = open(texto, encoding="utf-8")
                lista = []

                for linha in arquivo:
                    lista.append(linha.strip())

                for r in lista:
                    if r[0] == "2":
                        slug = r[81:111].strip()
                        quant_compra = r[642:675].strip()
                        preco_compra = r[676:709].strip()
                        data_hora_compra = str(r[710:729]).replace("|", " ")
                        data_hora_compra_banco = f"{data_hora_compra[6:10]}-{data_hora_compra[3:5]}-{data_hora_compra[0:2]} {data_hora_compra[11:]}"
                        cotacao_compra = r[730:763]

                        try:
                            conn = sqlite3.connect(BANCO_TABLE.banco)
                            c = conn.cursor()
                            c.execute(f"SELECT count(slug) FROM cripto_moed WHERE slug = '{slug}'")
                            dados = c.fetchall()
                            if dados[0][0] != 0:
                                continue
                            else:
                                c.execute("INSERT INTO cripto_moed (slug, id_crypto, valor_us, valor_rs, quant_compra, preco_compra, data_hora_compra, cotacao_compra) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                                          (slug, 0, '0.000000000000', '0.000000000000', quant_compra, preco_compra, data_hora_compra_banco, cotacao_compra))
                                conn.commit()
                                self.tela_import.progressBar.setMaximum(len(lista))
                                valor = valor + 1
                                self.tela_import.progressBar.setValue(valor)
                            conn.close()

                        except Exception as ERROR:
                            print(ERROR)
                            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')

                MENSAGEM_CAIXA.TimerMessageBox().func(f'{NOMES_SYSTEM.aviso_info}', f'Dados Inseridos Com Sucesso!', 1)
                self.tela_import.pushButton_CANCELA.click()
                self.actua()
                try:
                    conn2 = sqlite3.connect(BANCO_TABLE.banco)
                    c2 = conn2.cursor()
                    c2.execute("SELECT slug, cod FROM cripto_moed WHERE id_crypto = 0")
                    dados_nome = c2.fetchall()
                    lista_nome = []
                    lista_cod_nome = []
                    for b in dados_nome:
                        nome = b[0]
                        cod_nome = b[1]
                        lista_nome.append(nome)
                        lista_cod_nome.append(cod_nome)
                    nomes_str = ','.join(lista_nome)
                    CONSULT_API.Functions_API().thread_function_mult_slug(self.actua, nomes_str, lista_nome, lista_cod_nome)
                    conn2.close()
                except Exception as ERROR:
                    print(ERROR)

                arquivo.close()
                os.remove(texto)

            except PermissionError:
                MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Arquivo Não Encontrado!')

            except Exception as ERROR:
                print(type(ERROR))
        reconnect(self.tela_import.pushButton_SALVAR.clicked, importar_dados)

    def chama_cad_cp(self):
        if self.lineEdit.text():
            self.janela = QtWidgets.QDialog()
            self.tela = CAD_CP_M.Ui_Dialog()
            self.tela.setupUi(self.janela)
            self.janela.show()

            self.tela.label_4.setText("Incluindo")

            tratamento_dolar = float(self.lineEdit.text().replace(",", "."))
            self.tela.var_x = tratamento_dolar
            self.insere_cot_dolar()
            def verifica_se_existe():
                if self.tela.lineEdit_6.text() or self.tela.lineEdit_4.text():
                    nome = self.tela.lineEdit_6.text().lower()
                    id_crypto = self.tela.lineEdit_4.text()
                    try:
                        conn = sqlite3.connect(BANCO_TABLE.banco)
                        c = conn.cursor()
                        if id_crypto == "":
                            c.execute(f"SELECT cod, nome, id_crypto, valor_us, valor_rs, slug, quant_compra FROM cripto_moed WHERE slug = '{nome}'")
                        else:
                            c.execute(f"SELECT cod, nome, id_crypto, valor_us, valor_rs, slug, quant_compra FROM cripto_moed WHERE slug = '{nome}' OR id_crypto = '{id_crypto}'")
                        dados_lidos = c.fetchall()
                        if len(dados_lidos) == 0:
                            return None
                        else:
                            self.janela.setWindowTitle("Editar Cripto Moeda")
                            self.tela.label_4.setText("Alterando")
                            self.tela.cod = dados_lidos[0][0]
                            self.tela.lineEdit.setText(dados_lidos[0][1])
                            self.tela.lineEdit_4.setText(str(dados_lidos[0][2]))
                            self.tela.lineEdit_2.setText(str(dados_lidos[0][3]))
                            self.tela.lineEdit_3.setText(str(dados_lidos[0][4]))
                            self.tela.lineEdit_6.setText(str(dados_lidos[0][5]))
                            self.tela.lineEdit_5.setText(str(dados_lidos[0][6]))
                            self.tela.pushButton_SALVAR.setEnabled(True)

                            def salvar_dados_actua():
                                cod = self.tela.cod
                                symb_cpt = self.tela.lineEdit.text()
                                id_cripto = self.tela.lineEdit_4.text()
                                if id_cripto == "":
                                    id_cripto = 0
                                val_us = self.tela.lineEdit_2.text().replace(",", ".")
                                if val_us == "":
                                    val_us = "0"
                                trat_us = "{:_.12f}".format(float(val_us)).replace("_", "")
                                val_rs = self.tela.lineEdit_3.text().replace(",", ".")
                                if val_rs == "":
                                    val_rs = "0"
                                trat_rs = "{:_.12f}".format(float(val_rs)).replace("_", "")
                                nome_cpt = self.tela.lineEdit_6.text()
                                quant_cpt = self.tela.lineEdit_5.text().replace(",", ".")
                                if quant_cpt == "":
                                    quant_cpt = "0"
                                trat_quant = "{:_.12f}".format(float(quant_cpt)).replace("_", "")

                                try:
                                    conn = sqlite3.connect(BANCO_TABLE.banco)
                                    c = conn.cursor()
                                    c.execute(f"UPDATE cripto_moed SET nome = '{symb_cpt}',"
                                              f"id_crypto = '{id_cripto}',"
                                              f"valor_us = '{trat_us}',"
                                              f"valor_rs = '{trat_rs}',"
                                              f"slug = '{nome_cpt}',"
                                              f"quant_compra = '{trat_quant}' WHERE cod = '{cod}'")
                                    conn.commit()
                                    self.tela.pushButton_CANCELA.click()
                                    self.actua()
                                    self.tableWidget.keyboardSearch(nome_cpt)
                                    conn.close()
                                except Exception as ERROR:
                                    print(ERROR)
                                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Não Foi Possível Editar a CriptoMoeda\n{ERROR}')

                            reconnect(self.tela.pushButton_SALVAR.clicked, salvar_dados_actua)

                    except Exception as ERROR:
                        print(ERROR)
                else:
                    self.janela.setWindowTitle("Cadastrar Cripto Moeda")
                    self.tela.label_4.setText("Incluindo")
                    self.tela.cod = ""
                    self.tela.lineEdit_2.setText("")
                    self.tela.lineEdit_3.setText("")
                    self.tela.lineEdit_4.setText("")
                    self.tela.lineEdit_6.setText("")
                    self.tela.lineEdit_5.setText("")
                    reconnect(self.tela.pushButton_SALVAR.clicked, salvar_actua)

            reconnect(self.tela.lineEdit_6.editingFinished, verifica_se_existe)
            reconnect(self.tela.lineEdit_4.editingFinished, verifica_se_existe)

            def salvar_actua():
                try:
                    symb_cpt = self.tela.lineEdit.text()
                    id_cripto = self.tela.lineEdit_4.text()
                    if id_cripto == "":
                        id_cripto = 0
                    val_us = self.tela.lineEdit_2.text().replace(",", ".")
                    if val_us == "":
                        val_us = "0"
                    trat_us = "{:_.12f}".format(float(val_us)).replace("_", "")
                    val_rs = self.tela.lineEdit_3.text().replace(",", ".")
                    if val_rs == "":
                        val_rs = "0"
                    trat_rs = "{:_.12f}".format(float(val_rs)).replace("_", "")
                    nome_cpt = self.tela.lineEdit_6.text().lower()
                    quant_cpt = self.tela.lineEdit_5.text().replace(",", ".")
                    if quant_cpt == "":
                        quant_cpt = "0"
                    trat_quant = "{:_.12f}".format(float(quant_cpt)).replace("_", "")

                    try:
                        conn = sqlite3.connect(BANCO_TABLE.banco)
                        c = conn.cursor()
                        c.execute(f"SELECT count(id_crypto) FROM cripto_moed WHERE slug = '{nome_cpt}'")
                        dados = c.fetchall()
                        if dados[0][0] != 0:
                            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Cripto Moeda Já Cadastrado')
                            return None
                        c.execute("INSERT INTO cripto_moed (nome, id_crypto, valor_us, valor_rs, slug, quant_compra, preco_compra, data_hora_compra, cotacao_compra) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (symb_cpt, id_cripto, trat_us, trat_rs, nome_cpt, trat_quant, '0.000000000000', '0000-00-00 00:00:00', '0.000000000000'))
                        conn.commit()
                        self.tela.pushButton_CANCELA.click()
                        self.actua()
                        c.execute("SELECT count(*) FROM cripto_moed")
                        dados_lidos = c.fetchall()
                        num = dados_lidos[0][0] - 1
                        self.tableWidget.selectRow(num)
                        #else:
                        #    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'ID da Cripto Moeda Já Cadastrado')
                        #    return None
                        conn.close()

                    except sqlite3.IntegrityError:
                        MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Cripto Moeda Já Cadastrada')

                    except Exception as ERROR:
                        print(type(ERROR))
                        MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')

                except ValueError as ERROR:
                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Inserira os Valores Corretamente\n{ERROR}')

                except Exception as ERROR:
                    print(type(ERROR))

            reconnect(self.tela.pushButton_SALVAR.clicked, salvar_actua)

        else:
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Insira o Valor do Dólar')
            return None

    def editar_cptm(self):
        try:
            itens = self.tableWidget.selectedItems()
            cod_moed = itens[33].text()
            symbol_moed = itens[1].text()
            id_crypto = itens[0].text()
            val_moed_us = itens[3].text()
            val_moed_rs = itens[4].text()
            nome_moed = itens[2].text()
            quant_comp = itens[29].text()

            self.janela = QtWidgets.QDialog()
            self.tela = CAD_CP_M.Ui_Dialog()
            self.tela.setupUi(self.janela)
            self.janela.setWindowTitle("Editar Cripto Moeda")
            self.janela.show()

            self.tela.label_4.setText("Alterando")

            tratamento_dolar = float(self.lineEdit.text().replace(".", "").replace(",", "."))
            self.tela.cod = cod_moed
            self.tela.var_x = tratamento_dolar
            self.tela.lineEdit.setText(symbol_moed)
            self.tela.lineEdit_4.setText(id_crypto)
            self.tela.lineEdit_2.setText(val_moed_us)
            self.tela.lineEdit_3.setText(val_moed_rs)
            self.tela.lineEdit_6.setText(nome_moed)
            self.tela.lineEdit_5.setText(quant_comp)

            def salvar_dados_actua():
                cod = self.tela.cod
                symb_cpt = self.tela.lineEdit.text()
                id_cripto = self.tela.lineEdit_4.text()
                if id_cripto == "":
                    id_cripto = 0
                val_us = self.tela.lineEdit_2.text().replace(",", ".")
                if val_us == "":
                    val_us = "0"
                trat_us = "{:_.12f}".format(float(val_us)).replace("_", "")
                val_rs = self.tela.lineEdit_3.text().replace(",", ".")
                if val_rs == "":
                    val_rs = "0"
                trat_rs = "{:_.12f}".format(float(val_rs)).replace("_", "")
                nome_cpt = self.tela.lineEdit_6.text().lower()
                quant_cpt = self.tela.lineEdit_5.text().replace(",", ".")
                if quant_cpt == "":
                    quant_cpt = "0"
                trat_quant = "{:_.12f}".format(float(quant_cpt)).replace("_", "")

                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute(f"SELECT id_crypto FROM cripto_moed WHERE slug = '{nome_cpt}'")
                    dados = c.fetchall()
                    if dados[0][0] == id_cripto:
                        MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Cripto Moeda Já Cadastrado')
                        return None
                    c.execute(f"UPDATE cripto_moed SET nome = '{symb_cpt}',"
                              f"id_crypto = '{id_cripto}',"
                              f"valor_us = '{trat_us}',"
                              f"valor_rs = '{trat_rs}',"
                              f"slug = '{nome_cpt}',"
                              f"quant_compra = '{trat_quant}' WHERE cod = '{cod}'")
                    conn.commit()
                    self.tela.pushButton_CANCELA.click()
                    self.actua()
                    self.tableWidget.keyboardSearch(nome_cpt)
                    conn.close()
                except Exception as ERROR:
                    print(ERROR)
                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Não Foi Possível Editar a CriptoMoeda\n{ERROR}')
            reconnect(self.tela.pushButton_SALVAR.clicked, salvar_dados_actua)
        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Selecione o Registro!')


    def excluir_cpt(self):
        try:
            linha = self.tableWidget.currentRow()
            itens = self.tableWidget.selectedItems()
            cod_moed = itens[33].text()
            nome_moed = itens[2].text()

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Deletar Cripto Moeda")
            msg.setWindowIcon(QtGui.QIcon("images/moed.png"))
            msg.setText(f'Deseja Deletar "{nome_moed}" da Sua Base de Dados')
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            button_sim = msg.button(QtWidgets.QMessageBox.Yes)
            button_sim.setIcon(QtGui.QIcon("images/sim.png"))
            button_sim.setText('Sim')
            button_nao = msg.button(QtWidgets.QMessageBox.No)
            button_nao.setIcon(QtGui.QIcon("images/nao.png"))
            button_nao.setText("Não")
            resp = msg.exec_()

            if resp == QtWidgets.QMessageBox.Yes:
                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute(f"DELETE FROM cripto_moed WHERE cod = '{cod_moed}'")
                    conn.commit()
                    conn.close()
                    self.tableWidget.removeRow(linha)
                    self.actua()
                except Exception as ERROR:
                    print(ERROR)
                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Não Foi Possível Deletar a Cripto Moeda\n{ERROR}')
            else:
                return None
        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Selecione o Registro!')

    def zerar_valores(self):
        try:
            itens = self.tableWidget.selectedItems()
            cod_moed = itens[33].text()
            nome_moed = itens[2].text()

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Zerar Valores")
            msg.setWindowIcon(QtGui.QIcon("images/moed.png"))
            msg.setText("Deseja Zerar os Valores das Cripto Moedas?")
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.YesToAll |QtWidgets.QMessageBox.No)
            button_sim_uni = msg.button(QtWidgets.QMessageBox.Yes)
            button_sim_uni.setText(f'Zerar Apenas Para "{nome_moed}"')
            button_sim_geral = msg.button(QtWidgets.QMessageBox.YesToAll)
            button_sim_geral.setText("Zerar Todas Cripto Moedas")
            button_nao = msg.button(QtWidgets.QMessageBox.No)
            button_nao.setText("Cancelar")
            resp = msg.exec_()

            if resp == QtWidgets.QMessageBox.Yes:
                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute(f"UPDATE cripto_moed SET valor_us = '0.000000000000', valor_rs = '0.000000000000' WHERE cod = '{cod_moed}'")
                    conn.commit()
                    conn.close()
                    self.actua()
                except Exception as ERROR:
                    print(ERROR)
                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Não Foi Possível\n{ERROR}')

            if resp == QtWidgets.QMessageBox.YesToAll:
                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute("SELECT cod FROM cripto_moed")
                    dados_lidos = c.fetchall()
                    for b in dados_lidos:
                        codigo = b[0]
                        c.execute(f"UPDATE cripto_moed SET valor_us = '0.000000000000', valor_rs = '0.000000000000' WHERE cod = '{codigo}'")
                        conn.commit()
                    conn.close()
                    self.actua()
                except Exception as ERROR:
                    print(ERROR)
                    MENSAGEM_CAIXA.MessageBoxs.information(self, f'{NOMES_SYSTEM.aviso_erro}', f'Não Foi Possível Atualizar os Valores\n{ERROR}')
            else:
                return None
        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Selecione o Registro!')

    def chama_gera_txt(self):
        self.janela = QtWidgets.QDialog()
        self.tela_txt = EXPORT_TXT.Ui_Dialog()
        self.tela_txt.setupUi(self.janela)
        self.janela.show()

        data_hora = self.label_data.text()
        cot_dolar = self.lineEdit.text().replace(",", ".")

        self.tela_txt.data = data_hora[0:10]
        self.tela_txt.hora = data_hora[12:20]
        self.tela_txt.cot_dolar = cot_dolar

    def insere_cot_dolar(self):
        cot_dolar = self.lineEdit.text()
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("SELECT count(*) FROM cot_dolar")
            dados_lidos = c.fetchall()
            if dados_lidos[0][0] == 0:
                c.execute("INSERT INTO cot_dolar (valor) VALUES (?)", (cot_dolar,))
            else:
                c.execute("DELETE FROM cot_dolar")
                c.execute("INSERT INTO cot_dolar (valor) VALUES (?)", (cot_dolar,))
            conn.commit()
            conn.close()
        except Exception as ERROR:
            print(ERROR)

    def mostrar_cot_dolar(self):
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("SELECT count(*) FROM cot_dolar")
            dados_lidos = c.fetchall()
            if dados_lidos[0][0] == 0:
                try: self.lineEdit.setText(str("{:.4f}".format(float(cot_dolar.cot_dolar))))
                except: self.lineEdit.setText("")
            else:
                c.execute("SELECT valor FROM cot_dolar")
                dados_lidos = c.fetchall()
                valor = dados_lidos[0][0]
                try: self.lineEdit.setText(str("{:.4f}".format(float(cot_dolar.cot_dolar))))
                except: self.lineEdit.setText(str("{:.4f}".format(float(valor))))
            conn.close()
        except Exception as ERROR:
            print(ERROR)

    def formatar_line_cot_dolar(self):
        try:
            texto = self.lineEdit.text().replace(",", ".")
            self.lineEdit.setText("{:.4f}".format(float(texto)))
        except Exception as ERROR:
            print(ERROR)

    def question_actua(self):
        try:
            itens = self.tableWidget.selectedItems()
            cod_moed = itens[0].text()
            nome_moed = itens[2].text()
            cod_resgt = itens[33].text()

            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Atualizar Valores")
            msg.setWindowIcon(QtGui.QIcon("images/moed.png"))
            msg.setText("Deseja Atualizar os Valores das Cripto Moedas?")
            msg.setIcon(QtWidgets.QMessageBox.Question)
            msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.YesToAll | QtWidgets.QMessageBox.No)
            button_sim_uni = msg.button(QtWidgets.QMessageBox.Yes)
            button_sim_uni.setText(f'Atualizar Apenas Para "{nome_moed}"')
            button_sim_geral = msg.button(QtWidgets.QMessageBox.YesToAll)
            button_sim_geral.setText("Atualizar Todas Cripto Moedas")
            button_nao = msg.button(QtWidgets.QMessageBox.No)
            button_nao.setText("Cancelar")
            resp = msg.exec_()

            if resp == QtWidgets.QMessageBox.Yes:
                CONSULT_API.Functions_API().thread_function_uni(self.actua, cod_moed, nome_moed, cod_resgt)
                self.pushButton_pesq_dol.click()

            if resp == QtWidgets.QMessageBox.YesToAll:
                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute("SELECT id_crypto, cod FROM cripto_moed WHERE id_crypto > 0")
                    dados_id = c.fetchall()
                    lista_id_crypto = []
                    lista_cod = []
                    for a in dados_id:
                        id_c = a[0]
                        cod = a[1]
                        lista_id_crypto.append(id_c)
                        lista_cod.append(cod)
                    id_crypro_str = NOMES_SYSTEM.list_to_str(lista_id_crypto)
                    CONSULT_API.Functions_API().thread_function_mult_cod(self.actua, id_crypro_str, lista_id_crypto, lista_cod)
                    self.pushButton_pesq_dol.click()
                    c.execute("SELECT slug, cod FROM cripto_moed WHERE id_crypto = 0")
                    dados_nome = c.fetchall()
                    lista_nome = []
                    lista_cod_nome = []
                    for b in dados_nome:
                        nome = b[0]
                        cod_nome = b[1]
                        lista_nome.append(nome)
                        lista_cod_nome.append(cod_nome)
                    nomes_str = ','.join(lista_nome)
                    self.pushButton_pesq_dol.click()
                    CONSULT_API.Functions_API().thread_function_mult_slug(self.actua, nomes_str, lista_nome, lista_cod_nome)
                    conn.close()
                except Exception as ERROR:
                    print(ERROR)
            else:
                return None
        except IndexError:
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', 'Selecione o Registro!')
        except KeyError as ERROR:
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Verifique Sua Chave API\n{ERROR}')
        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')

    def encerrar_system(self, MainWindow):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Encerrar o Sistema")
        msg.setWindowIcon(QtGui.QIcon("images/moed.png"))
        msg.setText("Encerrar o Sistema?")
        msg.setIconPixmap(QtGui.QPixmap("images/moed.png"))
        msg.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        button_sim = msg.button(QtWidgets.QMessageBox.Yes)
        button_sim.setText("Sim")
        button_sim.setIcon(QtGui.QIcon("images/sim.png"))
        button_nao = msg.button(QtWidgets.QMessageBox.No)
        button_nao.setText("Não")
        button_nao.setIcon(QtGui.QIcon("images/nao.png"))
        resp = msg.exec_()

        if resp == QtWidgets.QMessageBox.Yes:
            MainWindow.close()
        else:
            return None

    def actua(self):
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("SELECT id_crypto, nome, slug, valor_us, valor_rs, circulating_supply, cmc_rank, date_added, is_active, is_fiat,"
                      "last_update, max_supply, num_market_pairs, fully_diluted_market_cap, quote_last_updated, market_cap, market_cap_dominance,"
                      "percent_change_1h, percent_change_24h, percent_change_30d, percent_change_60d, percent_change_7d, percent_change_90d, price,"
                      "volume_24h, volume_change_24h, name, symbol, total_supply, quant_compra, preco_compra, data_hora_compra, cotacao_compra, cod FROM cripto_moed")
            dados_lidos = c.fetchall()
            self.tableWidget.setRowCount(len(dados_lidos))
            self.tableWidget.resizeColumnToContents(0)
            self.tableWidget.setColumnCount(34)
            for i in range(0, len(dados_lidos)):
                for j in range(0, 34):
                    item = QtWidgets.QTableWidgetItem(str(dados_lidos[i][j]))
                    if j == 0:
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    if j > 2:
                        item.setTextAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
                    self.tableWidget.setItem(i, j, item)
            conn.close()

            header = self.tableWidget.horizontalHeader()
            header.setSectionResizeMode(0, 120)
            header.setSectionResizeMode(1, 120)
            header.setSectionResizeMode(2, 120)
            header.setSectionResizeMode(3, 120)
            header.setSectionResizeMode(4, 120)
            header.setSectionResizeMode(5, 120)
            header.setSectionResizeMode(6, 120)
            header.setSectionResizeMode(7, 120)
            header.setSectionResizeMode(8, 120)
            header.setSectionResizeMode(9, 120)
            header.setSectionResizeMode(10, 120)
            header.setSectionResizeMode(11, 120)
            header.setSectionResizeMode(12, 120)
            header.setSectionResizeMode(13, 120)
            header.setSectionResizeMode(14, 120)
            header.setSectionResizeMode(15, 120)
            header.setSectionResizeMode(16, 120)
            header.setSectionResizeMode(17, 120)
            header.setSectionResizeMode(18, 120)
            header.setSectionResizeMode(19, 120)
            header.setSectionResizeMode(20, 120)
            header.setSectionResizeMode(21, 120)
            header.setSectionResizeMode(22, 120)
            header.setSectionResizeMode(23, 120)
            header.setSectionResizeMode(24, 120)
            header.setSectionResizeMode(25, 120)
            header.setSectionResizeMode(26, 120)
            header.setSectionResizeMode(27, 120)
            header.setSectionResizeMode(28, 120)
            header.setSectionResizeMode(29, 120)
            header.setSectionResizeMode(30, 120)
            header.setSectionResizeMode(31, 120)
            header.setSectionResizeMode(32, 120)
            header.setSectionResizeMode(33, 120)

        except Exception as ERROR:
            print(ERROR)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
