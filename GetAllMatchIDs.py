import requests, KEYS, GetPUUID

API_KEY = KEYS.PROJECT
REGION = "americas"
HEADERS = {
    "X-Riot-Token": API_KEY
}

count = 95

def get_all_summoner_matches(summoner_name, tag_line):
    """
    Get match IDs for the player by PUUID
    """
    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        print("Failed to fetch PUUID.")
        return None
    
    url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/by-puuid/{encryptedPUUID}/ids?start=0&count={count}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        print(f"Total Matches Found: {len(data)}")
        for match_id in data:
            print(match_id)
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == '__main__':
    summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
    region = str(input("Enter summoner region: ")) # e.g. NA1 
    get_all_summoner_matches(summoner_name, region)