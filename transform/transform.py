import pandas as pd

def transform_df(df):
    if 'horario' in df.columns:
        df['horario'] = pd.to_datetime(df['horario']).dt.strftime('%d/%m/%Y %H:%M:%S')
    if 'preco' in df.columns:
        df['preco'] = [
            "USD {:,.2f}".format(float(valor)).replace(",", "X").replace(".", ",").replace("X", ".")
            for valor in df['preco']
        ]
    return df