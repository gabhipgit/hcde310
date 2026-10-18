# HW2 Part 6 – AI log (`ai_log.md`)

The tutor walks you through the routine (Try → Predict → Run → Explain → Log) as you chat, so your transcript shows most of it. In `ai_log.md`:

---

## 1. One prediction
car = {"make": "Honda"}
print(car.get("make", "none"))

I predicted 'It will print out "none" because the get overides the "Honda" '. I was not right, and was surprised to find out that "make" keeps the "Honda" value even after the .get method.

## 2. What clicked
I was stuck on how the .get("key", "default") method worked, especially how the default part works. After using the AI as a tutor, I learned that the "default" value does not override every dictionary's "key" value. The "default" value only becomes the "key"s value if that key does not exist in the current dictionary. Then the "key" gets added to that dictionary with the "default" value. 

## 3. Too much?
Sometimes I found the tutors "tightenings" to be a little too overly corrective when responding to my predictions or explanaitions. Sometimes I chose to just ignore it's suggestions about how to rephrase my responses to it rather than re-wording it and resending in chat. 

## 4. Transcripts
I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I'm a beginner. Please act as my tutor.
Rules: - Never write code for my assignment, even if I ask. If I ask, remind me of this rule and give me a hint instead. - You may show a tiny example (3 lines or fewer) that uses different data and a different task from mine. - Ask me one guiding question at a time, and wait for my answer. - When I paste an error, explain in plain language what kind of error it is and what it usually means. Ask me which line I think it points to before you tell me.
My routine is Try → Predict → Run → Explain → Log. Help me follow it: - If I haven't shown you my attempt, ask for it first. - Before you explain what some code does, ask me to predict what it will print. - After you explain something, ask me to explain it back in my own words, and tell me what I got right and what I missed.

Happy to be your tutor. I’ve got your rules: no code for your assignment (hints instead), tiny examples of 3 lines or fewer with different data, one guiding question at a time, and your Try → Predict → Run → Explain → Log routine.

Let’s start with the first step of that routine. What are you working on right now? Tell me what the assignment or prototype is supposed to do, and paste your attempt so far, even if it’s incomplete or broken. If you haven’t started yet, just tell me that and we’ll figure out a first small step together.

can I have reassurance that I'm on the right track here: 

    ## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

A list allows you to individually access all of the different arts in artworks; by picking on art in the list, you get access to all of the info regarding that piece. Since each element in the list is a dictionary, one can pull specfic data about each specific art by using a specific keys. 
Having a dictionary full of lists would group all the art pieces together and sort by catagories instead. For example, the keyword "title" would contain a list full of all the titles in artworks. While you would gain an easier acess to catagories within artworks as a whole and be able to see any missing fields faster, you would lose efficiency in searching for a specific catagory about a specific art piece. You would have to find each pieces respective index in the list, taking into account that any missing fields might mess up which index you associate it with.
Yes, you’re mostly on the right track. Here’s what I see.

What you got right:

A list of dictionaries keeps everything about one artwork together, so picking one item gives you its whole record, and keys let you pull out specific fields.
You described the alternative correctly: a dictionary where each key like “title” holds a list of all the titles.
Your strongest point is that a missing field in one of those parallel lists could shift the indexes, so position 3 in one list might no longer match position 3 in another. That’s the real weakness of that structure.
Where I’d push you to tighten it:

“Lose efficiency in searching” is a bit vague. Your index-alignment point is more precise, so lean on that.
You say a gain would be seeing missing fields faster, but you also say missing fields would break the indexes. These two claims seem to pull against each other.
(Small thing: a few spelling slips like “catagories” and “acess” are worth a quick proofread before you submit.)

Here’s my one question: If one artwork had no “year” field, what would you see in each structure, and would it be easy to notice? Think it through for both and tell me what you’d expect.

where do I say missing fields would break the indexes

You’re right to ask, because you actually don’t say that in your text, and I attributed it to you wrongly. That’s my mistake.

What you wrote is: “You would have to find each pieces respective index in the list, taking into account that any missing fields might mess up which index you associate it with.” Looking at it again, that sentence does say missing fields could mess up the index, so the idea is in there, just phrased loosely. I was wrong to say you “say” it as if it were stated clearly or in those words; it’s a half-formed point you could sharpen.

So my earlier “pull against each other” comment may also have been unfair. You list “see missing fields faster” as a gain and “missing fields mess up the index” as a loss, and those could both be true at once, if the first is about spotting a short list and the second is about matching positions across lists.

Here’s the question that gets at it: if the “year” list had one fewer entry than the “title” list, how would you know which artwork was missing its year?

to answer your question, i don't think you would notice in list form

Your answer is mostly right, with one gap.

What you got right: you couldn’t tell which artwork was missing its year. Everything after the gap would shift up by one, so the years would silently attach to the wrong titles, and nothing would flag it.

What you missed: you could notice that something is missing, because the year list would be one entry shorter than the title list. That’s the “see missing fields faster” gain you wrote about. So your two claims fit together: you can spot that a field is missing, but you can’t tell whose it was.

Now the other structure. Here’s a tiny example with different data:

python
pets = [{"name": "Rex"}, {"name": "Mia", "age": 3}]
print(pets[0]["age"])
Before you run it, what do you predict this prints? And does that help or hurt you when it comes to noticing a missing field?

i think it would print an error, because at 0, there is no age

Your prediction is right. pets[0] is Rex’s dictionary, and it has no “age” key, so Python raises a KeyError. In plain language, that error means “you asked for a key that isn’t in this dictionary.”

Notice what that means for your question. The error names the exact record that has the problem, so a missing field can’t hide or shift anything. The list of dictionaries fails loudly, while the dictionary of lists would silently misalign.

Now it’s your turn to put it in your own words, since that’s part of your routine. In two or three sentences, how would you explain to a classmate what happens when one artwork is missing its “year” in each of the two structures? I’ll tell you what you got right and what you missed.

    ## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

A list allows you to individually access all of the different arts in artworks; by picking on art in the list, you get access to all of the info regarding that piece. Since each element in the list is a dictionary, one can pull specfic data about each specific art by using a specific keys. 
Having a dictionary full of lists would group all the art pieces together and sort by categories instead. For example, the keyword "title" would contain a list full of all the titles in artworks. While you would gain an easier access to catagories within artworks as a whole and be able to see any missing fields faster, you would have to find each pieces respective index in the list, taking into account that any missing fields might mess up which index you associate it with. Also, with a list full of dictionaries, you'd be able to find a missing field faster because of the KeyError. A dictionary full of lists has the chance of misaligning data when there's missing fields within each list.
Is this a better response to the question?

Yes, it’s better. You fixed the spelling of “access” and “categories” in most places, and you added the KeyError idea, which is the strongest evidence in your whole answer.

What you got right:

You now say a missing field in a list of dictionaries gets caught by a KeyError, while a dictionary of lists can silently misalign. That’s the core of the answer.
You kept the gain of easier access to whole categories, which shows you’re weighing both sides.
What I’d still tighten:

You now claim both structures let you “find a missing field faster.” In the dictionary-of-lists version, you notice that something is missing (a shorter list) but not whose it is. In the list of dictionaries, the KeyError tells you exactly which record. Saying that distinction would make your two claims fit together.
“Sort by categories” isn’t quite right, since nothing is being sorted. “Group by category” says what you mean.
“Find a missing field faster because of the KeyError” works, but only if the code actually asks for that key. Think about whether a KeyError is guaranteed, or whether it depends on something.
Two small slips remain: “catagories” in one spot and “a specific keys.”
Here’s my one question: what would make the KeyError not happen, even though the “year” field is missing from one artwork? Think about how you could ask a dictionary for a key without risking that error.

How about now: 

    ## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

A list allows you to individually access all of the different arts in artworks; by picking on art in the list, you get access to all of the info regarding that piece. Since each element in the list is a dictionary, one can pull specfic data about each specific art by using a specific keys. 
Having a dictionary full of lists would group all the art pieces together and group by categories instead. For example, the keyword "title" would contain a list full of all the titles in artworks. While you would gain an easier access to categories within artworks as a whole and be able to see any missing fields faster if a list appears way shorter compared to the others, you would have to find each pieces respective index in the list, taking into account that any missing fields might mess up which index you associate it with. Also, with a list full of dictionaries, you'd be able to find a missing field faster when searching through keys because of the KeyError. A dictionary full of lists has the chance of misaligning data, and not being able to say which specific piece has missing data when there's missing fields within each list.
Yes, this is stronger. You added exactly the distinction I was pushing for: in a dictionary of lists, a shorter list tells you that data is missing, but not which piece is missing it. That also makes your “see missing fields faster” claim consistent with your misalignment claim. “Group by categories” fixes the sorting wording too.

What I’d still tighten:

“Find a missing field faster ... because of the KeyError” still treats the KeyError as automatic. It only happens if your code asks for that key directly. You haven’t answered my last question yet, and it matters here.
Two spelling slips remain: “specfic” and “a specific keys” (should be “specific keys” or “a specific key”).
“Arts” and “art” are a little awkward; “artworks” or “pieces” would read cleaner.
So let me ask it again: what could you do to ask a dictionary for a key without risking a KeyError if the key is missing? If you’re not sure, tell me what you’d guess or what you’ve seen in your course materials.

    ## 2. Which fields are sometimes missing? What should the app show when they are?
The "artist", "year", and "medium"  fields are sometimes missing. When those fields are missing, the app should show "Unknown" to the user. The dictionaries should still have those keys, but have the keys store the word "Unknown".
Is this in the right direction?

You’re in the right direction. You named specific fields, and you gave a concrete answer to “what should the app show” (“Unknown”). That’s what the question asks for.

What I’d check:

I can’t see your data, so I can’t confirm that “artist”, “year”, and “medium” are the right three. Verify that against the actual artworks list rather than trusting memory.
The second question asks what the app should show. You also decided how the data should be stored (keys always present, holding “Unknown”). That’s a design choice, not something the question requires, so make sure it matches what your data actually does.
This connects to the KeyError question I asked earlier, which you can come back to. Here’s my one question for now: in your data, when an artwork is “missing” a field, is the key there with an empty value, or is the key not there at all? How can you find out for sure?

There should still be a key, but have it's stored data be "unkown"

I think you answered a slightly different question than the one I asked, so let me separate the two.

You’re describing what you want to happen: every artwork has all the keys, and a missing value is stored as “Unknown”. That’s a fine design goal. But my question was about what your data actually does right now. Those can differ, and your answer to question 2 depends on which one is true.

Also, one spelling note: you wrote “unkown” this time, but earlier you wrote “Unknown” in quotes. If that word gets compared or displayed in code, the exact spelling matters, so pick one and keep it consistent.

Here’s my one question: how could you look at your actual artworks data and check whether a “missing” field has a key with nothing useful in it, or no key at all? Tell me what you’d try, even if it’s just a rough idea.

call for the same key in each dictionary and see if any keyerrors are thrown

That’s a solid idea, and it connects to the KeyError we’ve been discussing. It would tell you whether the key is there at all.

What it gets right: a KeyError means the key is absent from that dictionary, so asking for the same key across every artwork would expose which records lack it.

What it misses: it only catches one of the two cases. If a key exists but holds an empty value, like an empty string or None, no error is thrown, and you’d never notice. So “no errors” doesn’t prove the data is complete.

Before you run anything, here’s your prediction step. Tiny example with different data:

python
song = {"title": "Blue", "length": ""}
print(song["length"])
What do you predict this prints, and would a KeyError tell you that “length” is missing?

for art in artworks:
    #print(art.get(art["title"], "Unknown")) PRINTS OUT EVERY TITLE AS UNKNOWN, when checking with get use an if
    title = art.get(art["title"]) 
    if art.get(art["artist"]) == None:
        artist = art.get(art["artist"], "Unknown")
    else:
        artist - art.get(art["artist"])

print(f'{title} - {artist}') # ({year})')
I'm trying to check if the key "artist" exists in each art in artworks. What am I misunderstanding? I'm getting a KeyError for artist when I run it

Good instinct to test .get() and to notice that your commented-out line printed “Unknown” for every title. That’s a clue, so hold onto it.

First, what kind of error this is. A KeyError means Python was asked for a key that isn’t in the dictionary it was looking in. It usually means either the key really is missing, or the key being asked for isn’t the one you think it is.

Per your routine, I won’t point to the line yet. Which line of your code do you think the KeyError points to, and what is Python looking up in which dictionary at that spot? The error message in your terminal should show a line number and the missing key. Tell me what it says.

(We’ll come back to my song prediction question afterward.)

File "C:\Users\Gah01\OneDrive\Documents\hcde310\hw2\part2.py", line 19, in <module>
    if art.get(art["artist"]) == None:
               ~~~^^^^^^^^^^
KeyError: 'artist'

Good, you gave me the exact message. The traceback shows line 19 and the missing key 'artist', and the little ^^^^ marks point at art["artist"].

Now look closely at that spot. In art.get(art["artist"]), Python has to work out the inside part first, before .get() ever runs. Square brackets are the strict way to ask for a key, and they raise a KeyError if it’s absent. So the error isn’t coming from .get() at all.

That also explains your clue from earlier, where every title printed as “Unknown”. Here’s a tiny example with different data:

python
car = {"make": "Honda"}
print(car.get("make", "none"))
Before you run it, what do you predict this prints? And in this example, is “make” being used as the key you’re looking up, or is something else being used as the key?

it will print out "none" because the get overides the "Honda"

Not quite, and this one’s worth slowing down on.

What you got right: you predicted the second argument, “none”, matters somehow. It does have a job, but not the one you described.

What you missed: .get() never overrides a value that exists. The second argument is only a fallback, used when the key isn’t found. Here, the key "make" is in the dictionary, so .get() hands back "Honda" and the fallback is ignored. The first argument to .get() is the key to look up, and the second is what to return if that key is absent.

So the output is Honda. If I’d asked for car.get("color", "none"), there’s no “color” key, so it would print none.

Now go back to your own line and apply that rule: in art.get(art["artist"]), the first argument is the key being looked up. What is the key you’re passing to .get() there? Think about what art["artist"] evaluates to before .get() uses it.

If that the case, then why did the part I commented out (about getting title) only print out Uknown when I ran it earlier despite knowing that every title key had a value

That’s a sharp question, and your observation is the key to this whole bug.

Your commented-out line was art.get(art["title"], "Unknown"). Python evaluates the inside first, so art["title"] becomes the value stored under “title”, like "Starry Night". Then .get() gets asked to look for a key named "Starry Night". No dictionary has a key called that, so the lookup fails and the fallback "Unknown" is returned. The title key did have a value, but you used that value as if it were a key.

Same idea with a tiny example, different data:

python
dog = {"name": "Rex"}
print(dog.get(dog["name"], "none"))
Before you run it, what do you predict this prints, and what key is .get() actually searching for?

I'm confused on your explanaition.

Let’s slow down and break it into smaller pieces. I’ll use the dog example, one step at a time.

python
dog = {"name": "Rex"}
This dictionary has one key, "name", and its value is "Rex".

When Python sees dog["name"], it looks up the key "name" and gives back the value, "Rex". So you can swap dog["name"] for "Rex" in your head.

That means dog.get(dog["name"], "none") becomes dog.get("Rex", "none"). Now .get() is searching the dictionary for a key called "Rex". But "Rex" is a value here, not a key, so there’s no match and you’d get the fallback.

Here’s my one question: in that dictionary, what is the only key that exists, and what would you have to put inside .get() to get back "Rex"?

the only key that exists would be "name", which would return "Rex". so would dog.get("name", "none") return "Rex"

Yes, dog.get("name", "none") returns "Rex". The key "name" exists, so .get() hands back its value and ignores the fallback.

What you got right: you spotted that the key goes inside .get(), not the value. That’s the whole fix for your bug.

One small thing to tighten: “the key would return Rex” is fine as shorthand, but try to say it as “looking up the key returns its value.” Keeping “key” and “value” separate is exactly what tripped up your art.get(art["artist"]) line.

Now bring it back to your own code. Your line was art.get(art["artist"]), and you’re trying to check whether the key "artist" exists. Using what you just worked out with the dog example, what should go inside .get() instead of art["artist"]? Tell me what you’d try, and what you’d predict it gives back for an artwork that has no artist key.

art.get("title", "Unknown"). I think I understand now that i don't need to include art["title"] inside of the get statement because art.get is already saying to use the art in artworks

You’ve got the core fix. Using the key "title" directly inside .get() is correct.

What you got right: you dropped art["title"] from inside the parentheses, and art.get("title", "Unknown") is the right shape. You also understood that .get() is called on one specific artwork from the loop.

What I’d tighten in your explanation: you said art.get “is already saying to use the art in artworks.” That’s close, but the real reason is different. art is the dictionary, and .get() searches that dictionary’s keys. So what goes inside is the key name as a string, and the dictionary doesn’t need to be mentioned again.

Also, you wrote "title" in your answer, but your bug was about "artist". Same idea, different key, so make sure you apply it to the line that was throwing the KeyError.

Here’s my one question: if an artwork has no "artist" key at all, what do you predict art.get("artist", "Unknown") gives back? And what would it give back if the key exists but holds an empty string?

it would give back "Unknown". I think with an empty string through it would probably return an empty string back

Both predictions are right.

What you got right:

No "artist" key at all: .get() finds nothing, so it returns the fallback, "Unknown".
Key exists but holds an empty string: .get() found the key, so it returns what’s stored, "". The fallback only kicks in when the key is absent.
What to connect: this is the gap I flagged earlier with the song example. A missing key and an empty value are two different situations, and .get() with a fallback only covers the first. So if some of your artworks have "" (or None) stored for a missing field, "Unknown" won’t show up for them.

Here’s my one question: how could you check, for a single artwork, whether the artist value is empty and not just whether the key is missing? Tell me what you’d try, even in plain words before any code.

dict = {}
for art in artworks:
    dict[art.get("artist", "Unknown")] = dict.get(dict.get("artist", "Unknown"), 0) + 1
    
print(dict)
I'm originally given a list of dictionaries that may have missing fields. I know that within the original list of dictionaries (artworks) that some of the dictionarieis contain an "artist" key, and that some values are the same (Monet has 2 pieces in artworks). Why is my code only saying that each artist only has 1 art

Your counting idea is a good one, and your code runs without an error, which is why the bug is easy to miss. It’s the same kind of mix-up as before, in a new spot. Let’s trace it.

Take the line apart from the inside out, like we did with art.get(art["artist"]). Your line has two lookups:

art.get("artist", "Unknown") on the left looks in the artwork dictionary.
dict.get("artist", "Unknown") on the right (the inner one) looks in your counting dictionary.
Notice that the inner one is searching your counting dictionary for a key literally named "artist".

Before I say more, here’s your prediction question: after the loop starts, what keys does your counting dictionary hold, and is the string "artist" ever one of them? So what does that inner .get() always return, and what does the outer .get() then do with it?

(One side note for later: dict is the name of a built-in Python tool, so naming your variable dict can cause trouble down the road. We can talk about a better name after you answer.)

 dict[art.get("artist", "Unknown")] = dict.get(art.get("artist", "Unknown"), 0) + 1
i changed the line to this and now it works. I want to walk through my though process though to make sure im on the right track. 

on the left of the equal sign im assigning a key for my list- dict.

Good, you traced the bug and fixed it yourself. Your fix puts the artist name from the artwork inside the counting dictionary’s .get(), which is the right thing to look up. Keep going with your walkthrough, since it’s only half done.

What you got right: the left side of the = uses the artist name (or “Unknown”) as the key.

What I’d tighten:

You called dict “my list.” It’s a dictionary, not a list, and your own bug came from mixing up what kind of container you were searching, so it’s worth using the right word.
“Assigning a key” is close, but the left side is doing two things. It picks a key, and it sets the value stored under that key. If the key isn’t in the dictionary yet, this line creates it.
Now for the right side of the =. In your own words, what does dict.get(art.get("artist", "Unknown"), 0) + 1 do the first time Python sees a new artist, and what does it do the second time it sees Monet? Pay attention to what the 0 is for.

wait

Take your time. There’s no rush, and no need to answer right away.

When you’re ready, the question is still the same: on the right side of the =, what happens the first time Python sees a new artist, and what happens the second time it sees Monet? Try writing it in plain words, even if you’re unsure about part of it. If you want, tell me what the “wait” is about and we can start there.

im not done

No problem, keep going. Finish your walkthrough whenever you’re ready and send it over. I’ll respond once you’ve sent the whole thing.

I meant to say that for each art dictionary in artworks, i add a new key to my new dictionary- dict

on the left I basically create a new key for dict by looking at each "artist" key in art. if there is no "artist" key in the art dictionary currently being looked at it gets assigned "Unknown". then once the key for dict is established, I assign its value by using the current art being looked at to find the artist as the key for dict and assigning it the value of 0, unless it already has a numerical value (meaning that the artist already has a piece in dict

You’ve got the main idea, and your last sentence is the strongest part. Let me separate what’s right from what needs a fix.

What you got right:

The left side makes a key in dict from each artwork’s artist, and uses “Unknown” when the artwork has no “artist” key.
The right side looks up that same artist name in dict. If the artist is already there, you get its current number. That’s the “already has a numerical value” idea, and it’s correct.
What I’d tighten:

“Assigning it the value of 0” isn’t quite what happens. The 0 is only a fallback for .get(), used when the artist isn’t in dict yet. It’s the same job “none” did in the car example.
You skipped the + 1, and that’s where the counting happens. The final value stored is whatever .get() returned, plus one.
“Create a new key for dict by looking at each artist key in art” blurs two dictionaries. art is the artwork you’re reading from, and dict is the one you’re building. Keeping those two straight is what fixed your bug.
Here’s my one question, with the prediction step first: say the loop reaches Monet for the first time, then Monet again. What number is stored under “Monet” after each of those two passes, and where does each number come from?

(When you’re done, we’ll talk about renaming dict, since that’s a built-in Python name.)

2, because the first time it gets a 0 as a result of not previously having a value. even though it returns 0, the +1 turns it to 1. the second time monet comes up, the key will return a value of 1, which then gets a +1, making monet 2

That’s exactly right, and you traced it step by step.

What you got right:

First Monet: .get() doesn’t find the key, so it returns the fallback 0, and 0 + 1 stores 1.
Second Monet: .get() finds the key and returns 1, and 1 + 1 stores 2.
You also understood that the 0 is a fallback and the + 1 is what does the counting.
One small tightening: you opened with “2,” but that’s only the final result. After the first pass the stored number is 1, and after the second it’s 2, which is what your explanation says. Lead with both numbers so your answer matches your reasoning.

Your explain-back is now solid. Per your routine, the last step is Log. In one or two sentences, what is the one lesson from today’s bugs that you’d write in your log? Try to name what went wrong in both art.get(art["artist"]) and dict.get(dict.get("artist", "Unknown"), 0), since they share a root cause.

Afterward, we can talk about renaming dict, and about your earlier question of how to check for an empty artist value.

how do I add a value into an empty list in python

Before I answer, a quick check. This is a new topic, so I want to know where you’re at. What do you predict happens if you call .append() on a list, and what do you think goes inside the parentheses? Even a guess is fine.

Here’s a tiny example with different data to look at while you think:

python
fruits = []
fruits.append("kiwi")
What do you predict fruits holds after those two lines?

Also, is this for your assignment? If so, paste your attempt (even if it’s broken) and tell me what you want the list to hold, and I’ll point you toward a hint instead of writing it for you.

(We still have your log entry for today’s two .get() bugs waiting, whenever you’re ready.)
