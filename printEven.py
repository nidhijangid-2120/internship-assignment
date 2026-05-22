# Write a Python function to Print Even Numbers from a Given List
def print_even_numbers(input_list):
    even_numbers = []
    for number in input_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = print_even_numbers(numbers)
print("Even numbers in the list are:", result)