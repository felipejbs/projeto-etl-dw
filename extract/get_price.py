import requests
from datetime import datetime

# URL para obter o preço do Bitcoin
url = "https://api.coinbase.com/v2/prices/spot"
response = requests.get(url)

if response.status_code == 200:
    informacoes = {"preco": response.json()["data"]["amount"],
                   "ativo": response.json()["data"]["base"],
                   "moeda": response.json()["data"]["currency"],
                   "horario": datetime.now()
                   }
    print(informacoes)