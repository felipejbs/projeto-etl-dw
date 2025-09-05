import time
from extract.get_price import get_price_bitcoin_df
from transform.transform import transform_df
from load.load import load_df

while True:
    # Extrair os dados
    raw_df = get_price_bitcoin_df()

    # Transformar os dados
    transformed_df = transform_df(raw_df)
    
    # Carregar os dados
    load_df(transformed_df)

    print("Dados carregados com sucesso!")
    time.sleep(10)  # Espera por 60 segundos antes de buscar o preço novamente