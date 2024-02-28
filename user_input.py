# Use the input() function to ask the user for their name and store it in a variable called "name".
name=str(input("What is your name? "))
#se the input() function to ask the user for their age and store it in a variable called "age".
age=int(input("What is your current age? "))
# Use the input() function to ask the user for their location and store it in a variable called "location".
location=str(input("What is your current location? "))

# Print out a personalized message using the user's name, age, and location. For example:
#  "Hello [name], you are [age] years old and live in [location]."
print(f"Hello {name}, you are {age} years of age and live in {location} .")