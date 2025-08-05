import requests, KEYS, GetPUUID, GetAllMatchIDs
from collections import defaultdict
import json

API_KEY = KEYS.PROJECT
REGION = "americas"
HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_champion_vector(summoner_name, tag_line):
    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        print("Failed to fetch PUUID.")
        return None

    matchIDs = GetAllMatchIDs.get_all_summoner_matches(summoner_name, tag_line)
    if not matchIDs:
        print("Failed to fetch Match IDs.")
        return None

    champ_counter = defaultdict(int)

    for matchID in matchIDs:
        url = f"https://{REGION}.api.riotgames.com/lol/match/v5/matches/{matchID}"
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            data = response.json()
            participants = data["info"]["participants"]
            for participant in participants:
                if participant["puuid"] == encryptedPUUID:
                    champion = participant["championName"]
                    champ_counter[champion] += 1
        else:
            print(f"Error {response.status_code}: {response.text}")

    return champ_counter

if __name__ == "__main__":
    summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
    region = str(input("Enter summoner region: ")) # e.g. NA1
    champ_counter = get_champion_vector(summoner_name, region)
    if champ_counter:
        for champ, count in champ_counter.items():
            print(f"{champ}: {count}")
