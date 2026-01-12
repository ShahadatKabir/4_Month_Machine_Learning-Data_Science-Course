# The Frequency Counter 

word = input("Enter a word: ")

frequency = {}              # Initialized an empty dictionary

value = 0                   # Initialized the character counter 0

for ch in word:
    if frequency == {}:
        frequency[ch] = frequency.get(ch, value) + 1    # Incremented by 1 the first character
    else:
        frequency[ch] = frequency.get(ch, value) + 1    # Incremented by 1 if the character is seen before


# The Output
for key, value in frequency.items():
    print(key, value)
