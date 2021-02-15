# Python program to 
# demonstrate stack implementation
# using collections
from collections import deque

stack = deque()

# adding elements onto the stack
stack.append('A')
stack.append('B')
stack.append('C')
stack.append('D')

# displaying stack
print("Stack => %s" %stack)

# removing item from stack
element = stack.pop()

print("removed element '%s' from stack" %element)

print("removed element '%s' from stack" %stack.pop())
print("removed element '%s' from stack" %stack.pop())
print("removed element '%s' from stack" %stack.pop())

# displaying stack
print("Stack => %s" %stack)