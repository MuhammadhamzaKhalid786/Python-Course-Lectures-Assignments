# 1. Join Words Together (Concatenation)
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)

first_name = "John"
last_name = "Doe"
full_name = first_name + last_name
print(full_name)

city = "Lahore"
country = "Pakistan"
location = city + ", " + country
print(location)

lang = "Py" + "thon"
print(lang)


# 2. Repeat Something Many Times
laugh = "ha"
print(laugh * 3)

star = "*"
print(star * 5)

word = "Hi "
print(word * 4)

dash = "-"
print(dash * 10)


# 3. How Long is The String? (Length)
word = "python"
print(len(word))

text = "I ❤ python!"
print(len(text))

word = "pakistan! "
print(len(word))

sentence = "Learning Python"
print(len(sentence))


# 4. Picking a Letter by Its Spot (Indexing)
greeting = "Hello"
print(greeting[0])
print(greeting[-1])

# Positive indexing
print(greeting[0])
print(greeting[1])
print(greeting[2])
print(greeting[3])
print(greeting[4])

# Negative indexing
print(greeting[-1])
print(greeting[-2])
print(greeting[-3])
print(greeting[-4])
print(greeting[-5])

country = "Pakistan"
print(country[2])
print(country[-3])


# 5. Cut Out a Piece (Slicing)
text = "Hello"
print(text[0:2])
print(text[2:])

name = "Python"
print(name[0:4])
print(name[:3])
print(name[1:5])
print(name[-3:])
print(name[::-1])

word = "Programming"
print(word[0:6])
print(word[3:8])
print(word[:])


# 6. Change Letter Case
name = "python"
print(name.upper())
print(name.capitalize())
print("HELLO".lower())

sentence = "pYtHon is CoOl"
print(sentence.title())
print(sentence.swapcase())


# 7. Check If Something Is Inside (Membership)
fruit = "apple"
print("a" in fruit)
print("Z" in fruit)

fruit = "Mango"
print("M" in fruit)

word = "Python"
print("th" in word)
print("z" in word)


# 8. Change a Word or Letter (Replace)
sentence = "I love java"
new_sentence = sentence.replace("java", "python")
print(new_sentence)

text = "banana"
new_text = text.replace("a", "o")
print(new_text)

msg = "Hello World"
print(msg.replace("World", "Python"))


# 9. Break a Sentence into Words (Split)
txt = "apple,banana,orange"
print(txt.split(","))

sentence = "python is fun"
words = sentence.split()
print(words)

line = "one-two-three"
print(line.split("-"))


# 10. Glue Words Together (Join)
words = ["python", "is", "awesome"]
result = " ".join(words)
print(result)

letters = ["A", "B", "C"]
joined = "-".join(letters)
print(joined)
