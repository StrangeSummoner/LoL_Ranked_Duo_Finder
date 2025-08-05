import requests, KEYS, GetPUUID, GetChampionName

API_KEY = KEYS.PROJECT
REGION = "na1"
HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_specific_champion_mastery(summoner_name, tag_line):

    """
    Get SPECIFIC champion mastery for the player by PUUID and Champion ID
    
    """
    championId =  int(input("Enter champion ID: ")) # e.g. 111
    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        print("Failed to fetch PUUID.")
        return None
    
    url = f"https://{REGION}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}/by-champion/{championId}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        champion_id = GetChampionName.get_champion_name_by_id(data["championId"])
        champion_level = data['championLevel']
        champion_points = data['championPoints']
        print(f"Champion: {champion_id}, Level: {champion_level}, Points: {champion_points}")
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == '__main__':
    summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
    region = str(input("Enter summoner region: ")) # e.g. NA1
    get_specific_champion_mastery(summoner_name, region)