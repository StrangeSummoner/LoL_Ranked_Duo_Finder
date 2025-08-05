import requests

def get_all_champion_names():
    versions_url = "https://ddragon.leagueoflegends.com/api/versions.json"
    latest_version = requests.get(versions_url).json()[0]
    print(f"Latest version: {latest_version}")

    champion_url = f"https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion.json"
    champion_data = requests.get(champion_url).json()

    champion_names = list(champion_data["data"].keys())
    return champion_names


if __name__ == "__main__":
    get_all_champion_names()
    








