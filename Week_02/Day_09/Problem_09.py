# The Send Method

# Sub generator - 1
def child_gen(numbers):
    for i in numbers:
        result = i*i
        print(f"The squarer of {i} is:")
        yield result

def parent_gen():
    child = yield from child_gen(numbers)
    return child


numbers = [4,44,12,65,23,12,6,90]
generator =  parent_gen()

print(next(generator)) 

print(next(generator)) 



print(generator.send(55))         # added the value to the child and yields the child_gen's result
print(generator.send(45))

"""
#Output:

The squarer of 4 is:
16
The squarer of 44 is:
1936
The squarer of 12 is:
144
The squarer of 65 is:
4225
"""
