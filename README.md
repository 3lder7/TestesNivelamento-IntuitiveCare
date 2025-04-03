# TestesNivelamento-IntuitiveCare

Este é um teste de nivelamento passado pela empresa para um processo seletivo.

- A arquitetura do projeto não é das melhores
- Não me preocupei com perfomance
- Não resolvi as instalações de dependências
- Não previni erros, como "não ter a pasta criada", e apartir disso cria-lá, por isso um código acaba dependendo do outro
- A tabela CSV salva, não está muito bem organizada como gostaria.
- E muitos outros detalhes...

## 📦 Como Usar

### Preparação do ambiente...
1. Clone o repositório:
```
git clone https://github.com/3lder7/TestesNivelamento-IntuitiveCare
```
2. Crie o ambiente virtual:
```
python -m venv venv
```
3. Ative o ambiente virtual:
```
venv/Scripts/activate
```
4. Instale as dependências necessárias:
```
pip install -r requirements.txt
```
### 🚀 Rodando
1. Primeiro, execute o arquivo main.py, do teste_webscraping
```
python teste_webscraping/src/main.py
```
1.1. Caso ocorra erro nas bibliotecas por conta da versão do python, instale manualmente
```
pip install requests beautifulsoup4
```
1.2. Após isso, será feito o download e compactação dos arquivos PDFs na pasta "data".

2. Execute o arquivo main.py, do teste_transformacao_dados.
```
python teste_webscraping/src/main.py
```
2.1. Caso ocorra erro nas bibliotecas por conta da versão do python, instale manualmente
```
pip install pdfplumber pandas
```
2.3. Após isso, também na pasta data será armazenado o arquivo, tanto em .csv quando em .zip

2.4. Crie uma conexão MySQL, de preferência com esses dados, caso não queira alterar no código:
```
    host="localhost",
    user="root",
    password="0000",
    database="banco_ans"
```
2.5. E por fim, crie o database e as tabelas no arquivo banco_operadoa.sql

2.6. Execute os scripts .py em teste_banco_de_dados. 
