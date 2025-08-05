import requests, KEYS, GetPUUID

API_KEY = KEYS.PROJECT
REGION = "na1"
HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_summoner_rank(summoner_name, tag_line):
    
    """
    Get Summoner Ranked Stats (Solo/Duo)

    """

    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        return None

    url = f"https://{REGION}.api.riotgames.com/lol/league/v4/entries/by-puuid/{encryptedPUUID}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        type = data[0]['queueType']
        rank = data[0]['tier'] + " " + data[0]['rank']
        ratio = str(data[0]['wins']) + "/" + str(data[0]['losses'])
        print(f"Summoner name: {summoner_name}, Queue: {type}, Rank: {rank}, W/L Ratio: {ratio}")
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == '__main__':
    summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
    region = str(input("Enter summoner region: ")) # e.g. NA1
    get_summoner_rank('CTenk', 'NA1')