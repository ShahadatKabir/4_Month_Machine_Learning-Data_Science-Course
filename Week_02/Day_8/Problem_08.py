# The Sorting Cost (O(N log N))

# Type -1: Using Timesort, we get the values in-place 
print("Type 1:")
list_of_nums = [12,65,78,23,8]
print(f"The unsorted List: {list_of_nums}")

list_of_nums.sort()
print(f"The Sorted List: {list_of_nums}")

# Type -2 : Uisng Timesort, we get the values in new list
print("\nType 2:")
num_list = [11,44,83,2,7,56,89]
print(f"The unsorted List: {num_list}")
sorted_list = sorted(num_list)
print(f"The Sorted List: {sorted_list}")


# Output 
#Type 1:
#The unsorted List: [12, 65, 78, 23, 8]
#The Sorted List: [8, 12, 23, 65, 78]

#Type 2:
#The unsorted List: [11, 44, 83, 2, 7, 56, 89]
#The Sorted List: [2, 7, 11, 44, 56, 83, 89]
