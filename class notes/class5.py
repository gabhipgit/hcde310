#key error: no such key
#type error: (str + int) without proper toString or ,
#Index error: past the end of the list
#name error: name python hasn't seen
#attribute error: none has noUpper()

# def greet():
#     print("hi")

# greet()
# x = greet()
# print(x)
# would return none
# x.upper() would give error because print x returns nothing

def greet():
    return ("hi")
# need a return if you want to set the value
greet()
x = greet()
print(x)
x.upper()


art = {"title": "Nighthawks",
       "tags": ["city", "night", "diner"]}
print(art["tags"][1])
print(len(art["tags"])) #prints 3 because it gives length of tags

#print(art["tags"]) gives the list attached to the "tags" key. city, night, diner

#JSON = java script object notation 