# The Reference Trap
a = [1,2,3]
b = a       # copying the refereces 
b[0] = 99
print(a)    # The output: [99, 2, 3] 
