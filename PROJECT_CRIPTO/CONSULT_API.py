from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
from threading import Thread
from PyQt5 import QtWidgets
import MENSAGEM_CAIXA
import NOMES_SYSTEM
import BANCO_TABLE
import CONFIG
import sqlite3
import pprint
import MAIN
import json
import sys


class Functions_API(object):

    def thread_function_uni(self, actua, codT, simboloT, cod_regsT):
        function = Thread(target=self.atualizar_valores_uni(actua=actua, cod=codT, nome=simboloT, cod_regs=cod_regsT))
        function.start()

    def atualizar_valores_uni(self, actua=None, cod=None, nome=None, cod_regs=None):
        try:
            if cod == "0":
                metd = nome
                param = "slug"
            else:
                metd = cod
                param = "id"
            pp = pprint.PrettyPrinter(indent=4)
            self.janela = QtWidgets.QDialog()
            self.tela_key = CONFIG.Ui_Dialog()
            self.tela_key.setupUi(self.janela)
            key = self.tela_key.lineEdit_4.text()
            url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            print(url)
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': key,
            }
            parameters = {
                param: metd
            }
            session = Session()
            session.headers.update(headers)
            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                data = json.loads(response.text)

            for a in data['data']:
                circulating_supply = str(data['data'][a]['circulating_supply']).replace("None", "0")
                cmc_rank = str(data['data'][a]['cmc_rank']).replace("None", "0")
                date_added = data['data'][a]['date_added']
                date_added_semC = date_added[:19]
                date_added_format = date_added_semC.replace("T", " ")
                id_crypto = data['data'][a]['id']
                is_active = str(data['data'][a]['is_active']).replace("0", "N").replace("1", "S")
                is_fiat = str(data['data'][a]['is_fiat']).replace("0", "N").replace("1", "S")
                last_updated = data['data'][a]['last_updated']
                last_updated_semC = last_updated[:19]
                last_updated_format = last_updated_semC.replace("T", " ")
                max_supply = str(data['data'][a]['max_supply']).replace("None", "0")
                name = data['data'][a]['name']
                num_market_pairs = str(data['data'][a]['num_market_pairs']).replace("None", "0")
                # platform = data['data'][nome]['platform'] <- NÃO VAI
                fully_diluted_market_cap = str(data['data'][a]['quote']['USD']['fully_diluted_market_cap']).replace("None", "0")
                quote_last_update = data['data'][a]['quote']['USD']['last_updated']
                quote_last_update_semC = quote_last_update[:19]
                quote_last_update_format = quote_last_update_semC.replace("T", " ")
                market_cap = str(data['data'][a]['quote']['USD']['market_cap']).replace("None", "0")
                market_cap_dominance = str(data['data'][a]['quote']['USD']['market_cap_dominance']).replace("None", "0")
                percent_change_1h = str(data['data'][a]['quote']['USD']['percent_change_1h']).replace("None", "0")
                percent_change_24h = str(data['data'][a]['quote']['USD']['percent_change_24h']).replace("None", "0")
                percent_change_30d = str(data['data'][a]['quote']['USD']['percent_change_30d']).replace("None", "0")
                percent_change_60d = str(data['data'][a]['quote']['USD']['percent_change_60d']).replace("None", "0")
                percent_change_7d = str(data['data'][a]['quote']['USD']['percent_change_7d']).replace("None", "0")
                percent_change_90d = str(data['data'][a]['quote']['USD']['percent_change_90d']).replace("None", "0")
                price = str(data['data'][a]['quote']['USD']['price']).replace("None", "0")
                volume_24h = str(data['data'][a]['quote']['USD']['volume_24h']).replace("None", "0")
                volume_change_24h = str(data['data'][a]['quote']['USD']['volume_change_24h']).replace("None", "0")
                # ele_reported_circulating_supply = data['data'][metd]['self_reported_circulating_supply'] <- NÃO VAI
                # ele_reported_market_cap = data['data'][metd]['self_reported_market_cap'] <- NÃO VAI
                slug = data['data'][a]['slug']
                symbol = str(data['data'][a]['symbol'])
                total_supply = str(data['data'][a]['total_supply']).replace("None", "0")
    
                trat_circulating_supply = "{:.12f}".format(float(circulating_supply))
                trat_max_supply = "{:.12f}".format(float(max_supply))
                trat_fully_diluted_market_cap = "{:.12f}".format(float(fully_diluted_market_cap))
                trat_market_cap = "{:.12f}".format(float(market_cap))
                trat_market_cap_dominance = "{:.12f}".format(float(market_cap_dominance))
                trat_percent_change_1h = "{:.12f}".format(float(percent_change_1h))
                trat_percent_change_24h = "{:.12f}".format(float(percent_change_24h))
                trat_percent_change_30d = "{:.12f}".format(float(percent_change_30d))
                trat_percent_change_60d = "{:.12f}".format(float(percent_change_60d))
                trat_percent_change_7d = "{:.12f}".format(float(percent_change_7d))
                trat_percent_change_90d = "{:.12f}".format(float(percent_change_90d))
                trat_price = "{:.12f}".format(float(price))
                trat_volume_24h = "{:.12f}".format(float(volume_24h))
                trat_volume_change_24h = "{:.12f}".format(float(volume_change_24h))
                trat_total_supply = "{:.12f}".format(float(total_supply))
                self.janela = QtWidgets.QMainWindow()
                self.tela_p = MAIN.Ui_MainWindow()
                self.tela_p.setupUi(self.janela)
                trat_val_rs = "{:.12f}".format(float(float(price) * float(self.tela_p.lineEdit.text())))
    
                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute(f"UPDATE cripto_moed SET nome = '{symbol}',"
                              f"valor_us = '{trat_price}',"
                              f"valor_rs = '{trat_val_rs}',"
                              f"circulating_supply = '{trat_circulating_supply}',"
                              f"cmc_rank = '{cmc_rank}',"
                              f"date_added = '{date_added_format}',"
                              f"id_crypto = '{id_crypto}',"
                              f"is_active = '{is_active}',"
                              f"is_fiat = '{is_fiat}',"
                              f"last_update = '{last_updated_format}',"
                              f"max_supply = '{trat_max_supply}',"
                              f"name = '{name}',"
                              f"num_market_pairs = '{num_market_pairs}',"
                              f"fully_diluted_market_cap = '{trat_fully_diluted_market_cap}',"
                              f"quote_last_updated = '{quote_last_update_format}',"
                              f"market_cap = '{trat_market_cap}',"
                              f"market_cap_dominance = '{trat_market_cap_dominance}',"
                              f"percent_change_1h = '{trat_percent_change_1h}',"
                              f"percent_change_24h = '{trat_percent_change_24h}',"
                              f"percent_change_30d = '{trat_percent_change_30d}',"
                              f"percent_change_60d = '{trat_percent_change_60d}',"
                              f"percent_change_7d = '{trat_percent_change_7d}',"
                              f"percent_change_90d = '{trat_percent_change_90d}',"
                              f"price = '{trat_price}',"
                              f"volume_24h = '{trat_volume_24h}',"
                              f"volume_change_24h = '{trat_volume_change_24h}',"
                              # f"self_reported_circulating_supply = '{ele_reported_circulating_supply}',"
                              # f"self_reported_market_cap = '{ele_reported_market_cap}',"
                              f"slug = '{slug}',"
                              f"symbol = '{symbol}',"
                              f"total_supply = '{trat_total_supply}' WHERE cod = '{cod_regs}'")
                    conn.commit()
                    conn.close()
                    self.insere_table_historic(symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                          date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                          name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                          trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                          trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                          trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                          trat_volume_change_24h, slug, symbol, trat_total_supply)
                    MENSAGEM_CAIXA.TimerMessageBox().func(f'{NOMES_SYSTEM.aviso_info}', f'Moeda {symbol} Atualizada Com Sucesso!', 1)
                    actua()
                except Exception as ERROR:
                    print(ERROR)
                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')

        except KeyError as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Verifique Sua Chave API ou Certifique-se Que a Moeda {nome} Com o ID {cod} Existe')

        except Exception as ERROR:
            print(ERROR)
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')

    def thread_function_mult_cod(self, actua, id_str, id_list, cod_regsS):
        function = Thread(target=self.atualizar_moedas_geral_cod(actua, id_str=id_str, id_list=id_list, cod_regs=cod_regsS))
        function.start()

    def atualizar_moedas_geral_cod(self, actua, id_str=str, id_list=list, cod_regs=list):
        try:
            pp = pprint.PrettyPrinter(indent=4)
            self.janela = QtWidgets.QDialog()
            self.tela_key = CONFIG.Ui_Dialog()
            self.tela_key.setupUi(self.janela)
            key = self.tela_key.lineEdit_4.text()
            url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            print(url)
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': key,
            }
            parameters = {
                "id": id_str
            }
            session = Session()
            session.headers.update(headers)
            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                data = json.loads(response.text)

            for a, b in zip(id_list, cod_regs):
                circulating_supply = str(data['data'][str(a)]['circulating_supply']).replace("None", "0")
                cmc_rank = str(data['data'][str(a)]['cmc_rank']).replace("None", "0")
                date_added = data['data'][str(a)]['date_added']
                date_added_semC = date_added[:19]
                date_added_format = date_added_semC.replace("T", " ")
                id_crypto = data['data'][str(a)]['id']
                is_active = str(data['data'][str(a)]['is_active']).replace("0", "N").replace("1", "S")
                is_fiat = str(data['data'][str(a)]['is_fiat']).replace("0", "N").replace("1", "S")
                last_updated = data['data'][str(a)]['last_updated']
                last_updated_semC = last_updated[:19]
                last_updated_format = last_updated_semC.replace("T", " ")
                max_supply = str(data['data'][str(a)]['max_supply']).replace("None", "0")
                name = data['data'][str(a)]['name']
                num_market_pairs = str(data['data'][str(a)]['num_market_pairs']).replace("None", "0")
                # platform = data['data'][nome]['platform'] <- NÃO VAI
                fully_diluted_market_cap = str(data['data'][str(a)]['quote']['USD']['fully_diluted_market_cap']).replace("None", "0")
                quote_last_update = data['data'][str(a)]['quote']['USD']['last_updated']
                quote_last_update_semC = quote_last_update[:19]
                quote_last_update_format = quote_last_update_semC.replace("T", " ")
                market_cap = str(data['data'][str(a)]['quote']['USD']['market_cap']).replace("None", "0")
                market_cap_dominance = str(data['data'][str(a)]['quote']['USD']['market_cap_dominance']).replace("None", "0")
                percent_change_1h = str(data['data'][str(a)]['quote']['USD']['percent_change_1h']).replace("None", "0")
                percent_change_24h = str(data['data'][str(a)]['quote']['USD']['percent_change_24h']).replace("None", "0")
                percent_change_30d = str(data['data'][str(a)]['quote']['USD']['percent_change_30d']).replace("None", "0")
                percent_change_60d = str(data['data'][str(a)]['quote']['USD']['percent_change_60d']).replace("None", "0")
                percent_change_7d = str(data['data'][str(a)]['quote']['USD']['percent_change_7d']).replace("None", "0")
                percent_change_90d = str(data['data'][str(a)]['quote']['USD']['percent_change_90d']).replace("None", "0")
                price = str(data['data'][str(a)]['quote']['USD']['price']).replace("None", "0")
                volume_24h = str(data['data'][str(a)]['quote']['USD']['volume_24h']).replace("None", "0")
                volume_change_24h = str(data['data'][str(a)]['quote']['USD']['volume_change_24h']).replace("None", "0")
                # ele_reported_circulating_supply = data['data'][metd]['self_reported_circulating_supply'] <- NÃO VAI
                # ele_reported_market_cap = data['data'][metd]['self_reported_market_cap'] <- NÃO VAI
                slug = data['data'][str(a)]['slug']
                symbol = str(data['data'][str(a)]['symbol'])
                total_supply = str(data['data'][str(a)]['total_supply']).replace("None", "0")

                trat_circulating_supply = "{:.12f}".format(float(circulating_supply))
                trat_fully_diluted_market_cap = "{:.12f}".format(float(fully_diluted_market_cap))
                trat_market_cap = "{:.12f}".format(float(market_cap))

                trat_market_cap_dominance = "{:.12f}".format(float(market_cap_dominance))
                trat_max_supply = "{:.12f}".format(float(max_supply))
                trat_percent_change_1h = "{:.12f}".format(float(percent_change_1h))
                trat_percent_change_24h = "{:.12f}".format(float(percent_change_24h))
                trat_percent_change_30d = "{:.12f}".format(float(percent_change_30d))
                trat_percent_change_60d = "{:.12f}".format(float(percent_change_60d))
                trat_percent_change_7d = "{:.12f}".format(float(percent_change_7d))
                trat_percent_change_90d = "{:.12f}".format(float(percent_change_90d))
                trat_price = "{:.12f}".format(float(price))
                trat_volume_24h = "{:.12f}".format(float(volume_24h))
                trat_volume_change_24h = "{:.12f}".format(float(volume_change_24h))
                trat_total_supply = "{:.12f}".format(float(total_supply))
                self.janela = QtWidgets.QMainWindow()
                self.tela_p = MAIN.Ui_MainWindow()
                self.tela_p.setupUi(self.janela)
                trat_val_rs = "{:.12f}".format(float(float(price) * float(self.tela_p.lineEdit.text())))
                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute(f"UPDATE cripto_moed SET nome = '{symbol}',"
                              f"valor_us = '{trat_price}',"
                              f"valor_rs = '{trat_val_rs}',"
                              f"circulating_supply = '{trat_circulating_supply}',"
                              f"cmc_rank = '{cmc_rank}',"
                              f"date_added = '{date_added_format}',"
                              f"id_crypto = '{id_crypto}',"
                              f"is_active = '{is_active}',"
                              f"is_fiat = '{is_fiat}',"
                              f"last_update = '{last_updated_format}',"
                              f"max_supply = '{trat_max_supply}',"
                              f"name = '{name}',"
                              f"num_market_pairs = '{num_market_pairs}',"
                              f"fully_diluted_market_cap = '{trat_fully_diluted_market_cap}',"
                              f"quote_last_updated = '{quote_last_update_format}',"
                              f"market_cap = '{trat_market_cap}',"
                              f"market_cap_dominance = '{trat_market_cap_dominance}',"
                              f"percent_change_1h = '{trat_percent_change_1h}',"
                              f"percent_change_24h = '{trat_percent_change_24h}',"
                              f"percent_change_30d = '{trat_percent_change_30d}',"
                              f"percent_change_60d = '{trat_percent_change_60d}',"
                              f"percent_change_7d = '{trat_percent_change_7d}',"
                              f"percent_change_90d = '{trat_percent_change_90d}',"
                              f"price = '{trat_price}',"
                              f"volume_24h = '{trat_volume_24h}',"
                              f"volume_change_24h = '{trat_volume_change_24h}',"
                              # f"self_reported_circulating_supply = '{ele_reported_circulating_supply}',"
                              # f"self_reported_market_cap = '{ele_reported_market_cap}',"
                              f"slug = '{slug}',"
                              f"symbol = '{symbol}',"
                              f"total_supply = '{trat_total_supply}' WHERE cod = '{b}'")
                    conn.commit()
                    conn.close()
                    self.insere_table_historic(symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                          date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                          name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                          trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                          trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                          trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                          trat_volume_change_24h, slug, symbol, trat_total_supply)

                except sqlite3.IntegrityError:
                    MENSAGEM_CAIXA.TimerMessageBox().func(f'{NOMES_SYSTEM.aviso_info}', f'A Moeda Com ID {id_crypto} Já Existe Na Sua Base de Dados, Estamos Apagando a Réplica', 1)
                    c.execute(f"DELETE FROM cripto_moed WHERE cod = {b}")
                    conn.commit()
                    conn.close()
                    actua()

                except Exception as ERROR:
                    print(type(ERROR))
                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')
                MENSAGEM_CAIXA.TimerMessageBox().func(f'{NOMES_SYSTEM.aviso_info}', f'Moeda {symbol} Atualizada Com Sucesso!', 1)
                actua()

        except KeyError as ERROR:
            e = str(data['status']['error_message'])
            es = e.split(" ")
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Verifique Sua Chave API ou Certifique-se que a Moeda Com o ID {es[4]} Existe')

        except Exception as ERROR:
            print(type(ERROR))
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')

    def thread_function_mult_slug(self, actua, simbol_str, simbol_list, cod_regsS):
        function = Thread(target=self.atualizar_moedas_geral_slug(actua=actua, simbol_str=simbol_str, simbol_list=simbol_list, cod_regs=cod_regsS))
        function.start()

    def atualizar_moedas_geral_slug(self, actua, simbol_str=str, simbol_list=list, cod_regs=list):
        try:
            pp = pprint.PrettyPrinter(indent=4)
            self.janela = QtWidgets.QDialog()
            self.tela_key = CONFIG.Ui_Dialog()
            self.tela_key.setupUi(self.janela)
            key = self.tela_key.lineEdit_4.text()
            url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            print(url)
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': key,
            }
            parameters = {
                "slug": simbol_str
            }
            session = Session()
            session.headers.update(headers)
            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                data = json.loads(response.text)

            for b, c in zip(cod_regs, data['data']):
                circulating_supply = str(data['data'][str(c)]['circulating_supply']).replace("None", "0")
                cmc_rank = str(data['data'][str(c)]['cmc_rank']).replace("None", "0")
                date_added = data['data'][str(c)]['date_added']
                date_added_semC = date_added[:19]
                date_added_format = date_added_semC.replace("T", " ")
                id_crypto = data['data'][str(c)]['id']
                is_active = str(data['data'][str(c)]['is_active']).replace("0", "N").replace("1", "S")
                is_fiat = str(data['data'][str(c)]['is_fiat']).replace("0", "N").replace("1", "S")
                last_updated = data['data'][str(c)]['last_updated']
                last_updated_semC = last_updated[:19]
                last_updated_format = last_updated_semC.replace("T", " ")
                max_supply = str(data['data'][str(c)]['max_supply']).replace("None", "0")
                name = data['data'][str(c)]['name']
                num_market_pairs = str(data['data'][str(c)]['num_market_pairs']).replace("None", "0")
                # platform = data['data'][nome]['platform'] <- NÃO VAI
                fully_diluted_market_cap = str(data['data'][str(c)]['quote']['USD']['fully_diluted_market_cap']).replace("None", "0")
                quote_last_update = data['data'][str(c)]['quote']['USD']['last_updated']
                quote_last_update_semC = quote_last_update[:19]
                quote_last_update_format = quote_last_update_semC.replace("T", " ")
                market_cap = str(data['data'][str(c)]['quote']['USD']['market_cap']).replace("None", "0")
                market_cap_dominance = str(data['data'][str(c)]['quote']['USD']['market_cap_dominance']).replace("None", "0")
                percent_change_1h = str(data['data'][str(c)]['quote']['USD']['percent_change_1h']).replace("None", "0")
                percent_change_24h = str(data['data'][str(c)]['quote']['USD']['percent_change_24h']).replace("None", "0")
                percent_change_30d = str(data['data'][str(c)]['quote']['USD']['percent_change_30d']).replace("None", "0")
                percent_change_60d = str(data['data'][str(c)]['quote']['USD']['percent_change_60d']).replace("None", "0")
                percent_change_7d = str(data['data'][str(c)]['quote']['USD']['percent_change_7d']).replace("None", "0")
                percent_change_90d = str(data['data'][str(c)]['quote']['USD']['percent_change_90d']).replace("None", "0")
                price = str(data['data'][str(c)]['quote']['USD']['price']).replace("None", "0")
                volume_24h = str(data['data'][str(c)]['quote']['USD']['volume_24h']).replace("None", "0")
                volume_change_24h = str(data['data'][str(c)]['quote']['USD']['volume_change_24h']).replace("None", "0")
                # ele_reported_circulating_supply = data['data'][metd]['self_reported_circulating_supply'] <- NÃO VAI
                # ele_reported_market_cap = data['data'][metd]['self_reported_market_cap'] <- NÃO VAI
                slug = data['data'][str(c)]['slug']
                symbol = str(data['data'][str(c)]['symbol'])
                total_supply = str(data['data'][str(c)]['total_supply']).replace("None", "0")

                trat_circulating_supply = "{:.12f}".format(float(circulating_supply))
                trat_fully_diluted_market_cap = "{:.12f}".format(float(fully_diluted_market_cap))
                trat_market_cap = "{:.12f}".format(float(market_cap))

                trat_market_cap_dominance = "{:.12f}".format(float(market_cap_dominance))
                trat_max_supply = "{:.12f}".format(float(max_supply))
                trat_percent_change_1h = "{:.12f}".format(float(percent_change_1h))
                trat_percent_change_24h = "{:.12f}".format(float(percent_change_24h))
                trat_percent_change_30d = "{:.12f}".format(float(percent_change_30d))
                trat_percent_change_60d = "{:.12f}".format(float(percent_change_60d))
                trat_percent_change_7d = "{:.12f}".format(float(percent_change_7d))
                trat_percent_change_90d = "{:.12f}".format(float(percent_change_90d))
                trat_price = "{:.12f}".format(float(price))
                trat_volume_24h = "{:.12f}".format(float(volume_24h))
                trat_volume_change_24h = "{:.12f}".format(float(volume_change_24h))
                trat_total_supply = "{:.12f}".format(float(total_supply))
                self.janela = QtWidgets.QMainWindow()
                self.tela_p = MAIN.Ui_MainWindow()
                self.tela_p.setupUi(self.janela)
                trat_val_rs = "{:.12f}".format(float(float(price) * float(self.tela_p.lineEdit.text())))
                try:
                    conn = sqlite3.connect(BANCO_TABLE.banco)
                    c = conn.cursor()
                    c.execute(f"UPDATE cripto_moed SET nome = '{symbol}',"
                              f"valor_us = '{trat_price}',"
                              f"valor_rs = '{trat_val_rs}',"
                              f"circulating_supply = '{trat_circulating_supply}',"
                              f"cmc_rank = '{cmc_rank}',"
                              f"date_added = '{date_added_format}',"
                              f"id_crypto = '{id_crypto}',"
                              f"is_active = '{is_active}',"
                              f"is_fiat = '{is_fiat}',"
                              f"last_update = '{last_updated_format}',"
                              f"max_supply = '{trat_max_supply}',"
                              f"name = '{name}',"
                              f"num_market_pairs = '{num_market_pairs}',"
                              f"fully_diluted_market_cap = '{trat_fully_diluted_market_cap}',"
                              f"quote_last_updated = '{quote_last_update_format}',"
                              f"market_cap = '{trat_market_cap}',"
                              f"market_cap_dominance = '{trat_market_cap_dominance}',"
                              f"percent_change_1h = '{trat_percent_change_1h}',"
                              f"percent_change_24h = '{trat_percent_change_24h}',"
                              f"percent_change_30d = '{trat_percent_change_30d}',"
                              f"percent_change_60d = '{trat_percent_change_60d}',"
                              f"percent_change_7d = '{trat_percent_change_7d}',"
                              f"percent_change_90d = '{trat_percent_change_90d}',"
                              f"price = '{trat_price}',"
                              f"volume_24h = '{trat_volume_24h}',"
                              f"volume_change_24h = '{trat_volume_change_24h}',"
                              # f"self_reported_circulating_supply = '{ele_reported_circulating_supply}',"
                              # f"self_reported_market_cap = '{ele_reported_market_cap}',"
                              f"slug = '{slug}',"
                              f"symbol = '{symbol}',"
                              f"total_supply = '{trat_total_supply}' WHERE cod = '{b}'")
                    conn.commit()
                    conn.close()
                    self.insere_table_historic(symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                          date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                          name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                          trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                          trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                          trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                          trat_volume_change_24h, slug, symbol, trat_total_supply)

                except Exception as ERROR:
                    print(type(ERROR))
                    MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')
                MENSAGEM_CAIXA.TimerMessageBox().func(f'{NOMES_SYSTEM.aviso_info}', f'Moeda {symbol} Atualizada Com Sucesso!', 1)
                actua()


        except KeyError as ERROR:
            e = str(data['status']['error_message'])
            if e == '"slug" is not allowed to be empty':
                pass
            else:
                es = e.split(" ")
                MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'Verifique Sua Chave API ou Certifique-se que a Moeda Com o Símbolo {es[4]} Existe')


        except Exception as ERROR:
            print(type(ERROR))
            MENSAGEM_CAIXA.MessageBoxs.warning(self, f'{NOMES_SYSTEM.aviso_erro}', f'{ERROR}')

    def insere_table_historic(self, nome, valor_us, valor_rs, circulating_supply, cmc_rank, date_added, id_crypto, is_active, is_fiat, last_update, max_supply, name, num_market_pairs, fully_diluted_market_cap,
                              quote_last_update, market_cap, market_cap_dominance, percent_change_1h, percent_change_24h, percent_change_30d, percent_change_60d, percent_change_7d, percent_change_90d, price,
                              volume_24h, volume_change_24h, slug, symbol, total_supply):
        try:
            conn = sqlite3.connect(BANCO_TABLE.banco)
            c = conn.cursor()
            c.execute("INSERT INTO historic_cripto_moed (nome,"
                      "valor_us,"
                      "valor_rs,"
                      "circulating_supply,"
                      "cmc_rank,"
                      "date_added,"
                      "id_crypto,"
                      "is_active,"
                      "is_fiat,"
                      "last_update,"
                      "max_supply,"
                      "name,"
                      "num_market_pairs,"
                      "fully_diluted_market_cap,"
                      "quote_last_updated,"
                      "market_cap,"
                      "market_cap_dominance,"
                      "percent_change_1h,"
                      "percent_change_24h,"
                      "percent_change_30d,"
                      "percent_change_60d,"
                      "percent_change_7d,"
                      "percent_change_90d,"
                      "price,"
                      "volume_24h,"
                      "volume_change_24h,"
                      "slug,"
                      "symbol,"
                      "total_supply) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (nome, valor_us, valor_rs, circulating_supply, cmc_rank, date_added,
                       id_crypto, is_active, is_fiat, last_update, max_supply, name, num_market_pairs, fully_diluted_market_cap, quote_last_update, market_cap, market_cap_dominance,
                       percent_change_1h, percent_change_24h, percent_change_30d, percent_change_60d, percent_change_7d, percent_change_90d, price, volume_24h, volume_change_24h, slug, symbol, total_supply))
            conn.commit()
            conn.close()
        except Exception as ERROR:
            print(ERROR)

