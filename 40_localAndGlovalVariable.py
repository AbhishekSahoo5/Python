'''
Local and Global Variables
--------------------------

Local Variables
----------------
Local Variables are restricted to only one block of code and
cannot be changed throughout the program.

Global Variables
----------------
Global Variables are not restricted to one block of code and they can
be changed throughout the program.

'''

x=24     #global variabe
print("First Variables x=",x)
def hello():
    x=25     #local variable
    return x
print(hello())

print(x)