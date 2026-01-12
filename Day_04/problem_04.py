numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Before Squaring the even numbers: {numbers}")

numbers = [x**2 for x in numbers if x % 2 == 0]

print(f"After Squaring the even numbers:{numbers}")   
