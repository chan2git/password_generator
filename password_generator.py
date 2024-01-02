import string
import random
import sys

# Creates a function that accepts an argument representing the length of the password
def generate_password(length):
    # Creates a variable to hold commonly accepted special characters/punctuations for passwords
    accepted_specialchar = "!@#$%^&*_-+=<>?~" 
    
    # Assigns characters from ascii_letters (all upper/lower), digits (all numbers), and `accepted_specialchar` into `characters`
    # The reason string.printable is not used is due to inclusion of white space
    characters = string.ascii_letters + string.digits + accepted_specialchar

    # Uses a list comprehension to join a random character from `characters` each time i iterates within the range of `length`
    password = "".join(random.choice(characters) for i in range(length))

    # Returns the value for `password`
    return password



run_flag = True

# While `run_flag` is set to True, continue to prompt user
while run_flag:
    print("Enter how many characters you would like your generated password to have, or enter Q to quit")
    # Takes user's input and store into `length`
    length = input()

    # Checks if `length` value is a positive integer
    if length.isdigit() and int(length) > 0:
        # Converts value for `length` from string to int type
        length = int(length)

        # Calls the generate_password function, passes in `length`, and stores the returned value into `password`
        password = generate_password(length)

        # Prints the value for `password`
        print(f"Your generated password is: {password}")

        # Sets `run_flag` to False which breaks the While loop
        run_flag = False                     # Alternative: sys.exit()

    # Checks if `length` value is equal to Q
    elif length.upper() == "Q":
        # Prints a statement indicating the script is quitting
        print("...Quitting...")

        # Sets `run_flag` to False which breaks the While loop
        run_flag = False                     # Alternative: sys.exit()

    # Accounts for other error conditions and restarts the loop block
    else:
        print("Invalid input. Please enter a positive number or Q to quit")
