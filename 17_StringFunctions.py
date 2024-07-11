# String Function

a="hello"
b="Hello123"
c="123456"
d="HELLO"
e=" "
f="Hello 123"
g="1.234"
h="Harry Potter and The Goblet of Fire"

#isalnum - Returns True if all characters in the string are alphanumeric

print("a is Alphanumeric--",a.isalnum())
print("b is Alphanumeric--",b.isalnum())
print("c is Alphanumeric--",c.isalnum())
print("f is Alphanumeric--",f.isalnum())
print("g is Alphanumeric--",g.isalnum())
print("------------------------------------------")

#isalpha - Returns True if all characters in the string are in the alphabet

print("a is Alphabetic--",a.isalpha())
print("b is Alphabetic--",b.isalpha())
print("------------------------------------------")

#isdecimal - Returns True if all characters in the string are decimals

print("a is decimal--",a.isdecimal())
print("b is decimal--",b.isdecimal())
print("c is decimal--",c.isdecimal())
print("g is decimal--",g.isdecimal())
print("-----------------------------------------")


# isdigit -  Returns True if all characters in the string are digits
print("b is digit--",b.isdigit())
print("c is digit--",c.isdigit())
print("g is digit--",g.isdigit())
print("-----------------------------------------")

#isnumeric - Returns True if all characters in the string are numeric
print("isnumeric")
print(b.isnumeric())
print(c.isnumeric())
print("-----------------------------------------")


#islower -  Converts a string into lower case
print("islower")
print(a.islower())
print(c.islower())
print(d.islower())
print("-----------------------------------------")

#isupper -  Returns True if all characters in the string are upper case
print("isupper")
print(a.isupper())
print(c.islower())
print(d.isupper())
print("-----------------------------------------")


#isspace -  Returns True if all characters in the string are whitespaces
print("isspace")
print(f.isspace())
print(e.isspace())
print("-----------------------------------------")


#istitle - Return True if the string follows the rules of a title
print("istitle")
print(d.istitle())
print(f.istitle())
print(h.istitle())
print("Hi My Name Is Abhishek".istitle())
