# AI log

## HW0: Class 1, build an app with AI

Paste every prompt you sent, in order, with the AI's replies. A share link to the chat is fine too, but paste the prompts here either way. Your thinking about it goes in `day1.md`.

**Share link (optional): https://claude.ai/share/017bc609-be51-452b-88e9-48aa9d8f6b98**

### Prompt 1

```
Build a single-page interactive web app. It calls the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search) when the user searches or filters, and shows results with images. Keep it under ~150 lines. It's for students @ UW at who was design major. who want to look for Inso for their art assignment. My sketch is attached; follow it. Explain how the code works in plain language, section by section.
```

**AI's reply:**

I built it as a single HTML file, about 125 lines. Download it and open it in your browser. I didn't publish it as a hosted page because those block requests to other sites, so the museum API wouldn't load. I haven't tested it against the live API.

How the code works

1. The layout (HTML and CSS). This follows your sketch from top to bottom:

A search pill.
A row of four category chips.
A 3-column grid of artwork tiles that you scroll.
A bottom bar with the flower and person icons.

The header is "sticky", so search and filters stay put while the images scroll underneath. The colors are a light gallery-white with a pink-red accent, taken from your pen color. It switches to dark mode if your device is set to dark.

2. The setup. The code defines the museum's API address and the four categories: Painting, Sculpture, Photography, Print. It also creates one small "state" object that remembers what you're doing: the search words, the chosen category, which page of results you're on, and your saved artworks.

3. Category chips. The chips are created from that category list. Clicking one highlights it and reloads the results. Clicking it again clears the filter.

4. Search box. It waits 400ms after you stop typing before searching, so the app doesn't call the API on every keystroke.

5. load(), the part that calls the API. It joins your search words and category into one query, for example "portrait Photography". It then asks the museum for 24 results. The API only sends back image IDs, so the code turns each ID into a picture link. It skips anything with no image. A "token" number throws away old responses if you start a new search before the last one finishes. If the internet fails, you get a plain error message.

6. addCard(). It builds one tile per artwork with a lazy-loaded image. Lazy-loaded means it only downloads images as you scroll toward them. Clicking a tile opens the pop-up.

7. openModal(). The pop-up shows a larger image, the title, the artist and the date. It has three buttons:

"Save for later"
"View at museum", which opens the official artwork page
"Close"

I set text with textContent rather than pasting it into HTML, so odd characters in titles can't break the page.

8. Flower button (saved board). It switches between search results and the artworks you saved, which works like a mood board for your assignment. Saves are kept in memory only, so refreshing the page clears them.

9. Scrolling. An invisible marker sits at the bottom of the grid. When you get close to it, the next page loads automatically.

Two things to know. The person icon is a placeholder that just shows "Profiles are not built yet." Also, the category filter works by adding the word to the search, so results are close but not strict. For exact filtering, I could switch to the API's structured query, which takes more code.

### Prompt 2

```
on the same screen, provide recommended art pieces underneath the categories
```

**AI's reply:**

I added a "Picks for design students" row directly under the category chips, above the main grid. I haven't run it against the live API.

How it works

Where the picks come from. The code keeps a list of ten design-flavored themes, such as Bauhaus, poster, typography, Art Deco, and pattern textile. When the page opens, it picks one at random and asks the museum API for 12 matching artworks. The heading shows the theme, for example "Picks for design students: Bauhaus".
How it looks. The picks sit in a single row you swipe or scroll sideways, with smaller tiles than the main grid. That keeps the vertical scroll free for search results.
"Show different picks" button. It chooses a new theme, never the same one twice in a row. This gives students fresh ideas without typing anything.
Reused code. The picks use the same tile and pop-up as the main grid, so you can still open one and save it to your board. I changed addCard() so it can place a tile in either the row or the grid.

The picks are the same for everyone at the moment. They don't adapt to what a student searches or saves. If you'd like that, I can base the theme on the last search or on the saved board.

### Prompt 3

```
refer to the layout of the reference image, provide  art pieces from the Art Institute of Chicago API (https://api.artic.edu/api/v1/artworks/search)underneath the category cards
```

**AI's reply:**

I rebuilt the page to match your reference, and Art Institute of Chicago pieces now fill the space under the category tabs. I haven't run it against the live API.

What changed to match the reference

Search bar: a wide, soft grey rounded bar with a magnifier icon inside. I left out the camera and mic icons because they wouldn't do anything.
Categories: the pill buttons are now plain text tabs like "All / Aesthetic art", with a black underline on the active one. The tabs are All, Painting, Sculpture, Photography and Print.
Art feed: the grid is now a masonry layout with three columns, or two on a phone. Artworks keep their real proportions instead of being cropped, and have large rounded corners. Each new piece goes into whichever column is currently shortest, so the columns stay balanced while you scroll.
Under each piece: a short title on the left and a "..." button on the right, like the reference. The "..." opens the same pop-up as clicking the image, with a larger view, a museum link, and Save for later.

What appears under the tabs

On open: the feed shows art from a random design theme, such as Bauhaus, posters or typography, under the heading "Picks for design students: Bauhaus". "Show different picks" switches to a new theme.
When you search or pick a tab: the feed switches to those results, and the shuffle link hides.
Scrolling: more pieces load automatically near the bottom.

I merged the earlier sideways "Picks" row into this main feed, because two separate grids on one screen would repeat each other. The flower button at the bottom still switches to your saved board.

### Prompt 4

```
why you can't reach the museum.
```

**AI's reply:**

The museum's API is working. I just called it directly and it returned results (about 133,000 artworks), so the problem is where the page is running, not the API.

The most likely cause is that the page is open inside Claude's preview window. That window blocks requests to outside websites, so the app can't reach the museum and shows "Could not reach the museum." To fix it:

Download inspo-finder.html from the file card above.
Open the saved file in Chrome, Safari or Firefox (double-click it, or drag it into a browser window).

The page should then load artworks normally.

If it still fails in a regular browser, these are the next things to check:

Campus or school Wi-Fi: some networks block unfamiliar sites. Try your phone's hotspot.
Ad blockers or privacy extensions: try a private window with extensions off.
VPN: turn it off briefly.

I can't run the page myself because my sandbox has no internet access, so I can't confirm what you're seeing. If you tell me where you opened it and whether the error stays, I can narrow it down. I can also change the error message to show the actual reason (blocked, offline, or a bad response), so it's clear what went wrong next time.

### Prompt 5

```
this is what we are seeing from our end
```

**AI's reply:**

That screenshot looks like the app running inside Claude's preview pane. It's the narrow panel with the rounded edge on the right. The layout, tabs and search bar all render, but the preview blocks the page from talking to any outside website, so the request to the museum fails and you get "Could not reach the museum." Nothing is wrong with the code or the museum's API.

To see real artworks:

Download inspo-finder.html from the file card (the download button on the file).
Open the saved file in a regular browser tab, Chrome, Safari, or Firefox. On a Mac you can double-click it, or right-click and choose Open With.
It should then load the "color study" picks, and search and the tabs should work.

If you want to share it with classmates, give them the downloaded file to open the same way. It needs an internet connection but nothing to install.

If it still shows the error in a regular browser tab, tell me which browser and network you're on (home or campus Wi-Fi). I can also make two changes if you'd like: show the exact failure reason in the message, and add a few built-in sample artworks so the preview isn't empty when the museum can't be reached.

### Prompt 6

```
for the nav bar at the bottom, include clickable icons that represent: Saved (a book mark for example), User/Setting, Home
```

**AI's reply:**

'm wiring up the three nav buttons (Home, Saved, Settings) next, then I'll hand you the updated file.

Edited a file, shared files

The bottom bar now has three labeled icons: Home (house), Saved (bookmark), and Settings (person). I haven't run the page. As before, open the downloaded file in a regular browser tab for the museum images to load.

Home: clears the search box and category, goes back to "All", and scrolls to the top. The design-theme picks reload.
Saved: shows the artworks you saved from the pop-up.
Settings: opens a small panel with a Match device, Light or Dark switch. It also shows how many artworks you've saved and has a Clear saved button.

The icon for the screen you're on turns pink and fills in. When Settings is open it is the highlighted one, and closing it returns the highlight to Home or Saved.

Saved artworks are still kept only in memory, so refreshing the page clears them. I can store them in the browser so they survive a refresh, if you'd like that.

### Prompt 7

```
Explain how the code works in plain language, section by section.
```

**AI's reply:**

Here is the current file, from top to bottom. It's one HTML file with three parts: the structure (HTML), the look (CSS), and the behavior (JavaScript).

1. The look (CSS)
Colors: a few named colors sit at the top (background, text, grey, pink-red accent). Every other rule uses those names, so changing the look means changing one line. Dark mode swaps the same names for dark values.
Search bar and tabs: the search bar is a grey rounded box with an icon. The tabs are plain bold text, and the active one gets a black underline.
The grid: the feed is a row of side-by-side columns. Each artwork keeps its natural shape, with large rounded corners, and a short title and a "..." button sit underneath.
Sticky header and bottom bar: the search bar and tabs stay at the top, and the nav stays at the bottom, while the art scrolls between them.
2. The structure (HTML)

The page has a header (search and tabs), a main area (a heading with the "Show different picks" link, the empty feed, a status line, and an invisible marker at the bottom), and the nav with three buttons. There is also a hidden pop-up box (<dialog>) that gets filled in when you open an artwork or Settings.

3. The setup
Constants: the museum's address, the tab names, and ten design themes (Bauhaus, poster, typography, and so on).
s (the page's memory): it tracks your search words, the chosen tab, the current theme, which page of results you're on, whether a request is in progress, your saved artworks, and whether you're viewing the Saved screen.
img(): turns an image ID from the museum into a picture link. The size is a parameter, so the grid gets small images and the pop-up gets large ones.
4. Tabs and search
Tabs: the code builds the five tabs from the list. Clicking one sets the category, moves the underline, and reloads the feed.
Search box: it waits 400ms after you stop typing before searching, so the museum isn't asked on every keystroke.
Themes: pickTheme() chooses a random theme different from the last one. "Show different picks" calls it and reloads.
5. Loading the art
resetGrid(): empties the feed and builds fresh columns, three on a desktop or two on a phone. It also bumps a "token" number. That way, if you start a new search while the old one is still loading, the old answer is ignored.
load():
Sets the heading ("Results for…" or "Picks for design students: …").
Builds the search phrase from your words and tab. If both are empty, it uses the theme.
Asks the museum for 24 results.
Skips anything without an image and adds the rest.
Shows "No results" or an error message if needed.
6. Building the masonry (addCard)

Each artwork becomes a tile with an image, a title, and a "..." button. The museum sends each image's width and height, so the code reserves the right amount of space before the image loads and the page doesn't jump. It keeps a running height for each column and puts each new tile in the shortest one, which keeps the columns even.

7. The pop-up (openModal)

Clicking an image or "..." fills the pop-up with a larger image, the title, the artist and the date. It has three buttons: Save for later (or Remove), View at museum, and Close. Text goes in with textContent rather than as raw HTML, so unusual characters in titles can't break the page.

8. The bottom nav
Home: clears the search and tab, reloads the feed, and scrolls to the top.
Saved: swaps the feed for the artworks you saved, using the same tile builder.
Settings: fills the pop-up with a Match device, Light or Dark switch, a saved count, and Clear saved.
setNav(): highlights whichever icon matches the current screen.
9. Endless scrolling and startup

An invisible marker sits below the feed. When it comes within 600px of the screen, the browser tells the code to load the next page. The last line picks a starting theme and loads the first batch.

Saved artworks live only in memory, so they disappear when you refresh. The page also needs the internet to reach the museum, which is why it has to be opened in a normal browser tab.