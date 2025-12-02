# Basic range examples
for i in range(5):
    print(i)

for i in range(0, 5):
    print(i)  # 0, 1, 2, 3, 4

# starting point => 0
# ending point => 5 , EXCLUDED

my_listt = ["shivam", "golu", 44, 55, 88]
print(my_listt)

for i in my_listt:
    print(i)

# Note:
# If we apply for-loop on any sequence (string, list, tuple),
# Python uses indexing internally to access elements.

for i in range(0, 12):
    print(i)

# Jump statement 
# 1. break 
# 2. continue

# break statement => exits the loop instantly when condition is true
for i in range(0, 12):
    if i == 7:
        break
    print(i)

# continue => skips current iteration
for i in range(0, 12):
    if i == 7:
        continue
    print(i)

# break example with list
my_listt = ["Golu", "shivam", 44, 55, 88]
for i in my_listt:
    if i == 44:
        break
    print(i)

# break on 101
my_listt = ["Golu", "shivam", 101, 44, 55, 88]
for i in my_listt:
    if i == 101:
        break
    print(i)

# continue example
my_listt = ["shivam", "golu", 101, 44, 55, 88]
for i in my_listt:
    if i == 101:
        continue
    print(i)
