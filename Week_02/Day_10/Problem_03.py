# The Args Problem

def wrapper(func):
    def func_A(*args, **kwargs):
        print("Before Call")
        func(*args, **kwargs)
        print("After Call")
    return func_A

@wrapper
def add(a,b):
    print(f"The sum of {a} + {b} = {a+b}")

add(5,7)


# Output:
"""
Before Call
The sum of 5 + 7 = 12
After Call
"""
