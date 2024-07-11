#List Functions
# -------------------------------------


a=["Hulk","Thor","Ironman","Captain America","Hulk"]
print(a)

#to find the length of a list
print("Length= ",len(a))

#to count an occurance of a particular element
print("Hulk count= ",a.count("Hulk"))

# to add to a list
a.append("spiderman")
print(a)

#to add to a specific location
a.insert(1,"Vision")
a.insert(3,"Thanos")
print(a)


#to remove from list
a.remove(("Hulk"))
print(a)
a.remove(("Hulk"))
print(a)
a.remove("spiderman")
print(a)


# to remove from a certain location
rem=a.pop(2)
print(rem)
print(a)



# to create a copy of a list
b=[]
print(b)
b=a.copy()
print(b)


#to access index of an element
print(a.index("Ironman"))


#to extend the list
c=["Spiderman","Grut"]
a.extend(c)
print(a)

#to reverse the list
a.reverse()
print(a)


# to sort the list
a.sort()
print(a)

d=[1,8,9,10,22,12,0]
d.sort()
print(d)


# To clear all the data from the list
a.clear()
print(a)
d.clear()
print(d)


