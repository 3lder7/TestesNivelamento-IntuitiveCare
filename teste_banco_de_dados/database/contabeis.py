

import pandas as pd
import mysql.connector

#conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="banco_ans"
)
cursor = conn.cursor()#criar um cursor para executar comandos SQL

#ler o arquivo CSV
df = pd.read_csv('2023/1T2023.csv', delimiter=';', quotechar='"')

#inserir os dados na tabela
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO demonstracoes_1T2023 (DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
        VALUES (%s, %s, %s, %s, %s, %s) 
    """, (
        row['DATA'], 
        row['REG_ANS'], 
        row['CD_CONTA_CONTABIL'], 
        row['DESCRICAO'], 
        row['VL_SALDO_INICIAL'], 
        row['VL_SALDO_FINAL']
    ))

#confirmar e fechar a conexão
conn.commit()
cursor.close()
conn.close()