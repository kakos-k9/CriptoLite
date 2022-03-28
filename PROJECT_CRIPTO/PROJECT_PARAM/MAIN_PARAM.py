import sqlite3
import funcoes
import sys
import os

param_1 = sys.argv[0]
params_result = sys.argv[1:]
transform = [" ".join(params_result)]
camin_abs = transform[0]

caminho_txt = param_1.replace("MAIN_PARAM.py", "CONFIG_BANC.txt").replace("CriptoLite.exe", "CONFIG_BANC.txt")

def most_camin_bd():
    try:
        arquivo = open(f"{caminho_txt}", 'r')
        caminho = arquivo.readlines()
        arquivo.close()
        return caminho[0].replace("\n", "")
    except Exception as ERROR:
        print(ERROR)

banco = most_camin_bd()
print(banco)
def retorna_key_api():
    try:
        conn = sqlite3.connect(banco)
        c = conn.cursor()
        c.execute("SELECT desc_config FROM config WHERE cod = 1")
        dados = c.fetchall()
        chave = dados[0][0]
        conn.close()

        return chave
    except Exception as ERROR:
        print(ERROR)

chave_api = retorna_key_api()

def pegar_caminho_export_txt():
    try:
        conn = sqlite3.connect(banco)
        c = conn.cursor()
        c.execute("SELECT desc_config FROM config WHERE cod = 2")
        dados = c.fetchall()
        caminho = dados[0][0]
        conn.close()
        return caminho
    except Exception as ERROR:
        print(ERROR)

rota = pegar_caminho_export_txt()

funcoes.atualizar_valores_uni(camin_abs, chave_api, banco, rota)
