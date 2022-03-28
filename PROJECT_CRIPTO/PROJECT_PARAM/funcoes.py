from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
from cot_dolar import trat_dola
import datetime
import sqlite3
import pprint
import json
import os


def gera_arq_txt(slug, banco, rota):
    try:
        data_atual = str(datetime.datetime.today())
        dia_data_atual = data_atual[8:10]
        mes_data_atual = data_atual[5:7]
        ano_data_atual = data_atual[0:4]
        horas_data_atual = data_atual[11:13]
        minutos_data_atual = data_atual[14:16]
        segundos_data_atual = data_atual[17:19]

        caminho_absoluto = f"{rota}\\CRIPTO.TXT"

        if slug == "*":
            arquivo = open(caminho_absoluto, 'w+')
            arquivo.write("*|POWERED BY K&A SOFTWARE|\n")
            arquivo.write("*|DATA/ATUAL|HORATUAL|MOEDA/US$ | VALOR/COTACAO|\n")
            arquivo.write(f"1|{dia_data_atual}/{mes_data_atual}/{ano_data_atual}|{horas_data_atual}:{minutos_data_atual}:{segundos_data_atual}|US$       |{trat_dola.rjust(14, ' ')}|\n")
            arquivo.close()

        elif type(slug) == list:
            arquivo = open(caminho_absoluto, 'w+')
            arquivo.write("*|POWERED BY K&A SOFTWARE|\n")
            arquivo.write("*|DATA/ATUAL|HORATUAL|MOEDA/US$ | VALOR/COTACAO|\n")
            arquivo.write(f"1|{dia_data_atual}/{mes_data_atual}/{ano_data_atual}|{horas_data_atual}:{minutos_data_atual}:{segundos_data_atual}|US$       |{trat_dola.rjust(14, ' ')}|\n")
            arquivo.write("*|NOME/MOEDA|--------------------VALOR/US|------------------VALOR/REAL|ID-------|NOME/CRIPTO-------------------|FORNECIMENTO/CIRCULANTE----------|RANKTOP|DTCRIACAO-|HCRIACAO|A|F|ULTATUALIZ|HRUATUAL|SUPRIMENTO/MAXIMO----------------|NUM/PAR|VALOR/MERCADO/TOT/DILUIDO--------|DTULTCOTAC|HRULTCOT|VALOR/MERCADO--------------------|DOMINANCIA/CAP/MERCADO-----------|PERC/MUDANCA/1H--------|PERC/MUDANCA/24H-------|PERC/MUDANCA/30D-------|PERC/MUDANCA/60D-------|PERC/MUDANCA/7D--------|PERC/MUDANCA/90D-------|PRECO----------------------------|VOLUME/24H-----------------------|VOLUME/ALTERACAO/24H-------------|FORNECIMENTO/TOTAL---------------|QUANTIDADE/DE/COMPRA-------------|PRECO/DE/COMPRA------------------|DATACOMPRA|HORACOMP|COTACAO/COMPRA-------------------|\n")
            try:
                conn = sqlite3.connect(banco)
                c = conn.cursor()
                for i in slug:
                    c.execute(f"SELECT nome, valor_us, valor_rs, id_crypto, slug, circulating_supply, cmc_rank, date_added, is_active, is_fiat, last_update, max_supply, num_market_pairs, fully_diluted_market_cap, quote_last_updated,"
                              f"market_cap, market_cap_dominance, percent_change_1h, percent_change_24h, percent_change_30d, percent_change_60d, percent_change_7d, percent_change_90d, price, volume_24h, volume_change_24h, total_supply, quant_compra, preco_compra, data_hora_compra, cotacao_compra FROM cripto_moed WHERE slug = '{i}'")
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

                        arquivo.write(
                            f"2|{nome.ljust(10)}|{val_us.rjust(28)}|{val_rs.rjust(28)}|{id_crypto.rjust(9)}|{nome_crypto.ljust(30)}|{circulating_supply.rjust(33)}|"
                            f"{cmc_rank.rjust(7)}|{dia_date_added}/{mes_date_added}/{ano_date_added}|{horas_date_added}:{minuto_date_added}:{segundo_date_added}|"
                            f"{is_active}|{is_fiat}|{dia_last_update}/{mes_last_update}/{ano_last_update}|{horas_last_update}:{minuto_last_update}:{segundo_last_update}|"
                            f"{max_supply.rjust(33)}|{num_market_pairs.rjust(7)}|{fully_diluted_market_cap.rjust(33)}|{dia_quote_last_update}/{mes_quote_last_update}/{ano_quote_last_update}|"
                            f"{horas_quote_last_update}:{minuto_quote_last_update}:{segundo_quote_last_update}|{market_cap.rjust(33)}|{market_cap_dominance.rjust(33)}|{percent_change_1h.rjust(23)}|"
                            f"{percent_change_24h.rjust(23)}|{percent_change_30d.rjust(23)}|{percent_change_60d.rjust(23)}|{percent_change_7d.rjust(23)}|{percent_change_90d.rjust(23)}|{price.rjust(33)}|"
                            f"{volume_24h.rjust(33)}|{volume_change_24h.rjust(33)}|{total_supply.rjust(33)}|{quant_compra.rjust(33)}|{preco_compra.rjust(33)}|{dia_data_compra}/{mes_data_compra}/{ano_data_compra}|"
                            f"{horas_data_compra}:{minuto_data_compra}:{segundo_data_compra}|{cotacao_compra.rjust(33)}|\n")
                conn.close()
                arquivo.close()
            except Exception as ERROR:
                print(ERROR)

        else:
            arquivo = open(caminho_absoluto, 'w+')
            arquivo.write("*|POWERED BY K&A SOFTWARE|\n")
            arquivo.write("*|DATA/ATUAL|HORATUAL|MOEDA/US$ | VALOR/COTACAO|\n")
            arquivo.write(f"1|{dia_data_atual}/{mes_data_atual}/{ano_data_atual}|{horas_data_atual}:{minutos_data_atual}:{segundos_data_atual}|US$       |{trat_dola.rjust(14, ' ')}|\n")
            arquivo.write("*|NOME/MOEDA|--------------------VALOR/US|------------------VALOR/REAL|ID-------|NOME/CRIPTO-------------------|FORNECIMENTO/CIRCULANTE----------|RANKTOP|DTCRIACAO-|HCRIACAO|A|F|ULTATUALIZ|HRUATUAL|SUPRIMENTO/MAXIMO----------------|NUM/PAR|VALOR/MERCADO/TOT/DILUIDO--------|DTULTCOTAC|HRULTCOT|VALOR/MERCADO--------------------|DOMINANCIA/CAP/MERCADO-----------|PERC/MUDANCA/1H--------|PERC/MUDANCA/24H-------|PERC/MUDANCA/30D-------|PERC/MUDANCA/60D-------|PERC/MUDANCA/7D--------|PERC/MUDANCA/90D-------|PRECO----------------------------|VOLUME/24H-----------------------|VOLUME/ALTERACAO/24H-------------|FORNECIMENTO/TOTAL---------------|QUANTIDADE/DE/COMPRA-------------|PRECO/DE/COMPRA------------------|DATACOMPRA|HORACOMP|COTACAO/COMPRA-------------------|\n")
            try:
                conn = sqlite3.connect(banco)
                c = conn.cursor()
                c.execute(f"SELECT nome, valor_us, valor_rs, id_crypto, slug, circulating_supply, cmc_rank, date_added, is_active, is_fiat, last_update, max_supply, num_market_pairs, fully_diluted_market_cap, quote_last_updated,"
                          f"market_cap, market_cap_dominance, percent_change_1h, percent_change_24h, percent_change_30d, percent_change_60d, percent_change_7d, percent_change_90d, price, volume_24h, volume_change_24h, total_supply, "
                          f"quant_compra, preco_compra, data_hora_compra, cotacao_compra FROM cripto_moed WHERE slug = '{slug}'")
                dados_lidos = c.fetchall()

                nome = str(dados_lidos[0][0])
                val_us = str(dados_lidos[0][1])
                val_rs = str(dados_lidos[0][2])
                id_crypto = str(dados_lidos[0][3])
                nome_crypto = str(dados_lidos[0][4])
                circulating_supply = str(dados_lidos[0][5])
                cmc_rank = str(dados_lidos[0][6])

                date_added = str(dados_lidos[0][7])
                dia_date_added = date_added[8:10]
                mes_date_added = date_added[5:7]
                ano_date_added = date_added[0:4]
                horas_date_added = date_added[11:13]
                minuto_date_added = date_added[14:16]
                segundo_date_added = date_added[17:19]

                is_active = str(dados_lidos[0][8])
                is_fiat = str(dados_lidos[0][9])

                last_update = str(dados_lidos[0][10])
                dia_last_update = last_update[8:10]
                mes_last_update = last_update[5:7]
                ano_last_update = last_update[0:4]
                horas_last_update = last_update[11:13]
                minuto_last_update = last_update[14:16]
                segundo_last_update = last_update[17:19]

                max_supply = str(dados_lidos[0][11])
                num_market_pairs = str(dados_lidos[0][12])
                fully_diluted_market_cap = str(dados_lidos[0][13])

                quote_last_update = str(dados_lidos[0][14])
                dia_quote_last_update = quote_last_update[8:10]
                mes_quote_last_update = quote_last_update[5:7]
                ano_quote_last_update = quote_last_update[0:4]
                horas_quote_last_update = quote_last_update[11:13]
                minuto_quote_last_update = quote_last_update[14:16]
                segundo_quote_last_update = quote_last_update[17:19]

                market_cap = str(dados_lidos[0][15])
                market_cap_dominance = str(dados_lidos[0][16])
                percent_change_1h = str(dados_lidos[0][17])
                percent_change_24h = str(dados_lidos[0][18])
                percent_change_30d = str(dados_lidos[0][19])
                percent_change_60d = str(dados_lidos[0][20])
                percent_change_7d = str(dados_lidos[0][21])
                percent_change_90d = str(dados_lidos[0][22])
                price = str(dados_lidos[0][23])
                volume_24h = str(dados_lidos[0][24])
                volume_change_24h = str(dados_lidos[0][25])
                total_supply = str(dados_lidos[0][26])
                quant_compra = str(dados_lidos[0][27])
                preco_compra = str(dados_lidos[0][28])
                data_hora_compra = str(dados_lidos[0][29])
                dia_data_compra = data_hora_compra[8:10]
                mes_data_compra = data_hora_compra[5:7]
                ano_data_compra = data_hora_compra[0:4]
                horas_data_compra = data_hora_compra[11:13]
                minuto_data_compra = data_hora_compra[14:16]
                segundo_data_compra = data_hora_compra[17:19]

                cotacao_compra = str(dados_lidos[0][30])

                arquivo.write(
                    f"2|{nome.ljust(10)}|{val_us.rjust(28)}|{val_rs.rjust(28)}|{id_crypto.rjust(9)}|{nome_crypto.ljust(30)}|{circulating_supply.rjust(33)}|"
                    f"{cmc_rank.rjust(7)}|{dia_date_added}/{mes_date_added}/{ano_date_added}|{horas_date_added}:{minuto_date_added}:{segundo_date_added}|"
                    f"{is_active}|{is_fiat}|{dia_last_update}/{mes_last_update}/{ano_last_update}|{horas_last_update}:{minuto_last_update}:{segundo_last_update}|"
                    f"{max_supply.rjust(33)}|{num_market_pairs.rjust(7)}|{fully_diluted_market_cap.rjust(33)}|{dia_quote_last_update}/{mes_quote_last_update}/{ano_quote_last_update}|"
                    f"{horas_quote_last_update}:{minuto_quote_last_update}:{segundo_quote_last_update}|{market_cap.rjust(33)}|{market_cap_dominance.rjust(33)}|{percent_change_1h.rjust(23)}|"
                    f"{percent_change_24h.rjust(23)}|{percent_change_30d.rjust(23)}|{percent_change_60d.rjust(23)}|{percent_change_7d.rjust(23)}|{percent_change_90d.rjust(23)}|{price.rjust(33)}|"
                    f"{volume_24h.rjust(33)}|{volume_change_24h.rjust(33)}|{total_supply.rjust(33)}|{quant_compra.rjust(33)}|{preco_compra.rjust(33)}|{dia_data_compra}/{mes_data_compra}/{ano_data_compra}|"
                    f"{horas_data_compra}:{minuto_data_compra}:{segundo_data_compra}|{cotacao_compra.rjust(33)}|\n")
                conn.close()
                arquivo.close()


            except Exception as ERROR:
                print(ERROR)


    except Exception as ERROR:
        print(ERROR)

def verificar_codigos(banco):
    try:
        conn = sqlite3.connect(banco)
        c = conn.cursor()
        c.execute("SELECT cod FROM critpo_moed")
        conn.close()
    except Exception as ERROR:
        print(ERROR)

def atualizar_valores_uni(nome, key, banco, rota):
    try:
        pp = pprint.PrettyPrinter(indent=4)

        if nome == "*":
            gera_arq_txt(nome, banco, rota)
            pass
        elif nome[0:2] == "**":
            arquivo_lista_txt = nome[3:]
            atualizar_valores_slug(arquivo_lista_txt, key, banco, rota)
            #gera_arq_txt(nome, banco, rota)
            #pass
        else:

            key = key
            url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            print(url)
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': key,
            }
            parameters = {
                'slug': nome
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
                trat_val_rs = "{:.12f}".format(float(float(price) * float(trat_dola)))

                try:
                    conn = sqlite3.connect(banco)
                    c = conn.cursor()
                    c.execute(f"SELECT count(*) FROM cripto_moed WHERE slug = '{slug}'")
                    dados = c.fetchall()
                    if dados[0][0] != 0:
                        c.execute(f"SELECT cod FROM cripto_moed WHERE slug = '{slug}'")
                        dados = c.fetchall()

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
                                  f"total_supply = '{trat_total_supply}' WHERE cod = '{dados[0][0]}'")
                        conn.commit()
                        conn.close()
                        insere_table_historic(banco, symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                              date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                              name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                              trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                              trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                              trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                              trat_volume_change_24h, slug, symbol, trat_total_supply)
                        gera_arq_txt(slug, banco, rota)
                    else:
                        c.execute("INSERT INTO cripto_moed (nome,"
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
                                  # f"self_reported_circulating_supply = '{ele_reported_circulating_supply}',"
                                  # f"self_reported_market_cap = '{ele_reported_market_cap}',"
                                  "slug,"
                                  "symbol,"
                                  "total_supply,"
                                  "quant_compra,"
                                  "preco_compra,"
                                  "data_hora_compra,"
                                  "cotacao_compra) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                              date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                              name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                              trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                              trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                              trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                              trat_volume_change_24h, slug, symbol, trat_total_supply, '0.000000000000', '0.000000000000', '0000-00-00 00:00:00', '0.000000000000'))
                        conn.commit()
                        conn.close()
                        insere_table_historic(banco, symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                              date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                              name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                              trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                              trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                              trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                              trat_volume_change_24h, slug, symbol, trat_total_supply)
                    gera_arq_txt(slug, banco, rota)
                except Exception as ERROR:
                    print(ERROR)

    except KeyError as ERROR:
        print(ERROR)

    except Exception as ERROR:
        print(ERROR)

def atualizar_valores_slug(lista, key, banco, rota):
    try:

        pp = pprint.PrettyPrinter(indent=4)

        arquivo = open(f"{lista}", 'r')
        lista_criptos = arquivo.readlines()
        criptos = lista_criptos[0].replace("\n", "")
        criptos_list = criptos.split(",")
        arquivo.close()

        key = key
        url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        print(url)
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key,
        }
        parameters = {
            'slug': criptos
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
            trat_val_rs = "{:.12f}".format(float(float(price) * float(trat_dola)))

            try:
                conn = sqlite3.connect(banco)
                c = conn.cursor()
                c.execute(f"SELECT count(*) FROM cripto_moed WHERE slug = '{slug}'")
                dados_lidos = c.fetchall()
                if dados_lidos[0][0] != 0:
                    c.execute(f"SELECT cod FROM cripto_moed WHERE slug = '{slug}'")
                    dados = c.fetchall()
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
                              f"total_supply = '{trat_total_supply}' WHERE cod = '{dados[0][0]}'")
                    conn.commit()
                    conn.close()
                    insere_table_historic(banco, symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                          date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                          name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                          trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                          trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                          trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                          trat_volume_change_24h, slug, symbol, trat_total_supply)
                else:
                    c.execute("INSERT INTO cripto_moed (nome,"
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
                              # f"self_reported_circulating_supply = '{ele_reported_circulating_supply}',"
                              # f"self_reported_market_cap = '{ele_reported_market_cap}',"
                              "slug,"
                              "symbol,"
                              "total_supply,"
                              "quant_compra,"
                              "preco_compra,"
                              "data_hora_compra,"
                              "cotacao_compra) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                          date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                          name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                          trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                          trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                          trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                          trat_volume_change_24h, slug, symbol, trat_total_supply, '0.000000000000', '0.000000000000', '0000-00-00 00:00:00', '0.000000000000'))
                    conn.commit()
                    conn.close()
                    insere_table_historic(banco, symbol, trat_price, trat_val_rs, trat_circulating_supply, cmc_rank,
                                          date_added_format, id_crypto, is_active, is_fiat, last_updated_format, trat_max_supply,
                                          name, num_market_pairs, trat_fully_diluted_market_cap, quote_last_update_format,
                                          trat_market_cap, trat_market_cap_dominance, trat_percent_change_1h,
                                          trat_percent_change_24h, trat_percent_change_30d, trat_percent_change_60d,
                                          trat_percent_change_7d, trat_percent_change_90d, trat_price, trat_volume_24h,
                                          trat_volume_change_24h, slug, symbol, trat_total_supply)
                gera_arq_txt(criptos_list, banco, rota)

            except Exception as ERROR:
                print(ERROR)
        os.remove(lista)
    except KeyError as ERROR:
        print(ERROR)

    except Exception as ERROR:
        print(ERROR)

def insere_table_historic(banco, nome, valor_us, valor_rs, circulating_supply, cmc_rank, date_added, id_crypto, is_active, is_fiat, last_update, max_supply, name, num_market_pairs, fully_diluted_market_cap,
                          quote_last_update, market_cap, market_cap_dominance, percent_change_1h, percent_change_24h, percent_change_30d, percent_change_60d, percent_change_7d, percent_change_90d, price,
                          volume_24h, volume_change_24h, slug, symbol, total_supply):
    try:
        conn = sqlite3.connect(banco)
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
