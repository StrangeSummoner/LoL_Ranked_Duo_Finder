import requests, KEYS, GetChampionName

API_KEY = KEYS.PROJECT
HEADERS = {
    "X-Riot-Token": API_KEY
}

URL = "https://na1.api.riotgames.com/lol/platform/v3/champion-rotations"

REGION = "na1"  # change to your desired region
url = f"https://{REGION}.api.riotgames.com/lol/platform/v3/champion-rotations"

def get_champions():
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        champions = response.json()
        for champ in champions['freeChampionIds']:
            champ_name = GetChampionName.get_champion_name_by_id(champ)
            print(champ_name)
        return champions
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

get_champions()
