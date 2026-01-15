# The Return Value Thief

def wrapper(func):
    def func_A():
        func()
    return func_A

@wrapper
def information():
    return "Information is printed!"

print(information())
