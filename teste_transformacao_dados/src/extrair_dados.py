import pdfplumber #manipulação de pdf
import pandas as pd #manipulação de dados

def extrair_tabela (caminho_pdf):
    linhas_da_tabela = [] #lista que armazena as linhas da tabela

    with pdfplumber.open(caminho_pdf) as pdf: #abre o pdf
        for pagina in pdf.pages:
            tabelas = pagina.extract_tables() #extrai as tabelas da página com função do pdfplumber

            #-------------esse bloco foi gerado 100% com IA, e não entendi como funciona muito bem----------------
            for tabela in tabelas:
                for linha in tabela:
                    #pula linhas vazias ou cabeçalhos repetidos
                    if linha[0] and "PROCEDIMENTO" not in linha[0]:
                        linhas_da_tabela.append(linha)
            #---------------------------------------------------------------------------------------------------
    
    #colunas da tabela, são as mesmas do pdf
    #mas sem os espaços em branco
    colunas =[
        "PROCEDIMENTO", "RN", "VIGÊNCIA", "OD", "AMB", "HCO", 
        "HSO", "REF", "PAC", "DUT", "SUBGRUPO", "GRUPO", "CAPÍTULO"
    ]

    #---------------------CRIAÇÃO DO DATAFRAME PARA A TABELA-------------------------------
    #preparar os dados para serem transformados em um arquivo csv com pandas
    df = pd.DataFrame(linhas_da_tabela, columns=colunas)
    #remove linhas completamente vazias
    df = df.dropna(how='all')
    return df