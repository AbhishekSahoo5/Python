'''
Parameters:- Parameters are the variable written inside the parentheses
with the name of function.

Arguments:- Arguments are the values passed to the parameters while calling
the function.

'''

def add(x,y):
    print(y+x)

add(10,10)

def rectangle(length,width):
    print(f"Area={length*width}")

rectangle(10,20)


# Arbitary Arguments ----> multiple Arguments
def hello(*name):
    print(f"My name is {name[0]}")

hello("Abhishek","Shaan","Peter")



