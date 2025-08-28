import requests
from datetime import datetime
import pandas as pd

def get_price_bitcoin_df():
    # URL para obter o preço do Bitcoin
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)

    if response.status_code == 200:
        preco = response.json()["data"]["amount"]
        ativo = response.json()["data"]["base"]
        moeda = response.json()["data"]["currency"]
        horario = datetime.now()

        informacoes = {"preco": preco,
                       "ativo": ativo,
                       "moeda": moeda,
                       "horario": horario
                    }
        
        dataframe = pd.DataFrame([informacoes])
    return dataframe
