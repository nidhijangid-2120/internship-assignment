# Practice dictionary, tuples, set
# Dictionary
dict1 = {"name": "Alice", "age": 30, "city": "New York"}
print(dict1["name"])  # Output: Alice

# dictionary functions
print(dict1.keys())  # Output: dict_keys(['name', 'age', 'city'])
print(dict1.values())  # Output: dict_values(['Alice', 30, 'New York'])
print(dict1.items())  # Output: dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
print(len(dict1))  # Output: 3
print("name" in dict1)  # Output: True
print()

# accessing elements of a dictionary
print(dict1.get("age"))  # Output: 30
print(dict1.get("country"))  # Output: None
print(dict1["age"])  # Output: 30
# adding a new key-value pair to the dictionary
dict1["country"] = "USA"
print(dict1)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# updating the value of an existing key
dict1["age"] = 31
print(dict1)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}

# removing a key-value pair from the dictionary
del dict1["city"]
print(dict1)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}

# Nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 30},
    "person2": {"name": "Bob", "age": 25},
}
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}}

# accessing elements of a nested dictionary
print(nested_dict["person1"]["name"])  # Output: Alice
print(nested_dict["person2"]["age"])  # Output: 25

# dictionary methods
print(nested_dict.keys())  # Output: dict_keys(['person1', 'person2'])
print(nested_dict.values())  # Output: dict_values([{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}])
print(nested_dict.items())  # Output: dict_items([('person1', {'name': 'Alice', 'age': 30}), ('person2', {'name': 'Bob', 'age': 25})])
print(len(nested_dict))  # Output: 2

# dictionary methods for modifying the dictionary
nested_dict["person3"] = {"name": "Charlie", "age": 35}
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 30}, 'person2': {'name': 'Bob', 'age': 25}, 'person3': {'name': 'Charlie', 'age': 35}}
