# In-class 6: NASA EPIC (photos of the whole Earth from space), with the key kept in .env
#
# 1. Load the key from .env (python-dotenv: load_dotenv(), then os.getenv("NASA_API_KEY"))
# 2. Call https://api.nasa.gov/EPIC/api/natural with your key as the api_key parameter,
#    and timeout=10 so it gives up instead of hanging if the server is slow
# 3. Check r.status_code before you use the data
# 4. The reply is a list of today's photos. Print the caption and the date of the first one

import os #for key 
import requests #lets u work with api ?
from dotenv import load_dotenv
load_dotenv() #reads file
key = os.getenv("NASA_API_KEY") #gives key without giving key info
#key = 12222223333 
print(key is None)


#url = "https://api.nasa.gov/EPIC/api/natural"
#r = requests.get(url, params={"api_key": key}, timeout=10)

#print(r.status_code)

r = requests.get("https://api.nasa.gov/EPIC/api/natural", #gets the api
params={"api_key": key}, timeout=10) # gives key so NASA accepts, then gives up after 10 s

# if r.status_code == 200: #if status of code works
#     print(r.json()[0]["caption"]) #(r in json form so it's in list form, take index 0) print out caption of today's first photo of the whole Earth
#     print(r.json()[0]["date"]) #prints out todays first photo of whole earth's date

#     #alt code to combine both print statements
#     #photo = r.json()[0]
#     #print(photo["caption"], photo["date"])

# else:
#     print("Request failed:", r.status_code, r.reason) # 403 = bad or missing key

# def newest_photo(photos):
#     count = 0
#     for photo in photos:
#         count = count+1
#     print(r.json()[count]["date"])

# print(newest_photo(photos))

# AI-written
def newest_photo(photos):
    """Takes a list of photo dictionaries and returns the latest 'date' string."""
    newest = photos[0]["date"]
    for photo in photos:
        if photo["date"] > newest:
            newest = photo["date"]
    return newest

test = [
    {"date": "2026-10-20 03:12:00"},
    {"date": "2026-10-20 18:45:00"},
    {"date": "2026-10-20 09:30:00"},
]
print(newest_photo(test))