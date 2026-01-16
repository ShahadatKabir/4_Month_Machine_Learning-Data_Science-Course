# Equality

class User:
    def __init__(self,number):
        self.number = number

    def __eq__(self, other):
        if isinstance(other, User):
            return self.number == other.number
        return False


user1 = User(1)
user2 = User(1)

print(user1.__eq__(user2))           # Output: True
