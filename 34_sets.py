'''
sets
--------
Sets are unordered collection of data. Every element inside the set is uniqueand mutable.
    --> Sets are written inside the curly brackets
    --> The value inside a set is separated by comma(,)
    --> Mutable means once created, they can be changed.
'''

a={"Ironman","Hulk","Thor","Captain Amerira"}
print(a)
print(type(a))

#Set Functions
# ----------------------

#add
a.add("Spiderman")
print(a)

# pop  ---> remove random value
a.pop()
print(a)

#remove  ---> remove the selected value
# a.remove("Thor")
print(a)


#discard
a.discard("Hulk")
print(a)


#copy
b=a.copy()
print(b)

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-women"}
c={"Hulk","Thor"}

#isdisjoint
print(a.isdisjoint(b))       #-->b is not a part of a
print(a.isdisjoint(c))       #-->c is a part of a

print("------------------------------------------")

# issubset
print(a.issubset(b))
print(c.issubset(a))

print("------------------------------------------")

# issuperset()
print(b.issuperset(a))
print(a.issuperset(c))

print("------------------------------------------")

#update
a.update(b)
print(a)
a.update(c)
print(a)

#clear
a.clear()
print(a)

print("------------------------------------------")




a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-women"}
c={"Hulk","Thor"}


#union
print(a.union(b))
print(a.union(c))

print("------------------------------------------")

#difference
print(a.difference(c))       #--> no change in a

print("------------------------------------------")

#difference update
a.difference_update(c)         #--> change in a
print(a)

print("------------------------------------------")

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-women"}
c={"Hulk","Thor"}


#intersection
print(a.intersection(c))

#intersection update
a.intersection_update(c)
print(a)

print("------------------------------------------")

a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder-women"}
c={"Hulk","Thor","Abhishek"}

#symmetric difference
print(a.symmetric_difference(c))


#symmetric difference update
a.symmetric_difference_update(c)
print(a)

