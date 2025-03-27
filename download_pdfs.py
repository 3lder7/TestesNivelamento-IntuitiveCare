import os #biblioteca para interação com o sistema operacional
from bs4 import BeautifulSoup #biblioteca para trabalhar com o HTML da página
import requests #biblioteca para requisições HTTP

def baixar_pdfs(response):
    #criação de pasta para salvar os PDFs
    if not os.path.exists("pdfs"):
        os.makedirs("pdfs")
    try:
        #analisando conteúdo da página / beautifulsoup
        soup = BeautifulSoup(response.text, "html.parser")

        #ENCONTRAR LINKS PDFS PRESENTES NA PÁGINA-----------------------------------
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
            #retorna a quantidade de pdfs encontrados
            print(f"Encontrados {len(pdf_links)} links PDF.")

            #CONVERSÃO DE LINKS RELATIVOS EM ABSOLUTOS PARA TRABALHAR COM HTTP------------------------
            for pdf_absoluto in pdf_links:
                if not pdf_links.startswith("http"):
                    pdf_absoluto = requests.compat.urljoin(response, pdf_absoluto)

            #extraindo nome dos pdfs do links em pdf_absoluto
            nome_arquivo = os.path.join(pdf_absoluto.split("/")[-1])#talvez ocorra erro aqui###############

            #BAIXAR PDF---------------------------------------------------------------
            print(f"Baixando PDF: {nome_arquivo}") 
            #fazendo requisição no link do pdf convertido para absoluto
            pdf_final = requests.get(pdf_absoluto)
            #verificar erro na requisição
            pdf_final.raise_for_status()


    except Exception as e:
        print(f"Erro ao acessar o site ou baixar os PDFs: {e}")