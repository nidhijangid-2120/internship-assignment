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
# updating the value of an existing key
nested_dict["person1"]["age"] = 31
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 31}, 'person2': {'name': 'Bob', 'age': 25}, 'person3': {'name': 'Charlie', 'age': 35}}
# removing a key-value pair from the dictionary
del nested_dict["person2"]
print(nested_dict)  # Output: {'person1': {'name': 'Alice', 'age': 31}, 'person3': {'name': 'Charlie', 'age': 35}}



# Tuples
tuple1 = (1, 2, 3, 4, 5)
print(tuple1[0])  # Output: 1
print(tuple1[1:4])  # Output: (2, 3, 4)
print(len(tuple1))  # Output: 5
# Tuples are immutable, so we cannot modify them directly
# However, we can create a new tuple by concatenating existing tuples
tuple2 = tuple1 + (6, 7)
print(tuple2)  # Output: (1, 2, 3, 4, 5, 6, 7)
# We can also convert a list to a tuple
list1 = [8, 9, 10]
tuple3 = tuple(list1)
print(tuple3)  # Output: (8, 9, 10)
# tuple functions
print(tuple1.count(2))  # Output: 1
print(tuple1.index(3))  # Output: 2
# tuples can also be used as keys in a dictionary
dict2 = {(1, 2): "point A", (3, 4): "point B"}
print(dict2)  # Output: {(1, 2): 'point A', (3, 4): 'point B'}
print(dict2[(1, 2)])  # Output: point A



# Set
set1 = {1, 2, 3, 4, 5}
print(set1)  # Output: {1, 2, 3, 4, 5}
print(3 in set1)  # Output: True
print(6 in set1)  # Output: False
set1.add(6)
print(set1)  # Output: {1, 2, 3, 4, 5, 6}
set1.remove(2)
print(set1)  # Output: {1, 3, 4, 5, 6}
set1.discard(7)  # No error if the element is not present
print(set1)  # Output: {1, 3, 4, 5, 6}
set1.discard(3)
print(set1)  # Output: {1, 4, 5, 6}
set1.clear()
print(set1)  # Output: set()
#set operations
set2 = {1, 2, 3}
set3 = {3, 4, 5}
print(set2.union(set3))  # Output: {1, 2, 3, 4, 5}
print(set2.intersection(set3))  # Output: {3}
print(set2.difference(set3))  # Output: {1, 2}
print(set2.symmetric_difference(set3))  # Output: {1, 2, 4, 5}
# sets can also be used to remove duplicates from a list
list2 = [1, 2, 2, 3, 4, 4, 5]
set4 = set(list2)
print(set4)  # Output: {1, 2, 3, 4, 5}
# set functions
print(set2.issubset(set3))  # Output: False
print(set2.issuperset(set3))  # Output: False
print(set2.isdisjoint(set3))  # Output: False
