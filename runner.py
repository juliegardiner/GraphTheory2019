from regularExpressions2 import match


#User input for the infix regular expressions of the type infixes
infixes = input("Please enter an Infix Regular Expression ->")
type(infixes)

#User input for the Strings to be matched against the infix regular expressions
strings = input("Please enter a String value to be matched against the infix ->")
type(strings)

#Print a the result of the regular expression match to the user in the form of true false
print("The result is: ", match(infixes,strings))