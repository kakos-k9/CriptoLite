import MENSAGEM_CAIXA
import NOMES_SYSTEM
import sqlite3
import CONFIG
import NOME_DB
import PyQt5.QtWidgets
import keyboard
import os

banco = NOME_DB.most_camin_bd()

class Cria_Tabelas():

    def table_cripto(self):
        try:
            conn = sqlite3.connect(banco)
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS cripto_moed(cod INTEGER PRIMARY KEY AUTOINCREMENT,"
                      "nome                               VARCHAR(10),         "
                      "valor_us                           VARCHAR(40),         "
                      "valor_rs                           VARCHAR(40),         "
                      "circulating_supply                 VARCHAR(40),         "
                      "cmc_rank                           NUMERIC,             "
                      "date_added                         DATETIME,            "
                      "id_crypto                          INT,                 "
                      "is_active                          VARCHAR(1),          "
                      "is_fiat                            VARCHAR(1),          "
                      "last_update                        DATETIME,            "
                      "max_supply                         VARCHAR(40),         "
                      "name                               VARCHAR(30),         "
                      "num_market_pairs                   VARCHAR(40),         "
                      "fully_diluted_market_cap           VARCHAR(40),         "
                      "quote_last_updated                 DATETIME,            "
                      "market_cap                         VARCHAR(40),         "
                      "market_cap_dominance               VARCHAR(40),         "
                      "percent_change_1h                  VARCHAR(40),         "
                      "percent_change_24h                 VARCHAR(40),         "
                      "percent_change_30d                 VARCHAR(40),         "
                      "percent_change_60d                 VARCHAR(40),         "
                      "percent_change_7d                  VARCHAR(40),         "
                      "percent_change_90d                 VARCHAR(40),         "
                      "price                              VARCHAR(40),         "
                      "volume_24h                         VARCHAR(40),         "
                      "volume_change_24h                  VARCHAR(40),         "
                      #"self_reported_circulating_supply   VARCHAR(10),         "
                      #"self_reported_market_cap           VARCHAR(10),         "
                      "slug                               VARCHAR(30),         "
                      "symbol                             VARCHAR(10),         "
                      "total_supply                       VARCHAR(40),         "
                      "quant_compra                       VARCHAR(40),         "
                      "preco_compra                       VARCHAR(40),         "
                      "data_hora_compra                   DATETIME,            "
                      "cotacao_compra                     VARCHAR(40))         ")
            conn.commit()
            conn.close()
        except Exception as ERROR:
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Erro ao Criar a Tabela\n{ERROR}')
            print(ERROR)
            #print(type(ERROR))

        #except sqlite3.OperationalError:
        #    self.janela = PyQt5.QtWidgets.QDialog()
        #    self.tela = CONFIG.Ui_Dialog()
        #    self.tela.setupUi(self.janela)
        #    self.janela.show()
        #    keyboard.press("Tab")


    # TABELA DE HISTÓRICO
    def table_historic(self):
        try:
            conn = sqlite3.connect(banco)
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS historic_cripto_moed(cod INTEGER PRIMARY KEY AUTOINCREMENT,"
                      "nome                               VARCHAR(10),         "
                      "valor_us                           VARCHAR(40),         "
                      "valor_rs                           VARCHAR(40),         "
                      "circulating_supply                 VARCHAR(40),         "
                      "cmc_rank                           NUMERIC,             "
                      "date_added                         DATETIME,            "
                      "id_crypto                          INT,                 "
                      "is_active                          VARCHAR(1),          "
                      "is_fiat                            VARCHAR(1),          "
                      "last_update                        DATETIME,            "
                      "max_supply                         VARCHAR(40),         "
                      "name                               VARCHAR(30),         "
                      "num_market_pairs                   VARCHAR(40),         "
                      "fully_diluted_market_cap           VARCHAR(40),         "
                      "quote_last_updated                 DATETIME,            "
                      "market_cap                         VARCHAR(40),         "
                      "market_cap_dominance               VARCHAR(40),         "
                      "percent_change_1h                  VARCHAR(40),         "
                      "percent_change_24h                 VARCHAR(40),         "
                      "percent_change_30d                 VARCHAR(40),         "
                      "percent_change_60d                 VARCHAR(40),         "
                      "percent_change_7d                  VARCHAR(40),         "
                      "percent_change_90d                 VARCHAR(40),         "
                      "price                              VARCHAR(40),         "
                      "volume_24h                         VARCHAR(40),         "
                      "volume_change_24h                  VARCHAR(40),         "
                      #"self_reported_circulating_supply   VARCHAR(10),         "
                      #"self_reported_market_cap           VARCHAR(10),         "
                      "slug                               VARCHAR(30),         "
                      "symbol                             VARCHAR(15),         "
                      "total_supply                       VARCHAR(40),         "
                      "quant_compra                       VARCHAR(40),         "
                      "preco_compra                       VARCHAR(40),         "
                      "data_hora_compra                   DATETIME,            "
                      "cotacao_compra                     VARCHAR(40))         ")
            c.execute("PRAGMA table_info(historic_cripto_moed)")
            dados = c.fetchall()
            for a in dados:
                cod = a[0]
            if cod != 33:
                c.execute("ALTER TABLE historic_cripto_moed ADD quant_compra VARCHAR(40)")
                c.execute("ALTER TABLE historic_cripto_moed ADD preco_compra VARCHAR(40)")
                c.execute("ALTER TABLE historic_cripto_moed ADD data_hora_compra DATETIME")
                c.execute("ALTER TABLE historic_cripto_moed ADD cotacao_compra VARCHAR(40)")
            conn.commit()
            conn.close()
        except Exception as ERROR:
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Erro ao Criar a Tabela\n{ERROR}')
            print(ERROR)

    def table_cot_dola(self):
        try:
            conn = sqlite3.connect(banco)
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS cot_dolar(cod INTEGER PRIMARY KEY AUTOINCREMENT,"
                      "valor NUMERIC)")
            conn.commit()
            conn.close()
        except Exception as ERROR:
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Erro ao Criar a Tabela cot\n{ERROR}')


    def table_config(self):
        try:
            conn = sqlite3.connect(banco)
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS config(cod INTEGER PRIMARY KEY,"
                      "desc_config VARCHAR(120))")
            conn.commit()
            conn.close()
        except Exception as ERROR:
            print(ERROR)

    def insere_caminho_export_txt(self):
        try:
            conn = sqlite3.connect(banco)
            c = conn.cursor()
            c.execute("SELECT count(desc_config) FROM config WHERE cod = 2")
            dados = c.fetchall()
            if dados[0][0] == 0:
                caminho_pdr = f"{os.environ['USERPROFILE']}\\Desktop"
                c.execute("INSERT INTO config (cod, desc_config) VALUES (?, ?)", ('2', caminho_pdr))
                conn.commit()
            else:
                return None
            conn.close()
        except Exception as ERROR:
            print(ERROR)

    def insere_caminho_import_txt(self):
        try:
            conn = sqlite3.connect(banco)
            c = conn.cursor()
            c.execute("SELECT count(desc_config) FROM config WHERE cod = 3")
            dados = c.fetchall()
            if dados[0][0] == 0:
                caminho_pdr = f"{os.environ['USERPROFILE']}\\Desktop"
                c.execute("INSERT INTO config (cod, desc_config) VALUES (?, ?)", ('3', caminho_pdr))
                conn.commit()
            else:
                return None
            conn.close()
        except Exception as ERROR:
            print(ERROR)

