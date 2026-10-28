term = input("Search for: ") #input takes in anything entered and makes it a string
print("You searched for", term)
print(type(term))

# you can import your own files 
#from dotenv import load_dotenv

import os #for key 
import requests #lets u work with api ?
from dotenv import load_dotenv
load_dotenv() #reads file
key = os.getenv("NASA_API_KEY") 

print(key is None)

url = "https://api.nasa.gov/EPIC/api/natural"

response = requests.get(url, params={"api_key": key}) # how to send params in (aka accesss API Key)

print(response.status_code)