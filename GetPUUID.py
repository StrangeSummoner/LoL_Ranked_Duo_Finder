import requests, KEYS

API_KEY = KEYS.PROJECT
REGION = "americas"
HEADERS = {
    "X-Riot-Token": API_KEY
}


def get_account_puuid(summoner_name, tag_line):    
    """
    Provide summoner_name(in-game name) and tag_line(exact server name) and get player's PUUID

    """
    
    url = f"https://{REGION}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag_line}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        print(f"PUUID for {summoner_name}: {data['puuid']}")
        return data['puuid']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == '__main__':
    summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
    region = str(input("Enter summoner region: ")) # e.g. NA1 
    get_account_puuid(summoner_name, region)