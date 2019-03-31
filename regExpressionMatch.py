import thompsons
from thompsons import compile
import shuntingYard
from shuntingYard import shunt
#Regular Expressions Source: https://web.microsoftstream.com/video/6b4ba6a4-01b7-4bde-8f85-b4b96abc902a
#Julie Gardiner
#Student no: 10015150

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

