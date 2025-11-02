#nested if example program

num = int (input("enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("positive even number")
    else:
        print("positive odd number")
else:
        print("number is zero or negative")

# nested for loop (star pattern)
for i in range(1,6):
     for j in range(1,i + 1):
          print("*",end="")
print() 

#nested while loop

i = 1
while i <= 5:
     j = 1
     while j <= i:
          print(j,end=" ")
          j += 1
     print()
     i += 1

# nested function

def outer():
     print("this is outer function")

     def inner():
          print("this is inner function")
          inner()
outer()              