# HW3 Part 1 – Read the response first

AI Use: Stage 2 (Tutor)

Open `sample_response.json` (a saved Art Institute of Chicago search). In `notes.md`:

---

## 1. The total number of results is at `data["pagination"]["total"]`. What's the path to the first artwork's title?
data["data"][0]["title"] 

## 2. Find 3 more fields you'd want to show a user, and their paths
1. field: alt-text for the first artwork
data["data"][0]["thumbnail"]["alt_text]

2. field: artwork_type_title for the first artwork
data["data"][0]["artwork_type_title"]

3. field: artist_title for the first artwork
data["data"][0]["artist_title"]

## 3. Which fields are `null` for some works?
Overall the "preference" field is null, and for some works the "artist_title" field is null. 

## 4. Predict
*open `fetch.py` and read it, but don't change anything yet. What do you think will happen when you run it?*
Without making any changes yet and only reading the code, I predict that running it (once all the code is fully there) will allow a user to search the Chicago Art Institute for specific art works by inputing search terms. Assuming the response code sends back a code that indicates successful running, the computer will return artworks that match the inputed term and include their associated data. (Lack of data for a piece on no results for a term will return a default answer)

## 5. Run it
*run `python3 fetch.py`. When it asks for a search term, type a word (like `cat`) and press Enter. What actually happened? Read the traceback bottom line first: what went wrong, and which line of your file caused it?*
After pressing enter the code did not run, it sent a bunch of errors. The bottom line traceback says, "requests.exceptions.MissingSchema: Invalid URL '': No scheme supplied. Perhaps you meant https://?". This means that a big reason its not working right now is because we haven't provided a url yet, so our API can't even access the information it needs. Line 14 has the missing url, and line 16 has the API call that triggers the error. 