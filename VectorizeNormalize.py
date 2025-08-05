import numpy as np
from sklearn.preprocessing import normalize

import pandas as pd
import GetAllChampionNames
import GetSpecificMatch

# 1. Load all champions
champions = GetAllChampionNames.get_all_champion_names()

# 2. Load summoner champion counts
summoner_name = str(input("Enter summoner name: ")) # e.g. CTenk
region = str(input("Enter summoner region: ")) # e.g. NA1
summoner_champ_data = GetSpecificMatch.get_champion_vector(summoner_name, region)

vector = np.array([summoner_champ_data.get(champ, 0) for champ in champions])
print(vector)

normalized_vector = normalize([vector], norm='l2')[0]
print(normalized_vector)

df = pd.DataFrame({
    "Champion": champions,
    "Raw Count": vector,
    "Normalized (L2)": np.round(normalized_vector, 3)
})

print(df.to_string(index=False))
df.to_excel("vectorized_champion_choices.xlsx", index=False)