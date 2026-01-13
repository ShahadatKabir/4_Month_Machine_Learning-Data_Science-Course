
# The Input Guard

try:
    age = int(input("Enter your age: "))
    if age > 0 and age <150: 
        print(f"Your age is {age}")       # If the logic is True; Output: Your age is [entered age] 
    
except ValueError:
    print("Numbers Only")                 # If the Input is string or special character this part will execute
else:
    print("Please correctly enter your age.") 
