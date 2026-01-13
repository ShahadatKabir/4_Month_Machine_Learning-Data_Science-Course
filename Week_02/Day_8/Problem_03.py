# The Insertion Trap
import time

data = list(range(100000))  # 100,000 data

# Step 1: Using append (O(1))
start = time.time()
for i in range(10000):      
    data.append(i)         

print("Append time:", time.time() - start)  # Fast



data = list(range(100000))

# Step 2: Using insert(0, x) (O(n))
start = time.time()
for i in range(10000):
    data.insert(0, i)       
print("Insert time:", time.time() - start)   # Slower
