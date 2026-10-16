# HW2 Part 1 – Model first (in `design.md`, no code)

---

## 1. Why is `artworks` a list of dictionaries and not one big dictionary? What would you lose or gain the other way?

A list allows you to individually access all of the different arts in artworks; by picking on art in the list, you get access to all of the info regarding that piece. Since each element in the list is a dictionary, one can pull specfic data about each specific art by using a specific keys. 
Having a dictionary full of lists would group all the art pieces together and group by categories instead. For example, the keyword "title" would contain a list full of all the titles in artworks. While you would gain an easier access to categories within artworks as a whole and be able to see any missing fields faster if a list appears way shorter compared to the others, you would have to find each pieces respective index in the list, taking into account that any missing fields might mess up which index you associate it with. Also, with a list full of dictionaries, you'd be able to find a missing field faster when searching through specific keys because of the KeyError. A dictionary full of lists has the chance of misaligning data, and not being able to say which specific piece has missing data when there's missing fields within each list. 

## 2. Which fields are sometimes missing? What should the app show when they are?
The "artist", "year", and "medium"  fields are sometimes missing. Right now, the app would probably throw a KeyError when looking for a piece's specific fields if they are missing since those key terms literally don't exist in their dictionaries. However, when those fields are missing, the app should show "Unknown" to the user. The dictionaries should still have those keys, but have the keys store the word "Unknown".  