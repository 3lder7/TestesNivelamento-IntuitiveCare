import zipfile
import os

def compactando_csv(arquivo_saida, arquivo_zip):

    if not os.path.exists(arquivo_saida):
        print(f"Erro: O arquivo {arquivo_saida} não foi encontrado!")
        return
    
    with zipfile.ZipFile(arquivo_zip, "w") as zipf:# abre o arquivo zip para escrita
        zipf.write(arquivo_saida, os.path.basename(arquivo_saida))# adiciona o arquivo CSV ao ZIP
        print(f"Arquivo adicionado ao ZIP: {os.path.basename(arquivo_saida)}")#indica o nome do arquivo adicionado ao ZIP
    
    print("Arquivo CSV compactado com sucesso!")
