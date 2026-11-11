print("Hello Ankit")
age = 23
name = "Ankit"
print('name is:', name)

name = "Ankesh"
print('name is:', name)

print(type(name))
print(type(age))

isStudent = True
print(type(isStudent))


age = input("Enter Your Age: ")

# type casting
age = bool(age)
print(age, type(age))

# type conversion
print(9+2.5) # implicit
print(1+int(5.5)) # explicit