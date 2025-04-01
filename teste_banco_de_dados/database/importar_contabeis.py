#DECIDI TRABALHAR COM A BIBLIOTECA PANDAS PARA LER O ARQUIVO .CSV E PASSAR PARA O BANCO DE DADOS
#POIS USANDO DIRETAMENTE O COMANDO SQL ''LOAD DATA INFILE'' NÃO FUNCIONAOU DE JEITO NENHUM
#TERIA QUE FAZER ALTERAÇÕES NOS ARQUIVOS DO MYSQL SERVER
#E EU QUERO TENTAR DEIXAR O PROJETO O MAIS PRÁTICO POSSÍVEL
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

#-------------UTILIZANDO IA PARA TRATAR OS DADOS------------------
#ler o arquivo CSV
df = pd.read_csv('2023/1T2023.csv', delimiter=';', quotechar='"')

# Substituir vírgulas por pontos nas colunas de valores decimais
df['VL_SALDO_INICIAL'] = df['VL_SALDO_INICIAL'].astype(str).str.replace(',', '.').astype(float)
df['VL_SALDO_FINAL'] = df['VL_SALDO_FINAL'].astype(str).str.replace(',', '.').astype(float)
#-----------------------------------------------------------------

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
