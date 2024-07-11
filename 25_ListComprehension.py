l1=[30,40,50,60]
l2=[]

l2.extend(l1)
print(l2)

# or

for i in l1:
    if i>45:
        l2.append(i)

print(l2)

# List comprehension method
l3=[i for i in l1]
print(l3)

l4=[i for i in l1 if i>45]
print(l4)