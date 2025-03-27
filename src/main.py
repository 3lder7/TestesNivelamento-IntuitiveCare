from teste_conexao import testa_conexao
from download_pdfs import baixar_pdfs

def main():
    # URL do site para testar a conexão
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    #chamando a função testa_conexao
    response = testa_conexao(url)
    #se a conexão for bem sucedida:
    if response:
        baixar_pdfs(response)    

if __name__ == "__main__":
    main()