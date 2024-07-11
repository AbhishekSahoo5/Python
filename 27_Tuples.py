'''
Tuples
-----------
Tuples are the collection of ordered and un-mutable data.
--For tuples no brackets are mandetory. By choice on can use parenthesises.
--The value inside a Tuple is seperated by comma(,).
--Once created, tuples cannot be changed.
--Multiple datatypes can be written inside  tuples.
'''

a=("Apple","mango","banana",1,56,1.23)
print(type(a))
print(a)

# Tuple having 1 element
b="Ironman",
print(type(b))


print("-----------------------------------------------------------------")

# Slicing in Tuples
a=("Oneplus","Vivo","Redmi","Samsung","Nokia")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[::])
print(a[1::2])
print(a[::-1])
print(a[2::-1])

print("-----------------------------------------------------------------")


# Iteration in Tuples
a=("Oneplus","Vivo","Redmi","Samsung","Nokia")

#with for loop
for i in a:
    print(i)

print("---------------------------------")

#along with range and length in for loop
for i in range(len(a)):
    print(a[i])

print("---------------------------------")

#along with while loop
i=0
while i<len(a):
    print(a[i])
    i+=1

print("---------------------------------")


