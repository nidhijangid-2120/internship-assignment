# Practise reading, writting, appending data in a file
# Write a Python program to read a file and print its contents.
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
# Example usage
file_path = 'example.txt'  # Replace with your file path
read_file(file_path)
# Write a Python program to write a string to a file.
def write_to_file(file_path, text):
    with open(file_path, 'w') as file:
        file.write(text)
    print(f"Text has been written to {file_path}.")
# Example usage
file_path = 'example.txt'  # Replace with your file path
text = "Hello, this is a sample text to write to the file."
write_to_file(file_path, text)
# Write a Python program to append a string to a file.
def append_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + '\n')
    print(f"Text has been appended to {file_path}.")
# Example usage
file_path = 'example.txt'  # Replace with your file path
text = "This is an additional line to append to the file."
append_to_file(file_path, text)