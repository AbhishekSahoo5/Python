#endswith() - Returns true if the string ends with the specified value

a="Harry Potter"
print(a.endswith("r"))
print(a.endswith("ter"))
print(a.endswith("Har"))
print(a.endswith("t",6,9))  #With in a range
print("------------------------------------")

#startswith() -  Returns true if the string starts with the specified value
print(a.startswith("H"))
print(a.startswith("har"))
print(a.startswith("Pot",6,10))    #within a range
print("------------------------------------")


#swapcase() -  Swaps cases, lower case becomes upperecase and vice versa
c="Abhishek Sahoo"
print(c.swapcase())
print("------------------------------------")


#strip() - Returns a trimmed version of the string
d="   Abhishek Sahoo        "
print(d)
print(d.strip())

e="      ****Abhishek ........."
print(e.strip("*, "))
print(e.strip("*, ,."))
print("------------------------------------")


#split() -  Splits the string at the specified separator, and returns a list
f="#OOFD#BRB#OMG#FOMO"
print(f.split("#"))

f="hey.my.name.is.abhishek"
print(f.split("."))
print("------------------------------------")



#ljust() -  Returns a left justified version of the string
g="Abhishek Musk"
aa=a.ljust(20)
print(aa," is great")
aa=a.ljust(20,"_")
print(aa," is great")
print("------------------------------------")



#ljust() -  Returns a right justified version of the string
g="Abhishek Musk"
aa=a.rjust(20)
print(aa," is great")
aa=a.rjust(20,"_")
print(aa," is great")
print("------------------------------------")



#replace() - Returns a string where a specified value is replaced with a specified value
h="Virat is a GOAT & Virat is a legend"
print(h.replace("Virat","Kohli"))
print("------------------------------------")


#rindex -  Searches the string for a specified value and returns
# the last position of where it was found

i="Harry potter and Prisoner of Azkaban"
print(i.rindex("Prisoner"))
print(i.rindex("Harry"))
print(i.rindex("n"))
print(a.rindex("a",6,20))
print("------------------------------------")


#rfind -  Searches the string for a specified value and returns
# the last position of where it was found

i="Harry potter and Prisoner of Azkaban"
print(i.rfind("Prisoner"))
print(i.rfind("Harry"))
print(i.rfind("n"))


i="bibidy bobidy booi"
print(i.rfind("i",6,14))
print(i.rfind("i"))

print("------------------------------------")



