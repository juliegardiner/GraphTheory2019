#Shunting yard Algorithm
#Julie Gardiner
#02/03/2019




#This function performs the shunting yard algorithm which takes in an Infix expression
#and returns a postfix expression
def shunt(infix):

#Dictionary(like arrays indexed by strings)f specials, the values will represent the precidence of 
#the various operatorsKleene star (highest precedence)/Concatenate(second highest)/OR(lowest)

    specials = {'*' : 60, '.': 50, '|': 40, '+': 30, '?' : 20}

    pofix = ""
    stack = ""

#take a character from infix and check what that is and push it to the stack
    for c in infix:
        if c == '(':
          stack = stack + c

#While last character on the stack is not equal to the open bracket
#return the last character (stack[-1] is the LAST character in the string)
        elif c == ')':
            while stack[-1] !='(':
              pofix = pofix + stack[-1]
              stack = stack[:-1]
            stack = stack[:-1]  
#Checking if the character is in the dictionary specials
        elif c in specials:
          while stack and specials.get(c, 0)<= specials.get(stack[-1], 0):
            pofix,stack = pofix + stack[-1], stack[:-1] 
          stack = stack + c
           
#This just means it is a normal character/ regular expression
        else:
#Append the pofix character with whatever is in c          
          pofix = pofix + c
        
    while stack:
        pofix,stack = pofix + stack[-1],stack[:-1]
     
    return pofix