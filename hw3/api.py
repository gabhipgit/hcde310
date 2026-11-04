# api.py
import requests

# Fake data, same shape as the real API's "docs" list.
# One variable per case, so you can check how your page handles each one.
FAKE_ARTS = [
    {"title": "Cat Fake Art One", "artist_title": "van gough"},
    {"title": "Cathy Fake Art Two", "artist_title": "monet money"},
    {"title": "Dog Fake Art Three", "artist_title": "Pacita Abad"},
]

FAKE_EMPTY = []                                           # no results

FAKE_MISSING_FIELDS = [
    {"title": "Cat Fake Art One", "artist_title": "van gough"},
    {"title": "Cathy Fake Art Two"},                           # no artist
    {"title": None, "artist_title": "van gough" },          # title is there, but null
    {"artist_title": "dr seuss"},                         # no title at all
]

FAKE_ERROR = None                                         # what get_books_real() returns when the call fails

# Changed this line to try different cases
FAKE_DATA = FAKE_MISSING_FIELDS

# AI-written
#this helps with taking out art pieces that aren't relevant to inputted search. Without this function a gibberish input
#would result in a default list or artworks, same with artists that had less than 10 artworks in the API. 
def keep_relevant(arts, term):
    """Takes a list of artwork dictionaries and a search word, returns only those whose title or artist contains the word."""
    kept = []
    for art in arts:
        text = (art.get("title") or "") + " " + (art.get("artist_title") or "")
        if term.lower() in text.lower():
            kept.append(art)
    return kept

# AI-written
# deals with empty field states. Any art with empty or null artists would be dropped, 
# and any art with missing or empty titles are changed to "Unknown Title"
def clean_arts(arts):
    """Takes a list of artwork dictionaries and returns a new list with artist-less items dropped and missing titles set to "Unknown"."""
    cleaned = []
    for art in arts:
        if art.get("artist_title"):
            new_art = dict(art)
            if not new_art.get("title"):
                new_art["title"] = "Unknown Title"
            cleaned.append(new_art)
    return cleaned


def find_art_FAKE(artist_title):
    # Fake for now. When the path works, switch app.py to find_art.
    return FAKE_DATA

#This function gets the data from the API
def find_art(artist_title):
   FIELDS = "image_id,title,artist_title" 
   params = {"fields": FIELDS, "q": artist_title} #artist_title came from user input
   headers = {"AIC-User-Agent": "HCDE310 student project HW4"}
   r = requests.get("https://api.artic.edu/api/v1/artworks/search", params=params, headers=headers)
   if r.status_code != 200:
           print("API error:", r.status_code, r.reason)
           return None
   return r.json()["data"][:10]
