import requests

def get_champion_name_by_id(champion_id, version="14.14.1"):
    """
    Returns a dictionary that maps championId (int) -> championName (str)
    using Data Dragon static data.
    """
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/champion.json"
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Failed to fetch champion data: {response.status_code}")
        return "Unknown"
    
    data = response.json()

    for champ in data["data"].values():
        if int(champ["key"]) == champion_id:
            return champ["id"]  

    return "Unknown"

if __name__ == '__main__':
    champ_id = int(input("Enter the champion ID: "))
    print(get_champion_name_by_id(champ_id))
