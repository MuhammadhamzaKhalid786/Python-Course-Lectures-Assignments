
# FILE INPUT AND OUTPUT PRACTICE




# Writing to a file
with open("example_output.txt", "w") as file:
    file.write("Hello! this is a test write.")

# Reading from a file
with open("example_output.txt", "r") as file:
    content = file.read()
    print("Reading Example Output File:")
    print(content)
    print("-" * 40)

# Appending to a file
with open("example_output.txt", "a") as file:
    file.write("\nThis line is appended.")



# Example 1: Write new content
with open("example1.txt", "w") as file:
    file.write("This is Example 1.\nPython file handling is easy!")

# Example 2: Read the file
with open("example1.txt", "r") as file:
    content = file.read()
    print("Example 2 - Reading example1.txt:")
    print(content)
    print("-" * 40)

# Example 3: Append more text
with open("example1.txt", "a") as file:
    file.write("\nI just appended this line!")

# Example 4: Read line by line
with open("example1.txt", "r") as file:
    print("Example 4 - Reading line by line:")
    for line in file:
        print(line.strip())
    print("-" * 40)

# Example 5: Write multiple lines
lines = ["Python is fun!\n", "File handling is important.\n", "Assignments make practice better.\n"]
with open("example2.txt", "w") as file:
    file.writelines(lines)

# Example 6: Read multiple lines as list
with open("example2.txt", "r") as file:
    lines = file.readlines()
    print("Example 6 - Reading multiple lines as list:")
    print(lines)
    print("-" * 40)

# Example 7: Error handling (File not found)
try:
    with open("not_exist.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops! The file does not exist (Example 7).")
    print("-" * 40)

# Example 8: Writing diary note
user_note = "Today I learned File Handling in Python!"
with open("my_diary.txt", "w") as file:
    file.write(user_note)
print("Example 8 - User note written to my_diary.txt")
print("-" * 40)

# Example 9: Append diary note
with open("my_diary.txt", "a") as file:
    file.write("\nTomorrow I will practice Pandas too!")

print("Example 9 - Appended new diary entry.")
print("-" * 40)

# Example 10: Read diary again
with open("my_diary.txt", "r") as file:
    print("Example 10 - Reading diary again after append:")
    print(file.read())
    print("-" * 40)
