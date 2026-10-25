# HW3 Part 2 + Part 3 + Part 4
#
# Instructions: README.md in this folder (same as the assignment on Canvas).

import requests

FIELDS = "id,title,artist_title,artist_display,date_display"

# Functions go here (above the code that runs)
def count_by_artist(data):
    """This function takes into account all the art in artworks then returns a dictionary keeping track of how many art pieces each artist has."""
    pass
    diction = {}
    for art in data:
        diction[art.get("artist_title", "Unknown") or "Unknown"] = diction.get(art.get("artist_title", "Unknown"), 0) + 1
    return(diction)

term = input("Search the Art Institute for: ")

url = "https://api.artic.edu/api/v1/artworks/search"      # TODO: the search URL from step 2

params = {"q":term,"fields":FIELDS}   # TODO: q (the search term) and fields (FIELDS)
headers = {"AIC-User-Agent": "HCDE310 student project"}
response = requests.get(url, params=params, headers=headers)


# TODO step 3: check response.status_code before you use the data
if response.status_code != 200:
    print("Request failed:", response.status_code, response.reason)

else:
    data = response.json()

    # TODO steps 4-5: loop over the results and print each one (reuse your HW2 printing code),
    #                 print a default for null fields, and print a helpful message if there are no results
    #from sample_response.json import FIELDS
    if len(data["data"])== 0:
        print("No results for inputted search")
    else:
        for art in data["data"]:
            #title = art.get(data["data"][0]["title"] , "Unknown") 
            # i don't need to include the whole pathway because art in the loop is already in data["data"], and doesn't need an index counter because each art in loop is it's own
            title = art.get("title" , "Unknown") or "Unknown" 
            #this line first checks gets art's "title" value. if there is no "title key, it creates one and assigns the value "Unknown". If the key is there, but the value is null, the "or Unknown" gets set to "Unknown"
            artist = art.get("artist_title", "Unknown") or "Unknown"
            year = art.get("date_display", "Unknown") or "Unknown"
            print(f'{title} - {artist} ({year})')
        print(count_by_artist(data["data"]))