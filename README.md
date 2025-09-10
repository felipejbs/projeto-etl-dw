# Projeto DW Bitcoin

Este projeto tem como objetivo criar um pipeline ETL (Extract, Transform, Load) para coletar, transformar, armazenar e visualizar o preço do Bitcoin em tempo real. Utiliza Python para automação, SQLite para simplificar o armazenamento dos dados e Streamlit para visualização.

---

## Sumário

- [Visão Geral](#visão-geral)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Instalação](#instalação)
- [Execução do Pipeline ETL](#execução-do-pipeline-etl)
- [Execução da Interface Web](#execução-da-interface-web)
- [Detalhes dos Módulos](#detalhes-dos-módulos)
- [Banco de Dados](#banco-de-dados)

---

## Visão Geral

O projeto realiza a coleta periódica do preço do Bitcoin, transforma os dados conforme necessário e os armazena em um banco de dados SQLite. Uma interface web permite consultar o preço mais recente diretamente do banco, garantindo dados sempre atualizados a cada reload da página.

O uso do **SQLite** foi escolhido para simplificar a persistência dos dados, dispensando configurações complexas de servidores de banco de dados e facilitando o uso local e portabilidade do projeto.

---

## Estrutura do Projeto

```
projeto-dw-bitcion/
├── app.py                      # Interface Streamlit para consulta do preço
├── pipeline.py                 # Pipeline ETL (Extract, Transform, Load)
├── data/
│   └── bitcoin_prices.db       # Banco de dados SQLite
├── extract/
│   └── get_price.py            # Função para extrair o preço do Bitcoin
├── transform/
│   └── transform.py            # Função para transformar os dados extraídos
├── load/
│   └── load.py                 # Função para carregar os dados no banco
└── requirements.txt            # Dependências do projeto
```

---

## Instalação

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd projeto-dw-bitcion
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

---

## Execução do Pipeline ETL

O pipeline coleta o preço do Bitcoin a cada 10 segundos e armazena no banco de dados SQLite.

```bash
python pipeline.py
```

- O pipeline executa continuamente, realizando:
  - **Extração:** Busca o preço do Bitcoin de uma fonte externa (API).
  - **Transformação:** Limpa e prepara os dados.
  - **Carga:** Insere os dados no banco SQLite.

---

## Execução da Interface Web

A interface permite consultar o preço mais recente diretamente do banco de dados.

```bash
streamlit run app.py
```

- Acesse o endereço exibido pelo Streamlit (geralmente http://localhost:8501).
- A cada reload da página, o valor exibido será atualizado conforme o banco de dados.

---

## Detalhes dos Módulos

- **extract/get_price.py:**  
  Função `get_price_bitcoin_df()` retorna um DataFrame com o preço atual do Bitcoin.

- **transform/transform.py:**  
  Função `transform_df(df)` realiza limpeza e tratamento dos dados extraídos.

- **load/load.py:**  
  Função `load_df(df)` insere os dados transformados no banco SQLite.

- **pipeline.py:**  
  Orquestra o processo ETL, chamando os módulos de extração, transformação e carga em sequência.

- **app.py:**  
  Consulta o banco de dados SQLite e exibe o preço mais recente via Streamlit.  
  Exemplo de consulta:
  ```python
  def get_latest_bitcoin_price():
      conn = sqlite3.connect('data/bitcoin_prices.db')
      cursor = conn.cursor()
      cursor.execute("SELECT preco, horario FROM prices ORDER BY horario DESC LIMIT 1")
      result = cursor.fetchone()
      conn.close()
      return result
  ```

---

## Banco de Dados

- O banco de dados está localizado em `data/bitcoin_prices.db`.
- A tabela principal é `prices`, com pelo menos as colunas:
  - `preco` (valor do Bitcoin)
  - `horario` (timestamp da coleta)

Exemplo de criação da tabela:
```sql
CREATE TABLE prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    preco REAL NOT NULL,
    horario TEXT NOT NULL
);
```

---


## Contato

Dúvidas ou sugestões? Abra uma issue ou entre em contato pelo GitHub.
