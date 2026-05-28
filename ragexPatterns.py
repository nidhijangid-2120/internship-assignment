# 1) Explore more regex patterns Eg. The regex pattern used to validate email addresses, mobile no, string, and more
import re

# Email validation pattern
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Mobile number validation pattern (assuming 10 digits)
mobile_pattern = r'^\d{10}$'

# String validation pattern (alphanumeric and spaces only)
string_pattern = r'^[a-zA-Z0-9\s]+$'
# Test the patterns
test_email = "example@example.com"
test_mobile = "1234567890"
test_string = "Hello World"
if re.match(email_pattern, test_email):
    print(f"{test_email} is a valid email address.")
else:
    print(f"{test_email} is not a valid email address.")

if re.match(mobile_pattern, test_mobile):
    print(f"{test_mobile} is a valid mobile number.")
else:
    print(f"{test_mobile} is not a valid mobile number.")

if re.match(string_pattern, test_string):
    print(f"{test_string} is a valid string.")
else:
    print(f"{test_string} is not a valid string.")