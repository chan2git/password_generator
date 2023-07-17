# Import the random and string modules
import random
import string

# Create a function that will accept an argument referencing the length of the password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))                # List expression is used here. For i in range of length, randomly choose an item from characters and join it to password, which starts off as ''
    return password

# Prompt the user for the length of their password
length = int(input("Please enter the length of the generated password: "))


# Call the generate_password function to generate and return the password to the user
password = generate_password(length)
print("Your generated password is: ", password)









# Use this to see what all the characters are being assigned to from the string modules to the variable
#
#test_Characters = string.ascii_letters + string.digits + string.punctuation
#print(test_Characters)