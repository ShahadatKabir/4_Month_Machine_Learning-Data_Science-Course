# The Manual Wrapper

def wrapper(func):
    def func_A():
        print("Before Call")
        func()
        print("After Call")
    return func_A


def information():
    print("Information is printed!")

function = wrapper(information)
function()
