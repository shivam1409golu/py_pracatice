# string methods in Python


# string methods 

# 1. len():-
# => it returns the length of the string.

# my_name = "ROhit"

# print(len(my_name))  # Output: 5

# 2. lower():-
# => it converts all characters in the string to lowercase.

# my_name = "ROhit"
# print(my_name.lower())  # Output: rohit

# 3. upper():-
# => it converts all characters in the string to uppercase.

# my_name = "ROhit"
# print(my_name.upper())  # Output: ROHIT

# 4. strip():-
# => it removes any extra whitespace from the string.

# my_name = "   ROhit   "
# print(my_name)        # Output: "   ROhit   "
# print(my_name.strip())  # Output: "ROhit"

# 5. replace():-
# => it replaces a specified substring with another substring.

# my_sentence = "Python Programming is fun"
# print(my_sentence.replace("Python", "Java"))  # Output: Java Programming is fun

# 6. split():-
# => it splits the string into a list of substrings based on a specified delimiter.

# my_sentence = "Python Java C++ JavaScript"
# print(my_sentence.split(" "))  

# # Output: ['Python', 'Java', 'C++', 'JavaScript']

# # 7. find():-
# => it returns the index of the first occurrence of a specified substring.


# name = "ROHITTTTT"
# print(name.find("T")) # 4

# # # Output: 4

# 8. count():-
# => it returns the number of occurrences of a specified substring.

name = "ROHIrTwwTTT"
print(name.count("w"))

# # Output: 5

# 9. capitalize():-
# => it capitalizes the first character of the string.


# my_sentence = "hello world!"
# print(my_sentence.capitalize())  # Output: Hello world!

# 10. title():-
# => it capitalizes the first character of each word in the string.

my_sentence = "hello world! welcome to python."
print(my_sentence.title())  # Output: Hello World! Welcome To Python.