# List Comprehension Speed 

import time

# Measuring the time taken in list

start = time.time()
result_1 = [x*2 for x in range(10000)]
end = time.time()

print(f"List comprehension took {end - start} seconds.")     # List comprehension took 0.002976655960083008 seconds.

# Measuring the time taken in map

start = time.time()
result_2 = list(map(lambda x: x*2, range(10000)))
end = time.time()

print(f"Map function took {end - start} seconds.")           # Map function took 0.0022172927856445312 seconds.
