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

        #encontrando links PDFS na página
        pdf_links = []

        #looping para fazer a verificação da existência de links terminados em .pdf e adiciona-lós a lista
        #encontra todos os links da página
        for link in soup.find_all("a"):
            #verifica se o link termina com .pdf
            if link.get("href").endswith(".pdf"):
                #adiciona o link a lista
                pdf_links.append(link.get("href"))

        #CONVERSÃO DE LINKS RELATIVOS EM ABSOLUTOS-----------------------------------
        if not pdf_links:
            print("Nenhum link PDF encontrado.")
        else:
            #retorna a quantidade de pdfs encontrados
            print(f"Encontrados {len(pdf_links)} links PDF.")

            #converter pdf relativos em absolutos para trabalhar com http
            for pdf_absoluto in pdf_links:
                if not pdf_links.startswith("http"):
                    pdf_absoluto = requests.compat.urljoin(response, pdf_absoluto)

            #extraindo nome dos pdfs do links em pdf_absoluto
            nome_arquivo = os.path.join(pdf_absoluto.split("/")[-1])#talvez ocorra erro aqui###############

    except Exception as e:
        print(f"Erro ao acessar o site ou baixar os PDFs: {e}")