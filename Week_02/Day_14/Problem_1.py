list_A = [3,6,2,9,2,40,1,34,26,74,6,7]
list_B = [56,3,12,7,4,88,26,24,7,22,12]

target = 50
# Brute Force Approach
for i in list_A:
    for j in list_B:
        if i+j == target:
            print(f"{i} + {j} = {target}")


# Updated and Efficient approach 
def add_sum(list_A, list_B):
    needed=0
    for i in range(list_A):
        needed = target - i
    for j in range(list_B):
        if needed in range(list_B):
            return {needed, i}
        else:
            return 0


result = map(add_sum, list_A, list_B)
print(list(result))
