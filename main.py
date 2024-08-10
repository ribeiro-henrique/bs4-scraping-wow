from bs4 import BeautifulSoup
import requests
import pandas as pd

# Lista DPS em Raid
lista_dps_raid = []

# Fazendo a requisição para ver os dados de Raid
raid_dps = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-raids").content

# Criando o objeto BeautifulSoup da page de Raid
soup_raid = BeautifulSoup(raid_dps, 'html.parser')

# Buscando a lista das classes
ranking_raid = soup_raid.find('ol')

# Verificando se o ranking_raid foi encontrado
if ranking_raid:
    # Iterando sobre cada item da lista (li)
    for item in ranking_raid.find_all('li'):
        # Adicionando o texto de cada item à lista
        lista_dps_raid.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_raid))

# Criando um DataFrame com os dados
table = pd.DataFrame(lista_dps_raid, columns=['Melhores DPS em Raids'])

# Exportando o DataFrame para um arquivo Excel
table.to_excel('classes.xlsx', index=False)
