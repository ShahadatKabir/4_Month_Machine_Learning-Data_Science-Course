# The Property Decorator 
import datetime

class User:
    def __init__(self, username, birth_year):
        self.username = username
        self.birth_year = birth_year 

    @property
    def age(self):
        current_time = datetime.datetime.now().year
        calculated_age = current_time - self.birth_year
        return calculated_age

user = User("Anna",1997)
print(user.age)
