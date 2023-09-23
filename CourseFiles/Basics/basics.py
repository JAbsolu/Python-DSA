# If you want to specify the data type of a variable, this can be done with casting.

#Example 
x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# Case-Sensitive
# Variable names are case-sensitive.

# Example
# This will create two variables:

a = 4
A = "Sally"

print(a)
print(A)


'''
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

# ExampleGet your own Python Server
# Legal variable names:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

'''
Many Values to Multiple Variables
Python allows you to assign values to multiple variables in one line:

Example
'''
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

'''
One Value to Multiple Variables
And you can assign the same value to multiple variables in one line:

Example
'''
x = y = z = "Orange"
print(x)
print(y)
print(z)