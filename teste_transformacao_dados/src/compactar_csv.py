import zipfile
import os

def compactando_csv(arquivo_saida, arquivo_zip):

    if not os.path.exists(arquivo_saida):
        print(f"Erro: O arquivo {arquivo_saida} não foi encontrado!")
        return
    
    with zipfile.ZipFile(arquivo_zip, "w") as zipf:
        zipf.write(arquivo_saida, os.path.basename(arquivo_saida))
        print(f"Arquivo adicionado ao ZIP: {os.path.basename(arquivo_saida)}")
    
    print("Arquivo CSV compactado com sucesso!")

# Chama a função
compactando_csv()