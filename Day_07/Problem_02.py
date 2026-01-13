
# The Math Safety Net 
x = 0

try:
    result = 100 / x
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Any real number cannot divided by zero")

else:
    print("Result printed successfully.")
