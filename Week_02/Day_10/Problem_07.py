# The Memoizer (cache)

def memo(func):
    cache = {}
    def wrapper(num):
        if num in cache:
            return cache[num]
        cache[num] = func(num)
        return cache[num]
    return wrapper


@memo
def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num-1) + fibonacci(num-2)


num = int(input("Enter a number:"))
print(fibonacci(num))
