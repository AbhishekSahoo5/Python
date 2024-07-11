'''
Continue Statement:
----------------------
Continue statement is used when you want to skip a particular condition.

Break Statement:
---------------------
Break Statement is used when you want to destroy a loop at a certain condition and come out of the loop.

'''
#Continue
for i in range(1,11):
    if i==4 or i==7:
        continue
    print(i)

#Break
for i in range(1,11):
    if i==4 or i==7:
        break
    print(i)


