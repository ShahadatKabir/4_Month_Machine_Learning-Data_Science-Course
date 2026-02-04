# The Safe Open

with open("Anika.txt", "w") as f:
    f.write("Hello World!\n")
    




with open("Anika.txt", "r") as f:
    file = f.read()
    print(file)                                  # Output:  Hello World!
