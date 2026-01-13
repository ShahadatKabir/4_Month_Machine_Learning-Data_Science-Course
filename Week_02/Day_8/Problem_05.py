# The String Builder(O(N^2))
import time

s = ""
start = time.time()
for i in range(0, 10001):
    s += "a"
end = time.time()

print(f"Time taken before fixation: {(end - start):.6f} seconds")



# Fixed Parts
list_of_chars = []
start = time.time()

for i in range(10001):
    list_of_chars.append("a")

result = "".join(list_of_chars)

end = time.time()

print(f"Time taken after fixation: {(end - start):.6f} seconds")
