'''
Conditional Statement
-----------------------
Conditional Statement allows computer to execute a certain condition only if it is true.

Types of conditional statements:
    1. If
    2. if-else
    3. if-elif-else
    4. Nested if
    5. if (short hand)
'''

# if statements
marks=97
if marks>=90:
    print("You are Topper")
print("Thank you")

print("--------------------------------")

# if-else statements
age=19
if age>=18:
    print("Major")
else:
    print("minor")

print("---------------------------------")
#if-elif-else
myMarks=70
if myMarks>90:
    print("You are a Topper")
elif myMarks>40 and myMarks<90:
    print("You are an average")
else:
    print("You failed")

print("----------------------------------")
# Nested If
food="pizza"
# more="cheese"
more="not"
if food=="pizza":
    print("Get me a pizza")
    if more=="cheese":
        print("with more cheese")
    else:
        print("with extra chilli flex")

print("-----------------------------------")

# short hand if statements
name="abhishek"
if name=="virat": print("the GOAT")


# short hand if-else statements
print("the GOAT") if name=="virat" else print("Not a legend")

