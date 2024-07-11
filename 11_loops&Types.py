'''
A loop means to repeat something in the exact same way.
Types of loops:
    1. For loop
    2. While Loop
    3. While True
    4. Nested Loop
'''

'''
1. For loop
----------------------
--> For loop is a loop that repeats something in a given range.
--> The range has a starting point, ending point and a step/gep in it.
--> +1 is added to the ending point while defining a range.
'''
#Print number from 1 to 5
for i in range(1,6):
    print(i, end=" ")

print()
print("-------------------------")

#Print even numbers
for i in range(0,11,2):
    print(i, end=" ")

print()
print("-------------------------")

# Print table of 8
for i in range(1,11):
    print("8 X ",i," = ",8*i)


print("------------------------------")
print("****While Loop****")
'''
While Loop
-----------
--> While Loop executes till the given condition is true.
--> In while loop, the increment is done inside the loop.
'''

#print number till number is less than 10
i=2
while i<10:
    print(i)
    i+=1


#Print the table of 7
i=1
while(i<=10):
    print("7 X ", i, " = ", 7 * i)
    i+=1


print("------------------------------")
print("****While True****")
'''
While True
-------------
--> It is an infinite loop
--> To break a while true loop, break statement is used.
'''
i=10
while True:
    if(i>20):
        break
    print(i)
    i+=1


print("------------------------------")
print("****Nested Loop****")

'''
Nested Loops
---------------
--> A loop inside a loop is called as nested loop.
'''

for i in range(1,4):     #No. of sets
    for j in range(1,11):    #No. of reps
        print(j,"Pushups")
    print("*****",i,"Sets done")

#Pattern
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



print("------------------------------")
print("****For Loop with conditions****")

'''
For Loop with conditionals
-----------------------------
The use of if-else statements increases the ability of for loop to 
completes the task effectively. By useing if-else statements 
we can provide with special conditions inside for loop.
 
'''
for i in range(1,11):
    if i==3:
        print("Add this song to favs")
    else:
        print(i)

#common multiple of 8 and 12 between 1 to 100
for i in range(1,101):
    if(i%8==0 and i%12==0):
        print(i)


