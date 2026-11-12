import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"

#REWRITTEN WITH AI 
def get_artworks(artist):
    params = {
        "query[match][artist_title][query]": artist,
        "query[match][artist_title][operator]": "and",
        "fields": FIELDS,   # back to the comma-separated string
        "limit": 10,
    }
    headers = {"User-Agent": "hcde310-artist-search/1.0"}
    response = requests.get(URL, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json().get("data", [])
