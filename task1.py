#!python3

# Retrieve numerical input

# The following code will not work if the user enters in 
# invalid characters (ie non numerical characters)
# modify this code with  a try...except 
# block so that the user will allow them to enter an integer,
# or display an error message if they enter in something else.

n = input("Please enter in an integer value")

try:
    n = int(n)
    print(f"You entered \"{n}.\"")
except:
    print("Error: Your input was a string, and not a number.")