# faca consultas no banco de dados
import sqlite3
import pandas as pd

# Conectar ao banco de dados SQLite

conn = sqlite3.connect('data/bitcoin_prices.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM prices")

rows = cursor.fetchall()
# Obter os nomes das colunas da tabela
column_names = [description[0] for description in cursor.description]
#print(cursor.description)

#print(column_names)

df = pd.DataFrame(rows, columns=column_names)

print(df)
conn.close()