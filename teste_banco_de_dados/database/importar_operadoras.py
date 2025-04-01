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
cursor = conn.cursor()

#ler o arquivo CSV
df = pd.read_csv('Relatorio_cadop.csv', delimiter=';')  

# Tratar os valores de DDD para garantir que tenham no máximo 2 caracteres
df['DDD'] = df['DDD'].astype(str).str[:2]
# Tratar os valores de Numero para garantir que tenham no máximo 10 caracteres
df['Numero'] = df['Numero'].astype(str).str[:10]

#inserir os dados na tabela operadoras_ativas
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO operadoras_ativas (
            Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['Registro_ANS'],
        row['CNPJ'],
        row['Razao_Social'],
        row['Nome_Fantasia'],
        row['Modalidade'],
        row['Logradouro'],
        row['Numero'],
        row['Complemento'],
        row['Bairro'],
        row['Cidade'],
        row['UF'],
        row['CEP'],
        row['DDD'],
        row['Telefone'],
        row['Fax'],
        row['Endereco_eletronico'],
        row['Representante'],
        row['Cargo_Representante'],
        row['Regiao_de_Comercializacao'],
        row['Data_Registro_ANS']
    ))

#confirmar e fechar a conexão
conn.commit()
cursor.close()
conn.close()

print("Dados importados com sucesso!")