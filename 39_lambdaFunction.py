'''
Lambda Function
---------------
-->It is used when a anonymous function is required for a
short period of time.
-->It can take numerous arguments.
-->It can only have one expression.

'''

a=lambda b:b*5
print(a(10))

x=lambda a,b,c:(a+b)*c
print(x(10,2,20))