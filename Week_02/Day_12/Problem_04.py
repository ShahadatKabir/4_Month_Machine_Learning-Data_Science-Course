# Private Variables

class User:
    def __init__(self):
        self.__password = "Abdh%1920"


user = User()
user._User__password = "NewPassword123"  
user.password = "AnotherPassword456"

print(user._User__password)
