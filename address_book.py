import csv

# Create a CSV file for address book, CSV file should have column for name, address, mobile, email.
# Insert 2-3 dummy data entered by user.

def main():
    # Open the CSV file in write mode
    with open('address_book.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(['Name', 'Address', 'Mobile', 'Email'])

        # Get user input for 2-3 entries
        for _ in range(3):
            name = input("Enter name: ")
            address = input("Enter address: ")
            mobile = input("Enter mobile number: ")
            email = input("Enter email: ")

            # Write the user input as a new row in the CSV file
            writer.writerow([name, address, mobile, email])

if __name__ == '__main__': # This ensures that the main function is called only when this script is run directly, and not when it is imported as a module in another script.
    main() # Call the main function to execute the program
