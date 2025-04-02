# 035 : Formatted Strings
# - is a string that has been modified by a function or method to
#   include placeholders for data that will be inserted later
# - is called an f-string

name = "John"  # from DB, user input, etc.
age = 55
print(name)  # John
print(f"Hello, {name}. You are {age} years old.")  # Hello, John. You are 55 years old.
print(
    "Hello, {}. You are {} years old.".format(name, age)
)  # Hello, John. You are 55 years old.
print(
    "Hello, {0}. You are {1} years old.".format(name, age)
)  # Hello, John. You are 55 years old.
print(
    "Hello, {1}. You are {0} years old.".format(age, name)
)  # Hello, John. You are 55 years old.
print(
    "Hello, {name}. You are {age} years old."
)  # Hello, {name}. You are {age} years old.
print("Hello, {new_name}".format(new_name="Sally"))  # Hello, Sally.

# - f is used to format a string
# - {} is used to insert a variable
# - .format() is used to insert a variable
# - {0} is used to insert the first variable
# - {1} is used to insert the second variable
# - {name} is used to insert the variable name
# - {age} is used to insert the variable age
# - {new_name} is used to insert the variable new_name

# 1 What would be the output of the below 4 print statements?
# Try to answer these before you click RUN!
print("Hello {}, your balance is {}.".format("Cindy", 50))
print("Hello {0}, your balance is {1}.".format("Cindy", 50))
print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string? (Scroll down for answer)
name = "Cindy"
amount = 50
print(f"Hello {name}, your balance is {amount}.")
