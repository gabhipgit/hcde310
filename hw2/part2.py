# HW2 Part 2 – One dict = one thing
#
# In `part2.py`, print each artwork as `Title - Artist (Year)`, for example `The Bedroom - Vincent van
# Gogh (1889)`. Use `.get()` so a missing artist or year prints `Unknown` instead of crashing.

from artworks import artworks

for art in artworks:
    title = art.get("title", "Unknown")
    artist = art.get("artist", "Unknown")
    year = art.get("year", "Unknown")
    print(f'{title} - {artist} ({year})')