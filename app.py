import streamlit as st
import sqlite3

def get_latest_bitcoin_price():
    conn = sqlite3.connect('data/bitcoin_prices.db')
    cursor = conn.cursor()
    cursor.execute("SELECT preco, horario FROM prices ORDER BY horario DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result

st.title("Consulta do Preço do Bitcoin")

result = get_latest_bitcoin_price()
if result:
    preco, data = result
    st.metric("Preço Atual do Bitcoin", f"USD {preco}", help=f"Atualizado em: {data}")
else:
    st.warning("Nenhum dado encontrado no banco de dados.")