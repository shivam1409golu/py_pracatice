# Program 1: Local Variable
def local_example():
    a = 10   # local variable
    b = 20   # local variable
    print("Inside function:")
    print("a =", a)
    print("b =", b)

local_example()

# Neeche wali line error degi agar uncomment karo
# print(a)



# Program 2: Global Variable
x = 50   # global variable

def global_example():
    print("Inside function x =", x)

global_example()
print("Outside function x =", x)

# Program 3: Local aur Global (Same Name)
num = 100   # global variable

def test():
    num = 25   # local variable
    print("Inside function num =", num)

test()
print("Outside function num =", num)


# Program 4: global keyword ka use
value = 10   # global variable

def change_value():
    global value
    value = 99
    print("Inside function value =", value)

change_value()
print("Outside function value =", value)

#  Program 5: Real Life Example (Student Marks)
total_marks = 500   # global variable

def marks():
    obtained = 420   # local variable
    print("Obtained Marks =", obtained)
    print("Total Marks =", total_marks)

marks()
