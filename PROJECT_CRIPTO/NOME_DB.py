import os

nome_bd = "banco.db"

def most_camin_bd():
    try:
        arquivo = open("CONFIG_BANC.txt", 'r')
        caminho = arquivo.readlines()

        return caminho[0]
    except Exception as ERROR:
        print(ERROR)
