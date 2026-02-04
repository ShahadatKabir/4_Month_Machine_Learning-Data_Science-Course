# Append vs Write

# Writing operation
with open("Anika.txt", "w") as file:
    file.write("Hello World!\n")
    

# appending operation
with open("Anika.txt", "a") as appending_file:
    appending_file.write("\nHello World to Anika!\n")                                  # Output:  Hello World!


# Safety operation
try:
    with open("Anika.txt", "x") as safety_file:
        safety_file.write("\nBravo, Anika!\n")                                  # Output:  Hello World!
except FileExistsError:
    print("The file is existed")
except Exception as e:
    print(f"The error{e}")
