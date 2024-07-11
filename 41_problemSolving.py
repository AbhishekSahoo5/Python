#Problems

# Q1) Write a function to find maximum of three numbers in Python
def maxThree(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2>num3:
        return num2
    else:
        return num3


print(maxThree(10,20,30))
print(maxThree(20,30,10))
print(maxThree(30,20,10))
print("-----------------------------------------------------")


# Q2) Write a Python function to create and print a list where the values
#       are square of numbers between 1 and 30.

def createList():
    l=[]
    for i in range(1,31,1):
        l.append(i**2)
    return l

print(createList())
print("-----------------------------------------------------")




# Q3) Write a Python function that takes a number as a parameter and
#        check if the number is prime or not.

def checkPrime(num):
    if num==1:
        return "Not prime"

    if num==2:
        return "Prime"

    else:
        for i in range(2,num):
            if(num%i==0):
                return "Not prime"

        return "Prime"

print(checkPrime(11))
print("-----------------------------------------------------")





# Q4) Write a Python function to sum all the numbers in a list

def add(num):
    total=0
    for i in num:
        total+=i
    return total
print(add([1,2,3,4,5,6,7,8,9,10]))
print("-----------------------------------------------------")

# Solution2(using recursion)
def addRecur(num):
    if(len(num)==1):
        return num[0]
    else:
        return num[0] + addRecur(num[1:])

print(addRecur([1,2,3,4,5,6,7,8,9,10]))

print("-----------------------------------------------------")


# Q5) Write a Python program to solve the Fibonacci Sequence using Recursion.

def fibonacci(n):
    if(n==1): return 0
    if(n==2): return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(7))

print("-----------------------------------------------------")


