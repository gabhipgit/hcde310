#Flask, Hands on coding

#app.py 
# --- app.py ---
from flask import Flask, render_template, request
from api import find_books

app = Flask(__name__)

@app.route("/") #binds url to function  / returns homepage
def home():
   artworks = [{"title": "Lilies"},
               {"title": "Nighthawks"}]
   return render_template("home.html", artworks=artworks) 


@app.route("/about") #/acout returns to about us
def about():
   return "About us"


@app.route("/books")
def books():
   return render_template("books.html")


@app.route("/results")
def results():
   author = request.args.get("author_search", "")
   return render_template("results.html",
                          books=find_books(author))
