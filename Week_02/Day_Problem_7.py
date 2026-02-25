
import os

data = "miles to go before i sleep"
path = "Problem_7.txt"

if os.path.exists(path):
    with open(path, "w") as file:
        file.write(data)
        file.flush()
else:
    print("The file doesn't exists.")
