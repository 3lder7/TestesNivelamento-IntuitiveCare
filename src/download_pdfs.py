import os #biblioteca para interação com o sistema operacional
from bs4 import BeautifulSoup #biblioteca para trabalhar com o HTML da página
import requests #biblioteca para requisições HTTP

def baixar_pdfs(response):
    #criação de pasta para salvar os PDFs (caso não exista)
    if not os.path.exists("data/pdfs"):
        os.makedirs("data/pdfs")
    try:
        #analisando conteúdo da página / beautifulsoup
        soup = BeautifulSoup(response.text, "html.parser")

        #-------------------------------ENCONTRAR LINKS PDFS PRESENTES NA PÁGINA-----------------------------------------------
        pdf_links = []
        #looping para fazer a verificação da existência de links terminados em .pdf e adiciona-lós a lista
        #encontra todos os links da página
        for link in soup.find_all("a"):
            #verifica se o link termina com .pdf
            if link.get("href").endswith(".pdf"):
                #adiciona o link a lista
                pdf_links.append(link.get("href"))
        if not pdf_links:
            print("Nenhum link PDF encontrado.")
        else:
            print(f"Encontrados {len(pdf_links)} links PDF.")

            #--------------------------CONVERSÃO DE LINKS RELATIVOS EM ABSOLUTOS PARA TRABALHAR COM HTTP------------------------
            for pdf_absoluto in pdf_links:
                if not pdf_absoluto.startswith("http"):
                    pdf_absoluto = requests.compat.urljoin(response, pdf_absoluto)

                #extraindo nome dos pdfs do links em pdf_absoluto e salvando na variável
                nome_arquivo = os.path.join("data/pdfs", pdf_absoluto.split("/")[-1])

                #--------------------------------FILTRAGEM DOS ANEXO 1 E ANEXO 2------------------------------------------------
                #verifica se o nome do arquivo contém os anexos de interesse
                pdf_interesse = ["Anexo_I", "Anexo_II"]
                if not any(item in nome_arquivo for item in pdf_interesse):
                    print(f"Arquivo {nome_arquivo} não contém os anexos de interesse. Ignorando...")
                    continue
                
                #---------------------------------------------BAIXAR PDF---------------------------------------------------------
                print(f"Baixando PDF: {nome_arquivo}") 
                #fazendo requisição no link do pdf convertido para absoluto
                pdf_final = requests.get(pdf_absoluto)
                #verificar erro na requisição
                pdf_final.raise_for_status()

                #---------------------------------------SALVANDO PDF NO DISCO-----------------------------------------------------
                #wb = write/binary para abrir o arquivo em modo binário (essencial para arquivos PDF)
                with open(nome_arquivo, "wb") as arquivo_pdf: 
                    arquivo_pdf.write(pdf_final.content)#escreve o conteúdo do pdf baixado no arquivo
                print(f"PDF salvo como: {nome_arquivo}")  

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar o site ou baixar os PDFs: {e}")