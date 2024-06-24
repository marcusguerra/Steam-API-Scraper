import requests
import json

with open('unique_titles.txt', 'r') as file:
    game_titles = [line.strip() for line in file.readlines()]

title4 = game_titles[90000:120000]


def get_app_id(game_title):
    url = f'https://store.steampowered.com/api/storesearch/?term={game_title}&cc=US'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            return data['items'][0]['id']
    return None


app_ids = []
p = 0
atual = 0
total = len(title4)
for title in title4:
    try:
        atual += 1
        if(atual == 15103):
            continue
        print(f"Iteração: {atual} de {total}")
        app_id = get_app_id(title)
        if app_id is not None:
            app_ids.append(app_id)
        else:
            print(f"App ID not found for: {title}")
    except:
        p += 1
        print(f'ERRO:{p}')

# Write the app IDs to a new file
with open('app_ids4.txt', 'w') as file:
    for app_id in app_ids:
        file.write(f"{app_id}\n")
