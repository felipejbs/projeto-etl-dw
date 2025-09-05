import sqlite3

def load_df(df):
    conn = sqlite3.connect('data/bitcoin_prices.db')
    df.to_sql('prices', conn, if_exists='append', index=False)
    conn.close()