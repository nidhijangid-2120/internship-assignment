# Write a program to check Palindrome Number
def is_palindrome(num):
    # Convert the number to string to reverse it
    str_num = str(num)
    # Reverse the string
    reversed_str_num = str_num[::-1]
    # Check if the original string is equal to the reversed string
    return str_num == reversed_str_num  
# Take input from user
number = int(input("Enter a number: "))
# Check if the number is a palindrome
if is_palindrome(number):
    print(f"{number} is a Palindrome Number.")
else:    print(f"{number} is not a Palindrome Number.")