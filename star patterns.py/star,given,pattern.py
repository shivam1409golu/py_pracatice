# ⭐ 1) Simple Increasing Star Pattern
# Input: n = 5

n = int(input("Enter n: "))
for i in range(1, n+1):
    print('*' * i)


#⭐ 2) Number-Based Star Pattern
# Input: n = 5

n = int(input("Enter n: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

#⭐ 3) Star Pyramid (Centered)
Input: n = 5

n = int(input("Enter n: "))
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

#⭐ 4) Number Pattern Right Triangle
Input: n = 5

n = int(input("Enter n: "))
for i in range(1, n+1):
    print((str(i) + " ") * i)

# ⭐ 5) Combined (Numbers with Stars)
Input: n = 5

n = int(input("Enter n: "))
for i in range(1, n+1):
    print(''.join(str(j) for j in range(1, i+1)) + '*' * i)





