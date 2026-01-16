# The Constructor

class User:
    def __init__(self, username):
        self.name = username
        self.active = True

# Usage
user_obj = User("Sadia Afrin Anika")
print(user_obj.name)                       # Output: Sadia Afrin Anika
print(user_obj.active)                     # Output: True
