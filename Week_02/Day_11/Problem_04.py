# The Reducer
import functools

numbers = [1,2,3,4,5,6]

reducer = functools.reduce(lambda x, y: x*y, numbers) # This part reduces the list into a single value

print(reducer)                # Output: 720
