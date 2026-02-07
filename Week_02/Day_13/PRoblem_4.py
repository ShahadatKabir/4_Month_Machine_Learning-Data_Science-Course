# Encoding Hell

try:
    with open("Emoji.txt", "r", encoding = "UTF-8") as file:
        print(file.read())
except UnicodeDecodeError as error:
    print(f"We cannot read unicode, here is the error: {error}")
except Exception as e:
    print(f"The Error: {e}")


# Output:


"""
Here is the Emoji


"""
