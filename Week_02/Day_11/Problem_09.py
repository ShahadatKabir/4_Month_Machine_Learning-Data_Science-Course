# Partial Function

import functools


squared = functools.partial(lambda x, b: x**b, b = 2)

result = squared(3)

print(result)                      # Output: 9
