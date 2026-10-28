#api = a url your code asks instead of a person
#r is the response object: the whole replu, like an envelope 

#Status codes: the first digit tells you most of it.
    #2XX = it worked
    #3XX = go somewhere else
    #4XX = you made a mistake
    #5XX = the server had a problem
#e.reason gives the name, "not found"

import json
import requests
#import pandas won't work; ModuleNotFoundError: No module names 

#.venve is a folder in your project with its own Python and its own packages
#.venv\Scripts\activate
#Activate = this terminal now uses that folder
#(.venv) in you prompt means it's on
#ls .venv = look at what's in .venv
#deactivate = exit the venv

#API Documentation
# docs tell you the endpoints parameters, fields, rate limits, and terms
#how do you know

# 1. How to ask for only some fields and why: 
# There would be a lot of data for each art work, so when looking for specific ones use following format"
# fields= id,title,artist
# makes queries run faster, and gives aic ability to see which fields need continued support

# 2. How many requests per minute without a key
# 60 requests per minute 

# 3. How to get more than 12 results:
    #page for a specific page of results
    #limit for how many records each page returns

# 4. Yes, but any image can get unpublished or replaced at any time

# 5. has_not_been_viewed_much

base = "https://api.artic.edu/api/v1/artworks"

#r = requests.get(base + "?limit=1")
#r = requests.get(base + "/search?q=cats&limit=1")
r = requests.get(base + "/search?query[match][title] = cats")
print(r.status_code)
    #data = r.json()

#artworks = data["data"]
#print(data)
# requests.get(base + "/search?q=cats&limit=1")
# requests.get(base + "/search?q=zzzqqxx&limit=1")

# for each: r.json()["pagination"]["total"]
#API's key is app's ID Card 
#long random string that acts as you. DONT PUT THE KEY IN YOUR CODE
#AI tools often write the key straight into code; watch out for it
#put keys in the .env file 
# .env(in your project folder)
#NASA_API_KEY=abc123xyz
#.env is in .gitignore