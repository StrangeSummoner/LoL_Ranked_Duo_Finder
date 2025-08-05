import requests, KEYS, GetPUUID, json

API_KEY = KEYS.PROJECT
REGION = "na1"
HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_all_champion_masteries(summoner_name, tag_line, export_path="champion_mastery_export.json"):
    """
    Get ALL champion masteries for the player by PUUID and export as JSON file
    """
    encryptedPUUID = GetPUUID.get_account_puuid(summoner_name, tag_line)
    if not encryptedPUUID:
        print("Failed to fetch PUUID.")
        return None
    
    url = f"https://{REGION}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{encryptedPUUID}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        print(f"Total Champions with Mastery: {len(data)}")

        # Export data to JSON file
        with open(export_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"Exported to {export_path}")
        return data
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ = '__main__':
    get_all_champion_masteries("CTenk", "NA1")
