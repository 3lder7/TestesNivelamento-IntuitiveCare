import os
import zipfile#biblioteca python para trabalhar com arquivos ZIP
from download_pdfs import baixar_pdfs#função para baixar os PDFs

def compactar_pdfs():
    #cria a pasta pdfs_compactados caso não exista
    if not os.path.exists("data/pdfs_compactados"):
        os.makedirs("data/pdfs_compactados")

    #verifica se a pasta data/pdfs existe
    if not os.path.exists("data/pdfs"):
        print("Nenhum PDF encontrado para compactar.")
        return
    
    #----------------COMPACTAÇÃO DOS PDFs----------------
    #cria o arquivo zip
    with zipfile.ZipFile("data/pdfs_compactados/pdfs_compactados.zip", "w") as zipf:
        #looping para adicionar os arquivos PDF da pasta data/pdfs ao arquivo zip
        for root, _, files in os.walk("data/pdfs"):
            for file in files:
                if file.endswith(".pdf"):
                    #adiciona o arquivo PDF ao zip
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join("data/pdfs")))
                    print(f"Arquivo adicionado ao ZIP: {file}")
    print("Arquivos PDF compactados com sucesso!")
