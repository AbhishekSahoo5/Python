'''
Return Statement
-----------------
Return keyword in python is used to exit a function and return
the value of the function
'''

def hello():
    return "Hello World"

print(hello())


def add(a,b):
    return a+b

print(add(10,12))

print("---------------------------------------")

'''
Recursion in Python
---------------------
Recursion in modt commonly used mathematical and 
programming concept.

In simple words, recursion meand a function can call
itself, giving us a benefit of looping through data in
order to get a result
'''

def hello(n):
    if n==4 :
        return
    print("hello")
    return hello(n-1)

hello(10)

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))

'''
Advantages and Disadvantages of Recursion
-----------------------------------------
Advantages:
----------
1. They make the code look clean and organized.
2. By the use of recursive functions, a complex task can be broken down into
small  sub-parts.
3. Subsequance generation becomes easier.

Disadvantages
-------------
1. Recursive Functions take up a lot of memory.
2. Sometimes the logic becomes hard to follow.

'''