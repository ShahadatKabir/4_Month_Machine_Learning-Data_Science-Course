# The Memory Profile 
import sys

# List Comprehension 
list_comprehension = [x for x in range(1000000)]

print(sys.getsizeof(list_comprehension))               # Output: 8448728

# Generator Expression 
generator_expression = (x for x in range(1000000))     # Output:  192

print(sys.getsizeof(generator_expression))
