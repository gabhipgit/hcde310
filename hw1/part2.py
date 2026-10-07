# HW1 Part 2: Lists and loops
# Run it:  python3 part2.py
# Your output must match expected/part2.txt exactly.

from artworks import titles
count = 0
for title in titles:
    print(f"{count+1}. {title}")
    count = count +1

print (f"Titles: {count}")

countA = 0
for title in titles:
    #if "A" in title:
     #   countA = countA + 1 WHY DOESN"T THIS WORK (says there's 11 A's)
    if "a" in title: #does this account for uppercase as well?
        countA = countA + 1
print(f'Titles with an "a": {countA}')

longestTitle = ""
for title in titles:
    if len(title) > len(longestTitle):
        longestTitle = title
print(f"Longest: {longestTitle}")