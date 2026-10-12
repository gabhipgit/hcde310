# HW1 notes

## Part 4: Predict, run, explain

**My prediction for `predict.py` (written BEFORE running it):**
I think that for the first 4 titles, it will print the index number (starting at 0), then the title at that index, then the year it was published (plus an additional 100 years). On the next line it will print out the letter length of the current title. Then on the next line, it will print out the title length of the first title in the list 

0, The Bedroom, 1989
10
10
(it would repeat this pattern until the title "A Sunday on La Grande Jatte")

**What it actually printed:**
0 The Bedroom 1989
1 Nighthawks 2042
2 American Gothic 2030
10
11
It actually only printed 3 titles (in the same format I predicted), the length of how many titles were in title, then the length of the first title. 

**Explain:** If I was off, which line surprised me and why? If I was right, why do the last two lines print different numbers?
I think the line that most suprised me was line 6 (for i in range(3):). I thought it meant it would loop until an index of 3, meaning it would get through 4 titles. Instead, the 3 meant only 3 iterations. The two last lines only print once and are different because they are outside of the for loop. Even though I was not right, the length of titles differed between the two lines because the first one (without index) takes the amount of titles in artworks, and the length of titles with an index prints the length of the specific title. 

## Part 5: Reflection (about 100 words)

Look back at your Day 1 app: its code if you can still open it, or your screenshots of it running. Is there anything you can now recognize (a loop, an `if`, a list)? Where? If you only have screenshots, what do you think the code had to do to make the app behave that way?

There are many if-statements in the AI generated code from day 1. Most of them occur while figuring out which pieces from the Chicago website should be moved to the AI generated app. For example, there's an if-statement that checks if the website page was refreshed. There's also an if-statement that checks out whether the user scrolled to the bottom of the page in order to load more pieces. While I'm not seeing any for loops, I do see the method .ForEach(x) a lot, which makes me wonder if that acts as a for-loop as well. The .ForEach method also involves loading in certain amounts of artworks (either for every piece added also take in their data, or for each piece saved, save the information). There's a couple of lists at the beginning of the python code for the "filtering words" such as the tabs under the search bar. 