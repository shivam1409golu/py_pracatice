# pre define function 

## 1. print()

# Display/output karne ke liye

print("Hello Python")

## 2. len()

# Length nikalti hai (characters, items count).

name = "Shivam"
print(len(name))

## 3. type()

# Variable ka data type batata hai.

x = 10
print(type(x))

## 4. max()

# Maximum (sabse bada number).

print(max(10, 25, 7))

## 5. min()

# Minimum (sabse chhota number).

print(min(10, 25, 7))

## 6. input()

# User se value lene ke liye.

name = input("Enter name: ")
print(name)

## 7. range()

# Numbers ki series banata hai (loops me use hota hai).

for i in range(1, 5):
    print(i)

## 8. sum()

# List ke numbers ka sum.

marks = [50, 40, 30]
print(sum(marks))

## 9. abs() 
 
#  absolute value (negative ko positive banata hai)
x = -25
print(abs(x))

## 10. round() 

#  number ko round off karta hai

x = 4.67
print(round(x))
print(round(x, 1))

## 11. sorted() 

# list ko sort (ascending/descending) karta hai
nums = [5, 2, 9, 1]
print(sorted(nums))          # ascending
print(sorted(nums, reverse=True))  # descending


## 12. pow()  

# power calculate karta hai (x^y)

print(pow(2, 3))   # 2^3
print(pow(5, 2))   # 5^2


## 13. divmod() 

#  quotient + remainder dono deta hai

print(divmod(10, 3))

## 14. str() 

#  number ko string me convert karta hai

x = 100
print(str(x))
print(type(str(x)))

## 15. int() 

# string/float ko integer me convert karta hai

x = "25"
y = 3.99

print(int(x))
print(int(y))

## 16. float() 

#  integer/string ko float me convert

x = "40"
print(float(x))

## 17. list() 

#  string ko list me convert karta hai

text = "abc"
print(list(text))

## 18. type()  

# datatype batata hai

x = 10
print(type(x))

## 19. tuple() 

#  list ko tuple me convert karta hai

nums = [1, 2, 3]
print(tuple(nums))

## 20. id() 

#  variable ka memory address deta hai

a = 50
print(id(a))
