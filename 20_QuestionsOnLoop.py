#1 Write a program to get Fibonacci series up to 10 numbers

# 1 1 2 3 5 8 13

a=0
b=1

# n=int(input("Enter a numbers here"))
# if n==1:
#     print(1)
# else:
#     print(0)
#     print(1)
#     for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)

#2 WAP to check if a number is prime or not

# m=int(input("Enter a numbers here"))
# if m<=1:
#     print("Not a Prime no.")
# else:
#     for i in range(2,m):
#         if m%i==0:
#             print("Not a prime number")
#             break
#     else:
#         print("It is a prime no.")





#3 WAP to find palindrome of integers

# Palindrome ---> 121, 1331, 12321

# num3=int(input("Enter the number"))
# rev=0;
# temp=num3
# while(num3>0):
#     dig=num3%10;
#     rev=rev*10+dig
#     num3//=10
#
# if(rev==temp):
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


#4  WAP to create an area calculator
while(True):
    print("*****Area Calculator*****")
    print("press 1 to get area of square")
    print("press 2 to get area of rectangle")
    print("press 3 to get area of triangle")

    press=int(input("enter your choice[1-3]"))
    if press==1:
        while(True):
            side = int(input("enter side of the square"))
            print("Area of the square= ", side ** 2)
            repeat = input("Do you want to try again with square")
            if (repeat == "no"):
                break
    elif press==2:
        while(True):
            length = int(input("enter length of the rectangle"))
            breadth = int(input("enter breadth of the rectangle"))
            print("Area of rectangle= ", length * breadth)
            repeat = input("Do you want to try again with Rectangle")
            if (repeat == "no"):
                break
    elif press==3:
        while(True):
            base = int(input("enter base of the triangle"))
            height = int(input("enter height of the triangle"))
            print("Area of triangle", base * height)
            repeat = input("Do you want to try again with Traingle")
            if (repeat == "no"):
                break
    else:
        print("Invalid choice")

    repeat=input("Do you want to continue")
    if repeat=="no":
        print("Thank You For Using")
        break;

