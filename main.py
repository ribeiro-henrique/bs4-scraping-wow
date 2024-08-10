from bs4 import BeautifulSoup
import requests
import pandas as pd

# Lista DPS em Raid e Mítica
lista_dps_raid = []
lista_dps_mitica = []

# Fazendo a requisição para ver os dados de Raid e Mítica
raid_dps = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-raids").content
mitica_dps = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-mythic-plus").content

# Criando o objeto BeautifulSoup da page de Raid e Mítica
soup_raid = BeautifulSoup(raid_dps, 'html.parser')
soup_mitica = BeautifulSoup(mitica_dps, 'html.parser')

# Buscando a lista das classes
ranking_raid = soup_raid.find('ol')
ranking_mitica = soup_mitica.find('ol')

# Verificando se o ranking_raid foi encontrado
if ranking_raid:
    # Iterando sobre cada item 
    for item in ranking_raid.find_all('li'):
        # Adicionando somente o text
        lista_dps_raid.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_raid))
    
# Verificando se o ranking_mitica foi encontrado
if ranking_mitica:
    # Iterando sobre cada item da lista 
    for item in ranking_mitica.find_all('li'):
        # Adicionando somente o texto
        lista_dps_mitica.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_mitica))

# Verificando se as listas tem o mesmo tamanho
max_length = max(len(lista_dps_raid), len(lista_dps_mitica))

# Aqui preenchemos as listas menores com valores vazios, pois é necessário xD
lista_dps_raid.extend([''] * (max_length - len(lista_dps_raid)))
lista_dps_mitica.extend([''] * (max_length - len(lista_dps_mitica)))

# Criando um DataFrame com os dados das duas listas
table = pd.DataFrame({
    'Melhores DPS em Raids': lista_dps_raid,
    'Melhores DPS em Míticas': lista_dps_mitica
})

# Exportando o DataFrame para um arquivo Excel
table.to_excel('classes.xlsx', index=False)
