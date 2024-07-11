#1 Take an input from a user as a string then, reverse it.

# a=input("Enter anything here")
# print(a[::-1])



#2 WAP to check if a string contains only digits.
str2="122334"
str22="abhish23333"

print(str2.isdigit())
print(str22.isdigit())



#3 WAP to check if a string is palindrome

str3="madedam"
rev=str3[::-1]
if(str3==rev):
    print("Palindrome")
else:
    print("Not Palindrome")

#4 WAP to find number of vowels in a string

str4="abhishek"
vowels=0
for i in str4:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U" :
        vowels+=1

print(vowels)


#5 WAP to check if every word in a string begins with a capital letter

str5="Abhishek Sahoo Is A Goat"
print(str5.istitle())