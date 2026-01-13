# The Speed Trap(Lookup)
# List of 1M numbers 

numbers = list(range(-500000, 500001))
neg_number = -1
for i in numbers:
    if i == neg_number:
        print(f"{neg_number} is present in the list.")


# Set of 1M numbers 

num = set(range(-500000, 500001))
for i in num:
    if i == neg_number:
        print(f"{neg_number} is present in the set.")
