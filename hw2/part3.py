# HW2 Part 3 – Counting with a dictionary
#
# In `part3.py`:
#
# 1. Build a dictionary counting works per artist, and print it: `{'Vincent van Gogh': 1, ...}`. A
#    work with no artist counts under `'Unknown'`.
# 2. Print the artist with the most works: `Most works: Claude Monet (2)`
#
# (This is the letter-counting pattern from Class 3, applied to art.)

from artworks import artworks

dict = {}
mostCount = 0
mostArt = ""

for art in artworks:
    dict[art.get("artist", "Unknown")] = dict.get(art.get("artist", "Unknown"), 0) + 1
    if dict.get(art.get("artist", "Unknown"), 0) > mostCount:
        mostCount = dict.get(art.get("artist", "Unknown"))
        mostArt = art.get("artist", "Unknown")
    
print(dict)
print (f'Most works: {mostArt} ({mostCount})')



