# 1 printing output
print("Hello, World!")  # Prints a string literal
name = "shivam kumar"
print(f"Hello, {name}!")  # Uses an f-string to embed a variable

# 02 varibale data type program

# Integers
age = 30

# Floats
price = 19.99

# Strings
city = "New York"

# Booleans
is_active = True

print(f"Age: {age}, Price: {price}, City: {city}, Active: {is_active}")

# 3 basic arithmetic opration
num1 = 10
num2 = 5

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2
modulus = num1 % num2  # Remainder of division

print(f"Sum: {addition}, Difference: {subtraction}, Product: {multiplication}, Quotient: {division}, Remainder: {modulus}")

# 4  Conditional Statements (if-elif-else):
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"

print(f"Your grade is: {grade}")

 #5. Loops (for and while):
 # For loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While loop
count = 0
while count < 3:
    print(f"Count: {count}")
    count += 1

#6. Functions:
    def greet(name):
         """This function prints a greeting message"""
    print(f"Greetings, {name}!")

greet("Bob")

# 7 list function

my_list = [1, 2, 3, "hello", True]
print(my_list[0])  # Accessing an element by index
my_list.append(4)  # Adding an element
print(my_list)