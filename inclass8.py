import requests
import json

url = "https://api.artic.edu/api/v1/artworks/search"

all_artworks = []

for page in [1, 2]:
    params = {
        "q": "food",
        "limit": 50,
        "page": page,
        "fields": "id,title,artist_title,date_display,medium_display,image_id"
    }
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, params=params, headers=headers)
    
    data = response.json()

    all_artworks.extend(data["data"])

with open("group_d.json", "w") as file:
    json.dump(all_artworks, file, indent=2)

print("Saved", len(all_artworks), "artworks")