# The Database Merger

print("Before Merging the two dictionaries")
defaults = {
    "theme" : "light",
    "audio" : "on"
}
user_pref = {
    "theme": "dark"
}

print("defaults Dictionaries")
for key, value in defaults.items():
    print(key, value)

print("user_pref Dictionaries")
for key, value in user_pref.items():
    print(key, value)

defaults.update(user_pref)            # defaults dict is updated with user_pref dict's values

print("After Merging the two dictionaries")
for key, value in defaults.items():
    print(key, value)
