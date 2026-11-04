#Flask set up/ imports 
#import from flask, import api from chicago art museum 

#app.py  
# --- app.py --- 
from flask import Flask, render_template, request 
from api import find_art, clean_arts, keep_relevant

app = Flask(__name__) #

#Home page/main search page
#This should open to the home page, the user can "find art" by typing in an artist's name, 
#once 'find art' button is clicked, it should move to the results page

@app.route("/")
def home():
    return render_template("home.html")


#Results page
#takes the input from home page
#displays titles of art pieces associated with entered artist (happy state)
#if an empty search state, it should stay on home page and prompt the user to enter input 
#if user imputs search with no related art (no results state), it should go to results page and display error message "No results found for inputted search."
#if api not found/broken state, go to results page with error message "API Error: Search won't work"
#if missing fields state, take out any arts with missing artist values. Any arts with a known artist, but missing title get a default title of "Unknown Title" 

@app.route("/results")
def arts():
    # 1. Read the search term from the home form
    artist_title = request.args.get("artist_title_search", "").strip()

    # 2. Empty input state: home page + message 
    if artist_title == "":
        return render_template("home.html", message="Enter a search first to Find Art.")

    # 3. Call the API 
    arts = keep_relevant(clean_arts(find_art(artist_title)), artist_title)

    # 4. API error state: results page + message
    if arts is None:
        return render_template("results.html", artist_title=artist_title, message="API Error: Search won't work")

    # 5. No results state: results page + message
    if len(arts) == 0:
        return render_template("results.html", artist_title=artist_title, message="No results found for inputted search.")
  
    # 6. Happy state: results page
    return render_template("results.html", arts=arts, artist_title=artist_title)

    # 7. Missing field state: 
    #   this is handled in the api.py file through clean_arts(arts) function. Any arts with null or missing artist_title's get excluded from results
    #   and any art titles that are null or missing get a value of "Unknown Title", if they have usable artist_title
                      
