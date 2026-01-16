# The String Representation

# __str__ vs __repr__

class User:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"ID- 1AD, Dept - CSE"


info = User("Anika")
print(str(info))

print(repr(info))
