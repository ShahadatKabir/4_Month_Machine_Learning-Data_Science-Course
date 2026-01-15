# The Syntax Sugar


def wrapper(func):
    def func_A():
        print("Before Call")
        func()
        print("After Call")
    return func_A

@wrapper
def information():
    print("Information is printed!")

information()
