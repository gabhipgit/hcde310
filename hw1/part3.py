# HW1 Part 3: Decisions
# Run it:  python3 part3.py
# Your output must match expected/part3.txt exactly.

from artworks import titles, years

cutoff = 1900  # works made before this year are "old"

count = 0
for title in titles:
    if years[count] > cutoff:
        print(title)
    count = count +1


print()

count2 = 0
old = 0
modern = 0
for title in titles:
    if years[count2] > cutoff:
        print(f"{title}: modern")
        modern = modern +1
    else:
        print(f"{title}: old")
        old = old + 1
    count2 = count2 +1


print()
print(f"Old: {old}")
print(f"Modern: {modern}")
