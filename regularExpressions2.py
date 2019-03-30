
#Regular Expression and Thompson Construction
#Julie Gardiner


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

#A class(Blueprint) Takes variables and functions that are related
#class state is a state that contains 2 edges (Think automata layout)
#None value is like null,if we don't want to initialise with a value at that time
class state:
    label = None
    edge1 = None
    edge2 = None

#class nfa contains the states of the automata
class nfa:
    initial = None
    accept =  None

#Constructor(self is the current instance of that class)
    def __init__(self,initial,accept):
        self.initial = initial
        self.accept = accept

#Function that takes postfix regular expression as arg
def compile(pofix):
#Postfix has a stack(stack of NFAs) represented by an empty list    
    nfastack = []

    for c in pofix:
#Stack is lifo for pop off the stack  
# CONCATENATE      
        if c == '.':
          nfa2 = nfastack.pop()
          nfa1 = nfastack.pop()

#Set nfa1.accept edge1 to nfa2.initial
          nfa1.accept.edge1 = nfa2.initial
#Push this back to the nfastack
          newNFA = nfa(nfa1.initial,nfa2.accept)
          nfastack.append(newNFA)
         
# OR
        elif c == '|':
          nfa2 = nfastack.pop()
          nfa1 = nfastack.pop()
#Create new initial state,connect this to initial states of NFA1 and NFA2 popped off from stack
          initial = state()
          initial.edge1 = nfa1.initial
          initial.edge2 = nfa2.initial

#Create a new accept state, connecting the accept states of the two NFAs popped from the stack,
#to the new state.
          accept= state()
          nfa1.accept.edge1 = accept
          nfa2.accept.edge2 = accept

#Push new NFA to the stack using the constructor
          newNFA = nfa(initial,accept)
          nfastack.append(newNFA)

#KLEENE STAR
        elif c == '*':
# Pop 1 nfa off the Stack
          nfa1 = nfastack.pop()
#Creating new initial and accept states
          initial = state()
          accept = state()
#Join thenew initial state to the NFA1 initial state and new accept state
          initial.edge1 = nfa1.initial
          initial.edge2 = accept

#Join the old and new accept states and NFA1 initial state
          nfa1.accept.edge1 = nfa1.initial
          nfa1.accept.edge2 = accept
#Push to the stack
          newNFA = nfa(initial,accept)
          nfastack.append(newNFA)    

#PLUS OPERATOR (e.g at least 1 of)
        elif c == '+':   
#Pop both nfa's off the Stack beginning with NFA2
          nfa2 = nfastack.pop()
          nfa1 = nfastack.pop() 
         
#Creating new initial and accept states
          initial = state()
          accept = state()

          initial.edge1 = nfa1.initial
#Join the accept state of edge 1 to the nfa1 initial state
          nfa1.accept.edge1 = nfa1.initial
#Join the initial state of edge 2 to the nfa2 accept state
          initial.edge2 = accept
#Join the old and new accept states to NFA1 and NFA2 initial states 
          nfa2.accept.edge1 = nfa1.initial
          nfa1.accept.edge2 = nfa2.initial

          nfa2.accept.edge1 = accept
#Push to the stack
          newNFA = nfa(initial,accept)
          nfastack.append(newNFA) 


#? OPERATOR (0 or 1 times)
        elif c == '?':
#Pop both nfa's off the Stack beginning with NFA2
          nfa2 = nfastack.pop()
          nfa1 = nfastack.pop() 

#Creating new initial and accept states
          initial = state()
          accept = state()

#Join the new initial state to the NFA1 initial state
          initial.edge1 = nfa1.initial
#Join the new initial state to the NFA accept state
          initial.edge2 = accept
#Join the accept state of edge 1 to the nfa1 initial state
          nfa1.accept.edge1 = accept
#Push to the stack
          newNFA = nfa(initial,accept)
          nfastack.append(newNFA) 
             
#Create a new NFA with an accept(instance) state join initial(2 edges) to accept with arrow(label)
        else:
          accept = state()        
          initial = state()
          initial.label = c
          initial.edge1 = accept
            
          newNFA = (nfa(initial,accept))
          nfastack.append(newNFA)
    
    #nfastack should only have a single nfa on it here
    return nfastack.pop() 

    #Helper function follows "e"s state
def followes(state):
    """Returns the set of states that can be reached from state following the arrows"""
    #Creates a new set, with state as it only member
    states = set()
    states.add(state)

    #This will check if state has arrows labelled e from it (NB,States have 2 arrows)
    #If state.label is none,they have e arrows
    if state.label is None:
            #Check if edge1 is a state

          if state.edge1 is not None:
            #If there is edge 1 follow it..follow E arrow from whatever the state was to the current state
            # "|" is union of the set(or=) 

            states |= followes(state.edge1)
            #Check if edge 2 is a state
          if state.edge2 is not None:
            
            #If there is edge 2 follow it
            states |= followes(state.edge2)

    #Returns the set of states 
    return states    


def match(infix, string):
    """Matches the string to the infix regular expression""" 
    #shunt and compile the regular expression 
    postfix= shunt(infix)
    nfa = compile(postfix)

    #The current(as empty set) set of states with the next(nextS, as empty set) set of states
    current = set()
    next = set()

    # Add initial state to the current set
    current |= followes(nfa.initial)

    #Loop through the characters in the string
    for s in string:
        #Loop through the current set of states
        for c in current:
        #Check if the state is labelled s
          if c.label ==  s:
        #Add the edge1 state to the next set.
            next |= followes(c.edge1) 
        #Set current to next and flush next
        current = next
        next = set()

    #Check if accept state is in the list in the set of current states
    return (nfa.accept in current)       

#List of infix regular expressions  
infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c","ab+","a?a"]

#Strings to be matched against the infix regular expressions
strings = ["","abc","abbc","abcc","abad","abbbc","aaaab","a"]


for i in infixes:
    for s in strings:
       print(match(i,s),i,s)
