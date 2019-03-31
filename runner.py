import regExpressionMatch
from regExpressionMatch import match

"""Runner which has the menu options for either
 to View the Predefined list of Regular Expressions or 
 for a user to input their own in"""

print("1 View A predefined list of infix regular expressions \n2 Input your own Infixes \n3 Exit the System")
    
selection = int(input("Please make a selection: "))

if (selection == 1):
#List of infix regular expressions  
        infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c","ab+","a?a"]

#Strings to be matched against the infix regular expressions
        strings = ["","abc","abbc","abcc","abad","abbbc","aaaab","a"]
        for i in infixes:
            for s in strings:
                print(match(i,s),i,s)

#User input for the infix regular expressions of the type infixes
elif(selection ==2):
   
        infixes = input("Please enter an Infix Regular Expression -> ")
        type(infixes)

    #User input for the Strings to be matched against the infix regular expressions
        strings = input("Please enter a String value to be matched against the infix -> ")
        type(strings)

    #Print a the result of the regular expression match to the user in the form of true false
        print("The result is: ", match(infixes,strings))

elif(selection== 3):
        SystemExit

else:
    print("Invalid Selection")