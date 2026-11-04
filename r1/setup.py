import os, requests
from dotenv import load_dotenv
load_dotenv()

def lastfm(method, **params):
    r = requests.get("https://ws.audioscrobbler.com/2.0/", params={
        "method": method,
        "api_key": os.environ["LASTFM_API_KEY"],
        "format": "json",
        **params,
    })
    data = r.json()
    if "error" in data:
        raise Exception(f"Last.fm error {data['error']}: {data['message']}")
    return data

# Global top tracks
tracks = lastfm("chart.gettoptracks", limit=5)
for t in tracks["tracks"]["track"]:
    print(t["artist"]["name"], "-", t["name"])