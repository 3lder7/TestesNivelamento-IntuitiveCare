USE banco_ans;  --selecionando o banco 
CREATE TABLE demonstracoes_1T2023(
    DATA DATE,                  
    REG_ANS VARCHAR(10),        
    CD_CONTA_CONTABIL VARCHAR(20),  
    DESCRICAO TEXT,             
    VL_SALDO_INICIAL DECIMAL(15, 2),  
    VL_SALDO_FINAL DECIMAL(15, 2),    
    FOREIGN KEY (REG_ANS) REFERENCES operadoras_ativas(Registro_ANS)  --chave estrangeira para a tabela de operadoras ativas
);

/*----------------IMPORTANDO CSV----------------*/
LOAD DATA INFILE '../2023/1T2023.csv' -- inserir dados do csv nas colunas da tabela
INTO TABLE demonstracoes_1T2023
FIELDS TERMINATED BY ';'    -- delimitador 
ENCLOSED BY '"'           
LINES TERMINATED BY '\n'    -- fazr a quebra de linha
IGNORE 1 ROWS               -- ignorar o cabeçalho
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL); --especificando a ordem das colunas