# The Self Reference

"""
self method is required to connect the objects data uniquely,
for instance, while user.login() will execute, it has no reference and doesn't know where to relate.
In contrast, self method acts like a prototype, allowing the method to access the instance's attributes and methods.
"""


"""
Without Self:
class User:
    def login():
        print("Logged in")

user = User()
user.login()

it will throw an error

"""


class User:
    def login(self, user):
        self.user = user
        print(f"{self.user} logged in successfully!")


user = User()
user.login("Kabir")
