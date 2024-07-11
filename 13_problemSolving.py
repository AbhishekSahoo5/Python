# WAP to find a sum of all even numbers up to 50.
sum=0
for i in range(1,51):
    if(i%2==0):
        sum+=i
print(sum)


print("-----------------------------------------------")



# WAP to write first 20 numbers and their squared numbers.
for i in range(1,21):
    print(i," ",i**2)


print("-----------------------------------------------")



# WAP to find sum of first 10 odd numbers using while loop.
i=0
sum=0
while i<=20:
    if(i%2!=0):
        sum+=i
    i+=1
print(sum)


print("----------------------------------------------")




# WAP a program to check if a number is divisible  by 8 and 12 to 100 numbers.
for i in range(1,101):
    if(i%8==0 and i%12==0):
        print(i)

print("----------------------------------------------")



#WAP to create a billing system at supermarket.

while True:
    name=input("Enter your name")
    total=0
    while True:
        quantity=int(input("Enter quantity"))
        amt=int(input("Enter amount"))
        total+=amt*quantity
        repeat=input("If you want to repeat type 'y' else 'n' ")
        if(repeat=='n'):
            break

    print("****Bill****")
    print("Name: ",name)
    print("Total Amount: ",total)

    repeat1=input("do you want to go to the next customer (y/n) ")
    if(repeat1=='n'):
        break
