years = [1889, 1942, 1973]
for y in years:
    if y <= 1900:
        print(y, "old")
    elif y < 1950:
        print (y, "mid-century")
    else: 
        print (y, "recent")
        
    if y >= 1900 and y < 1950:
        print("first half of the 20th century")


#results = [a,b,c]
#results = []
#if results:
 #   print[each of resultsts]
#else:
 #   print[no results]

#list uses []
#key uses {}
#keys are usuallt strings, so needs quotes
# a dictionary stores key-value pairs:looks value by name {key}, not it's position
#LISTS LOOK BY POSITION, DICTIONARY LOOKS BY KEYS

phone = {"Ana": "555-1234", "Sam": "555-6789"}
print(phone["Ana"])


art = {"title": "The Bedroom",
       "artist": "Vincent van Gogh",
       "year": 1889}
print(art["title"])
print(art.get("medium", "Unknown")) #how to look something u w/o crashing if not there


artworks = [
    {"title": "The Bedroom", "artist": "Vincent van Gogh", "year":1889},
    {"title": "Nighthawks", "artist": "Edward Hopper"},
]

for art in artworks:
    print(art["title"], "-", art["artist"])



# PARALLELS CHCEK UR ASSIGNMENT
#titles = ["The Bedroom", "Nighthawks", "Mao"]
#years = [1889, 1942, 1973]
#for i in range(len(titles)):
 #   print(titles[i], years[i])


#counts = {}
#counts ["b"] = 1
#counts ["a"] = 1
#counts ["n"] = 1
#counts ["a"] = 2
#print (counts)

counts = {}
for letter in "banana":
    if letter in counts:
        counts[letter] = counts[letter] + 1
    else:
        counts[letter] = 1
print(counts)

#shortcut method
counts = {}
for letter in "banana":
    counts[letter] = counts.get(letter, 0) + 1
print(counts)
