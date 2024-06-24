import requests
import json

# Read the list of game titles from the file
with open('paralelismo/unique_titles.txt', 'r') as file:
    game_titles = [line.strip() for line in file.readlines()]

# Function to get the app ID from the Steam API
def get_app_id(game_title):
    url = f'https://store.steampowered.com/api/storesearch/?term={game_title}&cc=US'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'items' in data and len(data['items']) > 0:
            return data['items'][0]['id']
    return None

# List to hold the app IDs
app_ids = []

# Get app IDs for each game title
for title in game_titles:
    app_id = get_app_id(title)
    if app_id is not None:
        app_ids.append(app_id)
    else:
        print(f"App ID not found for: {title}")

# Write the app IDs to a new file
with open('app_ids.txt', 'w') as file:
    for app_id in app_ids:
        file.write(f"{app_id}\n")

print("App IDs have been written to app_ids.txt")
