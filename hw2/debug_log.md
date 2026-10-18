# HW2 Part 5 – Debug log (`debug_log.md`)

Record **at least 2 errors** you hit. No errors? Break something on purpose and log it. For each error, write:

---

## Entry 1

### 1. Error message
File "C:\Users\Gah01\OneDrive\Documents\hcde310\hw2\part2.py", line 19, in <module>
    if art.get(art["artist"]) == None:
               ~~~^^^^^^^^^^
KeyError: 'artist'


### 2. What I thought it meant
I thought this error meant that I was setting all the "artist" keys in art to None. I thought I was using the key "artist" correctly, so I believed I was somehow making all the "artist" keys override to None rather than trying to check if there was an "artist" key. 

### 3. What it actually meant
What this error actually meant was that the computer was not reading the "artist" key in the way I expected. Because I wrote it as art.get(art["artist"]) with art["artist"] in (), it was looking for a key matching the actual artist being held in that specific art, not "artist" as the key. 

### 4. The fix
art.get("artist", "Unknown")
The first fix was changing art.get(art["artist"]) to just art.get("artist"). The second change to get the correct code was realizing art.get("artist", "Unknown") was not going to set every "artist" key's value to "Unknown", but would only change any art in artworks without an "artist" key to have one with a value of "Unknown".

## Entry 2

### 1. Error message
 File "C:\Users\Gah01\OneDrive\Documents\hcde310\hw2\part4.py", line 23, in works_by
    artistList[art] = title
    ~~~~~~~~~~^^^^^
TypeError: list indices must be integers or slices, not dict


### 2. What I thought it meant
I thought this error meant that I was using the wrong variable to try and access artistList/set artistList with a title value. 

### 3. What it actually meant
art is not an integer, and therefore would not work as a way to access artistList at that specific index/place. Since art is not an integer, you can't set a title to that specific art in artistList either. 

### 4. The fix
artistList.append(title)
.append(value) is how to populate a new list when getting data from a for loop that doesn't keep track of index place