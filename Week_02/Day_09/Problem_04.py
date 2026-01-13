# The One-Time Trap

def g():
    start_point = 0
    end_point = 100

    while True:
        if start_point >= end_point:
            raise StopIteration
        value = start_point % 2    # The calculation is assumed
        yield value
        start_point += 1
        
generator = g()
print(next(generator))             # Output: 0
print(next(generator))             # Output: 1
print(next(generator))             # Output: 0
print(next(generator))             # Output: 1
