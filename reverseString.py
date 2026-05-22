# Write a Python program to reverse a string.
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string
# Example usage
user_input = input("Enter a string to reverse: ")
result = reverse_string(user_input)
print("Reversed string:", result)