is_student = True
has_passed = False

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if has_passed:
    print("Congratulations")
else:
    print("Try again,Next Time")


is_student = True
has_passed = True

if is_student:
    print("You are a student")
else:
    print("You are not a student")

if has_passed:
    print("Congratulations,You passed")
else:
    print("Try again,Next Time")


#LIST IN PYTHON
fruits = ["apple", "banana", "mango"]  
#display all item in a list
print("Fruit list:", fruits) 


fruits = ["apple", "banana", "mango"]  
print("Fruit list:", fruits)

fruits = ["apple", "banana", "mango"]  
print("Fruit list:", "fruits") 


fruits = ["apple", "banana", "mango"]  
print("Fruit list:", fruits)

#Acess a specific item in the list 
print("first fruit:", fruits[0])

fruits = ["apple", "banana", "mango"]  
print("Fruit list:", fruits)

#Acess a specific item in the list 
print("first fruit:", fruits[1])

fruits = ["apple", "banana", "mango"]  
print("Fruit list:", fruits)

#Acess a specific item in the list 
print("first fruit:", fruits[2])

fruits = ["apple", "banana", "mango"]  
print("Fruit list:", fruits)

#Acess a specific item in the list 
print("first fruit:", fruits[2])



print("Fruit name:", fruits)  

#Add a new item to the list
fruits.append("orange") 

print("Updated fruit list:", fruits)  


#Dictionary
person = {"name": "hamza", "age": 25, "city": "lahore"}

#Display the entire dictionary
print("Person info:", person)

#Acess a specific value by key
print("city:",person["city"])

#Add a new key_value pair
person["interest"] ="programming"

#dispaly the updated dictionary
print("updated list:",person)



#  Create a dictionary
student = {
    "name": "Hamza",
    "age": 20,
    "grade": "A",
    "city": "Haripur"
}
print("Student Info:", student)

# Access values using keys
print("Name:", student["name"])
print("Grade:", student["grade"])

# Add new key-value pair
student["subject"] = "Computer Science"
print("After Adding Subject:", student)

# Update existing value
student["grade"] = "A+"
print("After Updating Grade:", student)

# Delete a key-value pair
del student["city"]
print("After Removing City:", student)


# Length of dictionary
print("Total items in dictionary:", len(student))

# Clear all items from dictionary
student.clear()
print("After Clearing:", student)
