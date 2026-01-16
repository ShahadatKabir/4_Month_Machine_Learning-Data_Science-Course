# Any All

numbers = [12,-2, 45, -56, 67, -300]

# Any Number is negative

result_negative = any(x<0 for x in numbers)
print(result_negative)                             # Output: True

# Checking All numbers are Non-negative
result_positive = all(x>0 for x in numbers)
print(result_positive)                             # Output: True
