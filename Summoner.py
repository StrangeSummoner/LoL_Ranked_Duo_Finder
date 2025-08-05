import requests
import KEYS

API_KEY = KEYS.PROJECT
REGION = "na1"  
HEADERS = {
    "X-Riot-Token": API_KEY
}

def get_account_id(summoner_name):
    url = f"https://{REGION}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        print(f"Account ID for {summoner_name}: {data['accountId']}")
        return data['accountId']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Example usage
get_account_id("CTenk")
