# Class Variable vs Instance Variables

class User:
    species = "Human"

    def __init__(self, name):
        self.name = name

user1 = User("Hellen")
user2 = User("Butterfly")
print(user1.name + " " + user1.species)              # Output: Hellen Human
print(user2.name + " " + user2.species)              # Output: Butterfly Human


user2.species = "Swallowtails (Papilionidae)"

print("\n" + user1.name + " " + user1.species)              # Output: Hellen Human
print(user2.name + " " + user2.species)                     # Output: Butterfly Swallowtails (Papilionidae)
