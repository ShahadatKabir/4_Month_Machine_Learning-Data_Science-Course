# The Infinite Sequence

a = int(input("Enter an interger: "))

def fibonacci():
    a,b = 0,1
    i = 0
    while True:
        yield a
        stored_data = a + b
        a = b
        b = stored_data

result = fibonacci()


print(next(result))                  # Output: 0
print(next(result))                  # Output: 1
print(next(result))                  # Output: 1
print(next(result))                  # Output: 2
print(next(result))                  # Output: 3
print(next(result))                  # Output: 5
