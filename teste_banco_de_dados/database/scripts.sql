CREATE DATABASE banco_ans; --criando o banco
USE banco_ans; --selecionando o banco
CREATE TABLE operadoras_ativas ( 
    Registro_ANS VARCHAR(10) PRIMARY KEY,
    CNPJ VARCHAR(14),
    Razao_Social VARCHAR(255),
    Nome_Fantasia VARCHAR(255),
    Modalidade VARCHAR(255),
    Logradouro VARCHAR(255),
    Numero VARCHAR(10),
    Complemento VARCHAR(255),
    Bairro VARCHAR(255),
    Cidade VARCHAR(255),
    UF CHAR(2),
    CEP VARCHAR(8),
    DDD CHAR(2),
    Telefone VARCHAR(20),
    Fax VARCHAR(20),
    Endereco_eletronico VARCHAR(255),
    Representante VARCHAR(255),
    Cargo_Representante VARCHAR(255),
    Regiao_de_Comercializacao VARCHAR(255),
    Data_Registro_ANS DATE
);--para o tamanho/tipo das variáveis, usei IA para economizar tempo e evitar futuros erros problemáticos 