import streamlit as st
import sqlite3

def get_latest_bitcoin_price():
    conn = sqlite3.connect('data/bitcoin_prices.db')
    cursor = conn.cursor()
    cursor.execute("SELECT preco, data FROM prices ORDER BY data DESC LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    return result

st.title("Consulta do Preço do Bitcoin")

result = get_latest_bitcoin_price()
if result:
    preco, data = result
    st.metric("Preço Atual do Bitcoin", f"R$ {preco:,.2f}", label=f"Atualizado em: {data}")
else:
    st.warning("Nenhum dado encontrado no banco de dados.")