# WAP to check if a number is positive
num=-10
print("positive") if num>0 else print("Negetive")

#WAP to check wheather a number is odd or even
print("even") if num%2==0 else print("odd")

#WAP to check area calculator

# print("*****Area Calculator*****")
# print("press 1 to get area of square")
# print("press 2 to get area of rectangle")
# print("press 3 to get area of triangle")
#
# press=int(input("enter your choice[1-3]"))
# if press==1:
#     side=int(input("enter side of the square"))
#     print("Area of the square= ",side**2)
# elif press==2:
#     length=int(input("enter length of the rectangle"))
#     breadth=int(input("enter breadth of the rectangle"))
#     print("Area of rectangle= ",length*breadth)
# elif press==3:
#     base=int(input("enter base of the triangle"))
#     height=int(input("enter height of the triangle"))
#     print("Area of triangle",base*height)
# else:
#     print("Invalid choice")

#WAP a program check wheather the passed letter is a vowel or not
letter="E"
print("vowel") if letter in "aeiou" or letter in "AEIOU" else print("Not vowel")

#WAP to check if a number is a single digit number, 2-digit and so on..., upto 5 digits.
num=int(input("Enter a number"))
if num>=0 and num<=9 :
    print("One digit")
if num>=10 and num<=99 :
    print("two digit")
if num>=100 and num<=999 :
    print("three digit")
if num>=1000 and num<=9999 :
    print("four digit")
