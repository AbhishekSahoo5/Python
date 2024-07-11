'''
String Manipulation
-----------------------
Strings are the combination of number, symbols,
and letters, enclosed inside quotations.
'''

'''
CREATION OF A STRING:
-----------------------
String can be created by enclosing numbers, leters or special symbols inside double quotations.
It means assigning a string value to a variables.
'''

a=("Hello World")
print(a)
print(type(a))


'''
String built-in functions
----------------------------
length ---> no. of character
count ---> count no. of particular char
upper ---> Converts all the letters to uppercase
lower ---> Converts all the letters to Lowercase
index ---> find index of a char 
capitalize ---> Convert the first letter of the string to capital 
casefold   ---> Converts the first letter Capital to small 
find ---> to find index of a char
format
center ---> it fills the given char and centralizes a string
'''

b="Hello World"
print("Length=",len(b))
print("Count=",b.count("l"))
print("upper=",b.upper())
print("lower=",b.lower())
print("index= ",b.index("o"))
print("index= ",b.index("o",5,10))
print("Capitalize= ",b.capitalize())
print("CaseFold",b.casefold())
print("find=",b.find('r'))


name="Abhishek"
age=21
b="My name is {} and age is {}"
print(b.format(name,age))

print(name.center(20,"*"))


