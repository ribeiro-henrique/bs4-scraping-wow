from bs4 import BeautifulSoup
import requests
import pandas as pd

# Lista DPS em Raid e Mítica
lista_dps_raid = []
lista_dps_mitica = []

# Lista Healer em Raid e Mítica
lista_heal_raid = []
lista_heal_mitica = []

# Lista Tanks em Raid e Mítica
lista_tank_raid = []
lista_tank_mitica = []


# Fazendo a requisição para ver os dados de Raid e Mítica
req_raid_dps = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-raids").content
req_mitica_dps = requests.get("https://www.wowhead.com/guide/classes/tier-lists/dps-rankings-mythic-plus").content

req_raid_heal = requests.get("https://www.wowhead.com/guide/classes/tier-lists/healer-rankings-raids").content
req_mitica_heal = requests.get("https://www.wowhead.com/guide/classes/tier-lists/healer-rankings-mythic-plus").content

req_raid_tank = requests.get("https://www.wowhead.com/guide/classes/tier-lists/tank-rankings-raids").content
req_mitica_tank = requests.get("https://www.wowhead.com/guide/classes/tier-lists/tank-rankings-mythic-plus").content

# Criando o objeto BeautifulSoup do get das páginas
html_raid_dps = BeautifulSoup(req_raid_dps, 'html.parser')
html_mitica_dps = BeautifulSoup(req_mitica_dps, 'html.parser')

html_raid_heal = BeautifulSoup(req_raid_heal, 'html.parser')
html_mitica_heal = BeautifulSoup(req_mitica_heal, 'html.parser')

html_raid_tank = BeautifulSoup(req_raid_tank, 'html.parser')
html_mitica_tank = BeautifulSoup(req_mitica_tank, 'html.parser')


# Buscando a lista das classes
ranking_raid_dps = html_raid_dps.find('ol')
ranking_mitica_dps = html_mitica_dps.find('ol')

ranking_raid_heal = html_raid_heal.find('ol')
ranking_mitica_heal = html_mitica_heal.find('ol')

ranking_raid_tank = html_raid_tank.find('ol')
ranking_mitica_tank = html_mitica_tank.find('ol')

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
    
### TANK RAID ####
if ranking_raid_tank:
    # Iterando sobre cada item 
    for item in ranking_raid_tank.find_all('li'):
        # Adicionando somente o text
        lista_tank_raid.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_raid_tank))

### TANK MITICA ####
if ranking_mitica_tank:
    # Iterando sobre cada item da lista 
    for item in ranking_mitica_tank.find_all('li'):
        # Adicionando somente o texto                   
        lista_tank_mitica.append(item.text)
else:
    print("A lista {} não foi encontrada!".format(ranking_mitica_tank))


# Verificando se as listas tem o mesmo tamanho
max_length = max(len(lista_dps_raid), len(lista_dps_mitica), len(lista_heal_raid), len(lista_dps_mitica), len(lista_tank_raid), len(lista_tank_mitica))

# Aqui preenchemos as listas menores com valores vazios, pois é necessário xD
lista_dps_raid.extend([''] * (max_length - len(lista_dps_raid)))
lista_dps_mitica.extend([''] * (max_length - len(lista_dps_mitica)))
lista_heal_raid.extend([''] * (max_length - len(lista_heal_raid)))
lista_heal_mitica.extend([''] * (max_length - len(lista_heal_mitica)))
lista_tank_raid.extend([''] * (max_length - len(lista_tank_raid)))
lista_tank_mitica.extend([''] * (max_length - len(lista_tank_mitica)))

# Criando um DataFrame com os dados das duas listas
table = pd.DataFrame({
    'Melhores DPS em Raids': lista_dps_raid,
    'Melhores DPS em Míticas': lista_dps_mitica,
    'Melhores Healers em Raids': lista_heal_raid,
    'Melhores Healers em Míticas': lista_heal_mitica,
    'Melhores Tanks em Raids': lista_tank_raid,
    'Melhores Tanks em Míticas': lista_tank_mitica,
})

# Exportando o DataFrame para um arquivo Excel
table.to_excel('top_classes_wow.xlsx', index=False)
