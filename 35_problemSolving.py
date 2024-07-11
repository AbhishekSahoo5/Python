#Write a program to find the max and min in a set.
a={1,2,3,4,5,7}
print("Max=",max(a))
print("Min=",min(a))

#Write a program to find the common elements in three lists using sets
a=[1,2,3,4]
b=[4,5,6]
c=[4,3,2]

print(set(a) & set(b) & set(c))

# WAP to find difference between two sets
a={1,2,3,4}
b={1,2,3,4,5}
print(a.difference(b))
print(b.difference(a))


#WAP to remove an item from a set if it is present in the set.
a={1,2,3,4}
b={1,2,3,4,5}

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))


#WAP to check if a set is a subset of another set.
print(a.issubset(b))
print(b.issubset(a))

