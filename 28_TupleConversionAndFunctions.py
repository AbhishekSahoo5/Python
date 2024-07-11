a=("oneplus","Nokia","Redmi")


# Conversion of Tuple to List
print("Before Conversion",type(a))

a=list(a)
print("After Conversion",type(a))


a.append("Vivo")
print(a)

a=tuple(a)
print(type(a))
print(a)



# Functions in Tuples
print(a.count("Redmi"))
print(a.index("Redmi"))
