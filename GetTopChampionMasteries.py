import requests, KEYS, GetPUUID, GetChampionName

API_KEY = KEYS.PROJECT
REGION = "na1"
HEADERS = {
    "X-Riot-Token": API_KEY
}


def get_top_champion_masteries(summoner_name, tag_line):

    """
    Get TOP 3 (could be changed) champion masteries for the player by PUUID

    """
    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        print("Failed to fetch PUUID.")
        return None
    
    url = f"https://{REGION}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}/top"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        for champ in data:
            champ_name = GetChampionName.get_champion_name_by_id(champ["championId"])
            level = champ["championLevel"]
            points = champ["championPoints"]
            print(f"Champion: {champ_name}, Level: {level}, Points: {points}")
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == '__main__':
    summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
    region = str(input("Enter summoner region: ")) # e.g. NA1
    get_top_champion_masteries("CTenk", "NA1")