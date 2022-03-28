import requests

try:
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
    requisicao_dic = requisicao.json()
    cot_dolar = requisicao_dic['USDBRL']['bid']
except Exception as ERROR:
    pass
