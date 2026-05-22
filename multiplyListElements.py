# Write a Python function to multiply all the numbers in a list.
def multiply_list_elements(input_list):
    if not input_list:
        return 0  # Return 0 for an empty list
    product = 1
    for element in input_list:
        product *= element
    return product
# Example usage
numbers = [2, 3, 4]
result = multiply_list_elements(numbers)
print("The product of the numbers in the list is:", result)