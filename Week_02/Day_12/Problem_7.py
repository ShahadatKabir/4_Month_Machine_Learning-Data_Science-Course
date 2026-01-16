
# Inheritance 

class User:
    def __init__(self, username):
        self.username = username

    def info(self):
        return f"{self.username} is Added in user information."
        

class Admin(User):
    def __init__(self, username):
        super().__init__(username)

    def delete_db(self):
        return f"Admin {self.username} deleted the database!"


user = User("Anika")

print(user.info())                      # Output: Anika is Added in user information.


admin = Admin("Alice")
print(admin.delete_db())                # Output: Admin Alice deleted the database!
