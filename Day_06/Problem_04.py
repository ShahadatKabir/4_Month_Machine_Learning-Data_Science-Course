# The Logic Gate

def is_even(num):
    return num % 2 == 0                # Using Comparison Operator it checks the number whether it is even or odd 

num = 5
result = is_even(num)
print(f"Is {num} even? {result}")      # Output: Is 5 even? False
