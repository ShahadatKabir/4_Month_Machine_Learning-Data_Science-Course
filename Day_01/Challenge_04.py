seconds = int(input("Enter the time in seconds: "))
hours = seconds // 3600
minutes = seconds % 3600  // 60
remaining_seconds = seconds % 60
print(f"{hours} hours and {minutes} minutes and {remaining_seconds} seconds ")
