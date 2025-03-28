from extrair_dados import extrair_tabela
from compactar_csv import compactando_csv

def main():
    # ENTRADA
    caminho_pdf = "../teste_webscraping/data/pdfs/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"  # caminho do PDF
    arquivo_saida = "data/tabela.csv"  # caminho do arquivo de saída
    arquivo_zip = "data/tabela.zip"  # caminho do arquivo compactado

    # PROCESSAMENTO
    print(f"Extraindo dados de {caminho_pdf}...")
    dados = extrair_tabela(caminho_pdf)  # extrai a tabela do PDF
    dados.to_csv(arquivo_saida, index=False, sep=';', encoding='utf-8-sig')  # salva em uma tabela estruturada
    print(f"Dados salvos em {arquivo_saida}")

    print("Compactando arquivo...")
    compactando_csv(arquivo_saida, arquivo_zip)  # compacta o arquivo CSV
    print(f"Arquivo compactado em {arquivo_zip}")

    # SAÍDA
    print(f"Total de registros: {len(dados)}")

if __name__ == "__main__":
    main()
