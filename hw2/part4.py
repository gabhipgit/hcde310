# HW2 Part 4 – Your first functions
#
# In `part4.py`, turn code you already wrote into functions:
#
# 1. `works_by(artist, artworks)` → returns a list of titles by that artist, from the list you pass in
#    (an empty list if there are none)
# 2. `count_by_artist(artworks)` → returns your counting dictionary from Part 3
# 3. Replace each `TODO` docstring with one line saying what the function takes and what it returns
#
# Don't change the `print` lines at the bottom of `part4.py`. `check.py` uses them.

from artworks import artworks


def works_by(artist, artworks):
    """TODO: one line saying what it takes and what it returns.This function takrs in an artist name, and the artworks """
    pass
    artistList = []
    for art in artworks:
        title = art.get("title", "Unknown")
        painter = art.get("artist", "Unknown")
        if painter == artist:
            artistList.append(title)
    return(artistList)
#.append(value) is how to add to a list in Python



def count_by_artist(artworks):
    """TODO: one line saying what it takes and what it returns."""
    pass
    diction = {}
    for art in artworks:
        diction[art.get("artist", "Unknown")] = diction.get(art.get("artist", "Unknown"), 0) + 1
    return(diction)

print(works_by("Claude Monet", artworks))
print(works_by("Nobody", artworks))
print(count_by_artist(artworks))
