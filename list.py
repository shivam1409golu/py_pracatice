# List of integers
numbers = [1, 2, 3, 4, 5]

# List of strings
fruits = ['apple', 'banana', 'cherry']

# List with mixed data types
mixed_list = [10, "hello", 3.14, True]

# Accessing elements by index
first_number = numbers[0]
second_fruit = fruits[1]
last_item = mixed_list[-1] # Negative index accesses from the end

print(f"Numbers list: {numbers}")
print(f"First number: {first_number}")
print(f"Second fruit: {second_fruit}")
print(f"Last item in mixed list: {last_item}")

# Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(f"Squares of numbers 0-9: {squares}")

# Create a list of even numbers from 0 to 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers 0-9: {even_numbers}")

# Convert a list of names to uppercase
names = ['Alice', 'Bob', 'Charlie']
uppercase_names = [name.upper() for name in names]
print(f"Uppercase names: {uppercase_names}")

fruits = ["apple", "banana", "cherry"]

print("Iterating through the fruits list:")
for fruit in fruits:
    print(fruit)

# Using a for loop with range() to get both index and value
print("\nIterating using index:")
for index in range(len(fruits)):
    print(f"Index {index}: {fruits[index]}")
