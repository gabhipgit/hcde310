# def label(year):
#     if year < 1900:
#         return "old"
#     return "modern"

# print(label(1889),label(1942))

#def = define label = name of function 
#functions: jobs with a name
#takes parameters, and returns something 
# " " " = docstring; like a comment but readable by VSCode
#appen() function that adds items to end of list
# comment out = control + /

def works_by(artist, artists, titles):
    """return titles by one artist"""
    found = []
    for i in range(len(titles)):
        if artists[i] == artist:
            found.append(titles[i])
    return found

#why functions: 
# reuse: write once, call many times
# readability: the name says what it does
# testing: you can check one piece at a time

titles = ["Nighthawks", "The Bedroom", "Sky above Clouds IV"]

def titles_with(word, titles):
    """returns a list of titles with the word in it"""
    titlesWith = []
    for t in titles:
        if word in t.lower():
            titlesWith.append(t)
    return titlesWith

print(titles_with("the", titles))

#type error: i doesn't always mean a number. it can be a string !!
myList = ["cats", "dogs", "goats"]
for i in range(len(myList)):
    print(f"{i + 1}. {myList[i]}")

myList = ["cats", "dogs", "goats"]
for i, value in enumerate(myList, start = 1): #list view
    print(f"{i}. {value}")

#chats vs agents
#chat: you decide what goes in your files, it makes things but doesn't change your things
#agents: giving your computer access to generate files, move things arounds

import json
with open("aic_sample.json") as f:
    data = json.load(f)
results = data["data"] #a list
first = results [0] # a dict
print (first["title"])
