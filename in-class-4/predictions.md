# Class 4: Five broken snippets

Your name: Gabby Hipolito 
Collaborator: Saurav 

# Part 1: Predict

**Don't run anything yet.** Read each snippet in `exercise.py` and write your guesses. A wrong guess is fine: the point is to compare.

## Snippet 1
- Which line breaks? 8 
- What error will Python show? (the kind and the message) Key error; Room not recognized
- What's the fix? "Room" to "room"

## Snippet 2
- Which line breaks? 12
- What error will Python show? (the kind and the message) type error: trying to access code and string together
- What's the fix? use (f"")

## Snippet 3
- Which line breaks? 16 
- What error will Python show? (the kind and the message) index error: range starts at 0, + 1 will go out of bounds
- What's the fix? just take out the +1 in for loop

## Snippet 4
- Which line breaks? 29
- What error will Python show? (the kind and the message) name error: doesn't recognize "visit"
- What's the fix? turn visit to visits

## Snippet 5
- Which line breaks? 38
- What error will Python show? (the kind and the message) attribute error: functions NEED return statements
- What's the fix? instead of print; return (longest)

# Part 2: Run

Run `python3 exercise.py`. Python stops at the first error, so fix that snippet in `exercise.py`, run again, and see the next one. Fill in what actually happened.

## Snippet 1
- Which line broke? 8
- What error did Python show? KeyError: 'Room'
- What's the fix?exhibit["room"]

## Snippet 2
- Which line broke? 12 
- What error did Python show? TypeError: can only concatenate str (not "int") to str
- What's the fix? print(f"Find it in room {exhibit["room"]}")

## Snippet 3
- Which line broke? 17 
- What error did Python show? IndexError: list index out of range
- What's the fix? for i in range(len(exhibits)):

## Snippet 4
- Which line broke? 29
- What error did Python show? NameError: name 'visit' is not defined. Did you mean: 'visits'?
- What's the fix?

## Snippet 5
- Which line broke? 41
- What error did Python show? AttributeError: 'NoneType' object has no attribute 'upper'
- What's the fix? return(longest)

When all five are fixed, run `python3 check.py` until it says ✓.

Bonus: Snippet 5 prints something *before* it crashes. What, and why does it still crash?
it prints Water Lilies before it crashes but I'n not sure why. I thought it might've had something to do with the order which the method was called, but the only other method was toUpper, and the Water Lilies that printed were not in all caps.

# Part 3: Tutor practice (one snippet)

Pick one snippet. Write your guess first, then ask your tutor. Paste the chat (or a share link) below.

- Snippet #: 1
# Snippet 1
exhibit = {"title": "Water Lilies", "room": 243, "year": 1906}
print("Find it in room " + exhibit["Room"])

- Our guess before asking: it's probably going to point out the error as a key error. It will also probably encourage me to see what key's I have and double check it's the key that I want. 

- Chat: https://claude.ai/share/0634f51b-9417-4410-9a27-9e540908bdeb

- Did it give you too much? What did you do? It really talked me through all the issues, making me preict, and say what I learned back to it in my own words. It even caught a double quotes error that still ran, but improved syntax. In my opinion it was doing a lot for right now, but I can see how as the concepts increase in difficulty for AI to be a useful tutor tool, especially when getting stuck while coding later in the night
