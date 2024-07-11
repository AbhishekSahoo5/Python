Student={"name":"John","class":"6th","roll_no":23}

# get
x=Student.get("name")
print(x)

#item
y=Student.items()
print(y)

#keys
z=Student.keys()
print(z)

#Values
u=Student.values()
print(u)

#copy
v=Student.copy()
print(v)

# setdefault
s=Student.setdefault("roll_no",24)
print(s)


# update --> to change existing value and add new key-value pair
Student.update({"name":"Abhishek"})
print(Student)
Student.update({"car": "Porsche"})
print(Student)


# pop --> remove element
Student.pop("car")
print(Student)

# popitem --> remove last element
Student.popitem()
print(Student)

#clear   --> clear the dictionary
Student.clear()
print(Student)

