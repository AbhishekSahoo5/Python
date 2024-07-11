A=["Ross","Rachel","Monica","Joe"]

# WAP to swap first and forth element
A[0],A[3]=A[3],A[0]
print(A)

# WAP to add a new value at second position
A.insert(1,"Abhishek")
print(A)

# WAP to delete a value from 3rd position
A.pop(2)
print(A)


B=[13,7,12,10,234]
# WAP to multiply all the numbers in the list
mul=1
for i in B:
    mul*=i
    i+=1
print(mul)

# WAP to get the largest number from the list
B.sort()
print("Largest=",B[-1])

# WAP to get the smallest number from the list
B.sort()
print("Smallest=",B[0])