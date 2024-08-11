from bs4 import BeautifulSoup
import requests
import pandas as pd

# Lista DPS em Raid e Mítica
lista_dps_raid = []
lista_dps_mitica = []

# Lista Healer em Raid e Mítica
lista_heal_raid = []
lista_heal_mitica = []


# Fazendo a requisição para ver os dados de Raid e Mítica
raid_dps = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-raids").content
mitica_dps = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-mythic-plus").content

raid_heal = requests.get("https://www.wowhead.com/guide/classes/tier-lists/healer-rankings-raids").content
mitica_heal = requests.get("https://www.wowhead.com/guide/classes/tier-lists/healer-rankings-mythic-plus").content

# Criando o objeto BeautifulSoup do get das páginas
soup_raid_dps = BeautifulSoup(raid_dps, 'html.parser')
soup_mitica_dps = BeautifulSoup(mitica_dps, 'html.parser')

soup_raid_heal = BeautifulSoup(raid_heal, 'html.parser')
soup_mitica_heal = BeautifulSoup(mitica_heal, 'html.parser')


# Buscando a lista das classes
ranking_raid_dps = soup_raid_dps.find('ol')
ranking_mitica_dps = soup_mitica_dps.find('ol')

ranking_raid_heal = soup_raid_heal.find('ol')
ranking_mitica_heal = soup_mitica_heal.find('ol')

# Verificando se o rankings foram encontrados:

### DPS RAID ####
if ranking_raid_dps:
    # Iterando sobre cada item 
    for item in ranking_raid_dps.find_all('li'):
        # Adicionando somente o text
        lista_dps_raid.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_raid_dps))
    
### DPS MITICA ####
if ranking_mitica_dps:
    # Iterando sobre cada item da lista 
    for item in ranking_mitica_dps.find_all('li'):
        # Adicionando somente o texto                   
        lista_dps_mitica.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_mitica_dps))

### HEAL RAID ####
if ranking_raid_heal:
    # Iterando sobre cada item 
    for item in ranking_raid_heal.find_all('li'):
        # Adicionando somente o text
        lista_heal_raid.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_raid_heal))

### HEAL MITICA ####
if ranking_mitica_heal:
    # Iterando sobre cada item da lista 
    for item in ranking_mitica_heal.find_all('li'):
        # Adicionando somente o texto                   
        lista_heal_mitica.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_mitica_heal))


# Verificando se as listas tem o mesmo tamanho
max_length = max(len(lista_dps_raid), len(lista_dps_mitica), len(lista_heal_raid), len(lista_dps_mitica))

# Aqui preenchemos as listas menores com valores vazios, pois é necessário xD
lista_dps_raid.extend([''] * (max_length - len(lista_dps_raid)))
lista_dps_mitica.extend([''] * (max_length - len(lista_dps_mitica)))
lista_heal_raid.extend([''] * (max_length - len(lista_heal_raid)))
lista_heal_mitica.extend([''] * (max_length - len(lista_heal_mitica)))

# Criando um DataFrame com os dados das duas listas
table = pd.DataFrame({
    'Melhores DPS em Raids': lista_dps_raid,
    'Melhores DPS em Míticas': lista_dps_mitica,
    'Melhores Healers em Raids': lista_heal_raid,
    'Melhores Healers em Míticas': lista_heal_mitica,
})

# Exportando o DataFrame para um arquivo Excel
table.to_excel('top_classes_wow.xlsx', index=False)
