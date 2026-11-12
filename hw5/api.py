import requests

URL = "https://api.artic.edu/api/v1/artworks/search"
FIELDS = "id,title,artist_title,date_display,image_id"

#RE-WRITTEN WITH AI 
def get_artworks(artist):
    params = {
        "query[match][artist_title][query]": artist, 
        #This is the particular part AI changed from the original. Instead of q: artist, it now uses the structured query format.
        #This looks for an exact match to the artist title inputted by the user. 
        "query[match][artist_title][operator]": "and",
        #This query line is if the user inputs 2 names (such as a first and last name) so that both parts are combined then matched,
        #rather than just finding results for each name.
        "fields": FIELDS,   # back to the comma-separated string
        "limit": 10, #10 results max per search
    }
    headers = {"User-Agent": "hcde310-artist-search/1.0"} #same as original
    response = requests.get(URL, params=params, headers=headers, timeout=10) #same as original
    response.raise_for_status() #same as original
    return response.json().get("data", []) #This line originally had the limit 10 line, but is now handled by the params above.
