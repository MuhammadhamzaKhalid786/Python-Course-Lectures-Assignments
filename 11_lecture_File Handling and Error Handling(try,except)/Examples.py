
# Python File Handling & Error Handling
# Assignment with Solutions


# Q1: Write a program to create a file named "diary.txt"
# and write "Today I went to the park and saw a dog!" into it.
file = open("diary.txt", "w")
file.write("Today I went to the park and saw a dog!")
file.close()
print("Q1 Done File diary.txt created.\n")

# Q2: Write to a new file "notes.txt" and save your favorite food sentence in it.
file = open("notes.txt", "w")
file.write("I love Pizza and Today I ordered a large pizza.")
file.close()
print("Q2 Done notes.txt created with favorite food.\n")

# Q3: Read from "notes.txt" and print its content.
file = open("notes.txt", "r")
content = file.read()
print("Q3 Output:\n", content, "\n")
file.close()

# Q4: Use 'with open()' to write "Give me a large Pizza." into "notes.txt".
with open("notes.txt", "w") as file:
    file.write("Give me a large Pizza.")
print("Q4 Done notes.txt overwritten with new text.\n")


# Q5: Try to read "unknown.txt". If file does not exist, show error message.
try:
    file = open("unknown.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("Q5 Output: Oops! File not found. Maybe you forgot to create it?\n")
    
    
# Q6: Write and Read Together
# Step 1: Write "I went to school and played football" into "my_day.txt"
# Step 2: Read the content and print it.
file = open("my_day.txt", "w")
file.write("I went to school and played football")
file.close()

file = open("my_day.txt", "r")
print("Q6 Output:\n", file.read(), "\n")
file.close()

# Q7: Error handling while reading "abc.txt".
try:
    with open("abc.txt", "r") as file:
        print("Q7 Output:\n", file.read(), "\n")
except FileNotFoundError:
    print("Q7 Output: Oh no! The file does not exist.\n")
    
    
 # Q8: Append mode practice
with open("notes.txt", "a") as file:
    file.write("\nTomorrow I will go shopping.")

with open("notes.txt", "r") as file:
    print("Q8 Output:\n", file.read(), "\n")
    

# Q9: File overwrite practice
with open("notes.txt", "w") as file:
    file.write("My notes are now replaced.")

with open("notes.txt", "r") as file:
    print("Q9 Output:\n", file.read(), "\n")

# Q10: Real-life Mini Project – Personal Diary
try:
    user_input = input("Q10: Write something in your diary: ")
    with open("my_diary.txt", "a") as file:   # append mode so every entry saves
        file.write(user_input + "\n")

    with open("my_diary.txt", "r") as file:
        print("\nQ10 Output: Here is your diary content so far:\n")
        print(file.read())
except Exception as e:
    print("An error occurred:", e)    
    
    