# HW5 test_app.py: one example test. Add your own below it (step 5).
# Run from this folder:  python3 -m pytest
from app import app, get_artworks


def test_home_shows_search_form():
    client = app.test_client()        # a pretend browser, no server needed
    page = client.get("/")            # like typing "/" in the address bar
    assert page.status_code == 200    # the page loaded
    assert b"Artist name" in page.data  # the form's label is on the page


#Check 1- PASS
#Checks that valid search shows page with results
def test_search_shows_results(): 
    client = app.test_client()
    page = client.get("/results?artist=Monet")
    assert page.status_code == 200
    assert b'Results for "Monet"' in page.data



#Check 2- PASS
#empty search should stay on home.html, 
#but with specific error message 
#for no user inputted search
def test_empty_string_search(): 
    client = app.test_client()
    page = client.get("/results?artist=")
    assert page.status_code == 200
    assert b"No search term entered." in page.data

#Check 3- FAIL
#random string input should have no results
#with "no results found" message 
#on the results page
def test_random_string_search():
    client = app.test_client()
    page = client.get("/results?artist=asdfghjklkjhgfdsa")
    assert page.status_code == 200
    assert b"No results found for inputted search." in page.data


#Check 4- PASS
#makes sure only 10 results max per search
#'Monet' has multpile pieces, so it should show 10 results max. 
def test_ten_results_max():
    client = app.test_client()
    artworks = get_artworks("Monet")
    assert len(artworks) == 10
    

    