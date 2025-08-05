import requests, KEYS, GetPUUID

API_KEY = KEYS.PROJECT
REGION = "na1"
HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_total_champion_mastery(summoner_name, tag_line):

    """
    Get TOTAL champion mastery for the player by PUUID

    """

    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        print("Failed to fetch PUUID.")
        return None
    
    url = f"https://{REGION}.api.riotgames.com/lol/champion-mastery/v4/scores/by-puuid/{encryptedPUUID}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == '__main__':
    summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
    region = str(input("Enter summoner region: ")) # e.g. NA1   
    get_total_champion_mastery("CTenk", "NA1")