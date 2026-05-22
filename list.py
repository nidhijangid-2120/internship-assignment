# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct_elements(input_list):
    distinct_list = []
    for element in input_list:
        if element not in distinct_list:
            distinct_list.append(element)
    return distinct_list
# Example usage
input_list = [1, 2, 3, 2, 4, 1, 5]
result = distinct_elements(input_list)
print("The distinct elements in the list are:", result)