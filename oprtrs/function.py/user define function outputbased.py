# 1.
def show():
    print("Python")

show()
show()

# 2.
def add(a, b):
    print(a + b)

add(5, 10)
add(2, 3)

# 3.
def check(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

check(7)

# 4.
def calc(x):
    return x * 2

print(calc(5))
print(calc(10))

# 5.
def fun(a, b):
    c = a + b
    return c

x = fun(3, 4)
print(x)

# 6.
def message():
    print("Hello")
    return
    print("Bye")

message()

#(Because return ke baad wala code run nahi hota)

# 7.
def show():
    print("A")
    print("B")

print("Start")
show()
print("End")

# 8.
def test(a):
    print(a * a)

test(6)
