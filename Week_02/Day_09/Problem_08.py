# Yield From 

# Yield From

# Sub generator - 1
def sub_gen1(numbers):
    for i in numbers:
        result = i*i
        print(f"The squarer of {i} is:")
        yield result


# Sub generator - 2

def sub_gen2(data):
   
    for i in data:
        if i % 2 == 0:
            print(f"{i} -> even")
            yield i
            
        else:
            print(f"The number {i} is: odd")

# Parent Generator

def parent_gen(numbers):
    yield from sub_gen1(numbers)
    yield from sub_gen2(numbers)

numbers = [4,5,6,77,23,15,90]

gen = parent_gen(numbers)
print(next(gen))           


# Output: 
# The squarer of 4 is:
# 16
