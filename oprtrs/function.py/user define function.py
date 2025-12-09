# Basic User-Defined Function 

def greet():
    print("Hello, Welcome to Python!")

greet()   # function call

# 2. Function with Parameters

def welcome(name):
    print("Hello", name)

welcome("Shivam")
welcome("Ravi")

# 3. Function to Add Two Numbers

def add(a, b):
    print("Sum =", a + b)

add(10, 20)

# 4. Function with Return Value
    
def square(n):
    return n * n

result = square(5)
print("Square =", result)


# 5. Function Taking Input From User

def average():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Average =", (a + b) / 4)

average()


# 6. Function to Check Even or Odd

def check(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

check(11)
check(20)

# 7. Function for Student Marks Average (Your Topic)
    
def student_average():
    marks = [80, 75, 90, 85, 70]
    avg = sum(marks) / len(marks)
    print("Student Marks:", marks)
    print("Average Marks =", avg)

student_average()


