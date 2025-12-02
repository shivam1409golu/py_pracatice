my_dict = {
    "name": ["satyam", "shivam", "sundram"],
    "age": 21,
    "city": "Begusarai",
    "roll_no": 101
}

print(my_dict["name"])        # prints list of names
print(my_dict["name"][1])     # prints Ravi

# all key dictionary

my_dict = {
    "name": "shivam",
    "age": 21,
    "city": "Begusarai",
    "roll_no": 50
}

print(my_dict)
print(my_dict.keys())

# value() all dictionary

diwakar_dictionary = {
    "name": "shivam",
    "age": 20,
    "city": "Bangalore",
    "roll_no": 100
}

print(diwakar_dictionary)
print(diwakar_dictionary.values())

# items() dictionary

diwakar_dictionary = {
    "name": "shivam",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

print(diwakar_dictionary)
print(diwakar_dictionary.items())
print(diwakar_dictionary["city"].upper())

# get self value accese dictionary()

diwakar_dictionary = {
    "name": "shivam",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 99
}

print(diwakar_dictionary.get("name"))


# update change value add()

diwakar_dictionary = {
    "name": "shivam",
    "age": 20,
    "city": "Bangalore",
    "roll_no": 200
}

diwakar_dictionary.update({"roll_no": 251})
print(diwakar_dictionary)

# pop remove key pop value pair()

diwakar_dictionary = {
    "name": "shivam",
    "age": 24,
    "city": "Bangalore",
    "roll_no": 101
}

diwakar_dictionary.pop("age")
print(diwakar_dictionary)


