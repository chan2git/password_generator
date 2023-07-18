### Import the random, string, sys modules
import random
import string
import sys

### Create a function that will accept an argument referencing the length of the password
def generate_password(length):
    accepted_specialchar = "!@#$%^&*_-+=<>?~"                                                 # Assign a custom string of commonly accepted special characters for passwords
    characters = string.ascii_letters + string.digits + accepted_specialchar                        
    password = ''.join(random.choice(characters) for i in range(length))                            # List expression is used here. For i in range of length, randomly choose an item from characters and join it to password, which starts off as ''
    return password



### While condition is true, continue to prompt user for action
while True:
    user_length = input("Please enter the length of the generated password, or Q to quit: ")        # Prompts the user to enter the length of desired password

    if user_length.isdigit() and int(user_length) > 0:                                              # Checks if the user input is a positive integer
        user_length = int(user_length)                                                              # If conditions pass, officially convert user input to a int value and break the while loop
        break      
    elif user_length.upper() == "Q":                                                                # If user input is Q, exit this python script
        print(". . . Quitting . . .")
        sys.exit()                                                              
    else:
        print("Invalid input. Please enter a positive interger only.")


password = generate_password(user_length)                                                           # Call the generate_password function to generate and return the password to the user
print(f"Your generated password is: {password}")



################################################ FOOTNOTES ################################################

#############################
# Version:    1.01          #
# Date:       07/17/2023    #
# Coder:      CH @chan2git  #
#############################
