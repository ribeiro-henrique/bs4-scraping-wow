from bs4 import BeautifulSoup
import requests
import pandas as pd

# Lista para armazenar as classes
lista_classes = []

# Fazendo a requisição ao site
site = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-raids").content

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(site, 'html.parser')

# Buscando a lista ordenada (ol)
ranking = soup.find('ol')

# Verificando se o ranking foi encontrado
if ranking:
    # Iterando sobre cada item da lista (li)
    for item in ranking.find_all('li'):
        # Adicionando o texto de cada item à lista
        lista_classes.append(item.text)
else:
    print("Lista não encontrada!")

# Criando um DataFrame com os dados
table = pd.DataFrame(lista_classes, columns=['Melhores DPS em Raids'])

# Exportando o DataFrame para um arquivo Excel
table.to_excel('classes.xlsx', index=False)
