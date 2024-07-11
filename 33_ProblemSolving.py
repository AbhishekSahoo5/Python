

# Q1) WAP to sort a dictionary by value

a={"a":12,"b":23,"c":6,"d":91,"e":45}
a=sorted(a.values())
print(a)

print("----------------------------------------------")

# Q2) WAP to print a dictionary where the keys are
# numbers between 1 and 15 and the values are square of keys

dict={}
for i in range(1,16):
    dict[i]=i**2
print(dict)

# Q3) WAP to multiply all the items in a dictioanry
a={"a":1,"b":2,"c":3,"d":4,"e":5}

mul=1
for i in a:
    mul*=a[i]

print(mul)

# Q4) WAP to sort a dictionary by key.
a={12:"a",56:"b",23:"c",48:"d",91:"e"}
a=sorted(a.keys())
print(a)


