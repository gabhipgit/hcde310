#Flask set up/ imports 
#import from flask, import api from chicago art museum 

#app.py  
# --- app.py --- 
from flask import Flask, render_template, request 
from api import find_art_FAKE, clean_arts

app = Flask(__name__) #

#Home page/main search page
#This should be the search page, the user can type in input, and once 'search' is clicked, it should move to the results page
#If an empty search, it should prompt the user to enter input
#If search yeilds no result, it should still go to results page (but show error message)

@app.route("/")
def home():
    return render_template("home.html")


#arts page
#takes the "title" input from home page
#uses find_art("title") to get results and displays image, title, artist, year, type, and place
#if user imputs title with no results, displays error message "no works found"
#if api not found/broken, no results with error message "broken request: status code + reason"
#if fields missing for an art piece, set value to unknown

@app.route("/arts")
def arts():
    # 1. Read the search term from the form
    artist_title = request.args.get("artist_title_search", "").strip()

    # 2. Empty input? → home page + message (check BEFORE calling the API)
    if artist_title == "":
        return render_template("home.html", message="Enter a search first to Find Art.")

    # 3. Call the API (fake data for now)
    arts = clean_arts(find_art_FAKE(artist_title))
    #arts = None
    #arts=[]

    # 4. API error? (get_books returned None) → arts/results page + message
    if arts is None:
        return render_template("arts.html", artist_title=artist_title, message="API Error: Search won't work")


    # 5. No results, or nothing useful to show? → arts/results page + message
    if len(arts) == 0:
        return render_template("arts.html", artist_title=artist_title, message="No results found for inputted search.")
    
    # 6. Otherwise → results page
    return render_template("arts.html", arts=arts, artist_title=artist_title)





#results page
#This should display artworks and their details (title, artist, year, origin) that match the users search. 
#There should be a magnifying glass on the page, that when clicked takes user back to search page
#There should be an 'Artist Results' component on the top right of the page, showing artist count on current displayed pieces
#Clicking on an artwork, should increase img, as well as their details
#Save button that when clicked, saves all the artworks being displayed in list form. 

                          
