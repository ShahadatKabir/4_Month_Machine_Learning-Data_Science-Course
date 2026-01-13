# The Cleanup Crew

try:
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    print(f"Result after division: {number1/number2}")
except ZeroDivisionError:
    print("Any number cannot divided by zero.")
except ValueError:
    print("Enter the numbers.")
finally:
    print("Execution Completed")
