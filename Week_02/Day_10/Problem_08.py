# The Metadata Fix

from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(func):
        pass
    return wrapper

@decorator
def fibonacci():
    pass

print(fibonacci.__name__)
