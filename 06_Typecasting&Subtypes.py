'''
Type Casting
-------------
Conversion of one datatype to another is called as Type-casting.

There are two types of type-casting

    1. Implicit Type Casting:- Where python itself converts one datatype to another

    2. Explicit Type Casting:- Where the user converts one datatype to another.

'''

name="jhon"
print(type (name))       #---> str

age=19
print(type(age))         #---> int

print("--------------------------------")

a=123
b=1.23
print(type(a))            #int
print(type(b))            #float
#This is Implicit Type conversion
c=a+b
print(type(c))            #float
print("--------------------------------")


#This is explicit type conversion
a="123"
print(type (a))            #str
a=float(a)        #Type converted into Float
print(type (a))             #float



