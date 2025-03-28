from extrair_dados import extrair_tabela

def main():
    #ENTRADA
    caminho_pdf = "../teste_webscraping/data/pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf" #caminho do pdf até o primeiro teste
    arquivo_saida = "data/tabela.csv" #caminho do arquivo de saída
    
    #PROCESSAMENTO
    print(f"Extraindo dados de {caminho_pdf}...")
    dados = extrair_tabela(caminho_pdf) #extrai a tabela do pdf

    #SAÍDA
    dados.to_csv(arquivo_saida, index=False, encoding='utf-8-sig')
    print(f"Dados salvos em {arquivo_saida}")
    print(f"Total de registros: {len(dados)}")

if __name__ == "__main__":
    main()