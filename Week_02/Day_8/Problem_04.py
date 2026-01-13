# The Queue Bottleneck(pop)
import time
from collections import deque

queue_list = [11, 52, 30, 41, 15]

print("Original list:", queue_list)

# Remove from end (right side) 
item = queue_list.pop()          # Removes 5
print("After list.pop():", queue_list, " removed", item)

# Add back to the full cycle
queue_list.append(6)
print("After append(6):", queue_list)

# Remove from beginning (left side) 
item = queue_list.pop(0)         # Removes 1, shifts everything left
print("After list.pop(0):", queue_list, " removed", item)


# Using deque - the correct tool for FIFO queues
print("\n=== Using collections.deque (correct way) ===")
queue_deque = deque([1, 2, 3, 4, 5])

print("Original deque:", queue_deque)

# Remove from left (front) 
item = queue_deque.popleft()     # Removes 1
print("After popleft():", queue_deque, " removed", item)

# Add to right (back)
queue_deque.append(6)
print("After append(6):", queue_deque)

# Remove from right - also fast
item = queue_deque.pop()         # Removes 6
print("After pop():", queue_deque, " removed", item)
