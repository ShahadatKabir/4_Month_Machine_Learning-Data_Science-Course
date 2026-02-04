# Append vs Write

# Writing operation
with open("shihab.txt", "w") as file:
    file.write("Hello World!\n")
    

# appending operation
with open("shihab.txt", "a") as appending_file:
    appending_file.write("\nHello World to shihab!\n")                                  # Output:  Hello World!


# Safety operation
try:
    with open("shihab.txt", "x") as safety_file:
        safety_file.write("\good, shihab!\n")                                  # Output:  Hello World!
except FileExistsError:
    print("The file is existed")
except Exception as e:
    print(f"The error{e}")
