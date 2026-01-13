# The Basic Yield

def gen():
    n = 1
    yield n
    n += 1
    yield n
    n += 1
    yield n

result = gen()

print("Output:")
for item in gen():
    print(item)                  
    
# Output: 
# 1
# 2
# 3
