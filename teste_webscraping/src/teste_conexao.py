import requests #biblioteca para requisições HTTP

def testa_conexao(url):
#tentativa de conexão
    try:
        response = requests.get(url)
        response.raise_for_status()#verificar erro na requisição

        print("Conexão realizada.")
        print(f"Status: {response.status_code}")
        print("Conectado a URL:")
        print(f"{url}")
        return response #retorna a resposta da requisição
        
    except requests.exceptions.RequestException as e:
        print("Conexão NÃO realizada.")
        print(f"ERRO: {e}")
        return None #retorna None se a conexão falhar