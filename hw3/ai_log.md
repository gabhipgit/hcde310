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