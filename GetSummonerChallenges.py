import requests, KEYS, GetPUUID

API_KEY = KEYS.PROJECT
REGION = "na1"
HEADERS = {
    "X-Riot-Token": API_KEY
}


def get_summoner_challenges(summoner_name, tag_line):

    """
    Get Summoner Challenges for a specific player

    """

    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        return None

    url = f"https://{REGION}.api.riotgames.com/lol/challenges/v1/player-data/{encryptedPUUID}"
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
    get_summoner_challenges(summoner_name, region)