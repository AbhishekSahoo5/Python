#Q1) WAP to display a person's name, age and address in three different lines.

name="Abhishek Sahoo"
age=21
address="Flat No.-116, Jagannath Avanue, Jharpada, Bhubaneswar"

print(name,"\n",age,"\n",address)


#Q2) WAP to swap two variables
num1=10
num2=20

#swap
num1=num1+num2
num2=num1-num2
num1=num1-num2

print("num1=",num1)
print("num2=",num2)


#Q3) WAP to convert float into integer
numX=100
numX=float(numX)
print(type (numX))
print(numX)



#Q4) WAP a program to take details from a student from ID-card and then print it in different lines.
# name=input("Enter your name")
# DOB=int(input("Enter yoor DOB"))
# father_name=input("Enter your Father's name")
# roll_no=int(input("Enter your roll no"))

# print(name)
# print(DOB)
# print(father_name)
# print(roll_no)


#Q5)WAP to take an user input as integer then convert it to float.
integer=int(input("Enter a integer"))
print("Before Conversion")
print(type(integer))
print(integer)

print("After Conversion")
integer=float(integer)
print(type (integer))
print(integer)