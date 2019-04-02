from bs4 import BeautifulSoup
from clint.textui import colored
import requests

print(colored.red("Exemplo: https://site.com/"))
print(colored.red("Exemplo2: http://site.com/"))
url = input("Digite o site: ")

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                        'AppleWebKit/537.36 (KHTML, like Gecko) '
                        'Chrome/51.0.2704.103 Safari/537.36'}

reque = requests.get(url, headers=header)
html = reque.text
sopinha = BeautifulSoup(html, 'html.parser')


def opcao():
    banner = """
    __ __  ______  ____  ____   _____   ___  
    |  T  T|      Tl    j|    \ |     | /   \ 
    |  l  ||      | |  T |  _  Y|   __jY     Y
    |  _  |l_j  l_j |  | |  |  ||  l_  |  O  |
    |  |  |  |  |   |  | |  |  ||   _] |     |
    |  |  |  |  |   j  l |  |  ||  T   l     !
    l__j__j  l__j  |____jl__j__jl__j    \___/ 
   
        https://github.com/RyanAragao2
    """
    print(colored.yellow(banner))
    print("0- Sair da Ferramenta")
    print("1- Procurar Imagens")
    print("2- Procurar Títulos")
    print("3- Pegar Todos os Links do site")


opcao()
while True:
    opcaozinha = int(input("Digite o número da opção: "))
    if opcaozinha == 0:
        print("Até mais!")
        break
    elif opcaozinha == 1:
        imagem = sopinha.find_all('img')
        for i in imagem:
            print(i.get('src'))
    elif opcaozinha == 2:
        titulo = sopinha.find('title')
        for t in titulo:
            print(titulo)
    elif opcaozinha == 3:
        links = sopinha.find_all('a')
        for l in links:
            print(l.get('href'))
    else:
        print("Essa opção não existe")
