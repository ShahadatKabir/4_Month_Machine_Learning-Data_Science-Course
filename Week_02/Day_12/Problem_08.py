
# The Super Proxy

class User:
    def __init__(self, username):
        self.username = username

    def info(self):
        return f"{self.username} is Added in user information."
        

class Admin(User):
    def __init__(self, username, Access):
        super().__init__(username)
        self.access = Access
        
        
    def delete_db(self):
        return f"Admin {self.username} deleted the database and has access {self.access}!"


user = User("Anika")
print(user.info())                      # Output: Anika is Added in user information.


admin = Admin("Alice", True)
print(admin.delete_db())                # Output: Admin Alice deleted the database!
print(admin.username)                   # Output: Alice     
print(admin.access)                     # Output: True
