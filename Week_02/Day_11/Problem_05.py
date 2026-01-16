# The Custom Sort key

keys = ["100px", "20px", "3px"]

sorted_keys = sorted(keys, key = lambda x: int(x[:-2]))

print(sorted_keys)        # Output: ['3px', '20px', '100px']
