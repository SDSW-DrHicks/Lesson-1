print("Hello World")
# textual data, such as "Hello World," is called "string." It should always be surrounded by double or single quotes.
# Select Run from the "Run" menu.

# Variables are used to temporarily store data in the memory.
item = 20
print(item)
# note, no quotation marks since 20 is not a string.

# receive user input
name = input("What is your name? ")
print("Hello " + name)
#string concatenation
birth_year = input("Input your birth year: ")
age = 2022 - int(birth_year)
# use "int" to convert the string value of the birth year to an integer to be subtracted.
print(age)

# floating numbers are numbers with a decimal point. Use float() to convert.
# boolean values are logical values, to convert values to boolean, use bool()
# use int() for converting to integers

# another example
First = input("First Number: ")
Second = input("Second Number: ")
sum = float(First) + float(Second)
# need to convert the sum value to a string so that it can be concatenated
print("sum= " + str(sum))
