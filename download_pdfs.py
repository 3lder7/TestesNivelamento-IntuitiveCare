import os #biblioteca para interação com o sistema operacional
from bs4 import BeautifulSoup #biblioteca para trabalhar com o HTML da página

def baixar_pdfs(response):
    #criação de pasta para salvar os PDFs
    if not os.path.exists("pdfs"):
        os.makedirs("pdfs")
    try:
        #analisando conteúdo da página / beautifulsoup
        soup = BeautifulSoup(response.text, "html.parser")

        #encontrando links PDFS na página
        pdf_links = []#lista para armazenar os links dos PDFs

        #looping para fazer a verificação da existência de links terminados em .pdf e adiciona-lós a lista
        for link in soup.find_all("a"):
            if link.get("href").endswith(".pdf"):
                pdf_links.append(link.get("href"))

        #download dos PDFs
        if not pdf_links:
            print("Nenhum link PDF encontrado.")
        else:
            print(f"Encontrados {len(pdf_links)} links PDF.")

    except Exception as e:
        print(f"Erro ao acessar o site ou baixar os PDFs: {e}")