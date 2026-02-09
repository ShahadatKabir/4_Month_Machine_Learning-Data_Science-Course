import json

data = {
    "Name": "Kabir",
    "ID": "1234",
    "Age": 27
}

file_path = r"D:\LPL\Project\Python\week 2\data.json"

try:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    print("✅ File created at:", file_path)
except Exception as e:
    print("❌ Error:", e)
print("SCRIPT IS RUNNING")






# Output:
"""
{"Name": "Kabir", "ID": "1234", "Age": 27}
"""
