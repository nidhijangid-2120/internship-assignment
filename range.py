# Write a Python function to check whether a number falls within a given range.
def is_within_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False
# Example usage
number = float(input("Enter a number: "))
range_start = float(input("Enter the start of the range: "))
range_end = float(input("Enter the end of the range: "))
if is_within_range(number, range_start, range_end):
    print(f"{number} falls within the range {range_start} to {range_end}.")
else:
    print(f"{number} does not fall within the range {range_start} to {range_end}.")