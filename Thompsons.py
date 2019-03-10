#Thompsons Construction
# Julie Gardiner
# 10/03/2019

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
          nfa2  =  nfastack.pop()
          nfa1 = nfastack.pop()

#Set nfa1.accept edge1 to nfa2.initial
          nfa1.accept.edge1 = nfa2.initial
#Push this back to the nfastack
          newNFA = (nfa(nfa1.initial,nfa2.accept))
          nfastack.append(newNFA)
         
# OR
        elif c == '|':
          nfa2  =  nfastack.pop()
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
          newNFA = (nfa(initial,accept))
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
          newNFA = (nfa(initial,accept))
          nfastack.append(newNFA)

#Push new NFA to the stack
         
              
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

print(compile("ab.cd.|"))
print(compile ("aa.*"))








        











    
