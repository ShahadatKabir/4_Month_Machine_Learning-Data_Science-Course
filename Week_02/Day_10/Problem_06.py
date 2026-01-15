# The Authenticator(Guard)

global_user = "admin"

def admin_required(func):
    def inner():
        if global_user != "admin":
            raise PermissionError
        return func()
    return inner

@admin_required
def access():
    print("Admin access sucessful!")

access()
