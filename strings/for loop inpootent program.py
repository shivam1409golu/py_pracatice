# 1.  string characters chack

text = input("Enter string: ")

for i in text:
    print(i)

# 2. String me vowels count

text = input("Enter string: ")

vowels = "mhoverAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel Count:", count)

# 3. String ko  reverse (for loop)

text = input("Enter string: ")

rev = ""
for ch in text:
    rev = ch + rev

print("Reversed:", rev)

# 4. uppercase and lowercase letters chack

text = input("Enter string: ")

u = 0
l = 0

for ch in text:
    if ch.isupper():
        u += 1
    elif ch.islower():
        l += 1

print("Uppercase:", u)
print("Lowercase:", l)

# 5. String me  digits condision chack

text = input("Enter string: ")

count = 0

for ch in text:
    if ch.isdigit():
        count += 1

print("Digits:", count)

# 6. character ke frequency kitne bar aaya

text = input("Enter string: ")
ch = input("Enter character: ")

count = 0

for i in text:
    if i == ch:
        count += 1

print("Frequency:", count)

# 7. String ko bina spaces ke print karna 

text = input("Enter string: ")

for ch in text:
    if ch != " ":
        print(ch, end="")

# text = input("Enter string: ")

for ch in text:
    if ch != " ":
        print(ch, end="")

# Check string palindrome me hyy na nahi (yes/no)

text = input("Enter string: ")

rev = ""
for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
