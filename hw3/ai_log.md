# HW3 Part 4 – Save the results

AI Use: Stage 3 (Little helper) 

Write a new function, `save_results(artworks, filename)`, that writes one line per artwork (title, artist, date) to a `.txt` file. Call it so every search saves its results. Then run `fetch.py` for real once, with a search you pick, and **commit the `.txt` file it made**: that's your proof the live call works.

You may have the AI write this function (about 10 lines) using the **[Stage 3 helper prompt](https://canvas.uw.edu/courses/1959879/pages/stage-3-little-helper-prompt)** (rules on the [AI Use Card](https://canvas.uw.edu/courses/1959879/pages/ai-use-card)). Copilot autocomplete stays off. With or without AI, write each step in `ai_log.md` **as you go**:

Done early? Add `sort_by_date(artworks)` too (not graded).

---

## 1. Try
*paste your own attempt or plan for the function, even if it doesn't work*
def save_results(artworks, filename):
    """This function takes in a list of dictionaries representing different artworks and their info, then saves each artworks' title, artist, date, type of art, and origin place into a seperate .txt file (filename). The filled out .txt file is returned"""

    plan: 
    store the print statement lines as a string
    add that string into filename 
    i know in java theres a way to take inputs/outputs and inprint them into a separate file using file io stuff, so I'm guessing there's a similar method for python. 
    my plan is to use this function after every print(f'{title} - {artist} ({year}) - {type} - {place}') line in the for loop in fetch that gets every term's title, artist, year, type, and place.
    every time this method is called it should return the file name with a new line in it. 

    where i'm stuck: 
    I feel like there are other methods I can use to save and store a print line, and a method that "prints" this string into it's own file. I'm also not sure if returning the file after each loop iteration is the way to go

    the function i need: 
    save_results(artworks, filename). takes in a list of dictionaries representing different artworks and their info, then saves each artworks' title, artist, data, type, and place into a seperate .txt file (filename). The filled out .txt file is returned

## 2. Chat (AI only)
*paste the whole conversation, your messages and the AI's replies in order, or a share link from the Share button (the link in your address bar only works for you). No AI? Write "No AI used."*

LINK TO AI CHATs: 
Chatting with AI on Stage 2: https://claude.ai/share/1bfb7f2d-7ec6-4bd4-a1bc-b121f465c273 
Chatting with AI on Stage 3: https://claude.ai/share/5ec05810-2117-4016-9a2f-43c7da235687 


## 3. Predict, then compare
*before you run the function, write what you think the file will contain for the sample data (`check.py` uses it) or for your search. Then paste what it actually contains. (A wrong prediction gets full credit. Don't edit it after running.)*
I think using the sample data, the file will contain the following:
Lion (One of a Pair, South Pedestal) - Edward Kemeys (1893) - Sculpture - Chicago
Nude with Cats - Pablo Picasso (1901) - Painting - Spain
Baroque Pearl Mounted as a Cat Holding a Mouse - Unknown (17th century) - Costume and Accessories - Spain
Cat Making Up - Inagaki Tomoo (1962) - Print - Japan
Homesickness - René Magritte (c. 1948) - Drawing and Watercolor - Belgium

What the file actually contained: 
Lion (One of a Pair, South Pedestal) - Edward Kemeys (1893) - Sculpture - Chicago
Nude with Cats - Pablo Picasso (1901) - Painting - Spain
Baroque Pearl Mounted as a Cat Holding a Mouse - Unknown (17th century) - Costume and Accessories - Spain
Cat Making Up - Inagaki Tomoo (1962) - Print - Japan
Homesickness - Ren� Magritte (c. 1948) - Drawing and Watercolor - Belgium
Winter: Cat on a Cushion - Th�ophile-Alexandre Pierre Steinlen (1909) - Print - France
Border Fragments - Nasca (100 BCE�200 CE) - Textile - Peru
The Return of Odysseus (Homage to Pinturicchio and Benin) - Romare Howard Bearden (1977) - Drawing and Watercolor - United States
Lions on the Dreyfus Fund III - Larry Rivers (1964) - Painting - United States
Summer: Cat on a Balustrade - Th�ophile-Alexandre Pierre Steinlen (1909) - Print - France

## 4. What surprised me
*one or two sentences. Where were you wrong, or what did you learn? For example: "I thought a missing artist would print `none`, but `.get` gave the fallback `unknown`."*
One thing that surprised me was how useful debugging with print statements would be. I learned that especially when dealing with AttributeErrors, print statements can help me to debug by seeing what you think you're holding versus what you actualy have. 

## 5. Change one thing yourself
*once the function works, change one thing about it by hand, no AI. For example: a different line format (date first), a filename based on the search term, or sorted lines. Write what you changed and why, in one or two sentences.*
I added the or "Unknown" to this line in the save_results method: 

line = f"{art['title'] or "Unknown"} - {art['artist_title'] or "Unknown"} ({art['date_display'] or "Unknown"}) - {art['artwork_type_title'] or "Unknown"} - {art['place_of_origin'] or "Unknown"}"

This now means that when entering each art's details from artworks into a file, fields that have null values will be written as "Unknown" instead of "None". I changed it because I figured it would be good practice to make sure to be aware of null values and be able to manually change/re-word their values. 

-------------------------------------------------------------------------------------------------------------------------
# AI LOG FOR HW4

I'm a Human Centered Design & Engineering student learning Python so I can prototype interactive apps. I follow a routine: Try → Predict → Run → Explain → Log.
My attempt so far: [paste your code or plan, even if it doesn't work] Where I'm stuck: [one sentence] The function I need: [name]([inputs]) takes [what] and returns [what].
Rules: - Write only this one function, about 10 lines or fewer. No other code, and don't change mine. - Put # AI-written on the line above the function. - Start the function with a one-line docstring that says what it takes and returns. - Use only what a beginner would know: loops, if, lists, dictionaries, and the libraries I'm already using. If you need something new, tell me its name and what it does in one line. - Don't explain the code yet. Ask me to predict what it returns for [one real input]. Wait for my prediction. - After I've run it and told you the result, ask me to explain each line in my own words. Correct anything I got wrong, then ask me about one line I skipped. - Then suggest one small change I could make myself (don't write it). Wait until I tell you what I changed. - Then ask me: what's one thing that surprised you? Don't answer it for me. - For anything other than this one function, act as my tutor: hints and questions, no code.

Your message still has the template placeholders in it. The brackets for your attempt, where you’re stuck, and the function you need are all unfilled, so I don’t have anything to write yet. I don’t want to guess at a function and skip your “Try” step.

Could you send me these three things?

Your attempt so far: paste your code or your plan. A half-working attempt or a rough plan in plain words is fine.
Where you’re stuck: one sentence.
The function you need: its name, what it takes, and what it returns, like count_votes(votes) takes a list of strings and returns a dictionary of counts.

It would also help to know which libraries you’re already using (for example, just plain Python, or something like tkinter, streamlit, or pandas), so I stay inside what you know.

Once I have those, I’ll write just the one function, short and marked # AI-written, and then ask you for a prediction before explaining anything.

headers = {"User-Agent": "HCDE310 class demo"} 
this line is an example from class, what does it mean

Let’s take it apart piece by piece instead of me just telling you.

Piece 1: the shape. Look at the curly braces and the colon inside them. You’ve seen this structure when learning Python. What is it called, and what’s on the left of the colon versus the right? What is headers in relation to that?

Piece 2: the words. A hint for “User-Agent”: whenever a program asks a website for a page, it sends a little bundle of information along with the request, like a label on a package. That label is called a header. “User-Agent” is one standard label name, and its job is to say who or what is making the request.

Piece 3: the why. Think about your own experience. When you open a page in a browser, the website knows whether you’re on a phone or a laptop, in Chrome or Safari. Now picture a Python script asking for that same page. What would the website see if your script didn’t say anything about itself? Why might a website owner care to know who’s asking, especially if a script is making hundreds of requests?

Piece 4: the connection. The string “HCDE310 class demo” is the value. Why might it be helpful to put your class name there rather than something generic?

A few things to try:

Answer Pieces 1 and 3 in your own words, even if you’re unsure.
Look at the class example this line came from. Where does headers show up again after it’s created? That will tell you what it’s used for.

What do you think it does, based on those clues?

import requests

FIELDS = "id,title,artist_title,artist_display,date_display,artwork_type_title,place_of_origin"
#term = input("Search the Art Institute for: ")

  
headers = {"AIC-User-Agent": "HCDE310 student project"}
def find_art(term):
   params = {"fields":FIELDS, "term": term} 
   r = requests.get("https://api.artic.edu/api/v1/artworks/search", params=params, headers=headers)
   return r.json()["data"][:10]

I don't see headers anwhere else past the r = line

Glad it works. Here’s the function again, so you can go line by line.

python
# AI-written
def keep_relevant(arts, term):
    """Takes a list of artwork dictionaries and a search word, returns only those whose title or artist contains the word."""
    kept = []
    for art in arts:
        text = (art.get("title") or "") + " " + (art.get("artist_title") or "")
        if term.lower() in text.lower():
            kept.append(art)
    return kept

Describe each line in your own words, and say “not sure” where you’re unsure and guess. A few spots to think about:

What are kept and text at the start and end of each trip through the loop?
What does art.get("title") or "" do when the title is missing or None? How does that compare to what you saw in clean_arts?
Why is .lower() called on both term and text? What would change for “Monet” versus “monet” if it weren’t?
What does in check in term.lower() in text.lower()?

I’ll correct anything off, then ask about one line you skipped.

for each art in arts list, it get's the art's artist and title. then it checks if term.lower or text.lower (which im unsure what that does). if it is lower though it adds the art to the kept list and returns kept after loop

You’ve got the overall shape: loop through the artworks, keep the ones that pass a check, and return kept at the end. Here are the corrections.

.lower() doesn’t check anything. It’s a string method that returns a lowercase copy, so "Claude Monet".lower() gives "claude monet". Try print("Monet".lower()) in a scratch file to see it. The word or also isn’t part of that if line.
The check is in. Read the line as a question: is the lowercase search word found somewhere inside the lowercase text? If yes, the art goes into kept. If no, it’s skipped. Why do you think both sides get lowercased before the question is asked?
text isn’t just “getting” the title and artist. That line builds one single string out of the two, so one in check can search both.

A line you skipped: art.get("title") or "". Say what you think this does when the title is missing or None, and what would go wrong in the + part if it just used art.get("title") and the title were None. Also, what do you think the " " between the two pieces is for?

Answer that, and then I’ll give you the next step.

What surprised: I was surprised by how much I liked to explain my train of thought to the AI while stuck. Even when it didn't ask for it, I tried to always explain my reasoning. I guess it's like a mix between rubber duck coding, and talking through code problems with another person

What changed: I ended up just changing my vs code to auto save because a lot of troubleshooting I went through with AI was a result of me just forgetting to save before running code again. 