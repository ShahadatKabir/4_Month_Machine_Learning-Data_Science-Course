import pickle

# Data to save
info = "this is python 10 pkl"

# Save the data to a .pkl file (binary write mode)
with open("Problem_10.pkl", mode="wb") as file:
    pickle.dump(info, file)

# Load the data from the .pkl file (binary read mode)
with open("Problem_10.pkl", mode="rb") as file:
    data = pickle.load(file)

# Print the loaded data
print(data)
