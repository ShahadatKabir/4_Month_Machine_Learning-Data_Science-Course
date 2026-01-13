# The Custom Signal 

try:
    number = int(input("Enter a number: "))
    if number <0:
        raise ValueError("No negetive numbers")
    print(f"{number} is positive")
except ValueError as e:
    print(e)
