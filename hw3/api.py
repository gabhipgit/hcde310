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
    {"title": "Cathy Fake Art Two"},                           # no year
    {"title": None, "artist_title": "monet money"},          # title is there, but null
    {"artist_title": "dr seuss"},                         # no title at all
]

FAKE_ERROR = None                                         # what get_books_real() returns when the call fails

# Change this line to try a different case
FAKE_DATA = FAKE_ARTS


def find_art_FAKE(title):
    # Fake for now. When the path works, switch app.py to get_books_real().
    return FAKE_DATA

#This function gets the data from the API
def find_art(title):
   FIELDS = "image_id,title,artist_title" #date_display,artwork_type_title,place_of_origin"
   #title = input("Search the Art Institute for: ")
   params = {"fields":FIELDS, "title": title}
   headers = {"AIC-User-Agent": "HCDE310 student project HW4"}
   r = requests.get("https://api.artic.edu/api/v1/artworks/search", params=params, headers=headers)
   if r.status_code != 200:
           print("API error:", r.status_code, r.reason)
           return None
   return r.json()["data"][:10]
