import requests
from bs4 import BeautifulSoup

req = requests.get('https://www.cinemark.com.br/aracaju/filmes/em-cartaz')

soup = BeautifulSoup(req.text ,'html.parser')

lista = soup.find_all('div' , class_ = 'col-sm-6 col-md-3')

id = 0
for i in lista:
    titulo = (i.h3).text
    id += 1
    print(f'Filme {id}: {titulo}')
    print('-' * 40)


