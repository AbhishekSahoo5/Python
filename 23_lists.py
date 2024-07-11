'''
Lists
----------
Lists are the collection of ordered and mutable data.
    --> List written insode the squared brackets
    --> The value inside a list is seperated by comma(,)
    --> Mutable means once created, they can be chnaged
    --> Multiple datatypes can be written inside a list.

'''

fruits=["Apple","Mango","Banana",14,23,123.909]
print(fruits)
print(type (fruits))


# slicing Lists
# ----------------
a=["Ironman","Thor","Captain America","Hulk"]
print(a[0])
print(a[2])
print(a[3])
print(a[-2])
print(a[-3])
print(a[0:4])
print(a[0:3])
print(a[3:4])
print(a[:2])
print(a[1:])
print(a[0:4:2])
print(a[::-1])
print(a[-3:-1])
print(a[-1:-4:-1])
print("--------------------------------------------")

# List Iteration
#----------------------
a=["Hulk","Thor","Ironman","Captain America"]
for i in a:
    print(i)

print("--------------------------------------------")

#Iteration using for loop

for i in range(len(a)):
    print(a[i])

print("--------------------------------------------")


#Iteration usong while loop
i=0
while(i<len(a)):
    print(a[i])
    i+=1

print("--------------------------------------------")

#Using short-hand for loop

[print(i) for i in a]

print("--------------------------------------------")


