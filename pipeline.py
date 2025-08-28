import time
import sqlite3
from extract.get_price import get_price_bitcoin_df

while True:
    dataframe = get_price_bitcoin_df()
    print(dataframe)

    time.sleep(60)  # Espera por 60 segundos antes de buscar o preço novamente
    
    conn = sqlite3.connect('bitcoin_prices.db')
    dataframe.to_sql('prices', conn, if_exists='append', index=False)