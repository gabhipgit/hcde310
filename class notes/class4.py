#building a dict by counting, not typing answer
counts = {}
print (counts)
counts["cat"] = 1
counts["dog"] = 1
print (counts)


pets = [
    {"animal": "cat", "name": "Chairman Meow"},
    {"animal": "dog", "name": "Wishbone"},
    {"animal": "cat", "name": "Garfield"},
    {"animal": "dog", "name": "Lassie"},
    {"animal": "goat", "name": "Gruff"},
    {"animal": "dog", "name": "Snoopy"},
]

pet = pets[0]
print (pet)


def label(year):
    if year < 1900:
        return "old"
    return "modern"

print(label(1889),label(1942))
