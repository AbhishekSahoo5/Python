'''
Dictionary
----------------
Dictionary allows user to write the data in the form of keys and values.
    --Dictionaries are enclosed inside curly brackets{}.
    --Keys and Values are seperated by colon
    --Every key value pair is seperated by a comma(,).
'''

Employee_Data={"name":"John","age":24,"gender":"male"}
print(Employee_Data)
print(Employee_Data["age"])
print(Employee_Data["name"])

print("-------------------------------------------------------------------------")

# Iteration in Dictionary

Student={"name":"John","class":"6th","roll_no":23}

for x in Student:
    print(x)

print("----------------------------------------------------------")

for x in Student:
    print(Student[x])

print("----------------------------------------------------------")

#using value function
for i in Student.values():
    print(i)

print("----------------------------------------------------------")

#using items function
for i,j in Student.items():
    print(i,"-->",j)

